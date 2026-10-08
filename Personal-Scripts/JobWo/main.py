from config import SEARCH_TERMS, LOCATIONS, POSITIONS, ROLES
from sources.linkedin import collect_linkedin_jobs
from processing.normalize import normalize_jobs
from processing.deduplicate import deduplicate_jobs
from processing.filter import filter_jobs


#Collect all the raw jobs first from LinkedIn
raw_jobs = collect_linkedin_jobs(SEARCH_TERMS, LOCATIONS)

#Normalize according to our needs
myJobs = normalize_jobs(raw_jobs)

#Remove any duplicate jobs 
unique_jobs = deduplicate_jobs(myJobs)

#Jobs that I am looking for
finalJobs = filter_jobs(unique_jobs, POSITIONS, ROLES)
print(len(finalJobs))
for job in finalJobs:
    print(job["title"])
    print(job["company"])
    print(job["location"])
    print(job["date_posted"])
    print(job["job_url"])
    print("-" * 50)