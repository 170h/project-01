import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__)

class Scraper:
    def __init__(self, url):
        self.url = url
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }
        self.all_jobs = []

    def scraping(self, path):
        response = requests.get(f"{self.url}{path}", headers=self.headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            jobs = soup.find("ul", class_="jobs-list-items").find_all("li", class_="bjs-jlid")
            for job in jobs:
                title = job.find("h4", class_="bjs-jlid__h").text.strip()
                company = job.find("a", class_="bjs-jlid__b").text.strip()
                link = job.find("a", class_="b js-jlid__b")["href"]
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

    def engineering(self):
        response = requests.get(f"{self.url}/engineering", headers=self.headers)
        soup = BeautifulSoup(response.content, "html.parser")
        pages = len(soup.find("ul", class_="bsj-nav").find_all("a"))
        for page in range(1, pages + 1):
            self.scraping(f"/engineering/page/{page}")
    
    def skill_areas(self):
        skills = ["python", "typescript", "javascript", "rust"]
        for skill in skills:
            self.scraping(f"/skill-areas/{skill}")

@app.route('/')
def index():
    scraper = Scraper("https://berlinstartupjobs.com/")
    scraper.engineering()
    scraper.skill_areas()
    return render_template('index.html', jobs=scraper.all_jobs)

if __name__ == "__main__":
    app.run(debug=True)