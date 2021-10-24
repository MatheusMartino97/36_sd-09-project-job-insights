from src.jobs import read


def get_unique_job_types(path):
    jobs = read(path)
    unique_jobs = []
    for job in jobs:
        if job["job_type"] not in unique_jobs:
            unique_jobs.append(job["job_type"])
    return unique_jobs


def filter_by_job_type(jobs, job_type):
    jobs_filtered_by_job_type = []
    for job in jobs:
        if job["job_type"] == job_type:
            jobs_filtered_by_job_type.append(job)
    return jobs_filtered_by_job_type


def get_unique_industries(path):
    jobs = read(path)
    unique_industries = []
    for job in jobs:
        if job["industry"] not in unique_industries and job["industry"] != '':
            unique_industries.append(job["industry"])
    return unique_industries


def filter_by_industry(jobs, industry):
    jobs_filtered_by_industry = []
    for job in jobs:
        if job["industry"] == industry:
            jobs_filtered_by_industry.append(job)
    return jobs_filtered_by_industry


def get_max_salary(path):
    jobs = read(path)
    salaries = []
    for job in jobs:
        if (job["max_salary"].isnumeric() and job["max_salary"] not in salaries):
            salaries.append(int(job["max_salary"]))
    max_salary = max(salaries, key=int)
    return max_salary


def get_min_salary(path):
    jobs = read(path)
    salaries = []
    for job in jobs:
        if job["min_salary"].isnumeric() and job["min_salary"] not in salaries:
            salaries.append(int(job["min_salary"]))
    min_salary = min(salaries, key=int)
    return min_salary


def matches_salary_range(job, salary):
    if not ("min_salary" in job and "max_salary" in job):
        raise ValueError("The keys max_salary and min_salary must exist in job")
    
    if not (isinstance(job.get("min_salary"), int) and isinstance(job.get("max_salary"), int)):
        raise ValueError("The keys max_salary and min_salary must be integers")
    
    if job["min_salary"] > job["max_salary"]:
        raise ValueError("The max_salary value must be greater than the min_salary value")

    if not isinstance(salary, int):
        raise ValueError("Salary must be an integer")
    
    is_salary_between_range = int(job["min_salary"]) <= salary <= int(job["max_salary"])
    return is_salary_between_range


def filter_by_salary_range(jobs, salary):
    filtered_jobs = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filtered_jobs.append(job)
        except Exception:
            print('Something went wrong')
    return filtered_jobs
