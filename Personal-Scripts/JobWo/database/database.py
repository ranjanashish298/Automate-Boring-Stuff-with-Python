import sqlite3


def init_database():
    connection = sqlite3.connect("jobwo.db")

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            source TEXT NOT NULL,
            source_id TEXT NOT NULL,
            job_url TEXT,
            title TEXT,
            company TEXT,
            location TEXT,
            date_posted DATE,
            date_found DATE
        )
    """)

    connection.commit()
    connection.close()


def job_exists(source, source_id):
    connection = sqlite3.connect("jobwo.db")

    cursor = connection.cursor()

    cursor.execute(
        "SELECT id FROM jobs WHERE source = ? AND source_id = ?",
        (source, source_id)
    )

    result = cursor.fetchone()

    connection.close()

    return result is not None

def save_job(job):
    connection = sqlite3.connect("jobwo.db")

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO jobs (
            source,
            source_id,
            job_url,
            title,
            company,
            location,
            date_posted,
            date_found
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, DATE('now'))
    """, (
        job["source"],
        job["source_id"],
        job["job_url"],
        job["title"],
        job["company"],
        job["location"],
        job["date_posted"]
    ))

    connection.commit()
    connection.close()

def save_new_jobs(jobs):
    new_jobs = []

    for job in jobs:
        if not job_exists(job["source"], job["source_id"]):
            save_job(job)
            new_jobs.append(job)

    return new_jobs