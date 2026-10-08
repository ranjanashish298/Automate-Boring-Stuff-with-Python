def createEmail(jobs):
    html = ""

    html += """
    <html>
    <body>
        <h2>Hi Ashish, JobWo has these new jobs for you:</h2>
    """

    for job in jobs:
        html += f"""
        <div>
            <h3>{job["title"]}</h3>
            <p><strong>Company:</strong> {job["company"]}</p>
            <p><strong>Location:</strong> {job["location"]}</p>
            <p><strong>Posted:</strong> {job["date_posted"]}</p>
            <p><a href="{job["job_url"]}">View Job</a></p>
            <hr>
        </div>
        """

    html += """
    </body>
    </html>
    """

    return html