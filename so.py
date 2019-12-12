import requests
from bs4 import BeautifulSoup

URL = f"https://stackoverflow.com/jobs?q=python&sort=i"

def get_last_page():
  result = requests.get(URL)
  soup = BeautifulSoup(result.text, "html.parser")
  pages = soup.find("div", {"class":"s-pagination"}).find_all("a")
  last_page = pages[-2].get_text(strip=True)
  return last_page

def extract_jobs(last_page):
  jobs = []
  for page in range(last_page):
    print(pgae)




def get_jobs():
  last_page = get_last_page()
  jobs = extract_jbos(last_page)
  return jobs