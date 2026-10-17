#!/usr/bin/env python3
"""Local consistency check (read-only). Recomputes overall scores and evidence grades
from agents/*.yaml and reports mismatches. Exit code 1 on any hard mismatch.

Rules (Scoring rules v0.1 and Decisions 0010/0025):
  overall = 0.30*completion + 0.20*disputes + 0.25*adherence + 0.25*evidence, round half up
  counted sources: kind starts with 'independent performance' and counted != false
  <3 Insufficient evidence; 3-4 B-; 5-6 B;
  7+ A only if >=3 peer-reviewed AND >=1 test of the current version within 12 months,
  otherwise B. The current-version condition cannot always be read from data: if the
  test_date/version_tested fields do not settle it, the script reports WARN, not an error.
Usage: python3 scripts/check_scores.py [--strict]   (--strict makes WARN fail too)
"""
import sys,glob,os,re,yaml
from decimal import Decimal,ROUND_HALF_UP
W={'completion_rate':30,'disputes':20,'adherence_to_limits':25,'evidence_quality':25}
EQ={'A':(85,100),'B':(70,84),'B-':(55,69)}
root=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
err=warn=0
def dates(s):
    return [tuple(map(int,m)) for m in re.findall(r'(20\d\d)-(\d\d)',str(s))] or [(int(y),0) for y in re.findall(r'(20\d\d)',str(s))]
for f in sorted(glob.glob(os.path.join(root,'agents','*.yaml'))):
    if os.path.basename(f).startswith('_'): continue
    d=yaml.safe_load(open(f)); slug=d.get('slug'); g=d.get('evidence_grade')
    cs=[x for x in d.get('sources',[]) if str(x.get('kind','')).startswith('independent performance') and x.get('counted') is not False]
    n=len(cs); declared=(d.get('independent_source_count') or {}).get('performance')
    out=[]
    if declared is not None and declared!=n: out.append(f'ERROR count: yaml says {declared}, counted sources listed {n}')
    if d.get('overall_score') is None:
        if g!='Insufficient evidence': out.append(f'ERROR no score but grade {g}')
        if n>=3: out.append(f'ERROR {n} counted sources but Insufficient evidence')
    else:
        s=d['scores']; raw=sum(Decimal(str(s[k]))*W[k] for k in W)/100
        calc=int(raw.quantize(Decimal(1),ROUND_HALF_UP))
        if calc!=d['overall_score']: out.append(f'ERROR overall {d["overall_score"]} != computed {calc} ({raw})')
        missing=[x['url'] for x in cs if not all(k in x for k in ('peer_reviewed','version_tested','test_date'))]
        if missing: out.append(f'ERROR {len(missing)} counted sources missing peer_reviewed/version_tested/test_date')
        pr=sum(1 for x in cs if x.get('peer_reviewed') is True)
        if n<3: exp={'Insufficient evidence'}
        elif n<=4: exp={'B-'}
        elif n<=6: exp={'B'}
        else:
            if pr<3: exp={'B'}
            else:
                rev=str(d.get('last_reviewed') or '2026-10-17'); ry,rm=int(rev[:4]),int(rev[5:7])
                recent=[x for x in cs if any((ry-y)*12+(rm-(m or 1))<=12 for y,m in dates(x.get('test_date')))]
                known=[x for x in recent if x.get('version_tested') not in (None,'unstated')]
                if known: exp={'A'} if g=='A' else {'A','B'}
                else:
                    exp={'A','B'}
                    out.append(f'WARN 7+ sources, {pr} peer-reviewed; current-version test within 12 months not shown by data ({len(recent)} recent test(s), version unstated) - A/B is a judgment call')
        if g not in exp: out.append(f'ERROR grade {g}, rules give {"/".join(sorted(exp))} (n={n}, peer-reviewed={pr})')
        lo,hi=EQ.get(g,(0,100))
        if not lo<=s['evidence_quality']<=hi: out.append(f'WARN evidence_quality {s["evidence_quality"]} outside guide {lo}-{hi} for {g}')
        out.insert(0,f'overall {d["overall_score"]} (computed {calc}), grade {g}, counted {n}, peer-reviewed {pr}')
    else_ok = not any(o.startswith(('ERROR','WARN')) for o in out)
    for o in out:
        if o.startswith('ERROR'): err+=1
        if o.startswith('WARN'): warn+=1
    print(f'{"OK  " if else_ok else "FLAG"} {slug}: '+' | '.join(out) if out else f'OK   {slug}: Insufficient evidence, counted {n}')
print(f'\n{err} error(s), {warn} warning(s)')
sys.exit(1 if err or ('--strict' in sys.argv and warn) else 0)
