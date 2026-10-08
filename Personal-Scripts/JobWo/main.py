from config import SEARCH_TERMS, LOCATIONS, POSITIONS, ROLES
from sources.linkedin import collect_linkedin_jobs
from processing.normalize import normalize_jobs
from processing.deduplicate import deduplicate_jobs
from processing.filter import filter_jobs
from database.database import init_database, save_new_jobs

#Initialize the database 
init_database()

#Collect all the raw jobs first from LinkedIn
rawJobs = collect_linkedin_jobs(SEARCH_TERMS, LOCATIONS)

#Normalize according to our needs
myJobs = normalize_jobs(rawJobs)

#Remove any duplicate jobs 
uniqueJobs = deduplicate_jobs(myJobs)

#Jobs that I am looking for
finalJobs = filter_jobs(uniqueJobs, POSITIONS, ROLES)

#save the jobs to the database if they don't already exist
newFinalJobs = save_new_jobs(finalJobs) 

print("Jobs collected:", len(rawJobs))
print("Jobs after deduplication:", len(uniqueJobs))
print("Relevant jobs:", len(finalJobs))
print("New jobs:", len(newFinalJobs))

for job in newFinalJobs:
    print(job["title"])
    print(job["company"])
    print(job["location"])
    print(job["date_posted"])
    print(job["job_url"])
    print("-" * 50)