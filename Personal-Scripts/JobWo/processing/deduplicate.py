def deduplicate_jobs(jobs):
    seen = set()
    unique_jobs = []

    for job in jobs:
        key = (job["source"], job["source_id"])

        if key not in seen:
            seen.add(key)
            unique_jobs.append(job)

    return unique_jobs