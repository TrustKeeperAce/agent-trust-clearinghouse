#!/usr/bin/env python3
"""scripts/check_export.py (decision 0061). Read-only. Checks that public/data/* match the YAML
entries and the rendered pages (index, entry pages, llms.txt, sitemap), that every CSV row carries
the disclaimer and license, that agents.json validates against schema.json (if the jsonschema
package is installed), and that all JSON-LD parses and contains no Review/AggregateRating/Rating.
Decision 0065 adds: data/changelog.yaml vs changelog.html (no drift), updates.json (JSON Feed 1.1) and
updates.xml (Atom): unique and stable ids, latest values per agent match agents.json and the entry
pages, referenced agents/URLs/packets exist, both feeds hold the same items, disclaimer on every item,
valid JSON / well-formed XML, feed links and citation guidance present.
Exit 1 on any error."""
import os,sys,re,json,csv,glob,yaml
sys.dont_write_bytecode=True
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import build_data as B
P=B.P; err=[]
def E(m): err.append(m)
j=json.load(open(os.path.join(P,'data','agents.json'))); sch=json.load(open(os.path.join(P,'data','schema.json')))
y={e['id']:e for e in B.entries()}; x={e['id']:e for e in j['entries']}
if set(y)!=set(x): E(f'ids differ: yaml-only {set(y)-set(x)}, json-only {set(x)-set(y)}')
if j['dataset']['entry_count']!=len(x): E('entry_count mismatch')
if j['disclaimer']!=B.DISCLAIMER or j['usage_note']!=B.USAGE: E('disclaimer/usage_note mismatch')
if j['dataset']['license']!=B.LICENSE: E('license mismatch')
for k in y:
    if k in x and json.dumps(y[k],sort_keys=True)!=json.dumps(x[k],sort_keys=True): E(f'{k}: json differs from yaml (rerun build_data.py)')
    e=y[k]
    if e['independent_source_count']['performance'] not in (None,e['counted_performance_sources']): E(f'{k}: declared vs counted sources differ')
rows=list(csv.DictReader(open(os.path.join(P,'data','agents.csv'),newline='')))
if len(rows)!=len(y): E(f'csv rows {len(rows)} != {len(y)}')
for r in rows:
    e=y.get(r['id'])
    if not e: E(f"csv unknown id {r['id']}"); continue
    if r['disclaimer']!=B.DISCLAIMER: E(f"{r['id']}: csv disclaimer missing")
    if r['license']!=B.LICENSE: E(f"{r['id']}: csv license missing")
    if r['overall_score']!=('' if e['overall_score'] is None else str(e['overall_score'])) or r['evidence_grade']!=e['evidence_grade']: E(f"{r['id']}: csv score/grade")
    for f in B.FACTORS:
        if r[f]!=('' if e['scores'][f] is None else str(e['scores'][f])): E(f"{r['id']}: csv {f}")
    if r['counted_performance_sources']!=str(e['counted_performance_sources']): E(f"{r['id']}: csv source count")
idx=open(os.path.join(P,'index.html')).read()
for m in re.finditer(r'<a href="/agents/([a-z0-9-]+)\.html">[^<]*</a></th>.*?data-label="Overall score" class="num">(?:<span class="bar" style="--v:\d+">)?([^<]+)<.*?data-label="Evidence grade">([^<]+)<',idx):
    k,s,g=m.groups(); e=y.get(k)
    if not e: E(f'index unknown {k}'); continue
    if (s.strip()=='—')!=(e['overall_score'] is None) or (e['overall_score'] is not None and s.strip()!=str(e['overall_score'])): E(f'{k}: index score {s}')
    if g.strip()!=('—' if e['overall_score'] is None else e['evidence_grade']): E(f'{k}: index grade {g}')
# 0072 D7a: home-page last-reviewed dates equal agents.json and the entry page
nd=0
for m in B.IDX_ROW_RE.finditer(idx):
    k=m.group(2); d=re.search(r'<time datetime="([^"]*)">([^<]*)</time>',idx[m.end(1):m.end(1)+80]); e=y.get(k)
    if not e or not d: continue
    nd+=1; ep=open(os.path.join(P,'agents',k+'.html')).read(); pm=re.search(r'Last reviewed</dt><dd>(\d{4}-\d{2}-\d{2})',ep)
    if not (d.group(1)==d.group(2)==str(e['last_reviewed'])==(pm.group(1) if pm else None)): E(f'{k}: index last-reviewed {d.group(2)} vs agents.json {e["last_reviewed"]} vs entry page {pm.group(1) if pm else None}')
if nd!=len(y): E(f'index date rows {nd} != {len(y)}')
nidx=len(re.findall(r'<a href="/agents/([a-z0-9-]+)\.html">[^<]*</a></th>.*?data-label="Evidence grade">',idx))
if nidx!=len(y): E(f'index rows matched {nidx} != {len(y)}')
for k,e in y.items():
    t=open(os.path.join(P,'agents',k+'.html')).read()
    if e['overall_score'] is None:
        if 'Status: Insufficient evidence' not in t: E(f'{k}: page not insufficient')
    else:
        m=re.search(r'Overall score: (\d+)</strong> · <a href="/methodology.html#evidence-grade">Evidence grade</a>: ([AB-]+) · Independent sources: (\d+) performance',t)
        if not m or (int(m[1]),m[2],int(m[3]))!=(e['overall_score'],e['evidence_grade'],e['counted_performance_sources']): E(f'{k}: page scoreline {m and m.groups()}')
L=open(os.path.join(P,'llms.txt')).read()
for k,e in y.items():
    want=f"agents/{k}.html): "+('Insufficient evidence' if e['overall_score'] is None else f"overall {e['overall_score']}, evidence grade {e['evidence_grade']}")
    if want not in L: E(f'{k}: llms.txt line')
sm=open(os.path.join(P,'sitemap.xml')).read()
for k,e in y.items():
    if f"/agents/{k}.html</loc><lastmod>{e['last_reviewed']}</lastmod>" not in sm: E(f'{k}: sitemap lastmod')
if '/agents-data.html</loc>' not in sm: E('sitemap missing agents-data.html')
try:
    import jsonschema; jsonschema.validate(j,sch); print('schema: valid')
except ImportError: print('schema: jsonschema not installed, skipped')
except Exception as ex: E(f'schema: {str(ex)[:200]}')
ds=0
for f in glob.glob(P+'/*.html')+glob.glob(P+'/agents/*.html'):
    for blk in re.findall(r'<script type="application/ld\+json">(.*?)</script>',open(f).read(),re.S):
        try: d=json.loads(blk)
        except Exception as ex: E(f'{f}: JSON-LD parse {ex}'); continue
        s=json.dumps(d)
        if re.search(r'"@type": "(Review|AggregateRating|Rating)"',s): E(f'{f}: rating markup present')
        if '"@type": "Dataset"' in s: ds+=1
if ds!=1: E(f'expected exactly one Dataset JSON-LD block, found {ds}')
# ---- 0065 update feed ----
import subprocess,xml.etree.ElementTree as ET
clrows=B.changelog(); rid=[r['id'] for r in clrows]
if len(rid)!=len(set(rid)): E('changelog.yaml: duplicate row ids')
if [str(r['date']) for r in clrows]!=sorted((str(r['date']) for r in clrows),reverse=True): E('changelog.yaml: not newest first')
ch=open(os.path.join(P,'changelog.html')).read()
m=re.search(r'<table class="stack">.*?</table>',ch,re.S)
if not m or m.group(0)!=B.changelog_table(clrows): E('changelog.html table differs from data/changelog.yaml (rerun build_data.py)')
if len(re.findall(r'<td data-label="Date">',ch))!=len(clrows): E('changelog.html row count != changelog.yaml')
decs=os.listdir(os.path.join(B.R,'decisions'))
for r in clrows:
    for pk in r['decision_packets']:
        if not any(f.startswith(pk+'-') for f in decs): E(f"{r['id']}: decision {pk} not in decisions/")
    f=r['decision_url'].split('/blob/master/')[-1]
    if not os.path.exists(os.path.join(B.R,f)): E(f"{r['id']}: decision_url target {f} missing")
    for c in r['changes']:
        if c['agent_id'] not in y: E(f"{r['id']}: unknown agent {c['agent_id']}")
        if c['type'] not in ('new_entry','score_change','entry_update'): E(f"{r['id']}: bad type {c['type']}")
        if c['type']=='new_entry' and c['before'] is not None: E(f"{r['id']}/{c['agent_id']}: new_entry with before")
try: jf=json.load(open(os.path.join(P,'updates.json')))
except Exception as ex: E(f'updates.json invalid JSON: {ex}'); jf={'items':[]}
if jf.get('version')!='https://jsonfeed.org/version/1.1' or not jf.get('title') or 'items' not in jf: E('updates.json: not JSON Feed 1.1')
if jf.get('feed_url')!=B.BASE+'/updates.json': E('updates.json feed_url')
ji=jf.get('items',[]); jids=[i.get('id') for i in ji]
if len(jids)!=len(set(jids)): E('updates.json: duplicate item ids')
want=[i['id'] for i in B.feed_items(clrows,{e['id']:e['name'] for e in y.values()})]
if jids!=want: E('updates.json items differ from changelog.yaml (rerun build_data.py)')
for i in ji:
    if not i.get('id','').startswith(B.TAG): E(f"{i.get('id')}: id not domain-independent tag URI")
    if B.FEED_DISCLAIMER not in i.get('content_text','') or i.get('_clearinghouse',{}).get('disclaimer')!=B.FEED_DISCLAIMER: E(f"{i['id']}: disclaimer missing")
    xi=i.get('_clearinghouse',{})
    for k in ('type','agent_id','before','after','status','decision_packets','entry_url','as_of'):
        if k not in xi: E(f"{i['id']}: field {k} missing")
    if xi.get('entry_url') and not os.path.exists(os.path.join(P,xi['entry_url'][len(B.BASE)+1:])): E(f"{i['id']}: entry_url file missing")
    if not i.get('url','').startswith(B.BASE+'/'): E(f"{i['id']}: url")
latest={}
for i in ji:
    a=i['_clearinghouse'].get('agent_id')
    if a and a not in latest: latest[a]=i['_clearinghouse']['after']
J={e['id']:e for e in j['entries']}
for k,e in J.items():
    a=latest.get(k)
    if a is None: E(f'{k}: no feed item'); continue
    if (a.get('overall_score'),a.get('evidence_grade'),a.get('status'))!=(e['overall_score'],e['evidence_grade'],e['status']): E(f'{k}: latest feed values {a} != agents.json')
# previously published ids must persist (stability), compared with the last committed feed if any
prev=subprocess.run(['git','-C',B.R,'show','HEAD:public/updates.json'],capture_output=True,text=True)
if prev.returncode==0:
    try:
        old={i['id'] for i in json.loads(prev.stdout)['items']}
        if old-set(jids): E(f'unstable ids: {sorted(old-set(jids))[:5]} removed')
    except Exception as ex: E(f'previous updates.json unreadable: {ex}')
try:
    at=ET.parse(os.path.join(P,'updates.xml')).getroot(); ns={'a':'http://www.w3.org/2005/Atom'}
    aids=[en.findtext('a:id',namespaces=ns) for en in at.findall('a:entry',ns)]
    if aids!=jids: E('updates.xml and updates.json items differ')
    for en in at.findall('a:entry',ns):
        if B.FEED_DISCLAIMER not in (en.findtext('a:summary',namespaces=ns) or ''): E(f"atom {en.findtext('a:id',namespaces=ns)}: disclaimer missing")
except ET.ParseError as ex: E(f'updates.xml not well-formed: {ex}')
for f in B.ALT_PAGES:
    if B.ALT not in open(os.path.join(P,f)).read(): E(f'{f}: feed <link rel=alternate> missing')
for u in ('/updates.json','/updates.xml'):
    if B.BASE+u not in L: E(f'llms.txt missing {u}')
if 'Citation guidance: '+B.CITATION not in L: E('llms.txt citation guidance missing or stale')
import html as _h
ex_=J.get(B.example_entries()[0]['id'])
if not ex_ or f"{ex_['name']}: {ex_['overall_score']}/100, evidence grade {ex_['evidence_grade']}, as of {ex_['last_reviewed']}" not in B.CITATION: E('citation example out of date with agents.json')
print(f'feed: {len(clrows)} changelog rows, {len(jids)} items')
# ---- 0066 comparison pages ----
import html as _hh
Yd=B._yaml_by_id(); EL=list(J.values()); smx=open(os.path.join(P,'sitemap.xml')).read()
def _vis(t):  # visible text + meta content + title + JSON-LD (not tag/attribute names)
    body=re.sub(r'<script[^>]*>.*?</script>','',t,flags=re.S)
    parts=[re.sub(r'<[^>]+>',' ',body)]+re.findall(r'<meta [^>]*content="([^"]*)"',t)+re.findall(r'<script type="application/ld\+json">(.*?)</script>',t,re.S)
    return _hh.unescape(' '.join(parts))
for c in B.COMPARE:
    fp=os.path.join(P,c['path'])
    if not os.path.exists(fp): E(f"{c['path']}: missing"); continue
    t=open(fp).read(); ids=B.compare_ids(c,B.entries())
    if t!=B.render_compare(c,B.entries(),Yd,B.changelog_date(),(lambda a:(a[a.index('</head>')+7:a.index('<main id="main">')+16]+'\n',a[a.index('</main>'):]))(open(os.path.join(P,'agents-data.html')).read())): E(f"{c['path']}: stale (rerun build_data.py)")
    for i in ids:
        e=J.get(i)
        if not e: E(f"{c['path']}: unknown id {i}"); continue
        m=re.search(r'<a href="/agents/'+i+r'\.html">[^<]*</a></th>(.*?)</tr>',t)
        if not m: E(f"{c['path']}: no row for {i}"); continue
        cells=[_hh.unescape(x) for x in re.findall(r'<td[^>]*>(?:<time[^>]*>)?([^<]*)',m.group(1))]
        d=lambda v:'—' if v is None else str(v)
        want=[d(e['overall_score']),e['evidence_grade']]+[d(e['scores'][k]) for k in B.FACTORS]+[f"{e['counted_performance_sources']} ({e['peer_reviewed_counted_sources']})",e['last_reviewed']]
        if cells!=want: E(f"{c['path']}/{i}: table {cells} != agents.json {want}")
    if B.FEED_DISCLAIMER not in t: E(f"{c['path']}: disclaimer missing")
    if f"Data as of {B.changelog_date()} ({B.RULES})" not in t: E(f"{c['path']}: as-of date missing")
    if _hh.escape(B.CITATION,quote=True) not in t: E(f"{c['path']}: citation guidance missing")
    v=_vis(t)
    for b in B.BANNED:
        if re.search(b,v,re.I): E(f"{c['path']}: banned wording {b!r}")
    for blk in re.findall(r'<script type="application/ld\+json">(.*?)</script>',t,re.S):
        ty=json.loads(blk).get('@type')
        if ty not in ('ItemList','BreadcrumbList'): E(f"{c['path']}: unexpected JSON-LD {ty}")
    if re.search(r'"@type":\s*"(Review|AggregateRating|Rating)"|ratingValue|itemprop="(aggregateRating|review|reviewRating)"|itemtype="[^"]*(Review|Rating)"',t): E(f"{c['path']}: rating markup")
    if re.search(r'<script(?![^>]*application/ld\+json)',t): E(f"{c['path']}: script found")
    if f"{B.BASE}/{c['path']}</loc>" not in smx: E(f"{c['path']}: not in sitemap")
    if f"{B.BASE}/{c['path']})" not in L: E(f"{c['path']}: not in llms.txt")
    for f in ('index.html','methodology.html'):
        if f'href="/{c["path"]}"' not in open(os.path.join(P,f)).read(): E(f"{f}: Compare link to {c['path']} missing")
    if not any(f"/{c['path']}" in r['change_html'] for r in clrows): E(f"{c['path']}: no changelog/feed row")
# index category labels must match the data
for m in re.finditer(r'<a href="/agents/([a-z0-9-]+)\.html">[^<]*</a></th><td data-label="Category">([^<]*)<',idx):
    if m[1] in J and J[m[1]]['category']!=_hh.unescape(m[2]): E(f"{m[1]}: index category {m[2]!r} != {J[m[1]]['category']!r}")
print(f'compare: {len(B.COMPARE)} pages checked')
# ---- 0067 citing page ----
cp_=os.path.join(P,B.CITE_PATH); ct=open(cp_).read() if os.path.exists(cp_) else ''
if not ct: E('citing.html missing')
else:
    ad=open(os.path.join(P,'agents-data.html')).read()
    if ct!=B.render_citing(B.entries(),(ad[ad.index('</head>')+7:ad.index('<main id="main">')+16]+'\n',ad[ad.index('</main>'):])): E('citing.html: stale (rerun build_data.py)')
    byn=sorted(J.values(),key=lambda e:e['name'].lower())
    xs=[e for e in byn if e['status']=='Scored' and e['evidence_grade']=='A'][0]; xi=[e for e in byn if e['status']=='Insufficient evidence'][0]
    want_s=f"{xs['name']}: {xs['overall_score']}/100, evidence grade {xs['evidence_grade']}, as of {xs['last_reviewed']}"
    want_i=f"{xi['name']}: insufficient evidence to score (no overall score), as of {xi['last_reviewed']}"
    cu=_hh.unescape(ct)
    for w in (want_s,want_i,xs['url'],xi['url'],f"has an overall score of {xs['overall_score']}/100 with evidence grade {xs['evidence_grade']}"):
        if w not in cu: E(f'citing.html: example text not matching agents.json: {w!r}')
    if want_s not in B.CITATION: E('CITATION example not matching agents.json')
    for w in (B.FEED_DISCLAIMER,B.LICENSE,B.CITE_GEN_NOTE.format(gen=B.changelog_date()),B.ATTRIBUTION,B.CODE_SCOPE,B.LICENSE_FILE,B.QUOTE_DISCLAIMER):
        if w not in cu: E(f'citing.html: required text missing: {w[:60]!r}')
    for f_,t_ in (('citing.html',cu),('llms.txt',L),('CITATION',B.CITATION)):
        if re.search(r'None/100|\bNone\b,? evidence grade|'+re.escape(xi['name'])+r': 0/100|evidence grade Insufficient',t_): E(f'{f_}: unsafe Insufficient wording')
    m_=re.search(r'<table class="stack dont">.*?</table>',ct,re.S)
    if not m_: E('citing.html: do/don\'t table missing')
    else:
        outside=_vis(ct.replace(m_.group(0),'')); inside=_hh.unescape(re.sub(r'<[^>]+>',' ',m_.group(0)))
        for b in B.BANNED_CITE:
            if re.search(b,outside,re.I): E(f'citing.html: banned wording {b!r} outside the don\'ts table')
        for b in B.NEW_BANNED:
            if not re.search(b,inside,re.I): E(f'citing.html: {b!r} expected in the don\'ts table')
    for blk in re.findall(r'<script type="application/ld\+json">(.*?)</script>',ct,re.S):
        if json.loads(blk).get('@type') not in ('WebPage','BreadcrumbList'): E('citing.html: unexpected JSON-LD')
    if re.search(r'"@type":\s*"(Review|AggregateRating|Rating)"|ratingValue|itemprop=',ct): E('citing.html: rating markup')
    if re.search(r'<script(?![^>]*application/ld\+json)',ct): E('citing.html: script found')
    if f"{B.BASE}/citing.html</loc>" not in smx: E('citing.html not in sitemap')
    if f"{B.BASE}/citing.html)" not in L: E('citing.html not in llms.txt')
    if 'href="/citing.html"' not in open(os.path.join(P,'methodology.html')).read(): E('methodology.html: How to cite link missing')
    if 'href="/citing.html"' not in ad or 'id="citation"' not in ad or _hh.escape(B.ATTRIBUTION,quote=False) not in ad: E('agents-data.html: licence summary/link missing')
    if not any('/citing.html' in r['change_html'] for r in clrows): E('citing.html: no changelog/feed row')
    if sum(1 for f in glob.glob(os.path.join(P,'**','*.html'),recursive=True) if '"@type": "Dataset"' in open(f).read() or '"@type":"Dataset"' in open(f).read())!=1: E('expected exactly one Dataset JSON-LD block site-wide')
# typed-in example gone; feeds carry the generated guidance
for f in ['agents-data.html','llms.txt','citing.html']+[c['path'] for c in B.COMPARE]:
    if 'OpenHands (open-source): 61/100' in open(os.path.join(P,f)).read() and B.example_entries()[0]['id']!='openhands': E(f'{f}: typed-in OpenHands example still present')
if json.load(open(os.path.join(P,'updates.json')))['_clearinghouse']['citation']!=B.CITATION: E('updates.json citation guidance stale')
# extended words on compare pages, excluding quoted entry uncertainties
for c in B.COMPARE:
    t=re.sub(r'<ul class="quoted">.*?</ul>','',open(os.path.join(P,c['path'])).read(),flags=re.S)
    for b in B.NEW_BANNED:
        if re.search(b,_vis(t),re.I): E(f"{c['path']}: {b!r} outside quoted uncertainties")
for c in B.COMPARE:
    t=open(os.path.join(P,c['path'])).read(); ev=t[t.index('<h2 id="evidence">'):t.index('<h2 id="citation">')]
    for i in B.compare_ids(c,B.entries()):
        if f'<p>{J[i]["counted_performance_sources"]} counted independent performance source' not in ev or f'Noted uncertainties from the <a href="/agents/{i}.html">' not in ev: E(f"{c['path']}: evidence block for {i} missing")
for f in ['citing.html']+[c['path'] for c in B.COMPARE]:
    if re.search(r'<(ul|ol)[^>]*>\s*<(ul|ol)',open(os.path.join(P,f)).read()): E(f'{f}: list nested directly in a list')
print('citing: checked')
# ---- 0069 ----
foot_={}
for f in glob.glob(os.path.join(P,'**','*.html'),recursive=True):
    rel=os.path.relpath(f,P)
    if rel in B.FOOTER_SKIP: continue
    m=re.search(r'<footer>.*?</footer>',open(f).read(),re.S); foot_.setdefault(m.group(0) if m else None,[]).append(rel)
if len(foot_)!=1: E('footers differ: '+'; '.join(f'{len(v)} pages e.g. {v[0]}' for v in foot_.values()))
gen_pages=['citing.html']+[c['path'] for c in B.COMPARE]
for f in glob.glob(os.path.join(P,'**','*.html'),recursive=True):
    rel=os.path.relpath(f,P)
    if rel in B.FOOTER_SKIP: continue
    t=open(f).read(); ti=_hh.unescape((re.search(r'<title>(.*?)</title>',t) or [None,''])[1]); de=_hh.unescape((re.search(r'<meta name="description" content="([^"]*)"',t) or [None,''])[1])
    if len(de)>160: print(f'WARN {rel}: meta description {len(de)} chars > 160')
for e in J.values():
    y69=yaml.safe_load(open(os.path.join(B.R,'agents',e['id']+'.yaml')))
    if not e.get('scope'): print(f"WARN {e['id']}: empty scope")
    if e.get('grade_note')!=y69.get('grade_note'): E(f"{e['id']}: grade_note in agents.json differs from YAML")
    t=open(os.path.join(P,'agents',e['id']+'.html')).read()
    if y69.get('grade_note') and B.grade_note_html(y69['grade_note']) not in t: E(f"{e['id']}: grade note missing on entry page")
    if not y69.get('grade_note') and 'class="grade-note"' in t: E(f"{e['id']}: stray grade note on entry page")
vj=json.load(open(os.path.join(B.R,'vercel.json')))
if vj.get('outputDirectory')!='public' or set(vj)-{'outputDirectory','cleanUrls','headers','redirects'}: E('vercel.json: unexpected settings')
REDIRECT_0086=[{'source':'/:path((?!google4c18d564fd1acb53\\.html$).*)','has':[{'type':'host','value':'agent-trust-clearinghouse\\.vercel\\.app'}],'destination':B.BASE+'/:path','permanent':True}]  # 0086 D3a: old-host redirect, verification file excluded
if vj.get('redirects')!=REDIRECT_0086: E('vercel.json: redirects not exactly the 0086 old-host redirect')
if [h['source'] for h in vj.get('headers',[])]!=['/updates.xml'] or vj['headers'][0]['headers']!=[{'key':'Content-Type','value':'application/atom+xml; charset=utf-8'}]: E('vercel.json: headers rule not exactly /updates.xml Atom')
print('0069: checked')
# ---- 0070: license files and citation ----
import hashlib,shutil,subprocess
APACHE_SHA1='2b8b815229aa8a61e483fb4ba0588b8b6c491890'  # unmodified https://www.apache.org/licenses/LICENSE-2.0.txt
if hashlib.sha1(open(os.path.join(B.R,'LICENSE'),'rb').read()).hexdigest()!=APACHE_SHA1: E('LICENSE: not the unmodified Apache-2.0 text')
nt=open(os.path.join(B.R,'NOTICE')).read()
if 'Copyright 2026 TrustKeeperAce' not in nt or 'Apache License 2.0' not in nt or 'CC BY 4.0' not in nt: E('NOTICE: copyright or license lines missing')
ld=open(os.path.join(B.R,'LICENSE-DATA.md')).read()
for w in ('https://creativecommons.org/licenses/by/4.0/legalcode','`scripts/`','`public/style.css`','`vercel.json`','logo.svg','favicon.svg','Informational only'):
    if w not in ld: E(f'LICENSE-DATA.md: missing {w}')
rd=open(os.path.join(B.R,'README.md')).read()
if '## License' not in rd or 'Apache-2.0' not in rd or 'CC-BY-4.0' not in rd: E('README: license section missing')
cf=yaml.safe_load(open(os.path.join(B.R,'CITATION.cff')))
if cf.get('cff-version')!='1.2.0' or cf.get('license')!=['CC-BY-4.0','Apache-2.0'] or cf.get('repository-code')!=B.LICENSE_FILE.rsplit('/blob/',1)[0] or not cf.get('authors') or not cf.get('title') or not cf.get('message'): E('CITATION.cff: required fields wrong')
if any(k in cf for k in ('doi','identifiers')): E('CITATION.cff: unexpected identifier (none approved)')
cc=shutil.which('cffconvert') or os.path.expanduser('~/.local/bin/cffconvert')
if os.path.exists(cc):
    r=subprocess.run([cc,'--validate','-i',os.path.join(B.R,'CITATION.cff')],capture_output=True,text=True)
    if r.returncode: E('CITATION.cff: cffconvert validation failed: '+(r.stdout+r.stderr).strip()[:200])
else: print('WARN cffconvert not installed; CITATION.cff structural check only')
for f in ('agents-data.html','citing.html'):
    h=open(os.path.join(P,f)).read()
    if B._e(B.CODE_SCOPE) not in h or B.LICENSE_DATA_FILE not in h: E(f'{f}: license sentence not current')
    if 'not licensed for reuse' in h: E(f'{f}: old code-license sentence present')
if B.LLMS_LICENSE not in open(os.path.join(P,'llms.txt')).read(): E('llms.txt: license line not current')
print('0070: checked')
# ---- 0072: How this directory works ----
_cs=open(os.path.join(B.R,'scripts','check_scores.py')).read()
_W=eval(re.search(r'^W=(\{.*\})$',_cs,re.M).group(1))
if _W!=B.HOW_WEIGHTS: E('0072: callout weights differ from check_scores W')
if 'if n<3:' not in _cs or B.HOW_THRESHOLD!=3: E('0072: threshold differs from check_scores')
_mt=open(os.path.join(P,'methodology.html')).read()
if 'An overall score is given only when there are at least 3 <a' not in _mt and 'at least 3 independent performance sources' not in re.sub('<[^>]+>','',_mt): E('0072: methodology threshold sentence missing')
for lab,w in (('Completion rate',30),('Disputes',20),('Adherence to limits',25),('Evidence quality',25)):
    if f'<td data-label="Factor">{lab}</td><td data-label="Weight">{w}%</td>' not in _mt: E(f'0072: methodology weight {lab} {w}% missing')
_ct=' '.join(B.HOW_CALLOUT); _ft=' '.join(h+' '+x for h,x in B.HOW_FULL)
if 'three independent performance sources' not in _ct or 'at least 3 independent performance sources' not in _ft: E('0072: threshold wording')
for lab,w in (('completion rate',30),('disputes',20),('adherence to limits',25),('evidence quality',25)):
    if f'{lab} ({w}%)' not in _ft: E(f'0072: section weight {lab}')
if B.how_callout_html() not in idx: E('0072: home callout missing or not verbatim')
if idx.find('<aside class="how-dir"')>idx.find('<aside class="how"'): E('0072: callout not above How scores work')
if B.how_section_html() not in _mt: E('0072: methodology section missing or not verbatim')
if _mt.count(f'id="{B.HOW_ANCHOR}"')!=1: E('0072: anchor #how-it-works not unique')
if _mt.find('<section class="how-it-works"')>_mt.find('<h2',_mt.find('<h1')+1) : E('0072: section is not the first section')
if B.HOW_DATA_LINE not in open(os.path.join(P,'agents-data.html')).read(): E('0072: data-page link missing')
if B.HOW_LLMS not in open(os.path.join(P,'llms.txt')).read(): E('0072: llms.txt line missing')
for l in re.findall(r'href="(/methodology\.html#[^"]+)"',idx):
    if not re.search(r'id="'+re.escape(l.split('#')[1])+'"',_mt): E(f'0072: home link {l} does not resolve')
for b in B.BANNED_CITE+[r'\bunlike\b',r'\bonly\b(?! (?:when|if)\b)',r'\bfirst\b',r'\bunique\b']:
    if re.search(b,_ct+' '+_ft+' '+B.HOW_H+' '+B.HOW_CALLOUT_LINK,re.I): E(f'0072: banned {b} in new text')
print('0072: checked')
# 0073: README checks
README_LICENSE='## License\n- **Code** (`scripts/`, `public/style.css`, `vercel.json`): [Apache License 2.0](LICENSE). SPDX: `Apache-2.0`.\n- **Data and text** (`agents/`, `data/`, `public/data/`, feeds, generated pages, `decisions/`, `docs/`): [CC BY 4.0](LICENSE-DATA.md). SPDX: `CC-BY-4.0`.\n- **Not licensed:** the project name, logo and favicon; third-party sources and agent trademarks.\n- How to cite: [CITATION.cff](CITATION.cff) and https://www.agentclearinghouse.org/citing.html\n\nInformational only. Provided as is, without warranties; not a guarantee, endorsement, or certification.\n\n'
_rd=open(os.path.join(B.R,'README.md')).read()
for s_ in ['Phase 1','No agent entries','(none yet)','Scoring rules (v0)','published yet']:
    if s_ in _rd: E(f'0073: README stale phrase {s_!r}')
if README_LICENSE not in _rd: E('0073: README License section not byte-identical to 0070 text')
for l in re.findall(r'\]\(([^)\s]+)\)',_rd):
    if l.startswith('https://www.agentclearinghouse.org/'):
        pth,_,frag=l[len('https://www.agentclearinghouse.org/'):].partition('#')
        f_=os.path.join(P,pth or 'index.html')
        if not os.path.isfile(f_): E(f'0073: README live link {l} has no public/ file')
        elif frag and f'id="{frag}"' not in open(f_).read(): E(f'0073: README anchor {l} missing')
    elif not l.startswith('http'):
        if not os.path.exists(os.path.join(B.R,l)): E(f'0073: README repo link {l} missing')
if ' '.join(B.HOW_CALLOUT) not in _rd: E('0073: README callout not verbatim')
if B.FEED_DISCLAIMER not in _rd: E('0073: README disclaimer not verbatim')
_body=_rd.replace(README_LICENSE,'')
_body=re.sub(r'`[^`]*`|\([^)]*\)|https?://\S+','',_body.replace(' '.join(B.HOW_CALLOUT),'').replace('Python 3',''))
for n_ in re.findall(r'\d+',_body):
    if n_ not in ('0','100'): E(f'0073: README stale-count guard: number {n_}')
_rdb=_rd.replace(B.FEED_DISCLAIMER,'').replace(' '.join(B.HOW_CALLOUT),'')
for b in B.BANNED_CITE+[r'\bunlike\b',r'\bunique\b',r'\branking\b',r'\bverif']:
    if re.search(b,_rdb,re.I): E(f'0073: README banned {b}')
print('0073: checked')
# 0074: llms-full.txt and footer How to cite link
_lf_p=os.path.join(P,B.LLMS_FULL)
if not os.path.isfile(_lf_p): E('0074: llms-full.txt missing')
else:
    _lf=open(_lf_p).read()
    if _lf!=B.llms_full_text(): E('0074: llms-full.txt differs from a fresh generation')
    _J=json.load(open(os.path.join(P,'data','agents.json')))
    _blocks=re.split(r'\n### ',_lf.split('\n## Entries\n',1)[-1].split('\n## Changes\n')[0])[1:]
    _bym={}
    for b_ in _blocks:
        m_=re.search(r'^- Entry page: (\S+)$',b_,re.M)
        if m_: _bym.setdefault(m_.group(1),[]).append(b_)
    for e_ in _J['entries']:
        bl=_bym.get(e_['url'],[])
        if len(bl)!=1: E(f'0074: llms-full entry {e_["id"]} appears {len(bl)} times'); continue
        b_=bl[0]
        if not b_.startswith(e_['name']+'\n'): E(f'0074: llms-full heading mismatch {e_["id"]}')
        if f'- Status: {e_["status"]}\n' not in b_: E(f'0074: llms-full status mismatch {e_["id"]}')
        if e_['status']=='Scored':
            for k_,v_ in e_['scores'].items():
                if f'{k_.replace("_"," ")} {v_}' not in b_: E(f'0074: llms-full score {k_} mismatch {e_["id"]}')
            if f'- Overall score: {e_["overall_score"]}; evidence grade: {e_["evidence_grade"]}\n' not in b_: E(f'0074: llms-full overall/grade mismatch {e_["id"]}')
        elif '- Overall score: none' not in b_: E(f'0074: llms-full Insufficient wording {e_["id"]}')
        if e_.get('grade_note') and f'- Grade note: {e_["grade_note"]}\n' not in b_: E(f'0074: llms-full grade note mismatch {e_["id"]}')
        if f'- Counted independent performance sources: {e_["counted_performance_sources"]};' not in b_: E(f'0074: llms-full counted mismatch {e_["id"]}')
        if f'- Last reviewed: {e_["last_reviewed"]}\n' not in b_: E(f'0074: llms-full last_reviewed mismatch {e_["id"]}')
        if f'Note: {B.FEED_DISCLAIMER} As of {e_["last_reviewed"]}.' not in b_: E(f'0074: llms-full entry disclaimer missing {e_["id"]}')
    if len(_blocks)!=len(_bym) or sum(len(v) for v in _bym.values())!=len(_J['entries']): E(f'0074: llms-full has {len(_bym)} entry blocks for {len(_J["entries"])} entries')
    if not _lf.startswith(f'# Agent Reputation & Trust Clearinghouse: full text for language models\n\n> {B.FEED_DISCLAIMER}\n'): E('0074: llms-full header disclaimer missing')
    if _lf.count(B.FEED_DISCLAIMER)!=len(_J['entries'])+2: E('0074: llms-full disclaimer count wrong')
    _asof=max(e_['last_reviewed'] for e_ in _J['entries'])
    # 0075: dataset.generated follows the changelog date and may be later than the latest last_reviewed
    if f'Data as of {_asof} (' not in _lf or _J['dataset']['generated']<_asof: E(f'0074: llms-full as-of date is not {_asof}')
    _sz=len(_lf.encode())
    if _sz>B.LLMS_FULL_MAX: E(f'0074: llms-full.txt {_sz} bytes > {B.LLMS_FULL_MAX}')
    elif _sz>B.LLMS_FULL_WARN: print(f'WARN llms-full.txt {_sz} bytes > {B.LLMS_FULL_WARN}')
    _fr=_lf.split('\n## Entries\n')[0]+'\n'+_lf.split('\n## Changes\n')[-1]
    for s_ in [B.FEED_DISCLAIMER,B.CITATION,B.LLMS_FULL_DONT,' '.join(B.HOW_CALLOUT)]+[x for _,x in B.HOW_FULL]+['### '+h for h,_ in B.HOW_FULL]: _fr=_fr.replace(s_,'')
    _fr=re.sub(r'https?://\S+','',_fr)
    for b in B.BANNED_CITE+[r'\bunlike\b',r'\bunique\b',r'\branking\b']:
        if re.search(b,_fr,re.I): E(f'0074: llms-full banned {b} in generated framing')
if B.LLMS_FULL_LINE not in open(os.path.join(P,'llms.txt')).read(): E('0074: llms.txt link to llms-full.txt missing')
# 0090 D3: as-of dates on agents-data.html and llms.txt match the data
for _f in ('agents-data.html','llms.txt'):
    if f'Data as of {B.changelog_date()} (' not in open(os.path.join(P,_f)).read(): E(f'0090: {_f} as-of date is not {B.changelog_date()}')
# 0090 D1: the coding-agents caveat names every Coding agent entry
_cc=[c for c in B.COMPARE if c['path']=='compare/coding-agents.html'][0]['caveats'][0]
for _e in B.entries():
    if _e['category']=='Coding agent' and _e['name'].split(' (')[0] not in _cc: E(f"0090: coding-agents caveat does not name {_e['id']}")
if B.LLMS_FULL_DATA_LI not in open(os.path.join(P,'agents-data.html')).read(): E('0074: agents-data.html llms-full item missing')
if 'href="/llms-full.txt"' not in open(os.path.join(P,'citing.html')).read(): E('0074: citing.html llms-full link missing')
for f in glob.glob(os.path.join(P,'**','*.html'),recursive=True):
    rel=os.path.relpath(f,P)
    if rel in B.FOOTER_SKIP: continue
    m=re.search(r'<footer>.*?</footer>',open(f).read(),re.S)
    if not m or B.FOOTER_CITE_AFTER+B.FOOTER_CITE not in m.group(0): E(f'0074: footer How to cite link missing on {rel}')
if 'footer a{white-space:nowrap}' not in open(os.path.join(P,'style.css')).read(): E('0074: footer nowrap CSS rule missing')
print('0074: checked')
# 0075: titles on all pages
_sfx=' — '+B.SITE_NAME; _tseen={}
for f in sorted(glob.glob(os.path.join(P,'**','*.html'),recursive=True)):
    rel=os.path.relpath(f,P)
    if rel in B.FOOTER_SKIP: continue
    h_=open(f).read(); m_=re.findall(r'<title>(.*?)</title>',h_,re.S)
    if len(m_)!=1: E(f'0075: {rel} has {len(m_)} <title> elements'); continue
    ti=_hh.unescape(m_[0])
    if len(ti)>70: E(f'0075: {rel} title {len(ti)} chars > 70')
    if not ti.endswith(_sfx) or len(ti)<=len(_sfx): E(f'0075: {rel} title lacks suffix {_sfx!r}')
    _tseen.setdefault(ti,[]).append(rel)
    for prop,pat in (('og:title',r'<meta property="og:title" content="([^"]*)">'),('twitter:title',r'<meta name="twitter:title" content="([^"]*)">')):
        v_=re.findall(pat,h_)
        if len(v_)>1 or (v_ and _hh.unescape(v_[0])!=ti): E(f'0075: {rel} {prop} differs from title')
    for b in B.BANNED_CITE+[r'\bunlike\b',r'\bunique\b',r'\branking\b',r'\bverif']:
        if re.search(b,ti,re.I): E(f'0075: {rel} banned {b} in title')
for ti,rs in _tseen.items():
    if len(rs)>1: E(f'0075: duplicate title {ti!r} on {rs}')
print(f'0075: checked, {sum(len(v) for v in _tseen.values())} titles, max {max(len(k) for k in _tseen)}')
# 0078: one definition of source counts (B.source_counts) for agents.json, agents.csv and llms-full.txt
_LF=open(os.path.join(P,'llms-full.txt')).read()
if 'other listed sources' in _LF: E('0078: old llms-full label "other listed sources" present')
_csv78={r['id']:r for r in rows}
for k,e in y.items():
    sc=B.source_counts(e)
    if k not in x or k not in _csv78: E(f'0078 {k}: missing in json or csv'); continue
    if sc['counted']!=x[k]['counted_performance_sources']: E(f'0078 {k}: json counted')
    if sc['other']!=x[k]['independent_source_count']['other']: E(f'0078 {k}: json other')
    if _csv78[k]['counted_performance_sources']!=str(sc['counted']): E(f'0078 {k}: csv counted')
    if _csv78[k]['independent_other_sources']!=('' if sc['other'] is None else str(sc['other'])): E(f'0078 {k}: csv other')
    m=re.search(r'^### '+re.escape(e['name'])+r'\n(.*?)(?=^### |^## Changes)',_LF,re.S|re.M)
    if not m: E(f'0078 {k}: llms-full section missing'); continue
    blk78=m.group(1)
    want=(f"- Counted independent performance sources: {sc['counted']}; other sources (as in agents.json): "
          f"{B.other_text(sc['other'])}; all sources listed but not counted: {sc['listed_uncounted']}\n")
    if want not in blk78: E(f'0078 {k}: llms-full count line')
    # 0095: no per-entry source lists in llms-full.txt; one pointer line per entry that has sources
    if re.search(r'^(Counted sources|Sources listed but not counted):',blk78,re.M) or re.search(r'^- https?://',blk78,re.M): E(f'0095 {k}: llms-full source list present')
    if blk78.count(B.LLMS_FULL_SOURCES_LINE)!=(1 if e.get('sources') else 0): E(f'0095 {k}: llms-full sources pointer line missing or repeated')
    if re.search(r'^Other sources:$',blk78,re.M): E(f'0078 {k}: old llms-full heading "Other sources:" present')
print('0078: checked, source counts consistent across agents.json, agents.csv and llms-full.txt')
if _LF.count(B.LLMS_FULL_SOURCES_NOTE)!=1: E('0095: llms-full sources note missing or repeated')
print('0095: checked, llms-full.txt has a sources pointer per entry and no source lists')
# 0096: every source in agents.json is linked on its entry page (process rule; no scoring effect)
_n96=0
for _e96 in json.load(open(os.path.join(P,'data','agents.json')))['entries']:
    _h96=_hh.unescape(open(os.path.join(P,'agents',_e96['id']+'.html')).read())
    _l96={u.rstrip('/') for u in re.findall(r'href="(https?://[^"]+)"',_h96)}
    for _s96 in _e96['sources']:
        _n96+=1
        if _s96['url'].rstrip('/') not in _l96: E(f"0096 {_e96['id']}: source {_s96['url']} ({_s96['kind']}) not linked on its entry page")
print(f'0096: checked, all {_n96} sources in agents.json are linked on their entry pages')
# 0097: every outbound link on an entry page is a source of that entry in agents.json, its homepage, a decision
# record in this repository, or a row in data/page_only_links.yaml; every row there is linked on its page and is
# not also a source of that entry (process rule; no scoring effect)
_pol97=yaml.safe_load(open(os.path.join(P,'..','data','page_only_links.yaml'))) or []
_al97={}
for _r97 in _pol97:
    _k97=(_r97.get('entry'),str(_r97.get('url','')).rstrip('/'))
    if _k97 in _al97: E(f"0097 page_only_links: duplicate row {_k97[0]} {_r97.get('url')}")
    _al97[_k97]=_r97
    if _k97[0] not in x: E(f"0097 page_only_links: unknown entry {_k97[0]}")
    if _r97.get('place') not in ('excluded-list','text'): E(f"0097 page_only_links: {_k97[0]} {_r97.get('url')}: place must be excluded-list or text")
    if not str(_r97.get('note') or '').strip(): E(f"0097 page_only_links: {_k97[0]} {_r97.get('url')}: note missing")
_dec97=re.compile(r'https://github\.com/TrustKeeperAce/agent-trust-clearinghouse/blob/master/decisions/(\d{4}-[a-z0-9-]+\.md)$')
_n97=0; _used97=set()
for _e97 in j['entries']:
    _h97=_hh.unescape(open(os.path.join(P,'agents',_e97['id']+'.html')).read())
    _s97={s['url'].rstrip('/') for s in _e97['sources']}; _hp97=(_e97.get('homepage') or '').rstrip('/')
    for _u97 in dict.fromkeys(re.findall(r'href="(https?://[^"]+)"',_h97)):
        if re.match(r'https?://(www\.)?agentclearinghouse\.org(/|$)',_u97): continue
        _n97+=1; _k=_u97.rstrip('/')
        if (_e97['id'],_k) in _al97:
            _used97.add((_e97['id'],_k))
            if _k in _s97: E(f"0097 {_e97['id']}: {_u97} is a source in agents.json and also in data/page_only_links.yaml (remove the row)")
            continue
        if _k in _s97 or (_hp97 and _k==_hp97): continue
        _m97=_dec97.match(_u97)
        if _m97:
            if not os.path.exists(os.path.join(P,'..','decisions',_m97.group(1))): E(f"0097 {_e97['id']}: decision link {_u97} has no file in decisions/")
            continue
        E(f"0097 {_e97['id']}: outbound link {_u97} is not a source in agents.json, the homepage, a decision record or a row in data/page_only_links.yaml")
for _k,_r97 in _al97.items():
    if _k not in _used97: E(f"0097 page_only_links: {_k[0]} {_r97.get('url')} is not linked on its entry page (fix or remove the row)")
print(f'0097: checked, all {_n97} distinct outbound links on entry pages are sources, homepages, decision records or one of {len(_al97)} listed page-only links')
# 0079: typed independent_source_count.other must equal the number derived from the source list by kind
for k,e in y.items():
    try: d=B.derived_other(e)
    except ValueError as ex: E(f'0079 {ex}'); continue
    if e['independent_source_count']['other']!=d: E(f"0079 {k}: typed other {e['independent_source_count']['other']} != derived {d}")
    t=open(os.path.join(P,'agents',k+'.html')).read()
    m=re.search(r'Independent sources: \d+ performance(?: \([^)]*\))?, (\d+) other',t)
    if m and int(m.group(1))!=d: E(f'0079 {k}: entry page shows {m.group(1)} other, derived {d}')
    if not m and e['overall_score'] is not None: E(f'0079 {k}: scored entry page has no "N other" status text')
print('0079: checked, typed other equals derived other for all entries (and entry-page status text)')

# 0091: funding section verbatim, footer Funding link, privacy wording, Sponsors link only when live, banned words
_mt=open(os.path.join(P,'methodology.html')).read()
if B.funding_section_html() not in _mt: E('0091: methodology funding section missing or not verbatim')
if 'cookies, advertising, sponsored placements, or cross-site tracking' not in _mt: E('0091: privacy sentence missing')
if 'href="#funding">Funding and conflicts of interest</a>' not in _mt: E('0091: corrections link to #funding missing')
if B.FOOTER_FUNDING+B.FOOTER_FUNDING_BEFORE not in open(os.path.join(P,'index.html')).read(): E('0091: footer Funding link missing')
_sp=[os.path.relpath(f,P) for f in glob.glob(os.path.join(P,'**','*.html'),recursive=True) if 'github.com/sponsors/' in open(f).read()]
if B.SPONSORS_LIVE and _sp!=['methodology.html']: E(f'0091: Sponsors link should appear only on methodology.html, found {_sp}')
if not B.SPONSORS_LIVE and _sp: E(f'0091: Sponsors link present before profile is live: {_sp}')
_ft=re.sub('<[^>]+>','',B.funding_section_html())
for b in B.BANNED_CITE+[r'\btrusted\b',r'\brecommend',r'\brated\b',r'\brating']:
    if re.search(b,_ft,re.I): E(f'0091: banned wording {b!r} in funding section')

for m in err: print('ERROR',m)
print(f'entries {len(y)}, csv rows {len(rows)}, {len(err)} error(s)')
sys.exit(1 if err else 0)
