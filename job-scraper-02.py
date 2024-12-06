import requests
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, url):
        self.url = url
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }
        self.all_jobs = []
    
    def engineering(self):
        response = requests.get(f"{self.url}/engineering", headers=self.headers)
        soup = BeautifulSoup(response.content, "html.parser")
        page_count = len(soup.find("ul", class_="bsj-nav").find_all("a"))
        for page in range(1, page_count + 1):
            response = requests.get(f"{self.url}/engineering/page/{page}", headers=self.headers)
            soup = BeautifulSoup(response.content, "html.parser")
            jobs = soup.find("ul", class_="jobs-list-items").find_all("li", class_="bjs-jlid")
            if response.status_code == 200:
                for job in jobs:
                    title = job.find("h4", class_="bjs-jlid__h").text.strip()
                    company = job.find("a", class_="bjs-jlid__b").text.strip()
                    link = job.find("a", class_="bjs-jlid__b")["href"]
                    description = job.find("div", class_="bjs-jlid__description").text.strip()
                    job_data = {
                        "title": title,
                        "company": company,
                        "description": description,
                        "link": link
                    }
                    self.all_jobs.append(job_data)
            else:
                print(f"Error: {response.status_code}")

    def skill_areas(self):
        skills = ["python", "typescript", "javascript", "rust"]
        for skill in skills:
            response = requests.get(f"{self.url}/skill-areas/{skill}", headers=self.headers)
            soup = BeautifulSoup(response.content, "html.parser")
            jobs = soup.find("ul", class_="jobs-list-items").find_all("li", class_="bjs-jlid")

            print(f"{self.url}/skill-areas/{skill}")

            if response.status_code == 200:
                for job in jobs:
                    title = job.find("h4", class_="bjs-jlid__h").text.strip()
                    company = job.find("a", class_="bjs-jlid__b").text.strip()
                    link = job.find("a", class_="bjs-jlid__b")["href"]
                    description = job.find("div", class_="bjs-jlid__description").text.strip()
                    job_data = {
                        "title": title,
                        "company": company,
                        "description": description,
                        "link": link
                    }
                    self.all_jobs.append(job_data)
            else:
                print(f"Error: {response.status_code}")

scraper = Scraper("https://berlinstartupjobs.com/")
scraper.engineering()
scraper.skill_areas()

print(scraper.all_jobs)