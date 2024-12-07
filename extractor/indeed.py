# extractor/indeed.py

import requests
from bs4 import BeautifulSoup

def extract_indeed_jobs(keyword):
    url = f"https://www.indeed.com/jobs?q={keyword}&l="
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        job_list = []
        
        for job_card in soup.find_all('div', class_='job_seen_beacon'):
            title = job_card.find('h2', class_='jobTitle').text.strip()
            company = job_card.find('span', class_='companyName').text.strip()
            link = 'https://www.indeed.com' + job_card.find('a')['href']
            
            job_list.append({
                'title': title,
                'company': company,
                'link': link
            })
        
        return job_list
    else:
        return []