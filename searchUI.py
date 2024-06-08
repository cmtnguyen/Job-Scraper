import tkinter as tk
from tkinter import messagebox
from googleapiclient.discovery import build
api_key = <API_KEY>
pse_id = <PSE_ID>

service = build("customsearch", "v1", developerKey=api_key)

r = tk.Tk()
r.geometry('650x500')
r.title('Searching...')
tk.Label(r, text='Search Term', width=30).grid(row=0)
search = tk.StringVar()
e1 = tk.Entry(r, textvariable=search, width=50)
e1.insert(0, "Associate Product Manager")
e1.grid(row=0, column=1)

def google_search():
    search_term = search.get()
    if (search_term != ""):
        res = (service.cse().list(q=search_term, exactTerms=search_term, cx=pse_id, dateRestrict="w[1]", gl="us", siteSearch="jobs.lever.co", siteSearchFilter="i")).execute()
        jobs = res['items']
        res.update((service.cse().list(q=search_term, exactTerms=search_term, cx=pse_id, dateRestrict="w[1]", gl="us", siteSearch="boards.greenhouse.io", siteSearchFilter="i")).execute())
        jobs += res['items']
        show_result(jobs)
    else:
        messagebox.askretrycancel("Please Enter A Search Term", "There is no search term. Try again?")


def show_result(jobs):
    jobSet = []
    for job in jobs:
        jobSet.append([job['link'], job['title']])
    for job in jobSet:
        mylist.insert(tk.END, job[0])
        mylist.insert(tk.END, job[1])
        mylist.insert(tk.END, "")


tk.Button(r, text='Search', width=25, command=lambda: [mylist.delete(0, tk.END), google_search(), search.set("")],
                   justify="center").grid(row=1, column=0, columnspan=2)
scrollbar = tk.Scrollbar(r)
scrollbar.grid(row=2, column=3)
mylist = tk.Listbox(r, yscrollcommand=scrollbar.set, height=25, width=100)
mylist.grid(row=2, column=0, columnspan=3)
scrollbar.config(command=mylist.yview)

r.mainloop()
