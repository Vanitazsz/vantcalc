from tkinter import *
from functools import partial

win, row_num, col_num =Tk(), 2, 0
res = Label(win, width=28, height=3, text="0", borderwidth=4, relief="sunken", font=("Constania", 16), anchor=E, bg="green")
res.grid(row=0, column=0, columnspan=4)
btn_txt = ["**", "//", "%", "C", "7", "8", "9", "+", "4", "5", "6", "-", "1", "2", "3", "*", ".", "0", "=", "/"]
def calcf(value):
    current_text = res.cget("text")
    if value == "C":res.config(text="0")
    elif value == "=":
        try:
            result = eval(current_text)
            res.config(text=str(result))
        except Exception: res.config(text="Error")
    else:
        if current_text == "0" or current_text == "Error" or current_text == "Ellipsis":res.config(text=value)
        else: res.config(text=current_text + value)
for i in range(len(btn_txt)):
    btn_text = btn_txt[i]
    Button(win, width=5, height=2, padx=1,pady=3,text=btn_text, font=("Constania", 16),relief="raised", command=partial(calcf, btn_text), bd = 4, bg="lightblue").grid(row=row_num+2, column=col_num, padx=8, pady=5)
    col_num += 1
    if col_num == 4: col_num = 0; row_num += 1
win.title("Calculator ni Lhanzy"), win.geometry("360x505+800+260"), win.config(bg='#565051'), win.mainloop()
