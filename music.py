import tkinter as tk
from tkinter import messagebox
from playsound import playsound
#
# m1 =('D:\MHD\mp3\assignmentSong.mp3')
# m2 = ('D:\MHD\mp3\lastNightStory.mp3')

price = {'과제곡':0,'어젯밤 이야기':0,'화이트':0,'분홍신':0,'사쿠란보':0}
order = []
sum = 0

def add(item):
    global sum
    this_price = price.get(item)
    sum += this_price
    order.append(item)
    textarea.insert(tk.INSERT, item+"")
    label1['text'] ="선택한곡:"

def btn_exit():
    msgbox = tk.messagebox.askquestion('확인','플레이를 시작하겠습니까?')
    if msgbox == 'yes':
        exit()
window = tk.Tk()
window.title("노래 고르기")
window.geometry("400x600")

frame1 = tk.Frame(window)
frame1.pack()

tk.Button(frame1, text="과제곡",command=lambda:add("과제곡"),width=10,height=2).grid(row=0,column=0)
tk.Button(frame1, text="어젯밤이야기",command=lambda:add('어젯밤 이야기'),width=10,height=2).grid(row=1,column=0)
tk.Button(frame1, text="화이트",command=lambda:add("화이트"),width=10,height=2).grid(row=2,column=0)
tk.Button(frame1, text="분홍신",command=lambda : add('분홍신'),width=10,height=2).grid(row=3,column=0)
tk.Button(frame1, text="사쿠란보",command=lambda:add("사쿠란보"),width=10,height=2).grid(row=4,column=0)
tk.Button(frame1, text="나가기",command=btn_exit,width=10,height=2).grid(row=5,column=0)
label1 = tk.Label(window, text="플레이할곡: ", width=100,height=2,fg="blue")
label1.pack()
textarea = tk.Text(window)
textarea.pack()

window.mainloop()
