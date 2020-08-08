from tkinter import *
import time
import datetime
from tkinter import messagebox

root = Tk()
root.title("RMS")
price = []
ref = IntVar(root)
ref.set(1)

root.configure(background="powder blue")
lblInfo=Label(root,font=('TIMES NEW ROMAN',40,'bold'),text="RESTAURANT MANAGEMENT SYSTEM", bg="powder blue",bd=10,anchor='w')
lblInfo.pack(padx=20,pady=50)
frame_1 = Frame(root, bg="powder blue")
frame_1.pack(side=LEFT)

#---------------- PAYSLIP --------------
f2 = Frame(root, width=300, height=700, bd=8, bg="powder blue")
f2.pack(side=RIGHT)
DateOfOrder = StringVar()
DateOfOrder.set(time.strftime("%d/%m/%Y"))
payslip = Label(f2, textvariable=DateOfOrder, font=('arial', 21, 'bold'), fg="red", bg="powder blue").grid(row=0, column=0)
txtpayslip = Text(f2, height=22, width=42, bd=16, font=('arial', 13, 'bold'), fg="green", bg="powder blue")
txtpayslip.grid(row=1, column=0)
txtpayslip.insert(END, "\t\tPay Slip\n\n")
txtpayslip.insert(END, "ITEM\t\tQTY.\t\tPRICE\n\n")


starter = StringVar(root)
indian = StringVar(root)
chinese = StringVar(root)
extra = StringVar(root)

starter_choices = ['GOLD COIN', 'FRENCH FRIES', 'CHEESE BALLS', 'DRY MANCHURIAN']
indian_choices = ['PAVBHAJI', 'IDLI', 'DOSA', 'MENDUVADA', 'LUNCH PLATE', 'ROYAL LUNCH', 'DINNER PLATE', 'ROYAL DINNER']
chinese_choices = ['HAKKA NOODLES', 'HONGKONG NOODLES', 'SINGAPORE NOODLES', 'TRIPLE RICE', 'FRIED RICE', 'MANCHOW SOUP']
extra_choices = ['LEMON JUICE', 'BUTTERMILK', 'HOT CHOCLATE', 'SPRITE', 'MAAZA']
starter.set('STARTER')
indian.set('INDIAN')
chinese.set('CHINESE')
extra.set('BEVERAGES')
i = 4

popupMenu1 = OptionMenu(frame_1, starter, *starter_choices)
popupMenu1.grid(row=1, column=1,padx=30,pady=20)
popupMenu1.config(font=('TIMES NEW ROMAN',15,), bg="powder blue")
popupMenu2 = OptionMenu(frame_1, indian, *indian_choices)
popupMenu2.grid(row=2, column=1,padx=30,pady=20)
popupMenu2.config(font=('TIMES NEW ROMAN',15,), bg="powder blue")
popupMenu3 = OptionMenu(frame_1, chinese, *chinese_choices)
popupMenu3.grid(row=3, column=1,padx=30,pady=20)
popupMenu3.config(font=('TIMES NEW ROMAN',15,), bg="powder blue")
popupMenu4 = OptionMenu(frame_1, extra, *extra_choices)
popupMenu4.grid(row=4, column=1,padx=30,pady=20)
popupMenu4.config(font=('TIMES NEW ROMAN',15,), bg="powder blue")

frame_2 = Frame(root, bg="powder blue")
frame_2.pack(side=TOP)
label_a = Label(frame_2,text="ITEM", bg="powder blue",font=('TIMES NEW ROMAN',15,))
label_a.grid(row=1, column=1,padx=20)
label_b = Label(frame_2,text="QUANTITY", bg="powder blue",font=('TIMES NEW ROMAN',15,))
label_b.grid(row=1,column=2,padx=50)
label_c = Label(frame_2, text="PRICE", bg="powder blue",font=('TIMES NEW ROMAN',15,))
label_c.grid(row=1, column=3, padx=10)

def take_starter(*args):
    if starter.get()=="GOLD COIN":
        p = 80
        item = starter.get()
        show(p, item)
    elif starter.get()=="FRENCH FRIES":
        p = 50
        item = starter.get()
        show(p, item)
    elif starter.get()=="CHEESE BALLS":
        p = 90
        item = starter.get()
        show(p, item)
    elif starter.get()=="DRY MANCHURIAN":
        p = 70
        item = starter.get()
        show(p, item)

def take_indian(*args):
    if indian.get()=="PAVBHAJI":
        p = 100
        item = indian.get()
        show(p, item)
    elif indian.get()=="IDLI":
        p = 30
        item = indian.get()
        show(p, item)
    elif indian.get()=="DOSA":
        p = 35
        item = indian.get()
        show(p, item)
    elif indian.get()=="MENDUVADA":
        p = 30
        item = indian.get()
        show(p, item)
    elif indian.get()=="LUNCH PLATE":
        p = 130
        item = indian.get()
        show(p, item)
    elif indian.get()=="ROYAL LUNCH":
        p = 150
        item = indian.get()
        show(p, item)
    elif indian.get()=="DINNER PLATE":
        p = 130
        item = indian.get()
        show(p, item)
    elif indian.get()=="ROYAL DINNER":
        p = 150
        item = indian.get()
        show(p, item)

def take_chinese(*args):
    if chinese.get()=="HAKKA NOODLES":
        p = 120
        item = chinese.get()
        show(p, item)
    elif chinese.get()=="HONGKONG NOODLES":
        p = 135
        item = chinese.get()
        show(p, item)
    elif chinese.get()=="SINGAPORE NOODLES":
        p = 140
        item = chinese.get()
        show(p, item)
    elif chinese.get()=="TRIPLE RICE":
        p = 180
        item = chinese.get()
        show(p, item)
    elif chinese.get()=="FRIED RICE":
        p = 110
        item = chinese.get()
        show(p, item)
    elif chinese.get()=="MANCHOW SOUP":
        p = 120
        item = chinese.get()
        show(p, item)

def take_extra(*args):
    if extra.get()=="LEMON JUICE":
        p = 20
        item = extra.get()
        show(p, item)
    elif extra.get()=="BUTTERMILK":
        p = 25
        item = extra.get()
        show(p, item)
    elif extra.get()=="HOT CHOCLATE":
        p = 60
        item = extra.get()
        show(p, item)
    elif extra.get()=="SPRITE":
        p = 20
        item = extra.get()
        show(p, item)
    elif extra.get()=="MAAZA":
        p = 20
        item = extra.get()
        show(p, item)

frame_4 = Frame(root,bg="powder blue")
frame_4.pack(side=BOTTOM)
def show(p, item):
    frame_3 = Frame(root, bg="powder blue")
    frame_3.pack(side=TOP)
    label_0 = Label(frame_3,text=item, bg="powder blue", font=("TIMES NEW ROMAN", 15))
    label_0.grid(row=i,column=1,padx=10,pady=10)
    quantity = Entry(frame_3)
    quantity.grid(row=i,column=2,padx=20)
    label_2 = Label(frame_3,text=p, bg="powder blue", font=("TIMES NEW ROMAN", 15))
    label_2.grid(row=i,column=3,padx=10)
    if ref.get()==1:
        obj = open("slip.txt", "a")
        obj.write("\n\n\n\tST. JOHN RESTAURANT\n\n\t\tPay Slip\t\n\nITEM\t\t\tQTY.\t\tPRICE\n\n")
        obj.close()
    def no(event):
        if quantity.get()=="":
            messagebox.showinfo("RMS", "Enter some Quantity")
        #elif str(quantity.get()):
        #    messagebox.showinfo("RMS", "Enter a Valid Quantity")

        p3 = p * int(quantity.get())
        price.append(p3)
        pr = str(p3)
        txtpayslip.insert(END, item + "\t\t" + quantity.get() + "\t\t" + pr + "\n")
        obj = open("slip.txt", "a")
        obj.write(item + "\t\t" + quantity.get() + "\t\t" + pr + " Rs.\n")
        obj.close()
        ref.set(0)
        frame_3.destroy()

    next_button = Button(frame_3, text=" ADD ",bg="powder blue", font=("TIMES NEW ROMAN", 15))
    next_button.grid(row=i+1,column=2,padx=10,pady=10)
    next_button.bind("<Button-1>", no)

def finish(event):

    tp0 = sum(price)
    gst = (tp0//100)*18
    tp = str(tp0+gst)
    txtpayslip.insert(END, "\nSUB TOTAL\t\t\t\t" + str(tp0) + "\n")
    txtpayslip.insert(END, "\nCGST TAX\t\t9%\t\t" + str(gst//2) + "\n")
    txtpayslip.insert(END, "\nSGST TAX\t\t9%\t\t" + str(gst//2) + "\n")
    txtpayslip.insert(END, "\n\nTOTAL AMOUNT\t\t\t\t" + tp + "\n")
    obj = open("slip.txt", "a")
    obj.write("\n\tSUB TOTAL\t\t" + str(tp0) + " Rs.\n")
    obj.write("\tCGST TAX\t9%\t" + str(gst//2) + " Rs.\n")
    obj.write("\tSGST TAX\t9%\t" + str(gst // 2) + " Rs.\n")
    obj.write("\n\tTOTAL\t\t\t" + tp + " Rs.\n\n\t   THANK YOU FOR VISITING!!!\n\n")
    obj.close()


total_button = Button(frame_4, text="TOTAL",bg="powder blue", font=("TIMES NEW ROMAN", 20))
total_button.grid(row=1,column=1,padx=10,pady=10)
total_button.bind("<Button-1>", finish)

def initial(event):
    del price[::]
    txtpayslip.delete("2.0\n\n", END)
    starter.set('STARTER')
    indian.set('INDIAN')
    chinese.set('CHINESE')
    extra.set('BEVERAGES')
    txtpayslip.insert(END, "\n\nITEM\t\tQTY.\t\tPRICE\n\n")
    ref.set(1)
    take_starter()

reset_button = Button(frame_4, text="RESET", bg="powder blue", font=("TIMES NEW ROMAN", 20))
reset_button.grid(row=1, column=2, padx=10, pady=10)
reset_button.bind("<Button-1>", initial)

def close(event):
    exit = messagebox.askyesno("RMS", "Do you want to exit the system")
    if exit > 0:
        root.destroy()
        return

exit_button = Button(frame_4, text="EXIT", bg="powder blue", font=("TIMES NEW ROMAN", 20))
exit_button.grid(row=1, column=3, padx=10, pady=10)
exit_button.bind("<Button-1>", close)

starter.trace('w', take_starter)
indian.trace('w', take_indian)
chinese.trace('w', take_chinese)
extra.trace('w', take_extra)


root.mainloop()
