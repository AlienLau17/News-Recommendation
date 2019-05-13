import tkinter as tk
from tkinter import *
import webbrowser
from functools import partial
from PIL import ImageTk
from PIL import Image
from Data import news

# from s3 import get_recommendation_from_url
from tf_idf_v2 import get_recommendation_from_url



class basedesk():
    def __init__(self, master):

        self.root = master

        self.root.title('Welcome')
        self.root.geometry('800x500')
        # self.root.geometry('1000x1000')
        self.label = tk.Label(self.root, image=photo1)  # 图片
        self.label.pack()

        initface(self.root)

        self.root.mainloop()



class initface():
    def __init__(self, master):
        self.master = master

        # self.master.config(bg='green')
        # 基准界面initface
        self.initface = tk.Frame(self.master)
        self.initface.pack()

        btn1 = tk.Button(self.initface, text='BUSINESS', width=15, height=2, command=partial(self.change, 'business'))
        btn1.pack()
        btn2 = tk.Button(self.initface, text='ENTERTAINMENT', width=15, height=2, command=partial(self.change, 'entertainment'))
        btn2.pack()
        btn3 = tk.Button(self.initface, text='GENERAL', width=15, height=2, command=partial(self.change, 'general'))
        btn3.pack()
        btn4 = tk.Button(self.initface, text='HEALTH', width=15, height=2, command=partial(self.change, 'health'))
        btn4.pack()
        btn5 = tk.Button(self.initface, text='SPORT', width=15, height=2, command=partial(self.change, 'sport'))
        btn5.pack()
        btn6 = tk.Button(self.initface, text='SCIENCE', width=15, height=2,
                         command=partial(self.change, 'science'))
        btn6.pack()
        btn7 = tk.Button(self.initface, text='TECHNOLOGY', width=15, height=2,
                         command=partial(self.change, 'technology'))
        btn7.pack()

    def change(self, category):
        self.initface.destroy()
        App(self.master, category)




class App:
    def __init__(self, master, category):
        self.master = master
        self.category = category
        self.news = news
        self.category = category
        self.records = self.news[self.category][:10]
        self.mark = 0

        self.initWidgets()


    def initWidgets(self):
        self.topF = Frame(self.master, pady=5, width=100, height=10)
        self.topF.pack(fill=Y, expand=YES)

        self.v = StringVar()
        self.lb = Listbox(self.topF, width=80, height=10, listvariable=self.v)

        for ind, item in enumerate(self.records):
            self.lb.insert('end', str(ind + 1) + ". " + item['title'].split("-")[0])  # 从最后一个位置开始加入值

        for i in range(len(self.records)):
            if not i % 2:
                self.lb.itemconfig(i, fg="white", bg="#808080")

        self.lb.pack()


        self.btn_back = tk.Button(self.master, text='Back to Category', width=15, height=1, command=self.back)
        self.btn_back.place(x=37, y=8)


        button1 = tk.Button(self.topF, text='Browse', width=15, height=2, command=self.selection).place(x=200, y=200)

        button2 = tk.Button(self.topF, text='Other News', width=15, height=2, command=self.change_news).place(x=350,
                                                                                                              y=200)

    def back(self):
        self.topF.destroy()
        self.btn_back.destroy()
        initface(self.master)

    def change_news(self):
        self.mark += 10
        self.records = self.news[self.category][self.mark: self.mark + 10]

        self.display_recommend()

    def selection(self):
        value = self.lb.get(self.lb.curselection())
        value = value[:2]
        if '.' not in value:
            record_index = 9
        else:
            record_index = int(value[0]) - 1
        url = self.records[record_index]['url']
        webbrowser.open_new(url)

        # self.whether_like(url)

        self.recommend(url)

    # def whether_like(self, url):
    #
    #     self.top1 = tk.Toplevel()
    #     b1 = tk.Button(self.top1, text='like', command=self.like)
    #     b1.pack()
    #     b2 = tk.Button(self.top1, text='dislike', command=self.dislike)
    #     b2.pack()
    #     b3 = tk.Button(self.top1, text="don't care", command=self.do_not_care)
    #     b3.pack()
    #
    #     # self.top1.mainloop()
    #
    # def like(self):
    #     self.top1.destroy()
    #
    # def dislike(self):
    #     self.top1.destroy()
    #
    # def do_not_care(self):
    #     self.top1.destroy()

    def recommend(self, url):

        self.records = self.model(url)

        self.display_recommend()

    def model(self, url):
        '''
        :param url:
        :return: a list of dict:[{'url':xxx, ''title': xxx}, {'url':xxx, ''title': xxx}...]. Each dict represents a news
        '''
        # self.mark += 10
        # tmp = self.news[self.category][self.mark: self.mark + 10]
        tmp = get_recommendation_from_url(self.category, url)
        return tmp


    def display_recommend(self):
        tmp = ()
        for i in range(len(self.records)):
            tmp += (str(i + 1) + "." + self.records[i]['description'],)
        self.v.set(tmp)

        for i in range(len(self.records)):
            if not i % 2:
                self.lb.itemconfig(i, fg="white", bg="#808080")




root = tk.Tk()
photo1 = tk.PhotoImage(file=r"news2.gif")
# photo2 = tk.PhotoImage(file=r"newsletter.jpg")
photo2 = Image.open("news3.jpg")
photo2 = photo2.resize((725, 250), Image.ANTIALIAS)
photo2 = ImageTk.PhotoImage(photo2)
basedesk(root)