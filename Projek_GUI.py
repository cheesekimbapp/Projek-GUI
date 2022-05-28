import re
from tkinter import *
from tkinter.font import BOLD
import tkinter.messagebox
import random
from turtle import bgcolor
import Projek_backend
from tkinter import ttk

class info_siswa():
    def __init__(self, master):
        self.master = master
        self.master.title('Sistem Informasi dan Managemen Sekolah')
        self.master.geometry('1350x750')
        self.master.config(bgcolor = 'lightgreen')

        def informasi():
        
        #=======================================   Variabel   ===============================
            self.nama      = StringVar()
            self.nama_ayah = StringVar()
            self.nama_ibu  = StringVar()
            self.alamat    = StringVar()
            self.hp        = StringVar()
            self.email     = StringVar()
            self.lahir     = StringVar()
            self.gender    = StringVar()

        #=======================================   Fungsi   ================================
            def siswarec(event):
                try:
                    global selected_tuple

                    index = self.listbox.curselection()[0]
                    selected_tuple = self.listbox.get(index)

                    self.Entry_nama.delete(0,END)
                    self.Entry_nama.insert(END, selected_tuple[1])
                    self.Entry_nama_ayah.delete(0,END)
                    self.Entry_nama_ayah.insert(END, selected_tuple[2])
                    self.Entry_nama_ibu.delete(0,END)
                    self.Entry_nama_ibu.insert(END, selected_tuple[3])
                    self.Entry_alamat.delete(0,END)
                    self.Entry_alamat.insert(END, selected_tuple[4])
                    self.Entry_hp.delete(0,END)
                    self.Entry_hp.insert(END, selected_tuple[5])
                    self.Entry_email.delete(0,END)
                    self.Entry_email.insert(END, selected_tuple[6])
                    self.Entry_lahir.delete(0,END)
                    self.Entry_lahir.insert(END, selected_tuple[7])
                    self.Entry_gender.delete(0,END)
                    self.Entry_gender.insert(END, selected_tuple[8])
                except IndexError:
                    pass
            

            def add():
                if(len(self.nama.get()) != 0):
                    Projek_backend.insert(self.nama.get(), self.nama_ayah.get(), self.nama_ibu.get(), self.alamat.get(), self.hp.get(), self.email.get(), self.lahir.get(), self.gender.get())
                    self.listbox.delete(0, END)
                    self.listbox.insert(END, (self.nama.get(), self.nama_ayah.get(), self.nama_ibu.get(), self.alamat.get(), self.hp.get(), self.email.get(), self.lahir.get(), self.gender.get()))

            def display():
                    self.listbox.delete(0, END)
                    for row in Projek_backend.view():
                        self.listbox.insert(END, row, str(' '))

            def exit():
                exit = tkinter.messagebox.askyesno("Login System", "Confirm if you want to Exit")
                if exit > 0:
                    self.master.destroy()
                    return

            def reset():
                self.nama.set('')
                self.nama_ayah.set('')
                self.nama_ibu.set('')
                self.alamat.set('')
                self.hp.set('')
                self.email.set('')
                self.lahir.set('')
                self.gender.set('')
                self.listbox.delete(0,END)

            def delete():
                if(len(self.nama.get()) != 0):
                    Projek_backend.delete(selected_tuple[0])
                    reset()
                    display()
                
            def search():
                self.listbox.delete(0, END)
                for row in Projek_backend.serach(self.nama.get(), self.nama_ayah.get(), self.nama_ibu.get(), self.alamat.get(), self.hp.get(), self.email.get(), self.lahir.get(), self.gender.get()):
                    self.listbox.insert(END, row, str(' '))

            def update():
                if(len(self.nama.get()) != 0):
                    Projek_backend.delete(selected_tuple[0])
                if(len(self.nama.get()) != 0):
                    Projek_backend.insert(self.nama.get(), self.nama_ayah.get(), self.nama_ibu.get(), self.alamat.get(), self.hp.get(), self.email.get(), self.lahir.get(), self.gender.get())

                    self.listbox.delete(0, END)
                    self.listbox.insert(END, (self.nama.get(), self.nama_ayah.get(), self.nama_ibu.get(), self.alamat.get(), self.hp.get(), self.email.get(), self.lahir.get(), self.gender.get()))

        
        #===========================================   Frame   ============================================

            self.Main_Frame = LabelFrame(self.master, width= 1300, height= 500, font= ('arial',20, 'bold'), bg='lightgreen', bd=15, relief= 'ridge')
            self.Main_Frame.grid(row= 0, column= 0, padx= 10, pady= 20)
            self.Frame1 = LabelFrame(self.Main_Frame, width= 600, height= 400, font=('arial',15,'bold'), relief= 'ridge', bd= 10, bg= 'lightgreen', text= 'INFORMASI SISWA')
            self.Frame1.grid(row= 1, column= 0, padx= 10)
            self.Frame2 = LabelFrame(self.Main_Frame, width= 750, height= 400, font=('arial',15,'bold'), relief= 'ridge', bd= 10, bg= 'lightgreen', text= 'DATABASE SISWA')
            self.Frame2.grid(row= 1, column= 1, padx= 5)
            self.Frame3 = LabelFrame(self.master, width= 1200, height= 100, font= ('arial', 10, 'bold'), bg= 'lightgreen', relief= 'ridge', bd= 13)
            self.Frame3.grid(row= 2, column= 0, pady= 10)

        #======================================   Label Frame1   =========================================

            self.Label_nama = Label(self.Frame1, text= 'Nama', font=('arial', 20, 'bold'), bg= 'lightgreen')
            self.Label_nama.grid(row= 0, column= 0, sticky= W, padx= 20, pady= 10)
            self.Label_nama_ayah = Label(self.Frame1, text= 'Nama Ayah', font=('arial', 20, 'bold'), bg= 'lightgreen')
            self.Label_nama_ayah.grid(row= 1, column= 0, sticky= W, padx= 20)
            self.Label_nama_ibu = Label(self.Frame1, text= 'Nama Ibu', font=('arial', 20, 'bold'), bg= 'lightgreen')
            self.Label_nama_ibu.grid(row= 2, column= 0, sticky= W, padx= 20)
            self.Label_alamat = Label(self.Frame1, text= 'Alamat', font=('arial', 20, 'bold'), bg= 'lightgreen')
            self.Label_alamat.grid(row= 3, column= 0, sticky= W, padx= 20)
            self.Label_hp = Label(self.Frame1, text= 'Nomor Hp', font=('arial', 20, 'bold'), bg= 'lightgreen')
            self.Label_hp.grid(row= 4, column= 0, sticky= W, padx= 20)
            self.Label_email = Label(self.Frame1, text= 'Email', font=('arial', 20, 'bold'), bg= 'lightgreen')
            self.Label_email.grid(row= 5, column= 0, sticky= W, padx= 20)
            self.Label_lahir = Label(self.Frame1, text= 'Tanggal Lahir', font=('arial', 20, 'bold'), bg= 'lightgreen')
            self.Label_lahir.grid(row= 6, column= 0, sticky= W, padx= 20)
            self.Label_gender = Label(self.Frame1, text= 'Gender', font=('arial', 20, 'bold'), bg= 'lightgreen')
            self.Label_gender.grid(row= 7, column= 0, sticky= W, padx= 20)
