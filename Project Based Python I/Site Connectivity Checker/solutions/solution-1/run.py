# Source Code Link:
# https://hackr.io/blog/python-projects

import urllib.request
import tkinter as tk


def test_connectivity():
    window = tk.Tk()
    window.geometry('600x400')
    head = tk.Label(window, text='Website Connectivity Checker',
              font=('Calibri 15'))
    head.pack(pady=20)

    def check_url():
        web = (url.get())
        status_code = urllib.request.urlopen(web).getcode()
        website_is_up = status_code == 200

        if website_is_up:
            tk.Label(window, text='Website Available',
                   font=('Calibri 15')).place(x=260, y=200)
        else:
            tk.Label(window, text='Website Not Available',
                   font=('Calibri 15')).place(x=260, y=200)

    url = tk.StringVar()
    tk.Entry(window, textvariable=url).place(x=200, y=80, height=30, width=280)
    tk.Button(window, text='Check', command=check_url).place(x=285, y=150)
    window.mainloop()


if __name__ == '__main__':
    test_connectivity()