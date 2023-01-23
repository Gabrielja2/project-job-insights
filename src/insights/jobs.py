from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, mode="r") as file:
        DictReader_obj = csv.DictReader(file)
        return list(DictReader_obj)


def get_unique_job_types(path: str) -> List[str]:
    readedfile = read(path)
    job_set = set()
    for job in readedfile:
        job_set.add(job['job_type'])
    return list(job_set)


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    # return [job for job in jobs if job["job_type"] == job_type]
    types = []
    for job in jobs:
        if job["job_type"] == job_type:
            types.append(job)
    return types
