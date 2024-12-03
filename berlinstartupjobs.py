import requests
from bs4 import BeautifulSoup

all_jobs = []
skills = ["python", "typescript", "javascript", "rust"]
basic_url = "https://berlinstartupjobs.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def scrape_page(url):
    response = requests.get(f"{url}engineering/",headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    jobs = soup.find("ul", class_="jobs-list-items").find_all("li", class_="bjs-jlid")

    if response.status_code == 200:
        for job in jobs:
            title = job.find("h4", class_="bjs-jlid__h").text
            company = job.find("a", class_="bjs-jlid__b").text
            link = job.find("a", class_="bjs-jlid__b")["href"]
            description = job.find("div", class_="bjs-jlid__description").text
            job_data = {
                "title": title,
                "company": company,
                "description": description,
                "link": link
            }
            all_jobs.append(job_data)
    else:
        print(f"Error: {response.status_code}")

def get_pages(url):
    response = requests.get(
        "https://berlinstartupjobs.com/engineering/",
        headers={
            "User-Agent":
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        })
    soup = BeautifulSoup(response.content, "html.parser")
    page_count = len(soup.find("ul", class_="bsj-nav").find_all("a"))
    if page_count > 0:
        return page_count
    else:
        pass 


print(get_pages("https://berlinstartupjobs.com/engineering/"))