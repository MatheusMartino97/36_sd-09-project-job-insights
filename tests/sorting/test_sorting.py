import pytest
from src.sorting import sort_by


jobs_list = [
    {
        "name": "Carpinteiro",
        "min_salary": 1000,
        "max_salary": 30000,
        "date_posted": "2017-07-07"
    },
    {
        "name": "Balconista",
        "min_salary": 2000,
        "max_salary": 10000,
        "date_posted": "2016-06-06"
    },
    {
        "name": "Artista",
        "min_salary": 3000,
        "max_salary": 20000,
        "date_posted": "2015-05-05"
    }
]

expected_sort_by_min_salary = [
    jobs_list[0],
    jobs_list[1],
    jobs_list[2]
]

expected_sort_by_max_salary = [
    jobs_list[0],
    jobs_list[2],
    jobs_list[1]
]


def test_sort_by_criteria():
    sort_by(jobs_list, "min_salary")
    assert jobs_list == expected_sort_by_min_salary

    sort_by(jobs_list, "max_salary")
    assert jobs_list == expected_sort_by_max_salary
