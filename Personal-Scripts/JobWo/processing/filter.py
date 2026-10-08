def isJobRelevant(job, positions, roles):
    title = job["title"].lower()

    position_match = False
    role_match = False

    for position in positions:
        if position.lower() in title:
            position_match = True

    for role in roles:
        if role.lower() in title:
            role_match = True

    return position_match and role_match


def filter_jobs(jobs, positions, roles):
    relevantJobs = []

    for job in jobs:
        if isJobRelevant(job, positions, roles):
            relevantJobs.append(job)

    return relevantJobs