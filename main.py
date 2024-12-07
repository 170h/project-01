from extractor.indeed import extract_indeed_jobs
from extractor.wwr import extract_wwr_jobs

keyword = input("검색어를 입력하세요: ")
indeed = extract_indeed_jobs(keyword)
wwr = extract_wwr_jobs(keyword)
job = indeed + wwr

