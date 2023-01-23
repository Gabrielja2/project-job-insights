from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    readedfile = read(path)
    industrie_set = set()
    for industrie in readedfile:
        if industrie['industry'] == '':
            continue
        else:
            industrie_set.add(industrie['industry'])
    return list(industrie_set)


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    industries = []
    for job in jobs:
        if job["industry"] == industry:
            industries.append(job)
    return industries
