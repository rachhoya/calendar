from tkinter import *

window=Tk()
window.geometry("400x350")
window.title("Calendar")
window.config(background="green")

calendar=Label(window,text="CALENDAR",bg="dark grey",font=("Times",28,"bold"))
calendar.place(x=95,y=20)

enter=Label(window,text="Enter Year",bg="light grey",font=("Arial",16,"bold"))
enter.place(x=150,y=90)

entry_box=Entry(window,width=15,font=("Arial",16,"bold"),justify="center")
entry_box.place(x=112,y=130)

show=Button(window,text="Show calendar",bg="light grey",font=("Arial",16,"bold"))
show.place(x=120,y=180)

exit=Button(window,text="Exit",bg="pink",font=("Arial",16,"bold"),bd=3,relief="raised",command=exit)
exit.place(x=175,y=240)

window.mainloop()