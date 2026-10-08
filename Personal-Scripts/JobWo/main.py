from config import SEARCH_TERMS, LOCATIONS
from sources.linkedin import collect_linkedin_jobs
from processing.normalize import normalize_jobs

raw_jobs = collect_linkedin_jobs(SEARCH_TERMS, LOCATIONS)

myJobs = normalize_jobs(raw_jobs)
print(myJobs)