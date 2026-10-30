from tkinter import *
import calendar

window=Tk()
window.geometry("400x350")
window.title("Calendar")
window.config(background="green")

def show_calendar():
    window1=Tk()
    window.geometry("550x600")
    window.title("CALENDAR")
    window.config(background="white")
    year=int(entry_box.get())
    year2=calendar.calendar(year)

    contents=Label(window1,text=year2,font=("Consolas",10,"bold"))
    contents.grid(row=5,column=1,x=20)


    
    window1.mainloop()


cal=Label(window,text="CALENDAR",bg="dark grey",font=("Times",28,"bold"))
cal.place(x=95,y=20)

enter=Label(window,text="Enter Year",bg="light grey",font=("Arial",16,"bold"))
enter.place(x=150,y=90)

entry_box=Entry(window,width=15,font=("Arial",16,"bold"),justify="center")
entry_box.place(x=112,y=130)

show=Button(window,text="Show calendar",bg="light grey",font=("Arial",16,"bold"),command=show_calendar)
show.place(x=120,y=180)

exit=Button(window,text="Exit",bg="pink",font=("Arial",16,"bold"),bd=3,relief="raised",command=exit)
exit.place(x=175,y=240)

window.mainloop()
