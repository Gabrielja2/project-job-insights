from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    readedfile = read(path)
    salaries = []
    for job in readedfile:
        if job['max_salary'].isdigit():
            salaries.append(int(job['max_salary']))
    return max(salaries)


def get_min_salary(path: str) -> int:
    readedfile = read(path)
    salaries = []
    for job in readedfile:
        if job['min_salary'].isdigit():
            salaries.append(int(job['min_salary']))
    return min(salaries)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        min_salary = int(job["min_salary"])
        max_salary = int(job["max_salary"])
        salary = int(salary)
    except (ValueError, TypeError, KeyError):
        raise ValueError

    if min_salary > max_salary:
        raise ValueError

    return min_salary <= salary <= int(max_salary)


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
