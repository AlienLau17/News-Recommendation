import tkinter as tk
import webbrowser

from connect_db import FindData


connect_info = ["localhost","root","databasehw","LargeData",3306]
records = FindData(connect_info).test_db()[:10]


window = tk.Tk()
window.title('my window')
window.geometry('1000x1000')

# var1 = tk.StringVar()    #创建变量
# l =tk.Label(window,bg='yellow',width=4,textvariable=var1)
# l.pack()



def print_selection():
    value = lb.get(lb.curselection())   #获取当前选中的文本
    tmp = value[:2]
    print(tmp)
    if '.' not in tmp:
        record_index = 9
    else:
        print('here')
        record_index = int(value[0]) - 1
    print(record_index)
    webbrowser.open_new(records[record_index]['url'])
    for ind, item in enumerate(records[::-1]):
        lb.insert(ind, str(ind + 1) + ". " + item['title'].split("-")[0])
    for i in range(len(records)):
        if not i % 2:
            lb.itemconfig(i, fg="black", bg="#F5F5DC")
    lb.pack()


b1 = tk.Button(window, text='print selection', width=15,
              height=2, command=print_selection)
b1.pack()

#创建Listbox

lb = tk.Listbox(window, width=100, height=10)  #将var2的值赋给Listbox


for ind, item in enumerate(records):
    lb.insert('end', str(ind+1) +". "+ item['title'].split("-")[0])  #从最后一个位置开始加入值
# lb.insert(1, 'first')       #在第一个位置加入'first'字符
# lb.insert(2, 'second')      #在第二个位置加入'second'字符
# lb.delete(2)                #删除第二个位置的字符

for i in range(len(records)):
    if not i % 2:
        lb.itemconfig(i, fg="black", bg="#F5F5DC")
lb.pack()

#显示主窗口
window.mainloop()