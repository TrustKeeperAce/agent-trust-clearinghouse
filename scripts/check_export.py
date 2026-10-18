#!/usr/bin/env python3
"""scripts/check_export.py (decision 0061). Read-only. Checks that public/data/* match the YAML
entries and the rendered pages (index, entry pages, llms.txt, sitemap), that every CSV row carries
the disclaimer and license, that agents.json validates against schema.json (if the jsonschema
package is installed), and that all JSON-LD parses and contains no Review/AggregateRating/Rating.
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
for m in err: print('ERROR',m)
print(f'entries {len(y)}, csv rows {len(rows)}, {len(err)} error(s)')
sys.exit(1 if err else 0)
