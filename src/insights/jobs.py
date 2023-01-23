from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:    
    with open(path, mode="r") as file:
            DictReader_obj = csv.DictReader(file)
            return [row for row in DictReader_obj]    


def get_unique_job_types(path: str) -> List[str]:
   obj = read(path)
   for item in obj:
    return item['job_type']


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
