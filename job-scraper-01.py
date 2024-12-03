import requests
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, url):
        self.url = url
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }
        self.all_jobs = []

    def scrape_page(self):
        keywords = ["python", "typescript", "javascript", "rust"]
        for keyword in keywords:
            response = requests.get(f"{self.url}/remote-{keyword}-jobs", headers=self.headers)
            soup = BeautifulSoup(response.content, "html.parser")
            jobs = soup.find("table", id="jobsboard").find_all("tr", class_="job")

            print(f"{self.url}/remote-{keyword}-jobs")

            if response.status_code == 200:
                for job in jobs:
                    title = job.find("h2", itemprop="title").text.strip()
                    company = job.find("h3", itemprop="name").text.strip()
                    location = job.find("div", class_="location").text.strip()
                    tags = [tag.find("h3").text.strip() for tag in job.find("td", class_="tags").find_all("a")]
                    link = job.find("a", class_="preventLink")["href"]
                    self.all_jobs.append({
                        "title": title,
                        "company": company,
                        "location": location,
                        "link": f"{self.url}{link}",
                        "tags": tags
                    })
            else:
                print(f"{response.status_code}")

scraper = Scraper("https://remoteok.com")
scraper.scrape_page()

print(scraper.all_jobs)