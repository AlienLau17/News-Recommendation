from tkinter import *
import tkinter as tk
import webbrowser
from connect_db import FindData


class App:
    def __init__(self, master):
        connect_info = ["localhost", "root", "databasehw", "LargeData", 3306]
        self.news = FindData(connect_info).test_db()
        self.records = self.news[:10]
        self.mark = 0

        self.master = master
        self.initWidgets()


    def initWidgets(self):
        topF = Frame(self.master, width=100, height=10)
        topF.pack(fill=Y, expand=YES)


        self.v = StringVar()
        self.lb = Listbox(topF, width=100, height=10, listvariable=self.v)

        for ind, item in enumerate(self.records):
            self.lb.insert('end', str(ind + 1) + ". " + item['title'].split("-")[0])  # 从最后一个位置开始加入值

        for i in range(len(self.records)):
            if not i % 2:
                self.lb.itemconfig(i, fg="black", bg="#F5F5DC")

        self.lb.pack()



        button1 = tk.Button(topF, text='Browse', width=15, height=2, command=self.selection).pack()



    def selection(self):
        value = self.lb.get(self.lb.curselection())
        value = value[:2]
        if '.' not in value:
            record_index = 9
        else:
            record_index = int(value[0]) - 1
        webbrowser.open_new(self.records[record_index]['url'])

        self.recommend(record_index)


    def recommend(self, index):

        self.records = self.model(index)

        self.display_recommend()



    def model(self, url):
        '''

        :param url:
        :return: a list of dict:[{'url':xxx, ''title': xxx}, {'url':xxx, ''title': xxx}...]. Each dict represents a news
        '''
        self.mark += 10
        tmp = self.news[self.mark: self.mark + 10]
        return tmp


        pass

    def display_recommend(self):
        tmp = ()
        for i in range(len(self.records)):
            tmp += (str(i+1) + "." + self.records[i]['title'],)
        self.v.set(tmp)


        for i in range(len(self.records)):
            if not i % 2:
                self.lb.itemconfig(i, fg="black", bg="#F5F5DC")



root = Tk()
root.title('Welcome')
root.geometry('1000x300')

# 改变窗口图标
# root.iconbitmap('images/fklogo.ico')
App(root)
root.mainloop()
