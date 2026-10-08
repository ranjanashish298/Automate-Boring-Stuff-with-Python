def jobWo_job_model(job):
    return {
        "source": job["site"],
        "source_id": job["id"],
        "job_url": job["job_url"],
        "title": job["title"],
        "company": job["company"],
        "location": job["location"],
        "date_posted": job["date_posted"],
    }

def normalize_jobs(jobs):
    jobWo_jobs = []

    for i in range (len(jobs)):
        jobWo_jobs.append(jobWo_job_model(jobs.iloc[i])) 

    return jobWo_jobs