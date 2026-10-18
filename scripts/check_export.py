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
import os,sys,re,json,csv,glob
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
print('citing: checked')
for m in err: print('ERROR',m)
print(f'entries {len(y)}, csv rows {len(rows)}, {len(err)} error(s)')
sys.exit(1 if err else 0)
