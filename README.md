# Python Job Listings Scraper

A Python web scraping project that extracts job listings from the Fake Python Jobs website and stores the collected data in a CSV file.

## Project Overview

This project uses the Requests library to fetch webpage content and Beautiful Soup to parse HTML data. The scraper collects information from each job posting, including:

- Job Title
- Company Name
- Location
- Job Detail URL

The extracted data is then exported into a CSV file for further analysis or reporting.

## Features

- Scrapes job listings from the Fake Python Jobs website
- Extracts structured job information
- Handles missing data gracefully
- Exports results to a CSV file
- Uses clean and modular Python code

## Technologies Used

- Python 3
- Requests
- Beautiful Soup (bs4)
- CSV Module

## Project Structure

```
project/
│
├── scraper.py
├── jobs.csv
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository
2. Navigate to the project directory
3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

```bash
python scraper.py
```

After execution, a `jobs.csv` file will be generated containing all scraped job listings.

## Project Reference

This project was completed as part of the Roadmap.sh Python Projects collection:

https://roadmap.sh/projects/job-listings-scraper

## Learning Outcomes

- Web scraping fundamentals
- HTML parsing using Beautiful Soup
- HTTP requests using Requests
- Data extraction techniques
- CSV file handling in Python
- Basic error handling and data validation

## Data Source

https://realpython.github.io/fake-jobs/

This website is designed specifically for learning and practicing web scraping techniques.
