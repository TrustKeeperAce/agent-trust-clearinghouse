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
if 'Citation guidance: '+_h.escape(B.CITATION,quote=False) not in open(os.path.join(P,'agents-data.html')).read(): E('agents-data.html citation guidance missing')
ex_=J.get('openhands')
if not ex_ or f"{ex_['name']}: {ex_['overall_score']}/100, evidence grade {ex_['evidence_grade']}, as of {ex_['last_reviewed']}" not in B.CITATION: E('citation example out of date with agents.json')
print(f'feed: {len(clrows)} changelog rows, {len(jids)} items')
for m in err: print('ERROR',m)
print(f'entries {len(y)}, csv rows {len(rows)}, {len(err)} error(s)')
sys.exit(1 if err else 0)
