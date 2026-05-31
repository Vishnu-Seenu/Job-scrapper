import requests
from bs4 import BeautifulSoup
import csv

URL = "https://realpython.github.io/fake-jobs/"

def scrape_jobs():
    try:
        response = requests.get(URL)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching page: {e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")

    jobs = []

    job_cards = soup.find_all("div", class_="card-content")

    for job in job_cards:
        try:
            title = job.find("h2", class_="title")
            title = title.text.strip() if title else "N/A"

            company = job.find("h3", class_="company")
            company = company.text.strip() if company else "N/A"

            location = job.find("p", class_="location")
            location = location.text.strip() if location else "N/A"

            parent_card = job.parent

            link_tag = parent_card.find("a", string="Apply")

            if link_tag:
                detail_url = (
                    "https://realpython.github.io/fake-jobs/"
                    + link_tag["href"]
                )
            else:
                detail_url = "N/A"

            jobs.append({
                "Job Title": title,
                "Company": company,
                "Location": location,
                "Job URL": detail_url
            })

        except Exception as e:
            print(f"Error processing job: {e}")

    return jobs


def save_to_csv(jobs, filename="jobs.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["Job Title", "Company", "Location", "Job URL"]
        )

        writer.writeheader()
        writer.writerows(jobs)


if __name__ == "__main__":
    jobs = scrape_jobs()

    if jobs:
        save_to_csv(jobs)
        print(f"Successfully saved {len(jobs)} jobs to jobs.csv")
    else:
        print("No jobs found.")