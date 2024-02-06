
from tkinter import *
from tkinter import messagebox
window=Tk()
window.geometry("420x520")
window.title("BMI CALCULATOR")
icon=PhotoImage(file="bmi.png")
window.config(bg="#fc0362")
window.iconphoto(True,icon)
def calculate_bmi():
    height_=float(height_entry.get())
    weight=float(weight_entry.get())
    m=height_/100
    bmi_=float(weight/(m**2))
  
    
    label1.config(text=bmi_)
    if(bmi_<=18.5):
        label2.config(text="UnderWeight")  
    elif (bmi_>18.5 and bmi_<=25):
        label2.config(text="Normal Weight") 
    elif(bmi_>25 and bmi_<=29):
        label2.config(text="OverWeight")
    else:
        label2.config(text="OBESITY")

    
       
label=Label(window,text="Body Mass Index",bg="#fc0362",fg="black",font=("Calibri",20,"bold"))
label.place(x=20,y=30)
label=Label(window,text="Enter Your Height(in cm.):",bg="#fc0362",fg="black",font=("Calibri",20,"bold"))
label.place(x=20,y=120)
label=Label(window,text="Enter Your Weight(in kg.):",bg="#fc0362",fg="black",font=("Calibri",20,"bold"),)
label.place(x=20,y=200)
height_entry=Entry(window,font=("Calibri",16,"bold"),width=25,bg="white",fg="black")
height_entry.place(x=20,y=160)
weight_entry=Entry(window,font=("Calibri",16,"bold"),width=25,bg="white",fg="black")
weight_entry.place(x=20,y=240)
bmi=DoubleVar()

calculate_button=Button(window,text="CALCULATE",command=calculate_bmi,
                        font=("Calibri",10,"bold"),bg="black",fg="white",
                        width=10,height=4,activebackground="black",activeforeground="white")
calculate_button.place(x=80,y=280)
label1=Label(window,bg="#fc0362",fg="black",font=("Calibri",20,"bold"))
label1.place(x=80,y=380)
label2=Label(window,bg="#fc0362",fg="black",font=("Calibri",20,"bold"))
label2.place(x=80,y=420)
window.mainloop()