from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup

p = sync_playwright().start()

browser = p.chromium.launch(headless=False)

page = browser.new_page()

page.goto("https://www.wanted.co.kr/")
time.sleep(5)

page.click("button.Aside_searchButton__rajGo")
time.sleep(5)

page.get_by_placeholder("검색어를 입력해 주세요").fill("flutter")
time.sleep(5)

page.keyboard.down("Enter")
time.sleep(5)

page.click("a#search_tab_position")
time.sleep(5)

for x in range(5):
    page.keyboard.down("End")
    time.sleep(5)

content = page.content()

p.stop()
# 파일 이름이 playwright.py로 되어 있어 Python이 이를 Playwright 라이브러리 대신 로컬 파일로 인식
soup = BeautifulSoup(content, "html.parser")

jobs = soup.find("div", class_="JobList_container__Hv_EA").find_all("div", class_="JobCard_container__REty8")

jobs_list = []

for job in jobs:
    link = f"https://www.wanted.co.kr{job.find('a')['href']}"
    title = job.find("strong", class_="JobCard_title__HBpZf").text
    company = job.find("span", class_="JobCard_companyName__N1YrF").text
    reward = job.find("span", class_="JobCard_reward__cNlG5").text
    job = {
        "title": title,
        "company": company,
        "reward": reward,
        "link": link
    }
    jobs_list.append(job)

print(jobs_list)
print(len(jobs))