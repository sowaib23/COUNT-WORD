from tkinter import *
import re
def count_words():
    tx=entry.get("1.0",END)
    word=re.findall(r'\b\w+\b',tx)
    count=len(word)
    res.config(text=f"Words : {count}")
rt=Tk()
rt.title("Word Counter")
entry=Text(rt,height=10,width=40)
entry.pack()
btn=Button(rt,text="Count Words",command=count_words)
btn.pack()
res=Label(rt,text="Words : 0")
res.pack()
rt.mainloop()
