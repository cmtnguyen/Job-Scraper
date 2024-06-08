from googleapiclient.discovery import build

api_key = <API_KEY>
pse_id = <PSE_ID>
search = "Associate Product Manager"
search2 = "Product Manager I"
search3 = "Associate Product Owner"

service = build("customsearch", "v1", developerKey=api_key)

def google_search(search_term):
    res = (service.cse().list(q=search_term, exactTerms=search_term, cx=pse_id, dateRestrict="w[1]", gl="us", siteSearch="jobs.lever.co", siteSearchFilter="i")).execute()
    jobs = res['items']
    res.update((service.cse().list(q=search_term, exactTerms=search_term, cx=pse_id, dateRestrict="w[1]", gl="us", siteSearch="boards.greenhouse.io", siteSearchFilter="i")).execute())
    jobs += res['items']
    return jobs


jobs = google_search(search) + google_search(search2) + google_search(search3)
jobSet = []
for job in jobs:
    jobSet.append([job['link'], job['title']])

jobSet = list(set(map(tuple,jobSet)))

print(f"Generating {len(jobSet)} results\n")
for job in jobSet:
    print(job[0])
    print(job[1])
    print("\n")
