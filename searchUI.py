import tkinter as tk
from tkinter import messagebox
from googleapiclient.discovery import build
api_key = <API_KEY>
pse_id = <PSE_ID>

service = build("customsearch", "v1", developerKey=api_key)

r = tk.Tk()
r.geometry('650x500')
r.title('Searching for jobs...')
tk.Label(r, text='Search Role', width=30).grid(row=0)
search = tk.StringVar()
e1 = tk.Entry(r, textvariable=search, width=50)
e1.insert(0, "Associate Product Manager")
e1.grid(row=0, column=1)

def google_search():
    search_term = search.get()
    if search_term != "":
        res = (service.cse().list(q=search_term, exactTerms=search_term, cx=pse_id, dateRestrict="w[1]", gl="us", siteSearch="jobs.lever.co", siteSearchFilter="i")).execute()
        jobs = res['items']
        res.update((service.cse().list(q=search_term, exactTerms=search_term, cx=pse_id, dateRestrict="w[1]", gl="us", siteSearch="boards.greenhouse.io", siteSearchFilter="i")).execute())
        jobs += res['items']
        if len(jobs) > 0:
            show_result(jobs)
        else:
            messagebox.askretrycancel("Sorry!", "Your search had no results. Try again?")
    else:
        messagebox.askretrycancel("Please Enter A Search Term", "There is no search term. Try again?")


def show_result(jobs):
    jobSet = []
    for job in jobs:
        jobSet.append([job['link'], job['title']])
    for job in jobSet:
        search_list.insert(tk.END, job[0])
        search_list.insert(tk.END, job[1])
        search_list.insert(tk.END, "")


tk.Button(r, text='Search', width=25, command=lambda: [search_list.delete(0, tk.END), google_search(), search.set("")],
          justify="center").grid(row=1, column=0, columnspan=2)
scrollbar = tk.Scrollbar(r)
scrollbar.grid(row=2, column=3)
search_list = tk.Listbox(r, yscrollcommand=scrollbar.set, height=25, width=100)
search_list.grid(row=2, column=0, columnspan=3)
scrollbar.config(command=search_list.yview)

def save_file():
    if search_list.get(0) != "":
        with open("searchlog.txt", "w") as savefile:
            for x in search_list.get(0, tk.END):
                savefile.write(x)
                savefile.write("\n")

        print("Search has been successfully saved!")
    else:
        messagebox.askretrycancel("Please Conduct a Search", "There is no search data. Try again?")


tk.Button(r, text='Save', width=25, command=save_file,
                   justify="center").grid(row=3, column=0, columnspan=2)

r.mainloop()
