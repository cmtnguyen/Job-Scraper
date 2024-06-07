import requests
from bs4 import BeautifulSoup


url = "https://www.google.com/search?q=site:lever.co+OR+site:greenhouse.io+associate+product+manager&client=firefox-b-1-d&sca_esv=1c0c234ed71f94a2&sxsrf=ADLYWIJMs_HPqdJ5yAr9q34HVKh8CfdoTg:1717724863665&source=lnt&tbs=qdr:w&sa=X&ved=2ahUKEwjm_8fir8iGAxXIIjQIHVlkCcUQpwV6BAgBEAk&biw=1434&bih=742&dpr=1"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
}
resp = requests.get(url, headers=headers)
code = resp.status_code
if code != 200:
    print(f"There is an error requesting the specific URL. Error Code: {code}")
soup = BeautifulSoup(resp.content, "html.parser")
results = soup.find(id="rso")
job_elements = results.find_all("div", class_="MjjYud")
job_num = 1

for job_element in job_elements:
        title_element = job_element.find("h3", class_="LC20lb MBeuO DKV0Md", string=lambda text: "product" in text.lower())
        url_element = job_element.find("div", class_="yuRUbf")
        desc_element = job_element.find("div", class_="kb0PBd cvP2Ce A9Y9g")
        if url_element != None and title_element != None and desc_element != None:
            url_element = url_element.find("a")["href"]
            desc_element = desc_element.find("span")
            print(f"This is job {job_num}")
            job_num += 1
            print(url_element)
            print(title_element.text.strip())
            if desc_element != None:
                print(f"{desc_element.text.strip()} \n")
            else:
                print()




