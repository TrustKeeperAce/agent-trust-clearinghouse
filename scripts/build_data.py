#!/usr/bin/env python3
"""scripts/build_data.py (decisions 0061, 0065). Generates public/data/agents.json, agents.csv,
schema.json and public/sitemap.xml from agents/*.yaml and the changelog; and (0065) the changelog
table in public/changelog.html plus public/updates.json (JSON Feed 1.1) and public/updates.xml (Atom)
from data/changelog.yaml, the single source of truth for approved changes. Deterministic:
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
CHANGELOG=os.path.join(R,'data','changelog.yaml')
def changelog(): return yaml.safe_load(open(CHANGELOG))
def changelog_date(): return max(str(r['date']) for r in changelog())
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
# ---- 0065: changelog page + update feeds ----
FEED_DISCLAIMER=("Informational only. Scores summarize cited public evidence under published rules; they are not a "
                 "guarantee, endorsement, certification or ranking of quality.")
CITATION=("When quoting a score, include the agent name, overall score and evidence grade, the as-of date "
          "(last_reviewed, or as_of for a feed item), and a link to the entry page, e.g. \"OpenHands (open-source): 61/100, "
          "evidence grade A, as of 2026-10-17 (Agent Reputation & Trust Clearinghouse, CC BY 4.0, "
          "https://agent-trust-clearinghouse.vercel.app/agents/openhands.html)\". Say that the score is informational and "
          "not a guarantee, endorsement, certification or ranking. Do not present directory or feed order as a ranking.")
TAG='tag:agent-trust-clearinghouse,2026:'
ALT=('<link rel="alternate" type="application/feed+json" title="Agent updates (JSON Feed)" href="/updates.json">'
     '<link rel="alternate" type="application/atom+xml" title="Agent updates (Atom)" href="/updates.xml">')
ALT_PAGES=['index.html','changelog.html','agents-data.html']
def html_text(h): 
    import html as H; return H.unescape(re.sub(r'<[^>]+>','',h))
def changelog_table(rows):
    body=''.join(f'<tr><td data-label="Date">{r["date"]}</td><td data-label="Decision"><a href="{r["decision_url"]}">'
                 f'{", ".join(r["decision_packets"])}</a></td><td data-label="Change">{r["change_html"]}</td></tr>' for r in rows)
    return ('<table class="stack"><thead><tr><th scope="col">Date</th><th scope="col">Decision</th>'
            '<th scope="col">Change</th></tr></thead><tbody>'+body+'</tbody></table>')
def vstr(v):
    if v is None: return 'none'
    if v.get('overall_score') is None and v.get('status')=='Insufficient evidence': return 'Insufficient evidence'
    return f"{v.get('overall_score')} / {v.get('evidence_grade')}" if v.get('overall_score') is not None else 'not recorded'
def feed_items(rows,names):
    items=[]
    for r in rows:
        base=dict(decision_packets=r['decision_packets'],decision_url=r['decision_url'],as_of=str(r['date']),disclaimer=FEED_DISCLAIMER)
        text=html_text(r['change_html'])
        if not r['changes']:
            items.append(dict(id=TAG+'update/'+r['id'],url=BASE+'/changelog.html',date=str(r['date']),
                title=f"Site change ({', '.join(r['decision_packets'])})",text=text,tags=['site_change'],
                x=dict(type='site_change',agent_id=None,entry_url=None,before=None,after=None,status=None,**base)))
        for c in r['changes']:
            a,b=c['after'],c['before']; n=names.get(c['agent_id'],c['agent_id'])
            if c['type']=='new_entry': t=f"{n}: new entry, {vstr(a)}"
            elif c['type']=='score_change': t=f"{n}: {vstr(b)} → {vstr(a)}"
            else: t=f"{n}: entry updated, {vstr(a)} (unchanged)"
            items.append(dict(id=TAG+'update/'+r['id']+'/'+c['agent_id'],url=f"{BASE}/agents/{c['agent_id']}.html",date=str(r['date']),
                title=t,text=text,tags=[c['type']],
                x=dict(type=c['type'],agent_id=c['agent_id'],entry_url=f"{BASE}/agents/{c['agent_id']}.html",before=b,after=a,
                       status=(a or {}).get('status'),**base)))
    return items
def build_feeds():
    from xml.sax.saxutils import escape as X
    rows=changelog(); names={e['id']:e['name'] for e in entries()}; gen=changelog_date()
    cp=os.path.join(P,'changelog.html'); t=open(cp).read()
    t=re.sub(r'<table class="stack">.*?</table>',lambda m:changelog_table(rows),t,count=1,flags=re.S)
    open(cp,'w').write(t)
    for f in ALT_PAGES:
        fp=os.path.join(P,f); h=open(fp).read()
        if ALT not in h: h=h.replace('<link rel="stylesheet" href="/style.css">','<link rel="stylesheet" href="/style.css">'+ALT,1)
        open(fp,'w').write(h)
    items=feed_items(rows,names)
    jf={'version':'https://jsonfeed.org/version/1.1','title':'Agent Reputation & Trust Clearinghouse: agent updates',
        'home_page_url':BASE+'/changelog.html','feed_url':BASE+'/updates.json','language':'en',
        'description':'New entries, score and grade changes and other approved changes, newest first. '+FEED_DISCLAIMER,
        'authors':[{'name':'Agent Reputation & Trust Clearinghouse','url':BASE+'/'}],
        '_clearinghouse':{'generated':gen,'license':LICENSE,'disclaimer':FEED_DISCLAIMER,'citation':CITATION,
            'atom_feed':BASE+'/updates.xml','note':'before is null for new entries; values that could not be recovered are null.'},
        'items':[{'id':i['id'],'url':i['url'],'title':i['title'],'content_text':i['text']+' '+FEED_DISCLAIMER,
                  'date_published':i['date']+'T00:00:00Z','tags':i['tags'],'_clearinghouse':i['x']} for i in items]}
    open(os.path.join(P,'updates.json'),'w').write(json.dumps(jf,ensure_ascii=False,indent=1)+'\n')
    a=['<?xml version="1.0" encoding="utf-8"?>','<feed xmlns="http://www.w3.org/2005/Atom">',
       '<title>Agent Reputation &amp; Trust Clearinghouse: agent updates</title>',
       f'<subtitle>{X(FEED_DISCLAIMER)}</subtitle>',f'<id>{TAG}updates</id>',f'<updated>{gen}T00:00:00Z</updated>',
       f'<link rel="self" type="application/atom+xml" href="{BASE}/updates.xml"/>',
       f'<link rel="alternate" type="text/html" href="{BASE}/changelog.html"/>',
       '<author><name>Agent Reputation &amp; Trust Clearinghouse</name></author>',f'<rights>CC BY 4.0 {LICENSE}</rights>']
    for i in items:
        x=i['x']; extra=(f" Before: {vstr(x['before'])}. After: {vstr(x['after'])}." if x['agent_id'] else '')
        a+=['<entry>',f'<id>{X(i["id"])}</id>',f'<title>{X(i["title"])}</title>',f'<updated>{i["date"]}T00:00:00Z</updated>',
            f'<published>{i["date"]}T00:00:00Z</published>',f'<link rel="alternate" type="text/html" href="{X(i["url"])}"/>',
            f'<category term="{i["tags"][0]}"/>',
            f'<summary type="text">{X(i["text"]+extra+" Decision "+", ".join(x["decision_packets"])+". As of "+x["as_of"]+". "+FEED_DISCLAIMER)}</summary>',
            '</entry>']
    a.append('</feed>')
    open(os.path.join(P,'updates.xml'),'w').write('\n'.join(a)+'\n')
    print('changelog rows',len(rows),'feed items',len(items))
if __name__=='__main__': build(); build_feeds()
