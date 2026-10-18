#!/usr/bin/env python3
"""scripts/build_data.py (decision 0061). Generates public/data/agents.json, agents.csv,
schema.json and public/sitemap.xml from agents/*.yaml and the changelog. Deterministic:
'generated' is the latest approved changelog date, not the clock. No score logic here;
values are copied from the approved YAML. Rerun in every packet that changes an entry."""
import os,glob,re,json,csv,io,yaml
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); P=os.path.join(R,'public')
BASE='https://agent-trust-clearinghouse.vercel.app'
RULES='Scoring rules v0.1'
LICENSE='https://creativecommons.org/licenses/by/4.0/'
CONTACT='trustkeeperace@gmail.com'
DISCLAIMER=("Informational only; not a guarantee, endorsement, or certification. Scores reflect public sources "
            "and the stated rules as of each entry's last_reviewed date.")
USAGE=("If you use or quote these scores: they are informational, rule-based assessments of public evidence as of each "
       "entry's last_reviewed date (Scoring rules v0.1). They are not guarantees, endorsements, certifications, or rankings "
       "of overall quality. Quote the factor scores and evidence grade together, include the as-of date, and link the entry "
       "page. Do not describe an entry as 'verified', 'certified', 'approved' or 'trusted' by the Clearinghouse.")
FACTORS=['completion_rate','disputes','adherence_to_limits','evidence_quality']
def changelog_date():
    return max(re.findall(r'<td data-label="Date">(\d{4}-\d\d-\d\d)',open(os.path.join(P,'changelog.html')).read()))
def counted(s): return str(s.get('kind','')).startswith('independent performance') and s.get('counted') is not False
def entries():
    out=[]
    for f in sorted(glob.glob(os.path.join(R,'agents','*.yaml'))):
        if os.path.basename(f).startswith('_'): continue
        d=yaml.safe_load(open(f)); sc=d.get('scores') or {}; isc=d.get('independent_source_count') or {}
        srcs=d.get('sources') or []
        out.append({'id':d['slug'],'name':d['name'],'url':f"{BASE}/agents/{d['slug']}.html",'homepage':d.get('homepage'),
            'category':d.get('category'),'type':d.get('type'),'scope':d.get('scope'),
            'status':'Insufficient evidence' if d.get('overall_score') is None else 'Scored',
            'scores':{k:sc.get(k) for k in FACTORS},'overall_score':d.get('overall_score'),
            'evidence_grade':d.get('evidence_grade'),
            'independent_source_count':{'performance':isc.get('performance'),'other':isc.get('other')},
            'counted_performance_sources':sum(1 for s in srcs if counted(s)),
            'peer_reviewed_counted_sources':sum(1 for s in srcs if counted(s) and s.get('peer_reviewed') is True),
            'last_reviewed':str(d.get('last_reviewed')),'decision_packets':(lambda v:[] if v is None else (v if isinstance(v,list) else [v]))(d.get('decision_packet')),
            'sources':[{'url':s.get('url'),'kind':s.get('kind'),'accessed':str(s.get('accessed')),
                        'counted':counted(s),'peer_reviewed':s.get('peer_reviewed')} for s in srcs]})
    out.sort(key=lambda e:(e['overall_score'] is None,-(e['overall_score'] or 0),e['name'].lower()))
    return out
SCHEMA={"$schema":"https://json-schema.org/draft/2020-12/schema","$id":BASE+"/data/schema.json",
 "title":"Agent Reputation & Trust Clearinghouse export","description":DISCLAIMER,"type":"object",
 "required":["dataset","disclaimer","usage_note","entries"],"additionalProperties":False,
 "properties":{
  "dataset":{"type":"object","required":["name","version","generated","rules","license","canonical","source_repository","corrections_contact","entry_count"],
   "properties":{"name":{"type":"string"},"version":{"type":"string"},"generated":{"type":"string","pattern":"^\\d{4}-\\d{2}-\\d{2}$"},
    "rules":{"type":"string"},"license":{"type":"string","format":"uri"},"canonical":{"type":"string","format":"uri"},
    "source_repository":{"type":"string","format":"uri"},"corrections_contact":{"type":"string"},"entry_count":{"type":"integer","minimum":0}}},
  "disclaimer":{"type":"string","minLength":20},"usage_note":{"type":"string","minLength":20},
  "entries":{"type":"array","items":{"type":"object",
   "required":["id","name","url","category","status","scores","overall_score","evidence_grade","independent_source_count","counted_performance_sources","last_reviewed","sources"],
   "properties":{"id":{"type":"string","pattern":"^[a-z0-9-]+$","description":"Stable ID (slug); never reused"},
    "name":{"type":"string"},"url":{"type":"string","format":"uri"},"homepage":{"type":["string","null"]},
    "category":{"type":"string"},"type":{"type":["string","null"]},"scope":{"type":["string","null"]},
    "status":{"enum":["Scored","Insufficient evidence","withdrawn"]},
    "scores":{"type":"object","required":FACTORS,"properties":{k:{"type":["integer","null"],"minimum":0,"maximum":100} for k in FACTORS}},
    "overall_score":{"type":["integer","null"],"minimum":0,"maximum":100},
    "evidence_grade":{"enum":["A","B","B-","Insufficient evidence"]},
    "independent_source_count":{"type":"object","properties":{"performance":{"type":["integer","null"]},"other":{"type":["integer","null"]}}},
    "counted_performance_sources":{"type":"integer","minimum":0},"peer_reviewed_counted_sources":{"type":"integer","minimum":0},
    "last_reviewed":{"type":"string","pattern":"^\\d{4}-\\d{2}-\\d{2}$"},"decision_packets":{"type":"array","items":{"type":"string"}},
    "sources":{"type":"array","items":{"type":"object","required":["url","kind","accessed","counted"],
      "properties":{"url":{"type":"string"},"kind":{"type":"string"},"accessed":{"type":"string"},"counted":{"type":"boolean"},"peer_reviewed":{"type":["boolean","null"]}}}}}}}}}
CSV_COLS=['id','name','url','category','status','completion_rate','disputes','adherence_to_limits','evidence_quality',
          'overall_score','evidence_grade','independent_performance_sources','independent_other_sources',
          'counted_performance_sources','last_reviewed','license','disclaimer']
def build():
    gen=changelog_date(); E=entries()
    doc={'dataset':{'name':'Agent Reputation & Trust Clearinghouse','version':f'{RULES}; data {gen}','generated':gen,'rules':RULES,
         'license':LICENSE,'canonical':BASE+'/agents-data.html','source_repository':'https://github.com/TrustKeeperAce/agent-trust-clearinghouse',
         'corrections_contact':CONTACT,'entry_count':len(E)},'disclaimer':DISCLAIMER,'usage_note':USAGE,'entries':E}
    os.makedirs(os.path.join(P,'data'),exist_ok=True)
    open(os.path.join(P,'data','agents.json'),'w').write(json.dumps(doc,ensure_ascii=False,indent=1)+'\n')
    open(os.path.join(P,'data','schema.json'),'w').write(json.dumps(SCHEMA,ensure_ascii=False,indent=1)+'\n')
    b=io.StringIO(); w=csv.writer(b,lineterminator='\n'); w.writerow(CSV_COLS)
    for e in E:
        s=e['scores']; w.writerow([e['id'],e['name'],e['url'],e['category'],e['status']]+[('' if s[k] is None else s[k]) for k in FACTORS]+
            ['' if e['overall_score'] is None else e['overall_score'],e['evidence_grade'],e['independent_source_count']['performance'],
             e['independent_source_count']['other'],e['counted_performance_sources'],e['last_reviewed'],LICENSE,DISCLAIMER])
    open(os.path.join(P,'data','agents.csv'),'w').write(b.getvalue())
    # sitemap: entry pages use last_reviewed; site pages use latest changelog date
    urls=[(f"/agents/{e['id']}.html",e['last_reviewed']) for e in sorted(E,key=lambda e:e['id'])]
    urls+=[('/',gen),('/methodology.html',gen),('/changelog.html',gen),('/agents-data.html',gen)]
    sm='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(
        f'  <url><loc>{BASE}{u}</loc><lastmod>{d}</lastmod></url>\n' for u,d in urls)+'</urlset>\n'
    open(os.path.join(P,'sitemap.xml'),'w').write(sm)
    print('entries',len(E),'generated',gen,'sitemap urls',len(urls))
if __name__=='__main__': build()
