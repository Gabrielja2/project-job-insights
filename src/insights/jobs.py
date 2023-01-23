from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, mode="r") as file:
        DictReader_obj = csv.DictReader(file)
        return list(DictReader_obj)


def get_unique_job_types(path: str) -> List[str]:
    jobs = read(path)
    job_set = set()
    for job in jobs:
        job_set.add(job['job_type'])
    return list(job_set)


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError
