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
            'evidence_grade':d.get('evidence_grade'),'grade_note':d.get('grade_note'),
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
    "evidence_grade":{"enum":["A","B","B-","Insufficient evidence"]},"grade_note":{"type":["string","null"]},
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
# 0067: citation examples are generated from the data (never typed in)
def _by_name(E): return sorted(E,key=lambda e:e['name'].lower())
def example_entries(E=None):
    E=E if E is not None else entries()
    sc=[e for e in _by_name(E) if e['status']=='Scored' and e['evidence_grade']=='A']
    ins=[e for e in _by_name(E) if e['status']=='Insufficient evidence']
    return sc[0],ins[0]
SITE_NAME='Agent Reputation & Trust Clearinghouse'
def score_phrase(e):
    if e['overall_score'] is None: return f"{e['name']}: insufficient evidence to score (no overall score), as of {e['last_reviewed']}"
    return f"{e['name']}: {e['overall_score']}/100, evidence grade {e['evidence_grade']}, as of {e['last_reviewed']}"
def quote_line(e): return f"{score_phrase(e)} — {SITE_NAME}, {e['url']}, CC BY 4.0. {QUOTE_DISCLAIMER}"
QUOTE_DISCLAIMER="Informational only; not a guarantee, endorsement, certification or ranking."
_EXS,_EXI=example_entries()
CITATION=("When quoting a score, include the agent name, overall score and evidence grade, the as-of date "
          f"(last_reviewed, or as_of for a feed item), and a link to the entry page, e.g. \"{score_phrase(_EXS)} ({SITE_NAME}, CC BY 4.0, "
          f"{_EXS['url']})\". Say that the score is informational and "
          "not a guarantee, endorsement, certification or ranking. Do not present directory or feed order as a ranking. "
          f"More examples: {BASE}/citing.html")
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

# ---- 0066: comparison pages (generated; values only from entries()) ----
import html as _H
def _e(s): return _H.escape(str(s),quote=True)
COMPARE=[
 {'path':'compare/claude-code-and-openai-codex.html','h1':'Claude Code and OpenAI Codex compared: public evidence','title':'Claude Code and Codex compared: public evidence',
  'short':'Claude Code and OpenAI Codex compared',
  'desc':'Factor scores, evidence grades and counted independent sources for Claude Code and OpenAI Codex. Informational; not a ranking.',
  'groups':[('Entries',['claude-code','openai-codex'])],
  'caveats':['The two entries cover different products: the OpenAI Codex entry includes the cloud agent that opens pull requests as well as the CLI, IDE extension and desktop app; the Claude Code entry covers the CLI and headless mode only. Read each scope before comparing.',
             'Both entries combine many versions and the models each tool used at the time of each study.']},
 {'path':'compare/coding-agents.html','h1':'Coding agents compared: public evidence','short':'Coding agents compared',
  'desc':'Factor scores, evidence grades and counted independent sources for the coding agents in the directory. Informational; not a ranking.',
  'groups':[('Coding agent entries',('category','Coding agent'))],
  'caveats':['Open-source frameworks (OpenHands, SWE-agent, Aider) are run with a language model chosen by the user, so their evidence mixes many models; managed products (Claude Code, OpenAI Codex, GitHub Copilot coding agent, Devin) are tested as shipped.',
             'Some entries are cloud agents that open pull requests and others are command-line tools; read each scope before comparing.']},
 {'path':'compare/research-agents.html','h1':'Research and deep-research agents compared: public evidence','title':'Research agents compared: public evidence','short':'Research agents compared',
  'desc':'Factor scores, evidence grades and counted independent sources for the research and deep-research agents in the directory. Informational; not a ranking.',
  'groups':[('Academic search and review tools',['consensus','elicit']),
            ('General research and deep-research agents',('category','Research',['consensus','elicit']))],
  'related':[('perplexity','Perplexity is listed in the Verification category, scoped to citation-backed answering, so it is not included here.')],
  'caveats':['Academic search tools (Elicit, Consensus) are mostly tested on finding and summarising papers; general deep-research agents are tested on open web research tasks. Scores are not directly comparable across these groups.']},
]
COMPARE_CAVEATS=['Scores summarize the counted independent sources for each entry; they are not production outcomes and are not a ranking of quality.',
                 'Entries are reviewed separately, with different sources and dates; a higher overall score does not mean one agent is better for a given task.']
BANNED=[r'\bbest\b',r'\btop\b',r'\bwinners?\b',r'which is better',r'\bstars?\b','★',r'#1\b']
def _yaml_by_id():
    o={}
    for f in sorted(glob.glob(os.path.join(R,'agents','*.yaml'))):
        if os.path.basename(f).startswith('_'): continue
        d=yaml.safe_load(open(f)); o[d['slug']]=d
    return o
def first_sentence(s):
    s=' '.join(str(s or '').split()); m=re.match(r'(.+?[.!?])(\s|$)',s); return m.group(1) if m else s
def scope_text(e,y):
    return (e['scope'],False) if e.get('scope') else (first_sentence(y.get('summary')),True)
def compare_groups(c,E):
    out=[]
    for title,sel in c['groups']:
        if isinstance(sel,tuple): ids=[e['id'] for e in E if e['category']==sel[1] and e['id'] not in (sel[2] if len(sel)>2 else [])]
        else: ids=list(sel)
        out.append((title,ids))
    return out
def compare_ids(c,E): return [i for _,ids in compare_groups(c,E) for i in ids]
def _row(e):
    s=e['scores']; ins=e['overall_score'] is None; d=lambda v:'—' if v is None else v
    return (f'<tr><th scope="row" data-label="Agent"><a href="/agents/{e["id"]}.html">{_e(e["name"])}</a></th>'
            f'<td data-label="Overall score" class="num">{d(e["overall_score"])}</td>'
            f'<td data-label="Evidence grade">{_e(e["evidence_grade"])}</td>'
            +''.join(f'<td data-label="{l}" class="num">{d(s[k])}</td>' for k,l in zip(FACTORS,['Completion','Disputes','Adherence','Evidence quality']))+
            f'<td data-label="Counted sources (peer-reviewed)" class="num">{e["counted_performance_sources"]} ({e["peer_reviewed_counted_sources"]})</td>'
            f'<td data-label="Last reviewed"><time datetime="{e["last_reviewed"]}">{e["last_reviewed"]}</time></td></tr>')
TH=('<thead><tr><th scope="col">Agent</th><th scope="col">Overall score</th><th scope="col">Evidence grade</th><th scope="col">Completion</th>'
    '<th scope="col">Disputes</th><th scope="col">Adherence</th><th scope="col">Evidence quality</th><th scope="col">Counted sources (peer-reviewed)</th><th scope="col">Last reviewed</th></tr></thead>')
def render_compare(c,E,Y,gen,shell):
    J={e['id']:e for e in E}; ids=compare_ids(c,E); url=f'{BASE}/{c["path"]}'
    lr=sorted(J[i]['last_reviewed'] for i in ids)
    title=f'{_e(c.get("title",c["h1"]))} — Agent Reputation &amp; Trust Clearinghouse'
    ld1={'@context':'https://schema.org','@type':'ItemList','name':c['h1'],'itemListOrder':'https://schema.org/ItemListUnordered','numberOfItems':len(ids),
         'itemListElement':[{'@type':'ListItem','position':n+1,'name':J[i]['name'],'url':J[i]['url']} for n,i in enumerate(ids)]}
    ld2={'@context':'https://schema.org','@type':'BreadcrumbList','itemListElement':[
         {'@type':'ListItem','position':1,'name':'Directory','item':BASE+'/'},{'@type':'ListItem','position':2,'name':c['short'],'item':url}]}
    head=(f'<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">\n'
          f'<title>{title}</title><meta name="description" content="{_e(c["desc"])}"><link rel="canonical" href="{url}">'
          f'<meta property="og:type" content="article"><meta property="og:site_name" content="Agent Reputation &amp; Trust Clearinghouse">'
          f'<meta property="og:title" content="{title}"><meta property="og:description" content="{_e(c["desc"])}"><meta property="og:url" content="{url}">'
          f'<meta name="twitter:card" content="summary"><meta name="twitter:title" content="{title}"><meta name="twitter:description" content="{_e(c["desc"])}">'
          f'<link rel="icon" href="/favicon.svg" type="image/svg+xml"><meta name="theme-color" content="#0a0d12" media="(prefers-color-scheme: dark)"><meta name="theme-color" content="#f6f7f9" media="(prefers-color-scheme: light)">'
          f'<link rel="stylesheet" href="/style.css">{ALT}'
          f'<script type="application/ld+json">{json.dumps(ld1,ensure_ascii=False)}</script><script type="application/ld+json">{json.dumps(ld2,ensure_ascii=False)}</script></head>')
    b=[f'<nav aria-label="Breadcrumb"><p><a href="/">Directory</a> › <span aria-current="page">{_e(c["short"])}</span></p></nav>',
       f'<h1>{_e(c["h1"])}</h1>',
       f'<p class="notice"><strong>{FEED_DISCLAIMER}</strong></p>',
       f'<p><em>Data as of {gen} ({RULES}); entries last reviewed {lr[0]}{"" if lr[0]==lr[-1] else " to "+lr[-1]}. Generated from <a href="/data/agents.json">agents.json</a>; values match each entry page.</em></p>',
       '<h2 id="scope">Scope of each entry</h2><p>Read the scope before comparing: entries cover different products, versions and modes.</p><ul>']
    for i in ids:
        t,fb=scope_text(J[i],Y[i]); b.append(f'<li><a href="/agents/{i}.html">{_e(J[i]["name"])}</a>: {_e(t)}{" (summary)" if fb else ""}</li>')
    b.append('</ul><ul>'+''.join(f'<li>{_e(x)}</li>' for x in c['caveats'])+'</ul>')
    b.append('<h2 id="table">Scores and evidence</h2><p>Listed alphabetically within each group, not by score. Factor scores are 0–100; see the <a href="/methodology.html">methodology</a> for weights and evidence grades.</p>')
    for gt,gids in compare_groups(c,E):
        sc=sorted([i for i in gids if J[i]['overall_score'] is not None],key=lambda i:J[i]['name'].lower())
        ins=sorted([i for i in gids if J[i]['overall_score'] is None],key=lambda i:J[i]['name'].lower())
        if len(c['groups'])>1: b.append(f'<h3>{_e(gt)}</h3>')
        b.append('<table class="stack cmp">'+TH+'<tbody>'+''.join(_row(J[i]) for i in sc+ins)+'</tbody></table>')
        if ins: b.append('<p>Entries marked Insufficient evidence have fewer than 3 counted independent performance sources and no overall score.</p>')
    b.append('<h2 id="evidence">What the evidence does and doesn’t show</h2><ul>'+''.join(f'<li>{_e(x)}</li>' for x in COMPARE_CAVEATS)+'</ul>')
    for i in sorted(ids,key=lambda i:J[i]['name'].lower()):
        e=J[i]; u=[x for x in (Y[i].get('uncertainties') or []) if isinstance(x,str)][:2]
        b.append(f'<h3>{_e(e["name"])}</h3><p>{e["counted_performance_sources"]} counted independent performance source{"s" if e["counted_performance_sources"]!=1 else ""} '
                 f'({e["peer_reviewed_counted_sources"]} peer-reviewed). Noted uncertainties from the <a href="/agents/{i}.html">entry page</a>:</p>'
                 +('' if not u else '<ul class="quoted">'+''.join(f'<li>{_e(x)}</li>' for x in u)+'</ul>'))
    for rid,txt in c.get('related',[]):
        b.append(f'<p>Related: <a href="/agents/{rid}.html">{_e(J[rid]["name"])}</a>. {_e(txt)}</p>')
    b.append(f'<h2 id="citation">Citation guidance</h2><p>{_e(CITATION)}</p>')
    b.append('<h2 id="more">More</h2><ul><li><a href="/methodology.html">Methodology</a> (factors, weights, evidence grades)</li><li><a href="/changelog.html">Changelog</a> and <a href="/updates.json">update feed</a></li><li><a href="/agents-data.html">For agents / data</a> (JSON, CSV, license)</li></ul>')
    return head+shell[0]+'\n'.join(b)+'\n'+shell[1]
COMPARE_LINKS=('<p class="compare-links">Compare: '+' · '.join(f'<a href="/{c["path"]}">{_e(c["short"])}</a>' for c in COMPARE)+'</p>')
def build_compare():
    E=entries(); Y=_yaml_by_id(); gen=changelog_date()
    t=open(os.path.join(P,'agents-data.html')).read()
    shell=(t[t.index('</head>')+7:t.index('<main id="main">')+16]+'\n', t[t.index('</main>'):])
    os.makedirs(os.path.join(P,'compare'),exist_ok=True)
    for c in COMPARE: open(os.path.join(P,c['path']),'w').write(render_compare(c,E,Y,gen,shell))
    for f,anchor in (('index.html','<section aria-labelledby="scored">'),('methodology.html','<p>Each factor is scored 0–100')):
        fp=os.path.join(P,f); h=open(fp).read()
        h=re.sub(r'<p class="compare-links">.*?</p>','',h)
        assert anchor in h, f
        h=h.replace(anchor,COMPARE_LINKS+anchor,1); open(fp,'w').write(h)
    sm=open(os.path.join(P,'sitemap.xml')).read()
    add=''.join(f'  <url><loc>{BASE}/{c["path"]}</loc><lastmod>{max([e["last_reviewed"] for e in E if e["id"] in compare_ids(c,E)])}</lastmod></url>\n' for c in COMPARE)
    sm=re.sub(r'  <url><loc>[^<]*/compare/[^<]*</loc>.*?\n','',sm).replace('</urlset>',add+'</urlset>')
    open(os.path.join(P,'sitemap.xml'),'w').write(sm)
    print('compare pages',len(COMPARE))


# ---- 0067: citing page (generated; values only from entries() and the dataset block) ----
BANNED_CITE=BANNED+[r'\bcertified\b',r'\bverified\b',r'\bendorsed\b']
NEW_BANNED=BANNED_CITE[len(BANNED):]
CITE_PATH='citing.html'
CITE_TITLE='How to cite and quote this data'
CITE_DESC='Ready-to-copy citations (plain, APA-style, BibTeX, agent template), CC BY 4.0 attribution and how to quote scores. Informational only.'
LICENSE_FILE='https://github.com/TrustKeeperAce/agent-trust-clearinghouse/blob/master/LICENSE'
REPO='https://github.com/TrustKeeperAce/agent-trust-clearinghouse'
ATTRIBUTION=f'{SITE_NAME}, <entry URL>, data as of YYYY-MM-DD, CC BY 4.0.'
CODE_SCOPE='The code (scripts/, the stylesheet and vercel.json) is licensed under the Apache License 2.0; CC BY 4.0 covers the data, the decision records and the site text, including generated files. The project name, logo and favicon are not licensed.'
LICENSE_DATA_FILE='https://github.com/TrustKeeperAce/agent-trust-clearinghouse/blob/master/LICENSE-DATA.md'
LLMS_LICENSE=f'Data and site text: CC BY 4.0 ({LICENSE}). Code: Apache-2.0 ({LICENSE_FILE}). The project name, logo and favicon are not licensed.'
CITE_GEN_NOTE='Example values on this page are generated from the data as of {gen}; check the entry page for current values.'
DONTS=[('Include the agent name, overall score out of 100, evidence grade, as-of date and a link to the entry page.','Drop the as-of date, or quote a score without its evidence grade.'),
 ('Say the score is informational and not a guarantee, endorsement, certification or ranking.','Call an agent “best”, “top”, “#1” or a “winner”, or say it is “certified”, “verified”, “approved” or “endorsed” by the Clearinghouse.'),
 ('Say “insufficient evidence to score” when an entry has no overall score.','Turn Insufficient evidence into 0, a low score or a failure.'),
 ('Link to the entry page, or to the feed item for a change.','Present directory, table or feed order as a ranking.'),
 ('Note any changes you made to the data (CC BY 4.0 requires it).','Imply the Clearinghouse tested the agent itself; scores summarize cited public evidence.'),
 ('Check the live entry page before republishing an older quote.','Use the logo or site styling to suggest a partnership; the logo is not licensed.')]
def _bib(s): return s.replace('\\','\\textbackslash{}').replace('&','\\&').replace('%','\\%').replace('_','\\_').replace('#','\\#')
def cite_formats(E,ds):
    s,i=example_entries(E); gen=ds['generated']; yr=gen[:4]
    return {'scored':s,'insufficient':i,
     'template':'{name}: {overall}/100, evidence grade {grade}, as of {last_reviewed} — '+SITE_NAME+', {entry_url}, CC BY 4.0. '+QUOTE_DISCLAIMER,
     'template_ins':'{name}: insufficient evidence to score (no overall score), as of {last_reviewed} — '+SITE_NAME+', {entry_url}, CC BY 4.0. '+QUOTE_DISCLAIMER,
     'q_scored':quote_line(s),'q_ins':quote_line(i),
     'plain':(f"According to the {SITE_NAME}, {s['name']} has an overall score of {s['overall_score']}/100 with evidence grade {s['evidence_grade']}, "
              f"as of {s['last_reviewed']} ({s['url']}, CC BY 4.0). The score is informational and is not an endorsement, certification or ranking."),
     'apa_entry':f"{SITE_NAME}. ({yr}). {s['name']} [Data set entry; {ds['rules'].lower()}; last reviewed {s['last_reviewed']}]. Retrieved {gen}, from {s['url']}. CC BY 4.0.",
     'apa_dataset':f"{SITE_NAME}. ({yr}). {SITE_NAME} dataset (Version: {ds['version'][0].lower()+ds['version'][1:]}) [Data set]. {ds['canonical']}. CC BY 4.0.",
     'bibtex':('@misc{atc_dataset_'+gen.replace('-','_')+',\n'
               f"  author       = {{{{{_bib(SITE_NAME)}}}}},\n  title        = {{{_bib(SITE_NAME)} dataset}},\n  year         = {{{yr}}},\n"
               f"  version      = {{{ds['version']}}},\n  howpublished = {{\\url{{{BASE}/data/agents.json}}}},\n"
               f"  note         = {{CC BY 4.0. Informational only; not an endorsement, certification or ranking. Accessed {gen}.}}\n}}")}
def _ds(E):
    gen=changelog_date()
    return {'generated':gen,'rules':RULES,'version':f'{RULES}; data {gen}','canonical':BASE+'/agents-data.html'}
def render_citing(E,shell):
    ds=_ds(E); f=cite_formats(E,ds); gen=ds['generated']; url=f'{BASE}/{CITE_PATH}'
    title=f'{CITE_TITLE} — Agent Reputation &amp; Trust Clearinghouse'
    ld1={'@context':'https://schema.org','@type':'WebPage','name':CITE_TITLE,'url':url,'description':CITE_DESC,'license':LICENSE,'dateModified':gen}
    ld2={'@context':'https://schema.org','@type':'BreadcrumbList','itemListElement':[
         {'@type':'ListItem','position':1,'name':'Directory','item':BASE+'/'},{'@type':'ListItem','position':2,'name':'How to cite','item':url}]}
    head=(f'<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">\n'
          f'<title>{title}</title><meta name="description" content="{_e(CITE_DESC)}"><link rel="canonical" href="{url}">'
          f'<meta property="og:type" content="article"><meta property="og:site_name" content="Agent Reputation &amp; Trust Clearinghouse">'
          f'<meta property="og:title" content="{title}"><meta property="og:description" content="{_e(CITE_DESC)}"><meta property="og:url" content="{url}">'
          f'<meta name="twitter:card" content="summary"><meta name="twitter:title" content="{title}"><meta name="twitter:description" content="{_e(CITE_DESC)}">'
          f'<link rel="icon" href="/favicon.svg" type="image/svg+xml"><meta name="theme-color" content="#0a0d12" media="(prefers-color-scheme: dark)"><meta name="theme-color" content="#f6f7f9" media="(prefers-color-scheme: light)">'
          f'<link rel="stylesheet" href="/style.css">{ALT}'
          f'<script type="application/ld+json">{json.dumps(ld1,ensure_ascii=False)}</script><script type="application/ld+json">{json.dumps(ld2,ensure_ascii=False)}</script></head>')
    pre=lambda t:f'<pre><code>{_e(t)}</code></pre>'
    s,i=f['scored'],f['insufficient']
    b=['<nav aria-label="Breadcrumb"><p><a href="/">Directory</a> › <span aria-current="page">How to cite</span></p></nav>',
       f'<h1>{CITE_TITLE}</h1>',f'<p class="notice"><strong>{FEED_DISCLAIMER}</strong></p>',
       f'<p><em>{CITE_GEN_NOTE.format(gen=gen)}</em> Examples use the alphabetically first entry with evidence grade A ({_e(s["name"])}) and the alphabetically first entry with insufficient evidence ({_e(i["name"])}); the choice says nothing about either agent.</p>',
       '<h2 id="agents">Quoting a score (agents and tools)</h2><p>Use one line with every field. Template:</p>'+pre(f['template']),
       '<p>Example:</p>'+pre(f['q_scored']),
       '<p>When an entry has no overall score:</p>'+pre(f['template_ins'])+'<p>Example:</p>'+pre(f['q_ins']),
       '<p>For a change from the <a href="/updates.json">update feed</a>, use the item’s <code>as_of</code> date and the entry URL.</p>',
       '<h2 id="plain">Plain sentence</h2>'+pre(f['plain']),
       '<h2 id="apa">APA-style</h2><p>Laid out in APA style; check your style guide for exact requirements.</p><p>One entry:</p>'+pre(f['apa_entry'])+'<p>The whole dataset:</p>'+pre(f['apa_dataset']),
       '<h2 id="bibtex">BibTeX (dataset)</h2>'+pre(f['bibtex']),
       '<h2 id="attribution">Attribution (CC BY 4.0)</h2>'
       f'<p>The data and the site text are licensed under <a href="{LICENSE}">Creative Commons Attribution 4.0 International (CC BY 4.0)</a>. You may share and adapt them, including commercially, if you:</p>'
       f'<ul><li>credit “{_e(SITE_NAME)}”;</li><li>link to the license;</li><li>link to the entry page or dataset you used;</li><li>say if you changed anything;</li><li>keep the disclaimer with quoted scores.</li></ul>'
       f'<p>Suggested attribution: <q>{_e(ATTRIBUTION)}</q></p><p>{_e(CODE_SCOPE)} See <a href="{LICENSE_DATA_FILE}">LICENSE-DATA.md</a> and <a href="{LICENSE_FILE}">LICENSE</a>. Cited third-party sources, agent names and trademarks remain under their owners’ terms.</p>',
       '<h2 id="quoting">How to quote us</h2><table class="stack dont"><thead><tr><th scope="col">Do</th><th scope="col">Don’t</th></tr></thead><tbody>'
       +''.join(f'<tr><td data-label="Do">{_e(d)}</td><td data-label="Don’t">{_e(n)}</td></tr>' for d,n in DONTS)+'</tbody></table>',
       '<h2 id="machine-readable">Machine-readable locations</h2><ul>'
       '<li><a href="/data/agents.json">agents.json</a>, <a href="/data/agents.csv">agents.csv</a> and <a href="/data/schema.json">schema.json</a>: the data (CC BY 4.0). Field definitions are on <a href="/agents-data.html">For agents / data</a>.</li>'
       '<li><a href="/updates.json">updates.json</a> (JSON Feed) and <a href="/updates.xml">updates.xml</a> (Atom): changes, newest first (CC BY 4.0).</li>'
       '<li><a href="/llms.txt">llms.txt</a>: a summary for language-model agents.</li>'
       '<li><a href="/llms-full.txt">llms-full.txt</a>: all entries in one plain-text file, generated from the same data.</li><li><a href="/sitemap.xml">sitemap.xml</a>: all pages.</li>'
       f'<li><a href="{REPO}">GitHub repository</a>: data, decision records and site source. {_e(CODE_SCOPE)}</li>'
       '<li>Corrections: <a href="mailto:trustkeeperace@gmail.com?subject=Correction%20request">trustkeeperace@gmail.com</a>.</li></ul>',
       f'<h2 id="disclaimer">Disclaimer</h2><p>{FEED_DISCLAIMER}</p>']
    return head+shell[0]+'\n'.join(b)+'\n'+shell[1]
DATA_LICENSE=lambda: ('<h2 id="license">License and citation</h2>\n'
  f'<p>The data and the site text are licensed under <a href="{LICENSE}">Creative Commons Attribution 4.0 International (CC BY 4.0)</a>. You may share and adapt them, including commercially, if you give credit. Cited third-party sources remain under their own terms. {_e(CODE_SCOPE)} See <a href="{LICENSE_DATA_FILE}">LICENSE-DATA.md</a> and <a href="{LICENSE_FILE}">LICENSE</a>.</p>\n'
  f'<p>Suggested citation: <q>{_e(ATTRIBUTION)}</q></p>\n'
  '<p id="citation">Ready-to-copy citations (plain sentence, APA-style, BibTeX, agent template) and how to quote a score: <a href="/citing.html">How to cite and quote this data</a>.</p>\n')
CITE_LINK_METH='<p class="cite-link">Citing or quoting scores: <a href="/citing.html">How to cite</a>.</p>'
def build_citing():
    E=entries(); t=open(os.path.join(P,'agents-data.html')).read()
    t=re.sub(r'<h2 id="license">.*?(?=<h2 id="updates">)',lambda m:DATA_LICENSE(),t,count=1,flags=re.S)
    open(os.path.join(P,'agents-data.html'),'w').write(t)
    shell=(t[t.index('</head>')+7:t.index('<main id="main">')+16]+'\n', t[t.index('</main>'):])
    open(os.path.join(P,CITE_PATH),'w').write(render_citing(E,shell))
    mp=os.path.join(P,'methodology.html'); h=open(mp).read(); h=re.sub(r'<p class="cite-link">.*?</p>','',h)
    a='<h2 id="disclaimer">'; assert a in h; open(mp,'w').write(h.replace(a,CITE_LINK_METH+a,1))
    lp=os.path.join(P,'llms.txt'); L=open(lp).read()
    L=re.sub(r'^Citation guidance: .*$',lambda m:'Citation guidance: '+CITATION,L,count=1,flags=re.M)
    L=re.sub(r'^- \[How to cite\].*\n','',L,flags=re.M)
    L=re.sub(r'Data and site text: CC BY 4\.0 .*$',lambda m:LLMS_LICENSE,L,count=1,flags=re.M)
    ln=f'- [How to cite]({BASE}/citing.html): ready-to-copy citations, agent quote template, how to quote scores, license scope\n'
    k=L.index('- [For agents / data]'); k=L.index('\n',k)+1; L=L[:k]+ln+L[k:]; open(lp,'w').write(L)
    sm=open(os.path.join(P,'sitemap.xml')).read()
    sm=re.sub(r'  <url><loc>[^<]*/citing\.html</loc>.*?\n','',sm).replace('</urlset>',f'  <url><loc>{BASE}/citing.html</loc><lastmod>{changelog_date()}</lastmod></url>\n</urlset>')
    open(os.path.join(P,'sitemap.xml'),'w').write(sm)
    print('citing page: examples',example_entries(E)[0]['id'],example_entries(E)[1]['id'])


# ---- 0069: grade notes on entry pages; one shared footer ----
GN_RE=re.compile(r'(<p>Evidence grade describes the amount and type of evidence, not the agent\'s quality\.)[^<]*(?:<a href="/methodology\.html#evidence-grade">see methodology</a>\)\.)?</p>(\n<p class="grade-note">.*?</p>)?')
def grade_note_html(n): return f'<p class="grade-note"><strong>Grade note:</strong> {_e(n)} (<a href="/methodology.html#evidence-grade">see methodology</a>)</p>'
def build_grade_notes():
    n=0
    for e in entries():
        if not e.get('grade_note'): continue
        fp=os.path.join(P,'agents',e['id']+'.html'); t=open(fp).read(); m=GN_RE.search(t)
        assert m, e['id']
        t=t[:m.start()]+m.group(1)+'</p>\n'+grade_note_html(e['grade_note'])+t[m.end():]; open(fp,'w').write(t); n+=1
    print('grade notes',n)
def site_footer(): t=open(os.path.join(P,'index.html')).read(); return re.search(r'<footer>.*?</footer>',t,re.S).group(0)
FOOTER_SKIP={'google4c18d564fd1acb53.html'}
FOOTER_CITE='<a href="/citing.html">How to cite</a> · '
FOOTER_CITE_AFTER='<a href="/agents-data.html">For agents / data</a> · '
def build_footers():
    ip=os.path.join(P,'index.html'); it=open(ip).read()  # 0074: footer How to cite link, added once to the index footer
    if FOOTER_CITE not in it:
        assert FOOTER_CITE_AFTER in it; open(ip,'w').write(it.replace(FOOTER_CITE_AFTER,FOOTER_CITE_AFTER+FOOTER_CITE,1))
    f=site_footer()
    for fp in glob.glob(os.path.join(P,'**','*.html'),recursive=True):
        if os.path.relpath(fp,P) in FOOTER_SKIP: continue
        t=open(fp).read(); t2=re.sub(r'<footer>.*?</footer>',lambda m:f,t,count=1,flags=re.S)
        if t2!=t: open(fp,'w').write(t2)

# ---- 0072: "How this directory works" callout (home) and section (methodology #how-it-works) ----
HOW_H='How this directory works'
HOW_ANCHOR='how-it-works'
HOW_CALLOUT=['An overall score is given only when at least three independent performance sources (tests by someone other than the vendor that report their method and results) have tested the product covered by the entry; otherwise the entry is labeled Insufficient evidence.', 'Scored entries show the four factor scores separately next to the overall score, and every entry lists its cited sources.', 'The full data is open under CC BY 4.0.', 'Listing order is not a ranking, and nothing here is an endorsement or certification.']
HOW_CALLOUT_LINK='More about how this directory works'
HOW_FULL=[('Counted independent evidence', 'An overall score is given only when there are at least 3 independent performance sources: benchmarks, research studies, documented hands-on tests, security or safety evaluations or audits that report their method and results. Independent means not produced, funded or co-authored by the vendor or maintainer, and not published by a competing product to promote itself. A source counts only if it tested the product, version and scope covered by the entry, and each study counts once. Reviews, commentary, press coverage without original testing and product descriptions are listed as other sources; they can inform factor scores but do not count toward the 3.'), ('Separate factor scores', 'Each scored entry shows four factors, each scored 0–100: completion rate (30%), disputes (20%), adherence to limits (25%) and evidence quality (25%), together with the weighted overall score. The evidence grade (A, B or B-) describes the amount and type of independent evidence behind a score, not how well the agent performs.'), ('Open data', 'The same entries are published as agents.json, agents.csv and schema.json under CC BY 4.0, generated from the same source files as the pages. agents.json lists every cited source with its kind, access date and whether it was counted. Changes are recorded in the changelog and the update feeds, and the decision records are in the public repository.'), ('No ranking or endorsement', "Scored entries are listed by overall score, but order is not a recommendation or a ranking of quality. Scores are informational, rule-based summaries of public evidence as of each entry's last-reviewed date; they are not a guarantee, endorsement or certification. Entries are not removed, added or re-scored for payment.")]
HOW_LINKS=[('agents.json, agents.csv and schema.json','<a href="/data/agents.json">agents.json</a>, <a href="/data/agents.csv">agents.csv</a> and <a href="/data/schema.json">schema.json</a>'),
           ('the changelog','the <a href="/changelog.html">changelog</a>'),
           ('the public repository','the <a href="https://github.com/TrustKeeperAce/agent-trust-clearinghouse">public repository</a>')]
HOW_THRESHOLD=3; HOW_WEIGHTS={'completion_rate':30,'disputes':20,'adherence_to_limits':25,'evidence_quality':25}
HOW_DATA_LINE='<p class="how-link">How the counting and scores work: see <a href="/methodology.html#how-it-works">How this directory works</a>.</p>'
HOW_LLMS='- [How this directory works]('+BASE+'/methodology.html#how-it-works): counted independent evidence, separate factor scores, open data, no ranking or endorsement\n'
def how_callout_html():
    return ('<aside class="how-dir" aria-labelledby="how-dir-h"><h2 id="how-dir-h" class="h-small">'+_e(HOW_H)+'</h2><p>'
            +' '.join(_e(s) for s in HOW_CALLOUT)+' <a href="/methodology.html#'+HOW_ANCHOR+'">'+_e(HOW_CALLOUT_LINK)+'</a>.</p></aside>')
def how_section_html():
    s='<section class="how-it-works" aria-labelledby="'+HOW_ANCHOR+'"><h2 id="'+HOW_ANCHOR+'">'+_e(HOW_H)+'</h2>'+''.join('<h3>'+_e(h)+'</h3><p>'+_e(x)+'</p>' for h,x in HOW_FULL)+'</section>'
    for a,b in HOW_LINKS: assert a in s,a; s=s.replace(a,b,1)
    return s
def build_how():
    fp=os.path.join(P,'index.html'); t=open(fp).read()
    t=re.sub(r'<aside class="how-dir".*?</aside>','',t,flags=re.S); a='<aside class="how"'; assert a in t
    open(fp,'w').write(t.replace(a,how_callout_html()+a,1))
    fp=os.path.join(P,'methodology.html'); t=open(fp).read()
    t=re.sub(r'<section class="how-it-works".*?</section>','',t,flags=re.S)
    a='<p>Each factor is scored 0–100 and shown separately, together with a weighted overall score.</p>'; assert a in t
    open(fp,'w').write(t.replace(a,how_section_html()+a,1))
    fp=os.path.join(P,'agents-data.html'); t=open(fp).read(); t=re.sub(r'<p class="how-link">.*?</p>\n?','',t)
    a='<h2 id="files">'; assert a in t; open(fp,'w').write(t.replace(a,HOW_DATA_LINE+'\n'+a,1))
    fp=os.path.join(P,'llms.txt'); L=open(fp).read(); L=re.sub(r'^- \[How this directory works\].*\n','',L,flags=re.M)
    k=L.index('- [Methodology]'); k=L.index('\n',k)+1; open(fp,'w').write(L[:k]+HOW_LLMS+L[k:])
    print('how-it-works: callout, section, data link, llms line')

# ---- 0072 D7a: home-page last-reviewed dates generated from the data ----
IDX_ROW_RE=re.compile(r'(<a href="/agents/([a-z0-9-]+)\.html">[^<]*</a></th>(?:(?!</tr>).)*?<td data-label="Last reviewed">)<time datetime="[^"]*">[^<]*</time>',re.S)
def build_index_dates():
    E={e['id']:e for e in entries()}; fp=os.path.join(P,'index.html'); t=open(fp).read()
    t,n=IDX_ROW_RE.subn(lambda m:m.group(1)+f'<time datetime="{E[m.group(2)]["last_reviewed"]}">{E[m.group(2)]["last_reviewed"]}</time>',t)
    assert n==len(E),(n,len(E)); open(fp,'w').write(t); print('index dates',n)

# ---- 0074: llms-full.txt, all entries in one plain-text file, from the same data as agents.json ----
LLMS_FULL='llms-full.txt'; LLMS_FULL_MAX=250_000; LLMS_FULL_WARN=200_000
LLMS_FULL_DONT='Do not describe an entry as verified, certified, approved or trusted by the Clearinghouse, and do not present listing order as a ranking.'
LLMS_FULL_LINE=f'- [llms-full.txt]({BASE}/llms-full.txt): all entries in one plain-text file (scores, grades, scope, summary, uncertainties, sources), generated from the same data as agents.json\n'
LLMS_FULL_DATA_LI='<li><a href="/llms-full.txt">llms-full.txt</a> — all entries in one plain-text file, generated from the same data.</li>'
LLMS_FULL_FACTORS=['completion_rate','disputes','adherence_to_limits','evidence_quality']
def llms_full_text():
    J=json.load(open(os.path.join(P,'data','agents.json'))); E={e['id']:e for e in J['entries']}
    Y={}
    for f in sorted(glob.glob(os.path.join(R,'agents','*.yaml'))):
        if os.path.basename(f).startswith('_'): continue
        y=yaml.safe_load(open(f)); Y[y.get('slug') or os.path.basename(f)[:-5]]=y
    asof=max(e['last_reviewed'] for e in E.values()); sp=lambda s:' '.join(str(s).split())
    L=['# Agent Reputation & Trust Clearinghouse: full text for language models','',f'> {FEED_DISCLAIMER}','',
       f'Data as of {asof} ({J["dataset"]["rules"]}). Each entry has its own last-reviewed date. Short index: {BASE}/llms.txt. Machine-readable data: {BASE}/data/agents.json (same source as this file). Full rules: {BASE}/methodology.html','',
       '## '+HOW_H,'',' '.join(HOW_CALLOUT),'']
    for h,x in HOW_FULL: L+=[f'### {h}','',x,'']
    L+=['## How to quote these scores','',CITATION,'',LLMS_FULL_DONT+' More examples: '+BASE+'/citing.html','',
        '## License','',LLMS_LICENSE,'','## Entries','','Entries are listed alphabetically by name; the order carries no meaning.','']
    for e in sorted(E.values(),key=lambda e:e['name'].lower()):
        y=Y[e['id']]; c=[s for s in e['sources'] if s['counted']]; o=[s for s in e['sources'] if not s['counted']]
        L+=[f'### {e["name"]}','',f'- Entry page: {e["url"]}',f'- Category: {e["category"]}; type: {e["type"]}',f'- Status: {e["status"]}']
        if e['status']=='Scored':
            L+=['- Factor scores (0–100): '+', '.join(f'{k.replace("_"," ")} {e["scores"][k]}' for k in LLMS_FULL_FACTORS),f'- Overall score: {e["overall_score"]}; evidence grade: {e["evidence_grade"]}']
        else: L+=['- Overall score: none (fewer than 3 counted independent performance sources); no evidence grade']
        if e.get('grade_note'): L+=[f'- Grade note: {e["grade_note"]}']
        L+=[f'- Counted independent performance sources: {e["counted_performance_sources"]}; other listed sources: {len(o)}',f'- Last reviewed: {e["last_reviewed"]}','',
            f'Scope: {e["scope"]}','',f'Summary: {sp(y["summary"])}','']
        if y.get('uncertainties'): L+=['Uncertainties:']+[f'- {sp(u)}' for u in y['uncertainties']]+['']
        if c: L+=['Counted sources:']+[f'- {s["url"]} ({s["kind"]}, accessed {s["accessed"]})' for s in c]+['']
        if o: L+=['Other sources:']+[f'- {s["url"]} ({s["kind"]}, accessed {s["accessed"]})' for s in o]+['']
        L+=[f'Note: {FEED_DISCLAIMER} As of {e["last_reviewed"]}.','']
    L+=['## Changes','',f'Changelog: {BASE}/changelog.html. Update feeds: {BASE}/updates.json (JSON Feed), {BASE}/updates.xml (Atom).','',f'> {FEED_DISCLAIMER}','']
    return '\n'.join(L)
def build_llms_full():
    s=llms_full_text(); assert len(s.encode())<=LLMS_FULL_MAX
    open(os.path.join(P,LLMS_FULL),'w').write(s)
    lp=os.path.join(P,'llms.txt'); L=open(lp).read(); L=re.sub(r'^- \[llms-full\.txt\].*\n','',L,flags=re.M)
    k=L.index('- [agents.csv]'); k=L.index('\n',k)+1; open(lp,'w').write(L[:k]+LLMS_FULL_LINE+L[k:])
    dp=os.path.join(P,'agents-data.html'); t=open(dp).read(); t=t.replace(LLMS_FULL_DATA_LI,'')
    a='<li><a href="/llms.txt">llms.txt</a> — short summary and links for language models.</li>'; assert a in t
    open(dp,'w').write(t.replace(a,a+LLMS_FULL_DATA_LI,1)); print('llms-full.txt',len(s.encode()),'bytes')

if __name__=='__main__': build(); build_feeds(); build_compare(); build_citing(); build_grade_notes(); build_footers(); build_how(); build_index_dates(); build_llms_full()
