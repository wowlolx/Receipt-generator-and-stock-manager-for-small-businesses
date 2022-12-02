import os
try:
    from tkinter import *
    from tkinter import ttk
    from PIL import Image , ImageTk
    from win32api import GetSystemMetrics
    from tkinter import messagebox
    from datetime import datetime
    import random,os
    from tkinter.simpledialog import askstring
    import tempfile
    import win32api
    import win32print
    import json
    from base64 import b64encode
except:
    try:
        os.system("pip install tk")
        os.system("pip install Pillow")
        os.system("pip install pywin32") 
    except:
        print("Unknwon Error while importing and installing")

class Bill_App:
    def __init__(self,root):
        self.root = root
        width_scr = GetSystemMetrics(0)
        height_scr = GetSystemMetrics(1)
        self.root.geometry(f"{width_scr}x{height_scr}+0+0")  #windows width and height

        self.root.title("Sereena Billing Software")    

        #===========Variabels==================
        self.Path_To_Json = "database/data.json"
        self.Path_To_Customer_data = "database/customers.json"
        self.Path_To_Loan_data = "database/loan.json"
        self.Path_to_save_custommer_data = "saved bills/"
        self.Path_to_save_loan_data = "saved loans/"

        self.hold_cart_dict = {}
        self.hold_cart_list = []
        self.iterate = "1"
        self.c_name=StringVar() #done
        self.is_loan=StringVar()   #no need to done
        self.c_phone=StringVar()  #done
        self.bill_no=StringVar()
        self.is_billed = StringVar()

        self.bill_no.set("")     #no need to done

        self.c_address=StringVar()  #changed #done
        
        self.search_bill=StringVar()  #done
        
        self.company=StringVar()
        self.product=StringVar() #done
        self.prices=IntVar()  # done
        self.qty=IntVar()    #done
        self.sub_total=StringVar()
        self.Discount=IntVar() #changed
        self.total=StringVar()
        #self.loan = IntVar()
        self.l_list = []
        ###Variables End###
       
        #Product Categories list
        self.Category=["Select Option","Seeds","Fertilizers","Sprays and Pesticides","Miscellaneous"]
        
        ### TOP IMAGES START ###

        #Image1
        width_top_img = round(width_scr//2.731) #For me 500 as  width is 1366
        height_top_img = round(height_scr//5.89) #For me 130 as height is 768
        
        img=Image.open("image/newmypic2.jpg")
        img=img.resize((width_top_img,height_top_img),Image.Resampling.LANCZOS)  #image width and height
        self.photoimg=ImageTk.PhotoImage(img)

        lbl_img=Label(self.root,image=self.photoimg)
        lbl_img.place(x=0,y=0,width=width_top_img,height=height_top_img)   #same as above must

        #Image2
        img2=Image.open("image/mypic2.jpg")
        img2=img2.resize((width_top_img,height_top_img),Image.Resampling.LANCZOS)  #image width and height
        self.photoimg2=ImageTk.PhotoImage(img2)

        lbl_img2=Label(self.root,image=self.photoimg2)
        lbl_img2.place(x=width_top_img,y=0,width=width_top_img,height=height_top_img) 


        #Image3
        img3=Image.open("image/mypic3.jpg")
        img3=img3.resize((width_top_img,height_top_img),Image.Resampling.LANCZOS)  #image width and height
        self.photoimg3=ImageTk.PhotoImage(img3)

        lbl_img3=Label(self.root,image=self.photoimg3)
        lbl_img3.place(x=width_top_img*2,y=0,width=width_top_img,height=height_top_img) 
        ### TOP IMAGES DONE ###
      
        ### Main Frame/TITLE START ###
        height_main_title = round(height_scr//17.05) #For me 45  
             
        #Make a Label or image of name of shop
        lbl_title=Label(self.root,text="New Sereena Zarai Corporation",font=("Prestige Elite Std",40,"bold italic"),bg="white",fg="#135c1d")#466D1D
        #add text , font(style,area,type), background area , foreground area
        lbl_title.place(x=0,y=height_top_img,width=width_scr,height=height_main_title)  

        #Main frame
        start_height_main_frame = height_top_img + height_main_title  #175 for me
        height_main_frame = round((height_scr - start_height_main_frame)*0.894)  # 530 for me #89.4 % of remaining screen<10% for border>
        
        Main_Frame=Frame(self.root,bd=5,relief=GROOVE,bg="white")  #border and size and style
        Main_Frame.place(x=0,y=start_height_main_frame,width=width_scr,height=height_main_frame)    #may have to set all place() functions with current resolution
        
        ### Mainframe/TITLE END ###       
        ### Custome Frame Start ###
        #Customer Label 
        width_customer_frame = round(width_scr // 3.9) # 350
        height_customer_frame = round(height_main_frame // 3.78) #140 for me
        Cust_Frame=LabelFrame(Main_Frame,text="Customer Details",font=("Prestige Elite Std",12,"bold italic"),bg="white",fg="#466D1D")
        Cust_Frame.place(x=10,y=5,width=width_customer_frame,height=height_customer_frame) #
        
        #Customer details in Frame(mobile)
        self.lbl_mob=Label(Cust_Frame,text="Mobile No.",font=("Prestige Elite Std",12,"bold"),bg="white")
        self.lbl_mob.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        #Customer details(Customer name)
        self.lblCustName=Label(Cust_Frame,text="Customer Name",font=("Prestige Elite Std",12,"bold"),bg="white",bd=4)
        self.lblCustName.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        #Customer details(Address)
        self.lblAddress=Label(Cust_Frame,text="Address",font=("Prestige Elite Std",12,"bold"),bg="white",bd=4)
        self.lblAddress.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        #Entry for mobile number
        self.entry_mob=ttk.Entry(Cust_Frame,textvariable=self.c_phone,font=("Prestige Elite Std",12,"bold"),width=20)
        self.entry_mob.grid(row=0,column=1)
 
        #Entry for Customer name
        self.txtCustName=ttk.Combobox(Cust_Frame,textvariable=self.c_name,font=("Prestige Elite Std",12,"bold"),width=20)
        self.txtCustName.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        self.txtCustName.bind("<KeyRelease>",self.cust_name_search)
        self.txtCustName.bind("<<ComboboxSelected>>",self.cust_name_selected)

        #Entry for Address
        self.txtAddress=ttk.Entry(Cust_Frame,textvariable=self.c_address,font=("Prestige Elite Std",12),width=20)
        self.txtAddress.grid(row=2,column=1,sticky=W,padx=5,pady=2)  
        
        ###Customer Frame Ended ###      
        ###Produce Frame Started###   
        #Product Label Frame
        width_product_frame = width_top_img -20 #480 or 500 for me
        Product_Frame=LabelFrame(Main_Frame,text="Product",font=("Prestige Elite Std",12,"bold italic"),bg="white",fg="#466D1D")
        Product_Frame.place(x=width_customer_frame + 15,y=5,width=width_product_frame,height=height_customer_frame)

        #Category Label
        self.lblCategory=Label(Product_Frame,text="Select Categories",font=("Prestige Elite Std",12,"bold"),bg="white",bd=4)
        self.lblCategory.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        #Category combobox
        self.Combo_Category=ttk.Combobox(Product_Frame,font=("Prestige Elite Std",10,"bold"),value=self.Category,width=20,state="readonly")
        self.Combo_Category.current(0)
        self.Combo_Category.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        self.Combo_Category.bind("<<ComboboxSelected>>",self.categories1)
        
        #Company Label
        self.lblCompany=Label(Product_Frame,text="Company Name",font=("Prestige Elite Std",12,"bold"),bg="white",bd=4)
        self.lblCompany.grid(row=1,column=0,sticky=W,padx=5,pady=2)
        self.ComboCompany=ttk.Combobox(Product_Frame,value=[''],textvariable=self.company,font=("Prestige Elite Std",10,"bold"),width=20,state="readonly") #commenting for now
        self.ComboCompany.set("Select Company")
        self.ComboCompany.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        self.ComboCompany.bind("<<ComboboxSelected>>",self.companies1)

        #Product Label
        self.lblProduct=Label(Product_Frame,text="Product Name",font=("Prestige Elite Std",12,"bold"),bg="white",bd=4)
        self.lblProduct.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        #Product combobox
        self.ComboProduct=ttk.Combobox(Product_Frame,value=[''],textvariable=self.product,font=("Prestige Elite Std",10,"bold"),width=20 ,state="readonly") #commenting for now
        self.ComboProduct.set("Select Product")
        self.ComboProduct.grid(row=2,column=1,sticky=W,padx=5,pady=2)
        self.ComboProduct.bind("<<ComboboxSelected>>",self.products1)
        

        #Price Label
        self.lblPrice=Label(Product_Frame,text="Price",font=("Prestige Elite Std",12,"bold"),bg="white",bd=4)
        self.lblPrice.grid(row=3,column=0,sticky=W,padx=5,pady=2)

        #Price Combobox
        self.ComboPrice=ttk.Combobox(Product_Frame,textvariable=self.prices,font=("Prestige Elite Std",10,"bold"),width=20 ) #,state="readonly") #for now only
        self.ComboPrice.grid(row=3,column=1,sticky=W,padx=5,pady=2)

        #Quantity Label
        self.lblQty=Label(Product_Frame,text="Quantity",font=("Prestige Elite Std",12,"bold"),bg="white",bd=4)
        self.lblQty.grid(row=0,column=2,sticky=W,padx=5,pady=2)

        #Entry for Quantity
        self.ComboQty=ttk.Entry(Product_Frame,textvariable=self.qty,font=("Prestige Elite Std",12,"bold"),width=10)
        self.ComboQty.grid(row=1,column=2,sticky=W,padx=5,pady=1)
        
        ###Product Frame Ended###       

        ###Bill Area Started###
        #Right Frame for Bill area
        height_bill_frame = round((height_main_frame * 75.5) // 100)#400 for me
        start_width_bill_frame = width_customer_frame + 15 + width_product_frame + 20 # 865 for me
        width_bill_frame = width_scr - start_width_bill_frame - 25
        RightLabelFrame=LabelFrame(Main_Frame,text="Invoice",font=("Prestige Elite Std",12,"bold italic"),bg="white",fg="#466D1D")
        RightLabelFrame.place(x=start_width_bill_frame,y=2,width=width_bill_frame,height=height_bill_frame)

        #Scroll bar
        scrolll_y=Scrollbar(RightLabelFrame,orient=VERTICAL)
        self.textarea=Text(RightLabelFrame,yscrollcommand=scrolll_y.set,bg="white",fg="black",font=("Prestige Elite Std",12,"bold"))   #black for text of receipt and white of background
        scrolll_y.pack(side=RIGHT,fill=Y)
        scrolll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        ###Bill Area End###
        ###Bill Total Start###
        #Bill Counter LabelFrame
        height_bottom_frame = height_main_frame - height_bill_frame -18 # 112
        Bottom_Frame=LabelFrame(Main_Frame,text="Bill Counter",font=("Prestige Elite Std",12,"bold italic"),bg="white",fg="#466D1D")
        Bottom_Frame.place(x=5,y=height_bill_frame + 5,width=width_scr -20 ,height=height_bottom_frame)#y=405 for me


        #Label and entry fields for Bill counter LabelFrame(subtotal)
        self.lblSubTotal=Label(Bottom_Frame,text="Sub Total",font=("Prestige Elite Std",11,"bold"),bg="white",bd=4)
        self.lblSubTotal.grid(row=0,column=0,sticky=W,padx=5,pady=1)

        self.EntrySubTotal=ttk.Entry(Bottom_Frame,textvariable=self.sub_total,font=("Prestige Elite Std",11,"bold"),width=20,state="readonly")
        self.EntrySubTotal.grid(row=0,column=1,sticky=W,padx=5,pady=1)


        #Label and entry fields for Bill counter LabelFrame(Margin)
        self.lbl_Margin=Label(Bottom_Frame,text="Discount",font=("Prestige Elite Std",11,"bold"),bg="white",bd=4)
        self.lbl_Margin.grid(row=1,column=0,sticky=W,padx=5,pady=1)

        self.txt_Margin=ttk.Entry(Bottom_Frame,font=("Prestige Elite Std",11,"bold"),width=20,textvariable=self.Discount)
        self.txt_Margin.grid(row=1,column=1,sticky=W,padx=5,pady=1)
        self.txt_Margin.bind("<KeyRelease>",self.discount_keypress)

         #Label and entry fields for Bill counter LabelFrame(Total Amount)
        self.lblAmountTotal=Label(Bottom_Frame,text="Total",font=("Prestige Elite Std",11,"bold"),bg="white",bd=4)
        self.lblAmountTotal.grid(row=2,column=0,sticky=W,padx=5,pady=1)

        self.txtAmountTotal=ttk.Entry(Bottom_Frame,textvariable=self.total,font=("Prestige Elite Std",11,"bold"),width=20,state="readonly")
        self.txtAmountTotal.grid(row=2,column=1,sticky=W,padx=5,pady=0)
        ###Bill Total End###
        ###Button Frame Start###
        #Buttom Frame#1340
        start_width_button_frame = round(((width_scr -26)*23)//100) #308
        Btn_Frame=Frame(Bottom_Frame,bd=2,bg="white")
        Btn_Frame.place(x=start_width_button_frame,y=5)

        #Making Buttons
        self.BtnAddToCart=Button(Btn_Frame,command=self.AddItem,height=2,text="Add to Cart",font=("Prestige Elite Std",15,"bold"),bg="#4a5d23",fg="white",width=13,cursor="hand2")
        self.BtnAddToCart.grid(row=0,column=0)

        self.Btngenerate_bill=Button(Btn_Frame,command=self.gen_bill,height=2,text="Generate Bill",font=("Prestige Elite Std",15,"bold"),bg="#4a5d23",fg="white",width=13,cursor="hand2")
        self.Btngenerate_bill.grid(row=0,column=1)

        self.BtnSave=Button(Btn_Frame,height=2,command=self.save_bill,text="Save Bill",font=("Prestige Elite Std",15,"bold"),bg="#4a5d23",fg="white",width=13,cursor="hand2")
        self.BtnSave.grid(row=0,column=2)

        self.BtnPrint=Button(Btn_Frame,command=self.iprint,height=2,text="Print",font=("Prestige Elite Std",15,"bold"),bg="#4a5d23",fg="white",width=13,cursor="hand2")
        self.BtnPrint.grid(row=0,column=3)

        self.BtnClear=Button(Btn_Frame,command=self.clear,height=2,text="Clear",font=("Prestige Elite Std",15,"bold"),bg="#4a5d23",fg="white",width=13,cursor="hand2")
        self.BtnClear.grid(row=0,column=4)

        self.BtnExit=Button(Btn_Frame,height=2,command=self.root.destroy,text="Exit",font=("Prestige Elite Std",15,"bold"),bg="#4a5d23",fg="white",width=13,cursor="hand2")
        self.BtnExit.grid(row=0,column=5)
##########################################################
        self.BtnManage = Button(Btn_Frame,height=2,command=self.manage,text="Manage",font=("Prestige Elite Std",15,"bold"),bg="#4a5d23",fg="white",width=13,cursor="hand2")
        self.BtnManage.grid(row=0,column=6)
##########################################################        
        ###Bill Frame End###
     
        ###Central Accessories Start###
        #Search Area
        start_height_search_frame = height_customer_frame + 10 #174
        Search_Frame=Frame(Main_Frame,bd=2,bg="white")
        Search_Frame.place(x=4,y=start_height_search_frame,width=width_top_img + 20,height=40) #190 height

        self.lblBill=Label(Search_Frame,text="Bill Number",font=("Prestige Elite Std",12,"bold"),bg="green",fg="white")
        self.lblBill.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.txt_Entry_Search=ttk.Combobox(Search_Frame,textvariable=self.search_bill,font=("Prestige Elite Std",12,"bold"),width=24)
        self.txt_Entry_Search.grid(row=0,column=1,sticky=W,padx=5,pady=1)
        self.txt_Entry_Search.bind("<KeyRelease>",self.bill_search_by_name)

        self.BtnSearch=Button(Search_Frame,command=self.find_bill,text="Search",font=("Prestige Elite Std",10,"bold"),bg="#4a5d23",fg="white",width=13,cursor="hand2")
        self.BtnSearch.grid(row=0,column=2)
        ###Central Accessories END###
        #Middle Frame Start###
        #Middle Frame
        start_height_middle_frame = height_customer_frame + 50 + 5
        width_middle_frame = width_customer_frame + width_product_frame + 20 
        height_middle_frame = round((height_main_frame * 41.5)//100)
        MiddleFrame=Frame(Main_Frame,bd=10,bg="white")
        MiddleFrame.place(x=4,y=start_height_middle_frame,width=width_middle_frame,height=height_middle_frame)

        #Image1
        img12=Image.open("image/mypic.jpg")
        img12=img12.resize((width_middle_frame//2,height_middle_frame - 15),Image.Resampling.LANCZOS)  #image width and height
        self.photoimg12=ImageTk.PhotoImage(img12)

        lbl_img12=Label(MiddleFrame,image=self.photoimg12)
        lbl_img12.place(x=0,y=0,width=width_middle_frame//2,height=height_middle_frame -15)   #same as above must

        #Image2
        img13=Image.open("image/newpic13.jpg")
        img13=img13.resize((width_middle_frame//2,height_middle_frame -15),Image.Resampling.LANCZOS)  #image width and height
        self.photoimg13=ImageTk.PhotoImage(img13)

        lbl_img13=Label(MiddleFrame,image=self.photoimg13)
        lbl_img13.place(x=width_middle_frame//2,y=0,width=width_middle_frame//2,height=height_middle_frame -15) 
        self.welcome()
        self.backup_jsondata()

    ###FUNCTIONNS============###
    def welcome(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,"\t\tNew Sereena Corporation")
        self.textarea.insert(END,"\n\tDogar Market near HBL bank Aminpur Banglaw")
        self.textarea.insert(END,"\n\t\t\t03447861061")
        self.textarea.insert(END,f"\n Bill Number:      {self.bill_no.get()}")
        self.textarea.insert(END,f"\n Customer Name:    {self.c_name.get().lower()}")
        self.textarea.insert(END,f"\n Phone Number:     {self.c_phone.get()}")
        self.textarea.insert(END,f"\n Customer Address: {self.c_address.get()}")

        self.textarea.insert(END,"\n=======================================================")
        self.textarea.insert(END,f"\n Description\t\tPrice\t\tQuantity\t\tAmount")
        self.textarea.insert(END,"\n=======================================================")
        ###Welcome Function End###
       
    def AddItem(self):
        if self.is_billed.get() == "true":
            messagebox.showerror("ERROR","Clear Previous Bill to generate new one")
            return
        try:
            self.n_price = int(self.ComboPrice.get())
        except ValueError:
            messagebox.showerror("Error","Price must be a number ranging from zero to onwards")
            self.ComboPrice.config(value= 0)
            self.ComboPrice.current(0)
            return
        try:
            self.calc = int(self.ComboQty.get()) * self.n_price
        except ValueError:
            messagebox.showerror("Error","Quantity must be a number ranging from zero to onwards")
            self.qty.set(0)
            return
        self.l_list.append(self.calc)
        if self.product.get() =="Select Product" or self.product.get() == "" or self.product.get()=="Select Options" or self.product.get()=="Add another":
            messagebox.showerror("Error","Please Select the Product Name")
        else:
            #minnuus stock based onn product and quantity here
            self.check_stock_on_add_to_cart()
            if self.check_stock_add_cart == 0:
                return
            self.textarea.insert(END,f"\n {self.product.get()}")
            self.textarea.insert(END,f"\n \t\t{self.n_price}\t\t{int(self.ComboQty.get())}\t\t{self.calc}")
            self.textarea.insert(END,"\n-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --")
            self.sub_total.set(str('Rs.%.2f'%(sum(self.l_list))))
            try:
                self.Discount_value = int(self.txt_Margin.get())
            except ValueError:
                messagebox.showerror("Error","Discount must be a number ranging from zero to onwards")
                self.Discount.set(0)
                return
            self.ComboProduct.set("Add another")
            self.ComboPrice.config(value= 0)
            self.ComboPrice.current(0)
            self.qty.set(0)
            if self.Discount_value > sum(self.l_list):
                messagebox.showerror("Error","Discount cannot be greater than Total price")
            else:
                self.total.set(str('Rs.%.2f'%((sum(self.l_list))- self.Discount_value)))
            self.iterate = str(int(self.iterate) + 2)
            self.hold_cart_dict[self.iterate] = self.hold_cart_list

    ###Add to cart###
    #Generate Bill#
    def gen_bill(self):
               
        if self.product.get() =="Select Product" or self.product.get() == "":
            messagebox.showerror("Error","Please Add To Cart the product")
        elif self.is_billed.get() == "true":
            messagebox.showerror("ERROR","Clear Previous Bill to generate new one")
        else:
            lol=messagebox.askyesno("Payment Type","Is Payment-Method = Cash?")
            #
            #text=self.textarea.get(11.0,(10.0+ float(len(self.l_list))))
            try:
                self.discounted = int(self.txt_Margin.get())
            except ValueError:
                messagebox.showerror("Error","Discount must be a number ranging from zero to onwards")
                self.Discount.set(0)
                return
            if self.discounted > sum(self.l_list):
                messagebox.showerror("Error","Discount cannot be greater than Total price")
                return
            self.fill_customers_fields_if_not_exists()
            if self.check_customers_name_notempty == 0:
                messagebox.showerror("Error","Please fill the name field to add entry about the customer")
                return
            #setting bill no
            self.setting_bill_no()
            self.sub_total.set(str('Rs.%.2f'%(sum(self.l_list))))
            self.total.set(str('Rs.%.2f'%((sum(self.l_list))- self.discounted)))
            text=self.textarea.get(11.0,END)
            self.welcome()
            self.textarea.insert(END,f"\n{text}")
            self.textarea.insert(END,"\n=======================================================")
            self.textarea.insert(END,f"\n Sub-Total: \t\t\t\t\t{self.sub_total.get()}")
            self.textarea.insert(END,f"\n Discount: \t\t\t\t\t{int(self.txt_Margin.get())}")
            self.textarea.insert(END,f"\n Total: \t\t\t\t\t{self.total.get()}")
            if lol>0:
                self.textarea.insert(END,f"\n Payment Method: \t\t\t\t\tCash")
                self.is_loan.set("false")
            else:
                self.textarea.insert(END,"\n Payment Method: \t\t\t\t\tLoan")
                self.is_loan.set("true")
            self.textarea.insert(END,"\n=======================================================")
            self.textarea.insert(END,"\n=======================================================")
            self.textarea.insert(END,"\n\nDeveloped by Qitga--03347483125")
            self.textarea.insert(END,"\nwww.qitga.us")
            self.is_billed.set("true")
            self.txtCustName.config(state="readonly")
            

    #Save Bill
    def save_bill(self):
        if self.bill_no.get() == "":
            messagebox.showerror("Error","You cannot save bill without generating it")
        else:    
            op = messagebox.askyesno("Save Bill","Do you want to seperately save this bill")
            if op > 0:
                self.bill_data = self.textarea.get(1.0,END)
                try:
                    f1=open("Seperate_bills/" + str(self.bill_no.get())+".txt","w",encoding="utf-8")
                except FileNotFoundError:
                    named_file = askstring("Folder","Folder not found, Please enter full pth of folder where to save the file: ")
                    f1=open(named_file +  str(self.bill_no.get())+".txt","w",encoding="utf-8")
                f1.write(self.bill_data)
                messagebox.showinfo(f"Success",f"Bill Saved Successfully with Bill numeber: {self.bill_no.get()}")
                f1.close()


    #Print bill#
    def iprint(self):
        self.print_changing_customers_data()
        self.save_to_loan_and_data()
        self.update_stock_on_print()
        self.making_loan_customers_data()
        self.adding_to_loan_database()
        q = self.textarea.get(1.0,"end-1c")
        filename=tempfile.mktemp(".txt")
        open(filename,'w',encoding="utf-8").write(q)
        win32api.ShellExecute (
        0,
        "print",
        filename,
  #
  # If this is None, the default printer will
  # be used anyway.
  #
        '/d:"%s"' % win32print.GetDefaultPrinter (),
        ".",
        0
        )
        self.hold_cart_dict = {}
        messagebox.showinfo("Print","Status Done")
        self.clear()
    ###Welcome Function Start###
        
    
    #Search Bill#
    def find_bill(self):
        found = "No"
        for i in os.listdir("saved bills/"):
            if i.split(".txt")[0] == self.search_bill.get():
                f1=open(f"saved bills/{i}","r",encoding="utf-8")
                self.textarea.delete(1.0,END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                found="Yes"
        if found == "No":
            messagebox.showerror("ERROR","Invalid Bill No.")
        else:
            self.is_billed.set("true")

    def bill_search_by_name(self,event=""):
        here_list = []
        prod_name = event.widget.get()
        if prod_name != "":
            for i in os.listdir("saved bills/"):
                wow = i.split(".txt")[0]
                if prod_name in wow:
                    here_list.append(wow)
            for i in os.listdir("saved loans/"):
                lol = i.split(".txt")[0]
                if prod_name in lol:
                    if lol not in here_list:
                        here_list.append(lol)
            event.widget.config(value=here_list)
        elif prod_name == "":
            event.widget.config(value="")

    #Clear Function#
    def clear(self):
        self.textarea.delete(1.0,END)
        self.c_name.set("")
        self.c_phone.set("")
        self.c_address.set("")
        self.bill_no.set("")
        self.search_bill.set("")
        self.ComboProduct.config(value="")
        self.ComboCompany.config(value="")
        self.Combo_Category.current(0)
        self.product.set("Select Product")
        self.company.set("Select Company")
        self.is_billed.set("")
        self.prices.set(0)
        self.qty.set(0)
        self.l_list=[0]
        self.total.set("")
        self.sub_total.set("")
        self.Discount.set(0)
        self.is_loan.set("")
        self.discounted = 0
        self.txtCustName.config(state="normal")
        self.entry_mob.config(state="normal")
        self.txtAddress.config(state="normal")
        self.check_stock_add_cart = 0
        self.hold_cart_dict = {}
        self.hold_cart_list = []
        self.iterate = "1"
        self.welcome()

#Manage
    def manage(self):
        self.root.destroy()
        import manage


    #Backup Function
    def backup_jsondata(self):
        wow = datetime.now()
        wow_string = wow.strftime("%d.%m.%Y")
        with open(self.Path_To_Json,"r",encoding="utf-8") as f:
            data = json.load(f)
        try:
            with open("backup/" + wow_string +"_stock"+ ".txt","x",encoding="utf-8") as wow:
                json.dump(data,wow,indent=4)
        except FileExistsError:
            pass

        with open(self.Path_To_Customer_data,"r",encoding="utf-8") as f:
            lol = json.load(f)
        try:
            with open("backup/" + wow_string + "_customer"+".txt","x",encoding="utf-8") as wow:
                json.dump(lol,wow,indent=4)
        except FileExistsError:
            pass

        with open(self.Path_To_Loan_data,"r",encoding="utf-8") as f:
            lmao = json.load(f)
        try:
            with open("backup/" + wow_string +"_loan"+ ".txt","x",encoding="utf-8") as wow:
                json.dump(lmao,wow,indent=4)
        except FileExistsError:
            pass

    #new functions
    #Selecting categories
    def categories1(self,event=""):
        here_list = []
        prod_name = event.widget.get()
        if prod_name != "Select Option" or prod_name != "":
            with open(self.Path_To_Json,"r",encoding="utf-8") as f:
                data = json.load(f)
            for k,v in data[prod_name].items():
                here_list.append(k)
            here_list.sort()
            self.ComboCompany.config(value=here_list)
            self.ComboCompany.set("Select Company")        
            self.ComboProduct.set("Select Product")
            self.ComboPrice.set(0)
            self.qty.set(0)
    #Selecting companies
    def companies1(self,event=""):
        here_list = []
        cat = self.Combo_Category.get()
        prod_name = event.widget.get()
        if cat != "Select Option" or cat != "":
            if prod_name != "" or prod_name != "Select Company":
                with open(self.Path_To_Json,"r",encoding="utf-8") as f:
                    data = json.load(f)
                try:
                    for k,v in data[cat][prod_name].items():
                            here_list.append(k)
                except KeyError:
                    return
                here_list.sort()
                self.ComboProduct.config(value=here_list)
                self.ComboProduct.set("Select Product")
                self.ComboPrice.set(0)
                self.qty.set(0)
    #Selecting products
    def products1(self,event=""):
        price= 0 
        stock = 0
        cat = self.Combo_Category.get()
        com = self.ComboCompany.get()
        prod_name = event.widget.get()
        if cat != "Select Option" or cat != "":
            if com != "" or com != "Select Company":
                if prod_name != "" or prod_name != "Select Product" or prod_name != "Add another":
                    with open(self.Path_To_Json,"r",encoding="utf-8") as f:
                        data = json.load(f)
                    try:
                        data[cat][com][prod_name]
                    except KeyError:
                        return
                    price =  data[cat][com][prod_name]["price"]
                    stock = data[cat][com][prod_name]["stock"]
                    self.ComboPrice.set(price)
                    self.qty.set(1)
    #function keypress dicount
    def discount_keypress(self,event=""):
        discount = 0
        if self.sub_total.get() != "":
            try:
                discount = int(self.txt_Margin.get())
            except ValueError:
                self.Discount.set(0)
                
            if discount >= sum(self.l_list):
                self.total.set('Rs.0.00')
            else:
                self.total.set(str('Rs.%.2f'%((sum(self.l_list))- discount)))
    #Customer database functions

    def check_customer_existence(self):
        self.check_customers_name_notexist = 0
        self.check_customers_name_notempty = 0
        prod_name = self.c_name.get()
        if prod_name != "":
            prod_name = prod_name.lower()
            self.check_customers_name_notempty = 1
            with open(self.Path_To_Customer_data,"r",encoding="utf-8") as f:
                data = json.load(f)
            try:
                data["customers"][prod_name]
            except KeyError:
                self.check_customers_name_notexist = 1 #Customer not found
    def make_customers_fields_if_not_exists(self):
        self.check_customer_existence()
        if self.check_customers_name_notempty > 0:
            if self.check_customers_name_notexist > 0:
                prod_name = self.c_name.get()
                prod_name = prod_name.lower()
                with open(self.Path_To_Customer_data,"r",encoding="utf-8") as f:
                    data = json.load(f)
                data["customers"][prod_name] = {}
                data["customers"][prod_name]["phone"] = ""
                data["customers"][prod_name]["address"] = ""
                data["customers"][prod_name]["customer_id"] = "" #convert to str
                data["customers"][prod_name]["total sales"] = 0
                data["customers"][prod_name]["purchase"] = {}
                os.remove(self.Path_To_Customer_data)
                with open(self.Path_To_Customer_data,"w",encoding="utf-8") as f:
                    json.dump(data,f,indent=4)

    def fill_customers_fields_if_not_exists(self):
        self.make_customers_fields_if_not_exists()
        if self.check_customers_name_notempty > 0:
            if self.check_customers_name_notexist > 0:
                prod_name = self.c_name.get()
                prod_name = prod_name.lower()
                phone = self.c_phone.get()
                address = self.c_address.get()
                with open(self.Path_To_Customer_data,"r",encoding="utf-8") as f:
                    data = json.load(f)
                with open("database\current_id.txt","r",encoding="utf-8") as h:
                    lol = h.read()
                lol = str(int(lol) + 1)
                data["customers"][prod_name]["phone"] = phone
                data["customers"][prod_name]["address"] = address
                data["customers"][prod_name]["customer_id"] = lol
                os.remove("database\current_id.txt")
                with open("database\current_id.txt" , "w" , encoding="utf-8") as q:
                    q.write(str(int(lol) + 1))
                os.remove(self.Path_To_Customer_data)
                with open(self.Path_To_Customer_data,"w",encoding="utf-8") as f:
                    json.dump(data,f,indent=4)
    
    def setting_bill_no(self):
        cust_id = ""
        prod_name = self.c_name.get()
        prod_name = prod_name.lower()
        with open(self.Path_To_Customer_data,"r",encoding="utf-8") as f:
            data = json.load(f)
        cust_id = data["customers"][prod_name]["customer_id"]
        date_lol = datetime.now()
        date_str = date_lol.strftime("%d.%m.%Y-%H.%M.%S")
        bill_no_b64 = cust_id + "==" + ((b64encode(date_str.encode("ascii"))).decode())
        self.bill_no.set(bill_no_b64)  #Random bill with cust id is infront
    
    def print_changing_customers_data(self):
        bill_no = self.bill_no.get() 
        prod_name =self.c_name.get()
        prod_name = prod_name.lower()
        loan = self.is_loan.get()
        date_lol = datetime.now()
        total_value  = sum(self.l_list)- self.discounted
        date_str = date_lol.strftime("%d.%m.%Y-%H.%M.%S")
        with open(self.Path_To_Customer_data,"r",encoding="utf-8") as f:
            data = json.load(f)
        data["customers"][prod_name]["purchase"][bill_no] = {}
        data["customers"][prod_name]["purchase"][bill_no]["subtotal"] = sum(self.l_list)
        data["customers"][prod_name]["purchase"][bill_no]["discount"] = self.discounted
        data["customers"][prod_name]["purchase"][bill_no]["total"] = self.total.get()
        if loan.lower() == "false": 
            data["customers"][prod_name]["purchase"][bill_no]["payment"] = "Cash"
        elif loan.lower() == "true":
            data["customers"][prod_name]["purchase"][bill_no]["payment"] = "Loan"
        data["customers"][prod_name]["purchase"][bill_no]["timestamp"] = date_str
        data["customers"][prod_name]["total sales"] += total_value
        os.remove(self.Path_To_Customer_data)
        with open(self.Path_To_Customer_data,"w",encoding="utf-8") as f:
            json.dump(data,f,indent=4)

    def cust_name_search(self,event=""):
        here_list = []
        matched = ""
        prod_name = event.widget.get()
        prod_name = prod_name.lower()
        if prod_name != "":
            with open(self.Path_To_Customer_data,"r",encoding="utf-8") as f:
                data = json.load(f)
            for k,v in data["customers"].items():
                if prod_name in k.lower():
                    here_list.append(k)
                if prod_name == k.lower():
                    matched = k
            here_list.sort()
            event.widget.config(value=here_list)
            if matched == "":
                self.entry_mob.config(state="normal")
                self.txtAddress.config(state="normal")

    def cust_name_selected(self,event=""):
        here_list  = []
        matched = ""
        prod_name = event.widget.get()
        prod_name = prod_name.lower()
        if prod_name != "":
            with open(self.Path_To_Customer_data,"r",encoding="utf-8") as f:
                data = json.load(f)
            for k,v in data["customers"].items():
                if prod_name == k.lower():
                    here_list.append(k)
                    matched = k
            if matched != "":
                phone = data["customers"][prod_name]["phone"] 
                address = data["customers"][prod_name]["address"]
                self.c_address.set(address)
                self.c_phone.set(phone)
                self.entry_mob.config(state="readonly")
                self.txtAddress.config(state="readonly")

    def save_to_loan_and_data(self):
        bill_no = self.bill_no.get()
        bill_data_all = self.textarea.get(1.0,END)
        loan = self.is_loan.get()
        with open(self.Path_to_save_custommer_data + bill_no + ".txt","w",encoding="utf-8") as f:
            f.write(bill_data_all)
        if loan.lower() == "false":
            return
        elif loan.lower() == "true":
            with open(self.Path_to_save_loan_data + bill_no + ".txt","w",encoding="utf-8") as f:
                f.write(bill_data_all)

    def check_stock_on_add_to_cart(self):
        self.check_stock_add_cart = 0
        self.hold_cart_list = []
        prod_name = self.product.get()
        quan = int(self.ComboQty.get())
        cat = self.Combo_Category.get()  
        com = self.ComboCompany.get()
        with open(self.Path_To_Json,"r",encoding="utf-8") as f:
            data = json.load(f)
        lol = data[cat][com][prod_name]["stock"]
        if quan > int(lol):
            self.check_stock_add_cart = 0
            messagebox.showerror("Error","Selected quantity of product is greater than amount in stock. Kindly update your stock to continue the process")
        elif quan <= int(lol):
            self.check_stock_add_cart = 1
            self.hold_cart_list.append(cat)
            self.hold_cart_list.append(com)
            self.hold_cart_list.append(prod_name)
            self.hold_cart_list.append(quan)
            
    
    def update_stock_on_print(self):
        lol = []
        with open(self.Path_To_Json,"r",encoding="utf-8") as f:
            data = json.load(f)
        for k ,v in self.hold_cart_dict.items():
            lol = v
            lol_cat = lol[0]
            lol_com = lol[1]
            lol_prod = lol[2]
            lol_qty = lol[3]
            data[lol_cat][lol_com][lol_prod]["stock"] -= lol_qty
            if data[lol_cat][lol_com][lol_prod]["stock"] < 0:
                messagebox.showerror("Error","Same item was placed multiple times in cart, stock of products goes less than zero\n, so it is held to zero to prevent from dangerous effect.\n kindly update it")
                data[lol_cat][lol_com][lol_prod]["stock"] = 0
        os.remove(self.Path_To_Json)
        with open(self.Path_To_Json,"w",encoding="utf-8") as f:
            json.dump(data,f,indent=4)

    def making_loan_customers_data(self):
        loan = self.is_loan.get()
        prod_name = self.c_name.get()
        prod_name = prod_name.lower()
        if loan.lower() == "true":
            #Check Customer name and create database
            with open(self.Path_To_Loan_data,"r",encoding="utf-8") as f:
                data = json.load(f)
            try:
                data["loan"][prod_name]
            except KeyError:
                with open(self.Path_To_Customer_data,"r",encoding="utf-8") as f:
                    lol = json.load(f)
                phone = lol["customers"][prod_name]["phone"]
                address = lol["customers"][prod_name]["address"]
                cust_id = lol["customers"][prod_name]["customer_id"]
                data["loan"][prod_name] = {}
                data["loan"][prod_name]["phone"] = phone
                data["loan"][prod_name]["address"] = address
                data["loan"][prod_name]["customer_id"] = cust_id
                data["loan"][prod_name]["Total Loan"] = 0
                data["loan"][prod_name]["purchase"] = {}
                os.remove(self.Path_To_Loan_data)
                with open(self.Path_To_Loan_data,"w",encoding="utf-8") as f:
                    json.dump(data,f,indent=4)
    
    def adding_to_loan_database(self):
        bill_no = self.bill_no.get() 
        prod_name =self.c_name.get()
        prod_name = prod_name.lower()
        loan = self.is_loan.get()
        date_lol = datetime.now()
        total_value  = sum(self.l_list)- self.discounted
        date_str = date_lol.strftime("%d.%m.%Y-%H.%M.%S")
        if loan.lower() == "true":
            with open(self.Path_To_Loan_data,"r",encoding="utf-8") as f:
                data = json.load(f)
            data["loan"][prod_name]["purchase"][bill_no] = {}
            data["loan"][prod_name]["purchase"][bill_no]["subtotal"] = sum(self.l_list)
            data["loan"][prod_name]["purchase"][bill_no]["discount"] = self.discounted
            data["loan"][prod_name]["purchase"][bill_no]["total"] = self.total.get()
            data["loan"][prod_name]["purchase"][bill_no]["payment"] = "Loan"
            data["loan"][prod_name]["purchase"][bill_no]["timestamp"] = date_str
            data["loan"][prod_name]["Total Loan"] += total_value
            os.remove(self.Path_To_Loan_data)
            with open(self.Path_To_Loan_data,"w",encoding="utf-8") as f:
                json.dump(data,f,indent=4)



#if __name__ =='__main__':
root=Tk()
obj=Bill_App(root)
root.mainloop()