from src.sorting import sort_by


def test_sort_by_criteria():
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
            "max_salary": 20000,
            "date_posted": "2016-06-06"
        },
        {
            "name": "Artista",
            "min_salary": 3000,
            "max_salary": 10000,
            "date_posted": "2015-05-05"
        }
    ]
    
    expected_sort_by_min_salary = [
        {
            "name": "Carpinteiro",
            "min_salary": 1000,
            "max_salary": 30000,
            "date_posted": "2017-07-07"    
        },
        {
            "name": "Balconista",
            "min_salary": 2000,
            "max_salary": 20000,
            "date_posted": "2016-06-06"
        },
        {
            "name": "Artista",
            "min_salary": 3000,
            "max_salary": 10000,
            "date_posted": "2015-05-05"
        }
    ]
    
    expected_sort_by_max_salary = [
        {
            "name": "Carpinteiro",
            "min_salary": 1000,
            "max_salary": 30000,
            "date_posted": "2017-07-07"    
        },
        {
            "name": "Balconista",
            "min_salary": 2000,
            "max_salary": 20000,
            "date_posted": "2016-06-06"
        },
        {
            "name": "Artista",
            "min_salary": 3000,
            "max_salary": 10000,
            "date_posted": "2015-05-05"
        }
    ]
    
    expected_sort_by_date_posted = [
        {
            "name": "Carpinteiro",
            "min_salary": 1000,
            "max_salary": 30000,
            "date_posted": "2017-07-07"    
        },
        {
            "name": "Balconista",
            "min_salary": 2000,
            "max_salary": 20000,
            "date_posted": "2016-06-06"
        },
        {
            "name": "Artista",
            "min_salary": 3000,
            "max_salary": 10000,
            "date_posted": "2015-05-05"
        }
    ]
    
    result_sort_by_min_salary = sort_by(jobs_list, "min_salary")
    result_sort_by_max_salary = sort_by(jobs_list, "max_salary")
    result_sort_by_date_posted = sort_by(jobs_list, "date_posted")
    
    assert result_sort_by_min_salary == expected_sort_by_min_salary
    assert result_sort_by_max_salary == expected_sort_by_max_salary
    assert result_sort_by_date_posted == expected_sort_by_date_posted
    
    
    
    
