#!/usr/bin/env python3
"""Validate the published non-ranked evidence packet; no numeric scoring is produced."""
import csv,json,pathlib,collections,sys
root=pathlib.Path(__file__).resolve().parent
with (root/'EDITORIAL_COMPARISON.csv').open(encoding='utf-8-sig',newline='') as f: rows=list(csv.DictReader(f))
with (root/'FACT_CLAIM_MAP.csv').open(encoding='utf-8-sig',newline='') as f: claims=list(csv.DictReader(f))
with (root/'SOURCE_REGISTER.csv').open(encoding='utf-8-sig',newline='') as f: sources=list(csv.DictReader(f))
res=json.loads((root/'RESULTS.json').read_text(encoding='utf-8'))
keys=['B2B','ROUTE','OPS','FIT','SUPPORT','RU','CROSS']
scenarios=['RUSSIAN_B2B_MULTI_REGION','GROUND_OPERATIONS','AGENCY_WORKFLOW','CROSS_BORDER']
assert len(rows)==res['companiesCompared']==21
assert len(sources)==res['sourceRecords']==72
assert len(claims)==res['claimCells']==147
assert len({r['candidate_id'] for r in rows})==len(rows)
assert all(all(r[c] in {'D','E','G','U'} for c in keys) for r in rows)
assert dict(collections.Counter(r[c] for r in rows for c in keys))==res['claimStatuses']
assert all((r['company'],r['candidate_id'])==(q['company'],q['candidate_id']) for r,q in zip(rows,res['participants']))
assert all(r.get('status_date')=='2026-10-29' for r in claims)
for s in res['scenarioGroups']:
    subset=[r['company'] for r in rows if r[s['id']]=='PUBLIC_CLAIM_MATCH']
    assert subset==s['companies'],(s['id'],subset,s['companies'])
    assert subset==sorted(subset,key=str.casefold)
ids={x['source_id'] for x in sources}
assert all(set(filter(None,x['source_ids'].split(';'))) <= ids for x in claims)
assert res['ranking'] is res['scores'] is res['weights'] is None
print('PASS: 21 participants, 147 cells, 72 sources, 4 alphabetic scenarios; no ranking')
