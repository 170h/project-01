# extractor/wwr.py

import requests
from bs4 import BeautifulSoup

def extract_wwr_jobs(keyword):
    url = f"https://weworkremotely.com/remote-jobs/search?term={keyword}"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        job_list = []
        
        for job_card in soup.find_all('section', class_='jobs'):
            title = job_card.find('h2').text.strip()
            company = job_card.find("span", class_="company").text.strip()
            link = 'https://weworkremotely.com' + job_card.find('a')['href']
            
            job_list.append({
                'title': title,
                'company': company,
                'link': link
            })
        
        return job_list
    else:
        return []