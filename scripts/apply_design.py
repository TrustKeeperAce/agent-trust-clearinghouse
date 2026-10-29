"""scripts/apply_design.py (decision 0046). Design transform: applies the new header/brand, favicon, index hero and score bars to every page.
Layout and labels only; no score, rule or content text changes. Idempotent: safe to rerun after any entry build; also refreshes the index hero counts."""
import re,glob,os,sys
P=sys.argv[1] if len(sys.argv)>1 else os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'public')
MARK='<svg viewBox="0 0 44 44" aria-hidden="true" focusable="false"><rect class="mk-b" x="1" y="1" width="42" height="42" rx="11" stroke-width="2"/><rect class="mk-t" x="10" y="10" width="24" height="4" rx="2"/><rect class="mk-a" x="10" y="17.5" width="16" height="4" rx="2"/><rect class="mk-t" x="10" y="25" width="20" height="4" rx="2"/><rect class="mk-a" x="10" y="32.5" width="20" height="4" rx="2"/></svg>'
BRAND=f'<a class="brand" href="/">{MARK}<span class="wm"><b>Agent Reputation &amp; Trust</b><small>Clearinghouse</small></span></a>'
FROZEN='This directory is no longer actively maintained. Information may be out of date. Scores were informational only and are not guarantees or endorsements.'
FROZEN_HTML=f'<p class="frozen-notice" role="note">{FROZEN}</p>\n'  # decision 0102 (freeze): shown at the top of every page
def page(f,t):
    if 'class="frozen-notice"' not in t: t=t.replace('<a class="skip-link" href="#main">Skip to main content</a>\n','<a class="skip-link" href="#main">Skip to main content</a>\n'+FROZEN_HTML,1)
    assert t.count('class="frozen-notice"')==1,f
    t=re.sub(r'<link rel="icon" href="[^"]*">','<link rel="icon" href="/favicon.svg" type="image/svg+xml"><meta name="theme-color" content="#0a0d12" media="(prefers-color-scheme: dark)"><meta name="theme-color" content="#f6f7f9" media="(prefers-color-scheme: light)">',t)
    t=t.replace('<a class="brand" href="/">Agent Reputation &amp; Trust Clearinghouse</a>',BRAND)
    cur={'index.html':'/','methodology.html':'/methodology.html','changelog.html':'/changelog.html'}.get(os.path.basename(f))
    if cur and '/agents/' not in f and 'aria-current' not in t: t=t.replace(f'<nav aria-label="Primary"><a href="{cur}"',f'<nav aria-label="Primary"><a href="{cur}" aria-current="page"',1)
    # score bars (number stays as text; bar is decorative)
    t=re.sub(r'<td data-label="(Overall score|Score)" class="num">(\d+)</td>',lambda m:f'<td data-label="{m.group(1)}" class="num"><span class="bar" style="--v:{m.group(2)}">{m.group(2)}</span></td>',t)
    t=re.sub(r'<p><strong>Overall score: (\d+)</strong>',lambda m:f'<p class="scoreline" style="--v:{m.group(1)}"><strong>Overall score: {m.group(1)}</strong>',t)
    if 'class="bar-line"' not in t: t=re.sub(r'(<p class="scoreline" style[^>]*>.*?)</p>',lambda m:m.group(1)+'<span class="bar-line" aria-hidden="true"></span></p>',t,count=1,flags=re.S)
    t=t.replace('<p><strong>Status: Insufficient evidence</strong>','<p class="scoreline insufficient"><strong>Status: Insufficient evidence</strong>')
    t=t.replace('<p><strong>Citation check incomplete — recheck later.</strong></p>','<p class="note"><strong>Citation check incomplete — recheck later.</strong></p>')
    # footer privacy link (decision 0060)
    if 'href="/methodology.html#privacy"' not in t: t=t.replace(' · <a href="mailto:trustkeeperace@gmail.com?subject=Correction%20request">Request a correction</a></p></footer>',' · <a href="/methodology.html#privacy">Privacy</a> · <a href="mailto:trustkeeperace@gmail.com?subject=Correction%20request">Request a correction</a></p></footer>')
    # footer data link (decision 0061)
    if 'href="/agents-data.html">For agents / data</a>' not in t: t=t.replace(' · <a href="/methodology.html#privacy">Privacy</a>',' · <a href="/agents-data.html">For agents / data</a> · <a href="/methodology.html#privacy">Privacy</a>',1)
    return t
def index(t):
    sc=len(re.findall(r'<span class="bar" style="--v:\d+">',t.split('id="insufficient"')[0]))
    ins=t.split('id="insufficient"')[1].count('<th scope="row"')
    if '<ul class="stats"' in t:
        return re.sub(r'<ul class="stats" aria-label="Directory size">.*?</ul>',f'<ul class="stats" aria-label="Directory size"><li><b>{sc}</b>scored entries</li><li><b>{ins}</b>with insufficient evidence</li></ul>',t,count=1,flags=re.S)
    m=re.search(r'<section class="hero"><h1>(.*?)</h1><p class="lede">(.*?)</p></section><aside class="how" aria-label="How scores work"><h2 class="h-small">How scores work</h2><ul>(.*?)</ul><p>(.*?)</p></aside>',t,re.S)
    h1,lede,ul,lnk=m.groups()
    W=''.join(f'<div><span>{a}</span><span class="b" style="--v:{v}"></span><span class="n">{v}%</span></div>' for a,v in [('Completion',30),('Disputes',20),('Adherence',25),('Evidence',25)])
    hero=(f'<section class="hero"><div><p class="eyebrow">Informational directory</p><h1>{h1}</h1><p class="lede">{lede}</p>'
          f'<p class="notice">Informational only; not a guarantee, endorsement, or certification.</p>'
          f'<p class="cta"><a class="btn primary" href="#scored">Browse scored entries</a><a class="btn" href="/methodology.html">Read the methodology</a></p>'
          f'<ul class="stats" aria-label="Directory size"><li><b>{sc}</b>scored entries</li><li><b>{ins}</b>with insufficient evidence</li></ul></div>'
          f'<aside class="how" aria-label="How scores work"><h2 class="h-small">How scores work</h2><div class="weights" aria-hidden="true">{W}</div><ul>{ul}</ul><p>{lnk}</p></aside></section>')
    return t[:m.start()]+hero+t[m.end():]
n=0
for f in glob.glob(P+'/*.html')+glob.glob(P+'/agents/*.html'):
    if re.match(r'google[0-9a-f]+\.html$',os.path.basename(f)): continue  # Search Console verification file (0060): never modify
    t=open(f).read(); t=page(f,t)
    if f.endswith('/index.html'): t=index(t)
    open(f,'w').write(t); n+=1
print('pages',n)
