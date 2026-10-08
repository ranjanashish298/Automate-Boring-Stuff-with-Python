from jobspy import scrape_jobs
import pandas as pd

def search_linkedin(search_term, location):
    jobs = scrape_jobs(
        site_name=["linkedin"],
        search_term=search_term,
        location=location,
        results_wanted=10,
        hours_old=72,
        country_indeed="Germany",
    )

    return jobs

def collect_linkedin_jobs(search_terms, locations):
    all_jobs = []

    for search_term in search_terms:
        for location in locations:
            jobs = search_linkedin(search_term, location)
            all_jobs.append(jobs)

    return pd.concat(all_jobs, ignore_index=True)