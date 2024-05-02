import requests
from bs4 import BeautifulSoup
import time

skills_known = input("Enter your set of skills : ")
skill = skills_known.split(',')

def job_scrapping():
    # Make a GET request to the TimesJobs website and retrieve the HTML content
    html_content = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python+&txtLocation=").text

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'lxml')

    # Find all job listings on the page
    job_listings = soup.find_all("li", class_="clearfix job-bx wht-shd-bx")
    match_found = False  # Flag to track if any match is found
    for job_listing in job_listings:
        # Extract the skills required for each job listing
        skills_required = job_listing.find('span', class_="srp-skills").text.replace(" ", '').strip().split(',')

        if set(skill).intersection(set(skills_required)):
            company_name = job_listing.find("h3", class_="joblist-comp-name").text.replace(" ", '').strip()
            date = job_listing.find('span', class_="sim-posted").text.strip()
            jd = job_listing.header.h2.a['href']  # link
            print(f'''Company name : {company_name} 
                  Date : {date}
                 Link to apply: {jd}
           ''')
            print("####################")
            match_found = True  # Set the flag to True if a match is found

    if not match_found:
        print("no match")

if __name__ == '__main__':
    while True:
        job_scrapping()
        print("Waiting for 5 sec")
        time.sleep(2)  # Wait for 2 seconds before making the next request
