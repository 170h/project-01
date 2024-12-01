import requests

movie_ids = [
    238, 680, 550, 185, 641, 515042, 152532, 120467, 872585, 906126, 840430
]

url = "https://nomad-movies.nomadcoders.workers.dev/movies/"

for movie_id in movie_ids:
  response = requests.get(f"{url}{movie_id}")
  movie = response.json()
  
  title = movie["title"]
  vote = movie["vote_average"]
  overview = movie["overview"]
  
  print(f"\n{title} - {vote}")
  print(f"\n{overview}\n")
  


'''
import requests
from bs4 import BeautifulSoup

all_jobs = []

def scrape_page(url):
  response = requests.get(url)
git add .
  soup = BeautifulSoup(response.content, "html.parser")

  jobs = soup.find("section", class_="jobs").find_all("li")[1:-1]

  for job in jobs:
    title = job.find("span", class_="title").text
    company, position, *region = job.find_all("span", class_="company")
    region = "No Region" if not len(region) else region[0].text
    job_url = job.find("a")["href"]
    job_data = {
      "title": title,
      "company": company.text,
      "position": position.text,
      "region": region,
      "url": f"https://weworkremotely.com{job_url}"
    }
    all_jobs.append(job_data)

def get_pages(url):
  response = requests.get(url)
  soup = BeautifulSoup(response.content, "html.parser")
  return len(soup.find("div", class_="pagination").find_all("span", class_="page"))

total_pages = get_pages("https://weworkremotely.com/remote-full-time-jobs?page=1")

for x in range(total_pages):
  url = f"https://weworkremotely.com/remote-full-time-jobs?page={x+1}"
  scrape_page(url)

print(len(all_jobs))
'''