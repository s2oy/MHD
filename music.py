import tkinter as tk
from tkinter import messagebox
from lastnightstory import playlastnight
from sketerboy import playsketerboy
from sakuranbo import playsakuranbo
from assignmentSong import playassignmentsong
from white import playwhite

music = {'어젯밤 이야기':0, '과제곡':0,'화이트':0,'사쿠란보':0,'스케이터보이':0}
order = []
sum = 0

def select(item):
    global sum

    if item not in music\
            :
        print("선택 안함")
    this_music = music.get(item)
    sum += this_music
    order.append(item)
    textarea.insert(tk.INSERT, item+" ")
    label1['text'] = "선택한곡:"+str(sum)

def btn_exit():
    msgbox = tk.messagebox.askquestion('확인','플레이를 하시겠습니까?')
    if msgbox == 'yes':
        exit()

window = tk.Tk()
window.title('노래 고르기')
window.geometry("600x600")
frame1 = tk.Frame(window)
frame1.pack()

tk.Button(frame1, text="어젯밤 이야기", command=playlastnight,width=10, height=2).grid(row=0,column=1)
tk.Button(frame1, text="과제곡", command=playassignmentsong,width=10, height=2).grid(row=0,column=2)
tk.Button(frame1, text="화이트", command=playwhite,width=10, height=2).grid(row=0,column=3)
tk.Button(frame1, text="사쿠란보", command=playsakuranbo,width=10, height=2).grid(row=0,column=4)
tk.Button(frame1, text="스케이터보이", command=playsketerboy,width=10, height=2).grid(row=0,column=5)

label1 = tk.Label(window, text="선택한곡:",width=100,height=2,fg="blue")
label1.pack()

textarea = tk.Text(window)
textarea.pack()

window.mainloop()




