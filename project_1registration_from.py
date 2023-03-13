from tkinter import *
root = Tk()
root.geometry("1000x700")

def getvalues():
    print("Accepted")

# Heading
Label(root, text="python Registration Form", font="ar 15 bold").grid(row=0, column=3)

# Field Name
name = Label(root, text="Name")
gender = Label(root, text="Gender")
phone = Label(root, text="Phone")
emergency = Label(root, text="Emergency ")
payment_mode = Label(root, text="Payment_mode")

# Packing Fields
name.grid(row=1, column=2)
gender.grid(row=2, column=2)
phone.grid(row=3, column=2)
emergency.grid(row=4, column=2)
payment_mode.grid(row=5, column=2)

# Variable for  storing data
name_value = StringVar
gender_value = StringVar
phone_value = StringVar
emergency_value = StringVar
payment_mode_value = StringVar
check_value = IntVar

# Creating entry filed
nameentry = Entry(root, textvariable =name_value)
genderentry = Entry(root, textvariable =gender_value)
phoneentry = Entry(root, textvariable =phone_value)
emergencyentry = Entry(root, textvariable =emergency_value )
payment_modeentry = Entry(root,textvariable =payment_mode_value)

# packing entry fields
nameentry.grid(row=1, column=3)
genderentry.grid(row=2, column=3)
phoneentry.grid(row=3, column=3)
emergencyentry.grid(row=4, column=3)
payment_modeentry.grid(row=5, column=3)


# Crating check box
checkbtn = Checkbutton(text="remember me?", variable = check_value)
checkbtn.grid(row=6, column=3)

# Submit button
Button(text="Submit", command=getvalues).grid(row=7, column=3)
root.mainloop()
