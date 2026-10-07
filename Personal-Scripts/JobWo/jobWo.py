# This is my first attempt to automate a task I would like to do for myself.
# I would like to get job results everyday to my gmail account from LinkedIN. 

''' Requirements: 
1. LinkedIn scraper and see how it works
2. Define jobs I am looking for
3. Search for those jobs on LinkedIn
4. Find useful results
5. Print me the relevant information
'''

import csv
from jobspy import scrape_jobs

def normalize_job(job):
    return {
        "source":       job["site"],
        "source_id":    job["id"],
        "job_url":      job["job_url"],
        "title":        job["title"],
        "company":      job["company"],
        "location":     job["location"],
        "date_posted":  job["date_posted"]
    }

jobs = scrape_jobs(
    site_name=["linkedin"], # "bayt", "naukri", "bdjobs"
    search_term="Werkstudent Cloud Engineer",
    location="Baden-Württemberg, Germany",
    results_wanted=5,
    hours_old=72,
    country_indeed='Germany',
    # fetch_description=True # for boards whose search results don't include the description (slower)
    # proxies=["208.195.175.46:65095", "208.195.175.45:65095", "localhost"],
)

#print(jobs.head())
#jobs.to_csv("jobs.csv", quoting=csv.QUOTE_NONNUMERIC, escapechar="\\", index=False) # to_excel

normalized_jobs = []

for i in range(len(jobs)):
    normalized_jobs.append(normalize_job(jobs.iloc[i]))

for job in normalized_jobs:
    print(job["title"])
    print(job["company"])
    print(job["location"])
    print(job["date_posted"])
    print(job["job_url"])
    print("-" * 50)