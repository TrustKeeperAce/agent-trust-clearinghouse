#!/usr/bin/env python3
"""Monthly link check (read-only). Collects every outbound http(s) link in public/*.html
and public/agents/*.html, fetches each with a browser-like User-Agent (following redirects)
and sorts results into: OK (2xx/3xx final), BOT-BLOCK (403, 429, 202 - usually the site
refusing automated requests, not a dead page), and FAILURE (404/410/5xx/no response).
Failures are retried once after 20 s. Internal links are checked against the local files.
Usage: python3 scripts/check_links.py [--workers 8]
"""
import os,re,sys,time,html,urllib.request,urllib.error
from concurrent.futures import ThreadPoolExecutor
root=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'public')
SITE='https://www.agentclearinghouse.org'
UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130 Safari/537.36'
links={};internal={}
for d,_,fs in os.walk(root):
    for f in fs:
        if not f.endswith('.html'): continue
        p=os.path.join(d,f); rel=os.path.relpath(p,root)
        for u in re.findall(r'href="([^"]+)"',open(p,encoding='utf-8').read()):
            u=html.unescape(u)
            if u.startswith(SITE): continue  # canonical self-links; 404 until deployed
            if u.startswith('http'): links.setdefault(u,set()).add(rel)
            elif u.startswith('/'): internal.setdefault(u.split('#')[0] or '/',set()).add(rel)
def fetch(u):
    try:
        r=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':UA}),timeout=30); return r.status
    except urllib.error.HTTPError as e: return e.code
    except Exception: return 0
def classify(c):
    if c in (403,429,202): return 'BOT-BLOCK'
    if 200<=c<400: return 'OK'
    return 'FAILURE'
w=int(sys.argv[sys.argv.index('--workers')+1]) if '--workers' in sys.argv else 8
with ThreadPoolExecutor(w) as ex: res=dict(zip(links,ex.map(fetch,links)))
fails=[u for u,c in res.items() if classify(c)=='FAILURE']
if fails:
    time.sleep(20)
    for u in fails: res[u]=fetch(u)
groups={'OK':[],'BOT-BLOCK':[],'FAILURE':[]}
for u,c in sorted(res.items()): groups[classify(c)].append((c,u))
for path,pages in sorted(internal.items()):
    f=os.path.join(root,path.lstrip('/')) if path!='/' else os.path.join(root,'index.html')
    if not (os.path.isfile(f) or os.path.isfile(f+'.html')): groups['FAILURE'].append(('missing',path))
print(f"Checked {len(res)} outbound and {len(internal)} internal links, {time.strftime('%Y-%m-%d %H:%M %Z')}")
print(f"OK {len(groups['OK'])} | BOT-BLOCK {len(groups['BOT-BLOCK'])} | FAILURE {len(groups['FAILURE'])}")
for g in ('FAILURE','BOT-BLOCK'):
    print(f'\n== {g}')
    for c,u in groups[g]: print(f'{c} {u}  [{", ".join(sorted(links.get(u,internal.get(u,[]))))}]')
sys.exit(1 if groups['FAILURE'] else 0)
