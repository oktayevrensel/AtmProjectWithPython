from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import sqlite3

segoe_ui=("segoe ui",18) 
class Atm:
    def __init__(self,main):
        self.conn=sqlite3.connect("atm.db",timeout=150)
        self.login=False
        self.main=main
        self.top=Label(self.main,text='... Bank',bg='#1f1c2c',fg='white',font=('Courier',30,'bold'))
        self.top.pack(fill=X)
        self.frame=Frame(self.main,bg='#2193b0',width=600,height=500)

        self.account=Label(self.frame,text='Hesap Numarası',bg="#728B8E",fg="white",font=segoe_ui)
        self.accountEntry=Entry(self.frame,bg='#FFFFFF',highlightcolor="#50A8B0", highlightthickness=2, highlightbackground="white")
        self.pin=Label(self.frame,text='Şifre',bg="#728B8E",fg="white",font=segoe_ui)
        self.pinEntry=Entry(self.frame,show='*',bg='#FFFFFF',highlightcolor="#50A8B0", highlightthickness=2, highlightbackground="white")
        self.button=Button(self.frame,text='Giriş',bg='#1f1c2c',fg='white',font=('Courier',20,'bold'),command=self.validate)
        self.quit=Button(self.frame,text='Çıkış',bg='#1f1c2c',fg='white',font=('Courier',20,'bold'),command=self.main.destroy)

        self.account.place(x=45,y=100,width=220,height=20)
        self.accountEntry.place(x=325,y=97,width=200,height=25)
        self.pin.place(x=45,y=180,width=220,height=20)
        self.pinEntry.place(x=325,y=180,width=200,height=25)
        self.button.place(x=240,y=260,width=100,height=30)
        self.quit.place(x=400,y=420,width=100,height=30)
        self.frame.pack()

    def fetch(self):
        self.list=[]
        self.details=self.conn.execute('Select name, password, acc_no, type, balance from atm where acc_no = ?',(self.ac,))
        for i in self.details:
            self.list.append('Name = {}'.format(i[0]))
            self.list.append('Account no = {}'.format(i[2]))
            self.list.append('Type = {}'.format(i[3]))
            self.ac = i[2]
            self.list.append('Balance = Rs.{}'.format(i[4]))
    
    def validate(self):
        ac=False
        self.details=self.conn.execute('Select name, password, acc_no, type, balance from atm where acc_no = ?',(self.accountEntry.get(),))
        for i in self.details:
            self.ac = i[2]
            if i[2] == self.accountEntry.get():
                ac = True
            elif i[1] == self.pinEntry.get():
                ac = True
                m = "{}! ...BANK'A Hoşgeldiniz ".format(i[0])
                self.fetch()
                messagebox._show("Giriş Bilgilendirmesi", m)
                self.frame.destroy()
                self.menu()
            else:
                ac = True
                m = " Şifreniz Hatalı Lütfen Şifrenizi Kontrol Ediniz!"
                messagebox._show("Giriş Bilgilendirmesi", m)
            if not ac:
                m = " Hesap Numaranız Hatalı !"
                messagebox._show("Giriş Bilgilendirmesi", m)

    def menu(self):
        self.frame=Frame(self.main,bg='#2193b0',width=650 ,height=600)
        main.geometry("800x600")
        self.user_info=Button(self.frame,text='Hesap Bilgisi',bg='#1f1c2c',fg='white',font=('Courier',10,'bold'),command=self.account_details)
        self.balance_enquiry=Button(self.frame,text='Bakiye Sorgulama',bg='#1f1c2c',fg='white',font=('Courier',10,'bold'),command=self.check)
        self.deposit=Button(self.frame,text='Para Yatırma',bg='#1f1c2c',fg='white',font=('Courier',10,'bold'),command=self.deposit)
        self.withdraw=Button(self.frame,text='Para Çekme',bg='#1f1c2c',fg='white',font=('Courier',10,'bold'),command=self.withdraw)
        
        self.last=Button(self.frame,text='Son İşlem',bg='#1f1c2c',fg='white',font=('Courier',8,'bold'),command=self.history)
        self.changePin=Button(self.frame,text='Pin Değiştir',bg='#1f1c2c',fg='white',font=('Courier',8,'bold'),command=self.change)

        self.quit=Button(self.frame,text='Çıkış', bg='#1f1c2c', fg='white', font=('Courier', 10, 'bold'),command=self.main.destroy)

        self.user_info.place(x=0,y=0,width=200,height=50)
        self.balance_enquiry.place(x=0,y=450,width=200,height=50)
        self.deposit.place(x=450,y=0,width=200,height=50)
        self.withdraw.place(x=450,y=450,width=200,height=50)
        self.last.place(x=0,y=240,width=130,height=50)
        self.changePin.place(x=530, y=240, width=130, height=50)
        self.quit.place(x=270,y=470,width=100,height=30)
        self.frame.pack()

    def account_details(self):
        self.entires()
        self.remove_change_pin()
        self.fetch()
        display=self.list[0]+'\n'+self.list[1]+'\n'+self.list[2]
        self.label=Label(self.frame,text=display,font=('Courier',20,'bold'))
        self.label.place(x=180, y=180, width=300, height=100)

    def chek(self):
        self.entires()
        self.remove_change_pin()
        self.fetch()
        b=self.list[3]
        self.label = Label(self.frame, text=b, font=('Courier',20,'bold'))
        self.label.place(x=180, y=180, width=300, height=100)

    def deposit(self):
        self.remove_change_pin()
        self.label = Label(self.frame, text='Yatırmak İstediğiniz Miktarı Girin', font=('Courier', 10, 'bold'))
        self.label.place(x=180, y=180, width=300, height=100)
        self.amountEntry = Entry(self.frame,bg='#FFFFFF',highlightcolor="#50A8B0", highlightthickness=2, highlightbackground="white")
        self.submitButton = Button(self.frame,text='Submit',bg='#1f1c2c',fg='white',font=('Courier',10,'bold'))

        self.amountEntry.place(x=195,y=300,width=160,height=20)
        self.submitButton.place(x=365,y=300,width=100,height=20)
        self.submitButton.bind("<ButtonRelease-1>",self.deposit_trans)

    def deposit_trans(self):
        if(self.amountEntry.get()==''):
            d = 'Tutar Giriniz.'
            messagebox.showerror('Hatalı İşlem',d)
        else:
            self.label = Label(self.frame,text='Para Yatırma İşleminiz Başarı ile Gerçekleşmiştir!',font=('Courier',10,'bold'))
            self.label.place(x=180, y=180, width=300, height=100)
            self.conn.execute('Update atm set balance = balance+? where acc_no=?',(self.amountEntry.get(),self.ac))
            self.conn.commit()
            self.write_deposit()
            self.entries()
    
    def write_deposit(self):
        self.last_deposit='{} TL {} hesabına yatırılıyor.'.format(self.amountEntry.get(), self.list[2])
        f=open("last.txt","w")
        f.write(self.last_deposit)
        f.close

    def withdraw(self):
        self.remove_change_pin()
        self.label=Label(self.frame,text='Çekmek istediğiniz miktarı giriniz.', font=('Courier', 10, 'bold'))
        self.label.place(x=180, y=180, width=300, height=100)
        self.amountEntry=Entry(self.frame,self.frame, bg='#FFFFFF', highlightcolor="#50A8B0", highlightthickness=2,highlightbackground="white")
        self.amountEntry.place(x=195, y=300, width=160, height=20)
        self.submitButton=Button(self.frame, text='Onayla', bg='#1f1c2c', fg='white', font=('Courier', 10, 'bold'))
        self.submitButton.place(x=365, y=300, width=100, height=20)
        self.submitButton.bind("<ButtonRelease-1>", self.with_trans)

    def with_trans(self):
        if(self.amountEntry.get()==''):
            d="Lütfen Çekmek istediğiniz miktarı yazınız."
            messagebox.showwarning("Hatalı İşlem",d)
        else:
            self.label=Label(self.frame,text='İşlem Başarılı', font=('Courier', 10, 'bold'))
            self.label.place(x=180, y=180, width=300, height=100)
            self.conn.execute('Update atm set balance = balance-? where acc_no=?', (self.amountEntry.get(), self.ac))
            self.conn.commit()
            self.last_with()
            self.entiries()

    def last_with(self):
        self.last_withdraw='{} TL {} hesabından çekilmiştir.'.format(self.amountEntry.get(), self.list[2])
        f=open("last.txt","w")
        f.write(self.last_withdraw)
        f.close()

    def change(self):
        self.entries()
        self.label=Label(self.frame,text='Şifre Değiştirme',font=('Courier', 10, 'bold'))
        self.old=Entry(self.frame,bg='#FFFFFF', highlightcolor="#50A8B0", highlightthickness=2, highlightbackground="white")
        self.new=Entry(self.frame,bg='#FFFFFF', highlightcolor="#50A8B0", highlightthickness=2, highlightbackground="white")
        self.confrim=Entry(self.frame,bg='#FFFFFF', highlightcolor="#50A8B0", highlightthickness=2, highlightbackground="white")
        self.submit2=Button(self.frame,text='Değiştir', bg='#1f1c2c', fg='white', font=('Courier', 10, 'bold'))

        self.old.insert(0,'Eski Şifre')
        self.old.bind('<Focus In>',self.on_entry_click)
        self.new.insert(0,'Yeni Şifre')
        self.new.bind('<Focus In>',self.on_entry_click2)
        self.confrim.insert(0,'Yeni Şifreyi Tekrarla')
        self.confrim.bind('<Focus In>',self.on_entry_click3)
        self.submit2.bind('<Button-1>',self.change_req)

        self.label.place(x=180, y=180, width=300, height=100)
        self.old.place(x=230, y=300, width=180, height=20)
        self.new.place(x=230, y=330, width=180, height=20)
        self.confirm.place(x=230, y=360, width=180, height=20)
        self.submit2.place(x=230, y=390, width=180, height=20)

    def change_req(self,flag):
        if(self.old.get()==''or self.new.get()==''or self.confrim.get()==''):
            messagebox.showwarning('Hatalı Giriş',"Lütfen Bilgileri Gözden Geçirin")
        else:
            self.fetch()
            self.details=self.conn.execute('Select name, password, acc_no, type, balance from atm where acc_no = ?',(self.ac,))
            for i in self.details:
                p=i[1]
            if(self.old.get()==p):
                if(self.new.get()==self.confrim.get()):
                    self.label=Label(self.frame,text='Şifre Değiştirildi',font=('Courier', 10, 'bold'))
                    self.label.place(x=180, y=180, width=300, height=100)
                    self.conn.execute('Update atm set password = ? where acc_no=?', (self.new.get(), self.ac))
                    self.conn.commit()
                    self.remove_change_pin()
                    messagebox.showinfo("Yeniden Başlat","Lütfen Tekrar Giriş Yapınız.")
                    main.destroy()

    def on_entry_click(self,event):
        self.entry=True
        if self.entry:
            self.entry=False
            self.old.delete(0,'end')
            self.old.insert(0,'')

    def on_entry_click2(self,event):
        self.entry = True
        if self.entry:
            self.entry = False
            self.new.delete(0,'end')
            self.new.insert(0,'')

    def on_entry_click3(self,event):
        self.entry = True
        if self.entry:
            self.entry = False
            self.confirm.delete(0,'end')
            self.confirm.insert(0,'')

    def history(self):
        self.entries()
        self.remove_change_pin()
        f=open('last.txt','r')
        self.hist=f.readlines()
        f.close()
        self.label=Label(self.frame,text=self.hist, font=('Courier', 7, 'bold'))
        self.label.place(x=180, y=180, width=300, height=100)

    def entries(self):
        try:
            self.amountEntry.place_forget()
            self.submitButton.place_forget()
        except:
            pass
    
    def remove_change_pin(self):
        try:
            self.old.place_forget()
            self.new.place_forget()
            self.confirm.place_forget()
            self.submit2.place_forget()
        except:
            pass
    
main = Tk()
main.title('...Bank')
window_height = 500
window_width = 900

screen_width = main.winfo_screenwidth()
screen_height = main.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

main.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
main.resizable(width=False, height=False)
icon = PhotoImage(file='bank.png')
main.tk.call('wm','iconphoto',main._w,icon)
interface = Atm(main)
main.mainloop()



        



