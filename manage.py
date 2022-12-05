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
except:
    try:
        os.system("pip install tk")
        os.system("pip install Pillow")
        os.system("pip install pywin32") 
    except:
        print("Unknwon Error while importing and installing")




class Manage_App:
    def __init__(self,root):
        self.root = root
        width_scr = GetSystemMetrics(0)
        height_scr = GetSystemMetrics(1)
        self.root.geometry(f"{width_scr}x{height_scr}+0+0")  #windows width and height
        self.root.title("Sereena Billing Software") 
        ### TOP IMAGES START ###
        
        
        #Variables
        self.Path_To_Json = "D:\\files\\important files\\database\\data.json"
        self.Path_To_Customer_data = "D:\\files\\important files\\database\\customers.json"
        self.Path_To_Loan_data = "D:\\files\\important files\\database\\loan.json"
        self.search_loan_name = StringVar()
        self.minus_loan = IntVar()

        self.add_company = StringVar()
        self.remove_company = StringVar()
        self.rename_company_first = StringVar()
        self.rename_company_second = StringVar()
        
        self.Category_prod=["Select Option","Seeds","Fertilizers","Sprays and Pesticides","Miscellaneous"]
        self.company_prod = StringVar()
        self.add_prod = StringVar()
        self.remove_prod = StringVar()
        self.check_stock_prod = StringVar()
        
        self.Category_stock=["Select Option","Seeds","Fertilizers","Sprays and Pesticides","Miscellaneous"]
        self.company_stock = StringVar()
        self.product_stock = StringVar()
        self.add_prod_stock = IntVar()
        self.remove_prod_stock = IntVar()
        self.set_prod_stock = IntVar()
        self.set_price_stock = IntVar()
    
        self.show_all_products_cat_misc = ["Select Option","Seeds","Fertilizers","Sprays and Pesticides","Miscellaneous"]
        self.show_all_products_com_misc = StringVar()


        #Image1
        width_top_img = round(width_scr//2.731) #For me 500 as  width is 1366
        height_top_img = round(height_scr//5.89) #For me 130 as height is 768

        img=Image.open("D:\\files\\important files\\image\\newmypic2.jpg")
        img=img.resize((width_top_img,height_top_img),Image.Resampling.LANCZOS)  #image width and height
        self.photoimg=ImageTk.PhotoImage(img)

        lbl_img=Label(self.root,image=self.photoimg)
        lbl_img.place(x=0,y=0,width=width_top_img,height=height_top_img)   #same as above must

        #Image2
        img2=Image.open("D:\\files\\important files\\image\\mypic2.jpg")
        img2=img2.resize((width_top_img,height_top_img),Image.Resampling.LANCZOS)  #image width and height
        self.photoimg2=ImageTk.PhotoImage(img2)
        lbl_img2=Label(self.root,image=self.photoimg2)
        lbl_img2.place(x=width_top_img,y=0,width=width_top_img,height=height_top_img) 
        #Image3
        img3=Image.open("D:\\files\\important files\\image\\mypic3.jpg")
        img3=img3.resize((width_top_img,height_top_img),Image.Resampling.LANCZOS)  #image width and height
        self.photoimg3=ImageTk.PhotoImage(img3)
        lbl_img3=Label(self.root,image=self.photoimg3)
        lbl_img3.place(x=width_top_img*2,y=0,width=width_top_img,height=height_top_img) 
            ### TOP IMAGES DONE ###


        ### Main Frame/TITLE START ###
        height_main_title = round(height_scr//17.05) #For me 45  
             
        #Make a Label or image of name of shop
        lbl_title=Label(self.root,text="New Sereena Zarai Corporation Management",font=("Prestige Elite Std",40,"bold italic"),bg="white",fg="#135c1d")#466D1D
        #add text , font(style,area,type), background area , foreground area
        lbl_title.place(x=0,y=height_top_img,width=width_scr,height=height_main_title)
        
        

        #Main frame
        start_height_main_frame = height_top_img + height_main_title  #175 for me
        height_main_frame = round((height_scr - start_height_main_frame)*0.894)  # 530 for me #89.4 % of remaining screen<10% for border>
        
        Main_Frame=Frame(self.root,bd=5,relief=GROOVE,bg="white")  #border and size and style
        Main_Frame.place(x=0,y=start_height_main_frame,width=width_scr,height=height_main_frame)    #may have to set all place() functions with current resolution
        
        ### Mainframe/TITLE END ###
       

       ### Company Frame Start ###
        #Company Name 
        width_customer_frame = round(width_scr // 3.9) # 350
        height_customer_frame = round(height_main_frame // 3.78) #140 for me
        Company_Frame=LabelFrame(Main_Frame,text="Company Details",font=("Prestige Elite Std",12,"bold italic"),bg="white",fg="#466D1D")
        Company_Frame.place(x=10,y=5,width=width_customer_frame,height=height_customer_frame *1.2+ 20) #
        
        #Customer details in Frame(mobile)
        self.btn_add_company=Button(Company_Frame,command=self.add_to_company,text="Add Company",font=("Prestige Elite Std",10,"bold"),bg="#4a5d23",fg="white",height=1,width=15,cursor="hand2",bd=4)
        self.btn_add_company.grid(row=0,column=0,sticky=W,padx=5,pady=2)
    

        #Customer details(Customer name)
        self.btn_remove_company=Button(Company_Frame,text="Remove Company",command=self.remove_to_company,font=("Prestige Elite Std",10,"bold"),bg="#4a5d23",fg="white",height=1,width=15,cursor="hand2",bd=4)
        self.btn_remove_company.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        #Customer details(Address)
        self.btn_change_company=Button(Company_Frame,command=self.rename_to_company,text="Change Company\n name",font=("Prestige Elite Std",10,"bold"),bg="#4a5d23",fg="white",height=2,width=15,cursor="hand2",bd=4)
        self.btn_change_company.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        #Entry for mobile number
        self.entry_add_company=ttk.Combobox(Company_Frame,textvariable=self.add_company,font=("Prestige Elite Std",10,"bold"),width=20)
        self.entry_add_company.grid(row=0,column=1)
        self.entry_add_company.bind("<KeyPress>",self.company_key_press)
 
        #Entry for Customer name
        self.entry_remove_company=ttk.Combobox(Company_Frame,textvariable=self.remove_company,font=("Prestige Elite Std",10,"bold"),width=20)
        self.entry_remove_company.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        self.entry_remove_company.bind("<KeyPress>",self.company_key_press)
            
        #Entry for Address
        self.entry_change_company=ttk.Combobox(Company_Frame,textvariable=self.rename_company_first,font=("Prestige Elite Std",10,"bold"),width=20)
        self.entry_change_company.grid(row=2,column=1,sticky=W,padx=5,pady=2)
        self.entry_change_company.bind("<KeyPress>",self.company_key_press)

        self.lbl_changeto_company=Label(Company_Frame,text="\tTo",font=("Prestige Elite Std",12,"bold"),bg="white",bd=4)
        self.lbl_changeto_company.grid(row=3,column=1,sticky=W,padx=5,pady=1)

        self.entry_changeto_company=ttk.Combobox(Company_Frame,textvariable=self.rename_company_second,font=("Prestige Elite Std",10,"bold"),width=20)
        self.entry_changeto_company.grid(row=4,column=1,sticky=W,padx=5,pady=1)  
        
        ###Customer Frame Ended ###



        ###Produce Frame Started###   
        #Product Label Frame
        width_product_frame = width_customer_frame #480 or 500 for me
        Product_Frame=LabelFrame(Main_Frame,text="Product Details",font=("Prestige Elite Std",12,"bold italic"),bg="white",fg="#466D1D")
        Product_Frame.place(x=10 ,y=height_customer_frame*1.3+10,width=width_product_frame,height=height_customer_frame*1.5)
        #Select Category
        self.lbl_category_prod = Label(Product_Frame,text="Select Category",font=("Prestige Elite Std",12,"bold"),bg="white")
        self.lbl_category_prod.grid(row=0,column=0,sticky=W,padx=5,pady=2)
        self.entry_category_prod = ttk.Combobox(Product_Frame,value=self.Category_prod,font=("Prestige Elite Std",10,"bold"),width=20,state="readonly")
        self.entry_category_prod.current(0)
        self.entry_category_prod.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        
        #Select Companny
        self.lbl_company_prod = Label(Product_Frame,text="Select Company",font=("Prestige Elite Std",12,"bold"),bg="white")
        self.lbl_company_prod.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.entry_company_prod = ttk.Combobox(Product_Frame,textvariable=self.company_prod,font=("Prestige Elite Std",10,"bold"),width=20)
        self.entry_company_prod.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        self.entry_company_prod.bind("<KeyPress>",self.company_key_press)
        #Add Product Name
        self.btn_add_prod = Button(Product_Frame,command=self.add_to_prod,text="Add Product",font=("Prestige Elite Std",10,"bold"),bg="#4a5d23",fg="white",height=1,width=15,cursor="hand2",bd=4)
        self.btn_add_prod.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.entry_add_prod = ttk.Combobox(Product_Frame,textvariable=self.add_prod,font=("Prestige Elite Std",10,"bold"),width=20)
        self.entry_add_prod.grid(row=2,column=1,sticky=W,padx=5,pady=2)
        self.entry_add_prod.bind("<KeyPress>",self.product_key_press)
        #Remove Product Name
        self.btn_remove_prod = Button(Product_Frame,command=self.remove_to_product,text="Remove Product",font=("Prestige Elite Std",10,"bold"),bg="#4a5d23",fg="white",height=1,width=15,cursor="hand2",bd=4)
        self.btn_remove_prod.grid(row=3,column=0,sticky=W,padx=5,pady=2)

        self.entry_remove_prod = ttk.Combobox(Product_Frame,textvariable=self.remove_prod,font=("Prestige Elite Std",10,"bold"),width=20)
        self.entry_remove_prod.grid(row=3,column=1,sticky=W,padx=5,pady=2)
        self.entry_remove_prod.bind("<KeyPress>",self.product_key_press)
        #Check Stock of a Product
        self.btn_stock_prod = Button(Product_Frame,command=self.check_stock_to_prod,text="Check Stock/price\n of a Product",font=("Prestige Elite Std",10,"bold"),bg="#4a5d23",fg="white",height=2,width=15,cursor="hand2",bd=4)
        self.btn_stock_prod.grid(row=4,column=0,sticky=W,padx=5,pady=2)

        self.entry_stock_prod = ttk.Combobox(Product_Frame,textvariable=self.check_stock_prod,font=("Prestige Elite Std",10,"bold"),width=20)
        self.entry_stock_prod.grid(row=4,column=1,sticky=W,padx=5,pady=2)
        self.entry_stock_prod.bind("<KeyPress>",self.product_key_press)
        



        #Stock Frame
        height_product_frame = height_customer_frame *2
        width_product_frame = width_top_img -20 #480 or 500 for me
        Stock_Frame=LabelFrame(Main_Frame,text="Stock Management",font=("Prestige Elite Std",12,"bold italic"),bg="white",fg="#466D1D")
        Stock_Frame.place(x=width_customer_frame + 15,y=5,width=width_product_frame,height=height_product_frame)

        #Select Category
        self.lbl_category_stock = Label(Stock_Frame,text="Select Category",font=("Prestige Elite Std",12,"bold"),bg="white")
        self.lbl_category_stock.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.entry_category_stock = ttk.Combobox(Stock_Frame,value=self.Category_stock,font=("Prestige Elite Std",10,"bold"),width=30,state="readonly")
        self.entry_category_stock.current(0)
        self.entry_category_stock.grid(row=0,column=1,sticky=W,padx=5,pady=2)

        #Select Company
        self.lbl_company_stock = Label(Stock_Frame,text="Select Company",font=("Prestige Elite Std",12,"bold"),bg="white")
        self.lbl_company_stock.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.entry_company_stock = ttk.Combobox(Stock_Frame,textvariable=self.company_stock,font=("Prestige Elite Std",10,"bold"),width=30)
        self.entry_company_stock.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        self.entry_company_stock.bind("<KeyPress>",self.company_key_press)

        #Select Product
        self.lbl_product_stock = Label(Stock_Frame,text="Select Product",font=("Prestige Elite Std",12,"bold"),bg="white")
        self.lbl_product_stock.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.entry_product_stock = ttk.Combobox(Stock_Frame,textvariable=self.product_stock,font=("Prestige Elite Std",10,"bold"),width=30)
        self.entry_product_stock.grid(row=2,column=1,sticky=W,padx=5,pady=2)
        self.entry_product_stock.bind("<KeyPress>",self.product_key_press)

        #Add to Product Stock
        
        self.btn_add_stock = Button(Stock_Frame,command=self.add_products_to_stock,text="No. of Products\n to add",font=("Prestige Elite Std",10,"bold"),bg="#4a5d23",fg="white",height=2,width=15,cursor="hand2",bd=4)
        self.btn_add_stock.grid(row=3,column=0,sticky=W,padx=5,pady=2)

        self.entry_add_stock = ttk.Entry(Stock_Frame,textvariable=self.add_prod_stock,font=("Prestige Elite Std",10,"bold"),width=30)
        self.entry_add_stock.grid(row=3,column=1,sticky=W,padx=5,pady=2)

        #Remove From Product Stock
        self.btn_remove_stock = Button(Stock_Frame,command=self.remove_products_to_stock,text="No. of Products\n to remove",font=("Prestige Elite Std",10,"bold"),bg="#4a5d23",fg="white",height=2,width=15,cursor="hand2",bd=4)
        self.btn_remove_stock.grid(row=4,column=0,sticky=W,padx=5,pady=2)

        self.entry_remove_stock = ttk.Entry(Stock_Frame,textvariable=self.remove_prod_stock,font=("Prestige Elite Std",10,"bold"),width=30)
        self.entry_remove_stock.grid(row=4,column=1,sticky=W,padx=5,pady=2)

        #Change Product Stock to
        self.btn_change_stock = Button(Stock_Frame,command=self.set_prod_to_stock,text="Set Stock of\n  Product",font=("Prestige Elite Std",10,"bold"),bg="#4a5d23",fg="white",height=2,width=15,cursor="hand2",bd=4)
        self.btn_change_stock.grid(row=5,column=0,sticky=W,padx=5,pady=2)

        self.entry_change_stock = ttk.Entry(Stock_Frame,textvariable=self.set_prod_stock,font=("Prestige Elite Std",10,"bold"),width=30)
        self.entry_change_stock.grid(row=5,column=1,sticky=W,padx=5,pady=2)
        #Change Price
        self.btn_price_stock = Button(Stock_Frame,command=self.new_price_to_stock,text="New price of\n Product",font=("Prestige Elite Std",10,"bold"),bg="#4a5d23",fg="white",height=2,width=15,cursor="hand2",bd=4)
        self.btn_price_stock.grid(row=6,column=0,sticky=W,padx=5,pady=2)

        self.entry_price_stock = ttk.Entry(Stock_Frame,textvariable=self.set_price_stock,font=("Prestige Elite Std",10,"bold"),width=30)
        self.entry_price_stock.grid(row=6,column=1,sticky=W,padx=5,pady=2)
        


        #Loan Frame
        Loan_Frame=LabelFrame(Main_Frame,text="Loan And Others",font=("Prestige Elite Std",12,"bold italic"),bg="white",fg="#466D1D")
        Loan_Frame.place(x=width_customer_frame + 15,y= height_product_frame + 10,width=width_product_frame,height=height_customer_frame -40 -5)

        #Search People
        self.lbl_search_loan = Button(Loan_Frame,command=self.search_loan_btn_function,text="Search People's\n loan data",font=("Prestige Elite Std",8,"bold"),bg="#4a5d23",fg="white",height=2,width=15,cursor="hand2",bd=4)
        self.lbl_search_loan.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.entry_search_loan = ttk.Combobox(Loan_Frame,textvariable=self.search_loan_name,font=("Prestige Elite Std",10,"bold"),width=20)
        self.entry_search_loan.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        self.entry_search_loan.bind("<KeyRelease>",self.search_loan_and_others)

        #Loan Manipulation
        self.lbl_search_loan = Button(Loan_Frame,command=self.minus_btn_on_search,text="Minus Amount\n From Loan",font=("Prestige Elite Std",8,"bold"),bg="#4a5d23",fg="white",height=2,width=15,cursor="hand2",bd=4)
        self.lbl_search_loan.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.entry_search_loan = ttk.Entry(Loan_Frame,textvariable=self.minus_loan,font=("Prestige Elite Std",10,"bold"),width=20)
        self.entry_search_loan.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        self.entry_search_loan.bind("<KeyRelease>",self.minus_loan_on_search)

        #Text Area
        #Right Frame for Bill area
        height_bill_frame = round((height_main_frame * 75.5) // 100)#400 for me
        start_width_bill_frame = width_customer_frame + 15 + width_product_frame + 20 # 865 for me
        width_bill_frame = width_scr - start_width_bill_frame - 25
        RightLabelFrame=LabelFrame(Main_Frame,text="Text Area",font=("Prestige Elite Std",12,"bold italic"),bg="white",fg="#466D1D")
        RightLabelFrame.place(x=start_width_bill_frame,y=2,width=width_bill_frame,height=height_bill_frame)

        #Scroll bar
        scrolll_y=Scrollbar(RightLabelFrame,orient=VERTICAL)
        self.textarea=Text(RightLabelFrame,yscrollcommand=scrolll_y.set,bg="white",fg="black",font=("Prestige Elite Std",12,"bold"))   #black for text of receipt and white of background
        scrolll_y.pack(side=RIGHT,fill=Y)
        scrolll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        ###Bill Area End###




        #Accessories Buttons Frame
        Extras_Frame=LabelFrame(Main_Frame,text="Other Buttons",font=("Prestige Elite Std",12,"bold italic"),bg="white",fg="#466D1D")
        Extras_Frame.place(x=width_product_frame + 20,y= height_bill_frame + 10,width=width_product_frame*1.75,height=height_customer_frame *0.8)
        #Button Bill Generator
        self.Btn_BillGenerator=Button(Extras_Frame,command=self.bill_generate_go,height=2,text="Bill Generator",font=("Prestige Elite Std",15,"bold"),bg="#4a5d23",fg="white",width=20,cursor="hand2")
        self.Btn_BillGenerator.grid(row=0,column=0,sticky=W,padx=15,pady=5)

        #Button Clear
        self.Btn_clear=Button(Extras_Frame,command=self.clear,height=2,text="Clear",font=("Prestige Elite Std",15,"bold"),bg="#4a5d23",fg="white",width=20,cursor="hand2")
        self.Btn_clear.grid(row=0,column=1,sticky=W,padx=15,pady=5)

        #Button Exit
        self.Btn_exit=Button(Extras_Frame,command=self.root.destroy,height=2,text="Exit",font=("Prestige Elite Std",15,"bold"),bg="#4a5d23",fg="white",width=20,cursor="hand2")
        self.Btn_exit.grid(row=0,column=2,sticky=W,padx=15,pady=5)


        #Miscellaneous frame started
        #Miscellaneous Frame
        Miscellaneous_Frame=LabelFrame(Main_Frame,text="Miscellaneous",font=("Prestige Elite Std",12,"bold italic"),bg="white",fg="#466D1D")
        Miscellaneous_Frame.place(x=10 ,y=height_customer_frame*2.9,width=width_product_frame,height=height_customer_frame * 0.77)

        #Show all Companies
        self.btn_show_all_companies = Button(Miscellaneous_Frame,command=self.show_all_to_companies,text="Show all companies",font=("Prestige Elite Std",10,"bold"),bg="#4a5d23",fg="white",height=1,width=17,cursor="hand2",bd=4)
        self.btn_show_all_companies.grid(row=0,column=0,sticky=W,padx=5,pady=2)
        #Show all Products of a category
        self.btn_show_all_products_cat = Button(Miscellaneous_Frame,command=self.show_all_products_to_category,text="Show all Products,\nPrices and Stock\n(of a CSategory) ",font=("Prestige Elite Std",10,"bold"),bg="#4a5d23",fg="white",height=3,width=17,cursor="hand2",bd=4)
        self.btn_show_all_products_cat.grid(row=1,column=0,sticky=W,padx=5,pady=2)
        self.entry_show_all_products_cat = ttk.Combobox(Miscellaneous_Frame,value=self.show_all_products_cat_misc,font=("Prestige Elite Std",10,"bold"),width=20,state="readonly")
        self.entry_show_all_products_cat.current(0)
        self.entry_show_all_products_cat.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        #Show all Products of a company
        self.btn_show_all_products_com = Button(Miscellaneous_Frame,command=self.show_all_products_to_company,text="⮝Show all Products,\nPrices and Stock\n(of a Company) ",font=("Prestige Elite Std",10,"bold"),bg="#4a5d23",fg="white",height=3,width=17,cursor="hand2",bd=4)
        self.btn_show_all_products_com.grid(row=1,column=3,sticky=W,padx=5,pady=2)
        self.entry_show_all_products_com = ttk.Combobox(Miscellaneous_Frame,textvariable=self.show_all_products_com_misc,font=("Prestige Elite Std",10,"bold"),width=20)
        self.entry_show_all_products_com.grid(row=0,column=3,sticky=W,padx=5,pady=2)
        self.entry_show_all_products_com.bind("<KeyPress>",self.company_key_press)




        #Structure Complete
        self.welcome()
        self.backup_jsondata()
    #Functions
    #Companyy Functions
    def welcome(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,"\t\tNew Sereena Management Portal")
        self.textarea.insert(END,"\n\tDogar Market near HBL bank Aminpur Banglaw")
        self.textarea.insert(END,"\n\t\t\t03447861061")
        self.textarea.insert(END,"\n=======================================================")
        
    #Add company
    def add_to_company(self):
            wow = self.add_company.get()
            if wow =="":
                messagebox.showerror("ERROR","Please Enter some Text in the box to add in database")
                self.welcome()
                self.textarea.insert(END,"\n Empty field(s).Warning! Not Done")
                self.textarea.insert(END,"\n Status: \t\t\tFailed")
            elif wow != "":
                data = 0
                try:
                    with open(self.Path_To_Json,'r',encoding="utf-8") as f:
                        data = json.load(f)
                        data["Seeds"][f"{wow}"]
                        data["Fertilizers"][f"{wow}"]
                        data["Sprays and Pesticides"][f"{wow}"]
                        data["Miscellaneous"][f"{wow}"]
                        messagebox.showerror("ERROR","This Company is already in the database")
                    self.welcome()
                    self.textarea.insert(END,f"\n \"{wow}\" cannot be added as it already exists")
                    self.textarea.insert(END,"\n Status: \t\t\tFailed")
                except KeyError:
                    with open(self.Path_To_Json,'r',encoding="utf-8") as f:
                        data = json.load(f)
                        data["Seeds"][f"{wow}"] = {}
                        data["Fertilizers"][f"{wow}"] = {}
                        data["Sprays and Pesticides"][f"{wow}"] = {}
                        data["Miscellaneous"][f"{wow}"] = {}
                    os.remove(self.Path_To_Json)
                    with open(self.Path_To_Json,"w",encoding="utf-8") as f:
                        json.dump(data,f,indent=4)
                    self.welcome()
                    self.textarea.insert(END,f"\n Added \"{wow}\" as a companyy")
                    self.textarea.insert(END,"\n Status: \t\t\tSuccess")
                self.add_company.set("")

    #Remove Company
    def remove_to_company(self):
        wow = self.remove_company.get()
        asker = askstring("Are You sure!!","Removing a company will delete all its data along with its products\n prices and stock\n Type \"yes\" to continue the process")
        try:
            asker.lower()
        except AttributeError:
            messagebox.showerror("Error","Operation not done, Denied by user")
            self.welcome()
            self.textarea.insert(END,"\n Denied")
            self.textarea.insert(END,"\n Status: \t\t\tFailed")
            return
        if  asker.lower() != "yes":
            messagebox.showerror("Error","Company could not be removed because the user\n did not type \"yes\" in the asking field")
            self.welcome()
            self.textarea.insert(END,"\n Company could not be removed\n Try again and type \"yes\" in the prompt box to remove it")
            self.textarea.insert(END,"\n Status: \t\t\tFailed")
            self.remove_company.set("")
            return
        if wow == "":
            messagebox.showerror("Error","Please Enter some Text in box to remove from database")
            self.welcome()
            self.textarea.insert(END,"\n Empty field(s).Warning! Not Done")
            self.textarea.insert(END,"\n Status: \t\t\tFailed")
        if wow != "":
            op=messagebox.askyesno("Sure!!","All products and all data of that company will be erased. Are you sure?")
            if op == 0:
                self.welcome()
                self.textarea.insert(END,"\n Denied")
                self.textarea.insert(END,"\n Status: \t\t\tFailed")
            elif op > 0:
                data = 0 
                try: 
                    with open(self.Path_To_Json,"r",encoding="utf-8") as f:
                        data = json.load(f)
                        del data["Seeds"][f"{wow}"]
                        del data["Fertilizers"][f"{wow}"]
                        del data["Sprays and Pesticides"][f"{wow}"]
                        del data["Miscellaneous"][f"{wow}"]
                    os.remove(self.Path_To_Json)
                    with open(self.Path_To_Json,"w",encoding="utf-8") as f:
                        json.dump(data,f,indent=4)
                    self.welcome()
                    self.textarea.insert(END,f"\n \"{wow}\" removed from company's list")
                    self.textarea.insert(END,"\n Status: \t\t\tSuccess")
                except KeyError:
                    messagebox.showerror("ERROR","The specified item does not exist, Please check your spelling and punctuation and try again")
                    self.welcome()
                    self.textarea.insert(END,f"\n \"{wow}\" cannot be removed because not found")
                    self.textarea.insert(END,"\n Status: \t\t\tFailed")
            self.remove_company.set("")
                
    #Rename Company
    def rename_to_company(self):
        wow = self.rename_company_first.get()
        wow2 = self.rename_company_second.get()
        if wow =="" or wow2 == "":
            messagebox.showerror("Error","Please fill both fields to specify what name of company you want to change")
            self.welcome()
            self.textarea.insert(END,"\n Empty field(s).Warning! Not Done")
            self.textarea.insert(END,"\n Status: \t\t\tFailed")
        elif wow != "" and wow2 != "":
            op=messagebox.askyesno("Sure!!",f"Are you sure you want to replace company name from {wow} to {wow2}")
            if op == 0:
                self.welcome()
                self.textarea.insert(END,"\n Denied")
                self.textarea.insert(END,"\n Status: \t\t\tFailed")
            elif op >0:
                data = 0
                if wow == wow2:
                    messagebox.showerror("Error","Oops you gave same names in both fields")
                    self.welcome()
                    self.textarea.insert(END,"\n Both fields same.Warning! Not Done")
                    self.textarea.insert(END,"\n Status: \t\t\tFailed")
                else:
                    try:
                        with open(self.Path_To_Json,"r",encoding="utf-8") as f:
                            data = json.load(f)
                            data["Seeds"][f"{wow2}"] = data["Seeds"][f"{wow}"] 
                            data["Fertilizers"][f"{wow2}"] = data["Fertilizers"][f"{wow}"]
                            data["Sprays and Pesticides"][f"{wow2}"] =  data["Sprays and Pesticides"][f"{wow}"]
                            data["Miscellaneous"][f"{wow2}"] =  data["Miscellaneous"][f"{wow}"]

                            del data["Seeds"][f"{wow}"]
                            del data["Fertilizers"][f"{wow}"]
                            del data["Sprays and Pesticides"][f"{wow}"]
                            del data["Miscellaneous"][f"{wow}"]
                        os.remove(self.Path_To_Json)
                        with open(self.Path_To_Json,"w",encoding="utf-8") as f:
                            json.dump(data,f,indent=4)
                        self.welcome()
                        self.textarea.insert(END,f"\n \"{wow}\" replaced by \"{wow2}\"")
                        self.textarea.insert(END,"\n Status: \t\t\tSuccess")
                    except KeyError:
                        messagebox.showerror("ERROR","The specified Company doen not exist, Please check your spellings and punctuation and try again")
                        self.welcome()
                        self.textarea.insert(END,f"\n \"{wow}\" cannot be renamed as \"{wow2}\"\n  because the company does not exist in database")
                        self.textarea.insert(END,"\n Status: \t\t\tFailed")
            self.rename_company_first.set("")
            self.rename_company_second.set("")

    #Product functions
    #Product check 
    def verify_prod(self):
        self.is_checked_prod = 1
        self.cat_prod = self.entry_category_prod.get()
        self.com_prod = self.company_prod.get()
        if self.cat_prod == "" or self.cat_prod == "Select Option":
            messagebox.showerror("Error","Please Select a Category")
            self.welcome()
            self.textarea.insert(END,"\n No Category Selected")
            self.textarea.insert(END,"\n Status: \t\t\tFailed")
            self.is_checked_prod = 0
        else:
            if self.com_prod == "":
                messagebox.showerror("Error","Please Select a Company")
                self.welcome()
                self.textarea.insert(END,"\n No Company Selected")
                self.textarea.insert(END,"\n Status: \t\t\tFailed")
                self.is_checked_prod = 0

    #Add Product name
    def add_to_prod(self):
        self.verify_prod()
        if self.is_checked_prod > 0:
            prod_name = self.add_prod.get()
            if prod_name == "":
                messagebox.showerror("Error","Please Select a Product")
                self.welcome()
                self.textarea.insert(END,"\n No Product Selected")
                self.textarea.insert(END,"\n Status: \t\t\tFailed")
            else:
                if self.cat_prod in self.Category_prod:    
                    data = 0                
                    try:
                        with open(self.Path_To_Json,"r",encoding="utf-8") as f:
                            data = json.load(f)
                            data[f"{self.cat_prod}"][f"{self.com_prod}"]
                            try:
                                data[f"{self.cat_prod}"][f"{self.com_prod}"][f"{prod_name}"]
                                messagebox.showerror("ERROR","The specified Product already exist, Please check your spellings and punctuation and try again")
                                self.welcome()
                                self.textarea.insert(END,f"\n \"{prod_name}\" cannot be added because\n  product name already exist")
                                self.textarea.insert(END,"\n Status: \t\t\tFailed")
                                prod_name = ""
                                self.company_prod.set("")
                                self.cat_prod = ""
                                self.com_prod = ""
                                self.add_prod.set("")
                                self.entry_category_prod.current(0)
                                return
                            except KeyError:
                                pass
                            data[f"{self.cat_prod}"][f"{self.com_prod}"][f"{prod_name}"] = {"stock":0,"price":0}
                        os.remove(self.Path_To_Json)
                        with open(self.Path_To_Json,"w",encoding="utf-8") as f:
                            json.dump(data,f,indent=4)
                        self.welcome()
                        self.textarea.insert(END,f"\n Product \"{prod_name}\" created in \"{self.com_prod}\"")
                        self.textarea.insert(END,"\n Status: \t\t\tSuccess")
                    except KeyError:
                        messagebox.showerror("ERROR","The specified Company does not exist, Please check your spellings and punctuation and try again")
                        self.welcome()
                        self.textarea.insert(END,f"\n \"{prod_name}\" cannot be added because\n  company name doesnot exist")
                        self.textarea.insert(END,"\n Status: \t\t\tFailed")
            prod_name = ""
            self.company_prod.set("")
            self.cat_prod = ""
            self.com_prod = ""
            self.add_prod.set("")
            self.entry_category_prod.current(0)

    #Remove Product
    def remove_to_product(self):
        self.verify_prod()
        if self.is_checked_prod > 0:
            prod_name = self.remove_prod.get()
            if prod_name == "":
                messagebox.showerror("Error","Please Select a Product to remove")
                self.welcome()
                self.textarea.insert(END,"\n No Product Selected for removal")
                self.textarea.insert(END,"\n Status: \t\t\tFailed")
            else:
                if self.cat_prod in self.Category_prod:
                    op=messagebox.askyesno("Sure!!",f"Are you sure you want to remove \"{prod_name}\" from products")
                    if op == 0:
                        messagebox.showerror("Error","Operation not done, Denied by user")
                        self.welcome()
                        self.textarea.insert(END,"\n Denied")
                        self.textarea.insert(END,"\n Status: \t\t\tFailed")
                    elif op >0:
                        try:
                            with open(self.Path_To_Json,"r",encoding="utf-8") as f:
                                data = json.load(f)
                                data[f"{self.cat_prod}"][f"{self.com_prod}"]
                                try:
                                    del data[f"{self.cat_prod}"][f"{self.com_prod}"][f"{prod_name}"]
                                except KeyError:
                                    messagebox.showerror("ERROR","The specified Product does not exist, Please check your spellings and punctuation and try again")
                                    self.welcome()
                                    self.textarea.insert(END,f"\n \"{prod_name}\" cannot be removed because\n  product name doesnot exist")
                                    self.textarea.insert(END,"\n Status: \t\t\tFailed")
                                    prod_name = ""
                                    self.company_prod.set("")
                                    self.cat_prod = ""
                                    self.com_prod = ""
                                    self.remove_prod.set("")
                                    self.entry_category_prod.current(0)
                                    return
                            os.remove(self.Path_To_Json)
                            with open(self.Path_To_Json,"w",encoding="utf-8") as f:
                                json.dump(data,f,indent=4)
                            self.welcome()
                            self.textarea.insert(END,f"\n Product \"{prod_name}\" removed from \"{self.com_prod}\"")
                            self.textarea.insert(END,"\n Status: \t\t\tSuccess")
                        except KeyError:
                            messagebox.showerror("ERROR","The specified Company does not exist, Please check your spellings and punctuation and try again")
                            self.welcome()
                            self.textarea.insert(END,f"\n \"{prod_name}\" cannot be removed because\n  company name doesnot exist")
                            self.textarea.insert(END,"\n Status: \t\t\tFailed")
            prod_name = ""
            self.company_prod.set("")
            self.cat_prod = ""
            self.com_prod = ""
            self.remove_prod.set("")
            self.entry_category_prod.current(0)

    #Check stock/price of a product function
    def check_stock_to_prod(self):
        self.verify_prod()
        if self.is_checked_prod > 0:
            prod_name = self.check_stock_prod.get()
            if prod_name == "":
                messagebox.showerror("Error","Please Select a Product to show stock")
                self.welcome()
                self.textarea.insert(END,"\n No Product Selected for stock checking")
                self.textarea.insert(END,"\n Status: \t\t\tFailed")
            else:
                if self.cat_prod in self.Category_prod:    
                    data = 0                
                    try:
                        with open(self.Path_To_Json,"r",encoding="utf-8") as f:
                            data = json.load(f)
                            data[f"{self.cat_prod}"][f"{self.com_prod}"]
                            try:
                                data[f"{self.cat_prod}"][f"{self.com_prod}"][f"{prod_name}"]
                            except KeyError:
                                messagebox.showerror("ERROR","The specified Product does not exist, Please check your spellings and punctuation and try again")
                                self.welcome()
                                self.textarea.insert(END,f"\n \"{prod_name}\" stock cannot be shown because\n  product name doesnot exist")
                                self.textarea.insert(END,"\n Status: \t\t\tFailed")
                                prod_name = ""
                                self.company_prod.set("")
                                self.cat_prod = ""
                                self.com_prod = ""
                                self.check_stock_prod.set("")
                                self.entry_category_prod.current(0)
                                return
                            stock = data.get(self.cat_prod,{}).get(self.com_prod,{}).get(prod_name,{}).get("stock")
                            price = data.get(self.cat_prod,{}).get(self.com_prod,{}).get(prod_name,{}).get("price")
                            self.welcome()
                            self.textarea.insert(END,f"\n \"{prod_name}\" has stock of \"{stock}\" and \"{price}\" price")
                            self.textarea.insert(END,"\n---------------------------------------------------------------------------------------")
                            self.textarea.insert(END,"\n---------------------------------------------------------------------------------------")
                            self.textarea.insert(END,f"\n\nProduct: \t\t{prod_name}")
                            self.textarea.insert(END,f"\nStock: \t\t{stock}")
                            self.textarea.insert(END,f"\nPrice: \t\t{price}\n")
                            self.textarea.insert(END,"\n---------------------------------------------------------------------------------------")
                            self.textarea.insert(END,"\n---------------------------------------------------------------------------------------")
                            self.textarea.insert(END,"\n Status: \t\t\tSuccess")
                    except KeyError:
                            messagebox.showerror("ERROR","The specified Company does not exist, Please check your spellings and punctuation and try again")
                            self.welcome()
                            self.textarea.insert(END,f"\n \"{prod_name}\" cannot be checked because\n  company name doesnot exist")
                            self.textarea.insert(END,"\n Status: \t\t\tFailed")

            prod_name = ""
            self.company_prod.set("")
            self.cat_prod = ""
            self.com_prod = ""
            self.check_stock_prod.set("")
            self.entry_category_prod.current(0)
    
    #Stock Functions
    def verify_stock(self):
        self.is_checked_stock = 1
        self.cat_stock = self.entry_category_stock.get()
        self.com_stock = self.company_stock.get()
        self.pro_stock = self.product_stock.get()
        if self.cat_stock == "" or self.cat_stock == "Select Option":
            messagebox.showerror("Error","Please Select a Category")
            self.welcome()
            self.textarea.insert(END,"\n No Category Selected")
            self.textarea.insert(END,"\n Status: \t\t\tFailed")
            self.is_checked_stock = 0
        else:
            if self.com_stock == "":
                messagebox.showerror("Error","Please Select a Company")
                self.welcome()
                self.textarea.insert(END,"\n No Company Selected")
                self.textarea.insert(END,"\n Status: \t\t\tFailed")
                self.is_checked_stock = 0
            else:
                if self.pro_stock == "":
                    messagebox.showerror("Error","Please Select a Product")
                    self.welcome()
                    self.textarea.insert(END,"\n No Product Selected")
                    self.textarea.insert(END,"\n Status: \t\t\tFailed")
                    self.is_checked_stock = 0
                else:
                    if self.cat_stock not in self.Category_stock:
                        messagebox.showerror("Error","Selected Category not found")
                        self.welcome()
                        self.textarea.insert(END,"\n Selected category does not exist.\n  Please check your spellings and punctuation and try again")
                        self.textarea.insert(END,"\n Status: \t\t\tFailed")
                        self.is_checked_stock = 0
                    else:
                        with open(self.Path_To_Json,"r",encoding="utf-8") as f:
                            data = json.load(f)
                            try:
                                data[f"{self.cat_stock}"][f"{self.com_stock}"]
                                try:
                                    data[f"{self.cat_stock}"][f"{self.com_stock}"][f"{self.pro_stock}"]
                                except KeyError:
                                    messagebox.showerror("Error","Selected Product not found")
                                    self.welcome()
                                    self.textarea.insert(END,f"\n Selected Product:\"{self.pro_stock}\" does not exist.\n  Please check your spellings and punctuation and try again")
                                    self.textarea.insert(END,"\n Status: \t\t\tFailed")
                                    self.is_checked_stock = 0
                            except KeyError:
                                messagebox.showerror("Error","Selected Company not found")
                                self.welcome()
                                self.textarea.insert(END,f"\n Selected Company:\"{self.com_stock}\" does not exist.\n  Please check your spellings and punctuation and try again")
                                self.textarea.insert(END,"\n Status: \t\t\tFailed")
                                self.is_checked_stock = 0
    #Verify num and empty 
    def num_empty_stock(self,x):
        if x == "" or x == 0:
            messagebox.showerror("Error","Product number not found or is empty or set to zero")
            self.welcome()
            self.textarea.insert(END,f"\n Please Select the product number to add")
            self.textarea.insert(END,"\n Status: \t\t\tFailed")
            self.is_checked_stock = 0
        else:
            if not isinstance(x ,(int,float)):
                messagebox.showerror("Error","Given value must be a number")
                self.welcome()
                self.textarea.insert(END,"\n Operation field must be a number")
                self.textarea.insert(END,"\n Status: \t\t\tFailed")
                self.is_checked_stock = 0

    #No. of products add function
    def add_products_to_stock(self):
        self.verify_stock()
        if self.is_checked_stock > 0:
            prod_num = int(self.entry_add_stock.get())
            self.num_empty_stock(prod_num)
            if self.is_checked_stock > 0:
                with open(self.Path_To_Json,"r",encoding="utf-8") as f:
                    data = json.load(f)
                    try:
                        data[f"{self.cat_stock}"][f"{self.com_stock}"][f"{self.pro_stock}"]["stock"]
                    except KeyError:
                        data[f"{self.cat_stock}"][f"{self.com_stock}"][f"{self.pro_stock}"]["stock"] = 0 
                    data[f"{self.cat_stock}"][f"{self.com_stock}"][f"{self.pro_stock}"]["stock"] += prod_num
                    lol = data[f"{self.cat_stock}"][f"{self.com_stock}"][f"{self.pro_stock}"]["stock"]
                os.remove(self.Path_To_Json)
                with open(self.Path_To_Json,"w",encoding="utf-8") as f:
                    json.dump(data,f,indent=4)
                self.welcome()
                self.textarea.insert(END,f"\n {prod_num} products added to stock of \"{self.pro_stock}\"\n New stock of \"{self.pro_stock}\" is {lol}")
                self.textarea.insert(END,"\n Status: \t\t\tSuccess")
        prod_num = 0
        self.add_prod_stock.set(0)
        self.cat_stock = ""
        self.com_stock = ""
        self.pro_stock = ""
        self.company_stock.set("")
        self.product_stock.set("")
        self.entry_category_stock.current(0)
                
    #No. of products remove function
    def remove_products_to_stock(self):
        self.verify_stock()
        if self.is_checked_stock > 0:
            prod_num = int(self.entry_remove_stock.get())
            self.num_empty_stock(prod_num)
            if self.is_checked_stock > 0:
                with open(self.Path_To_Json,"r",encoding="utf-8") as f:
                    data = json.load(f)
                if prod_num > data[f"{self.cat_stock}"][f"{self.com_stock}"][f"{self.pro_stock}"]["stock"]:
                    messagebox.showerror("Error","Given data is greater than actual number of products in stock. Can't hold negative values")
                    self.welcome()
                    self.textarea.insert(END,"\n Operation field must be a number less than actual\n amount of products")
                    self.textarea.insert(END,"\n Status: \t\t\tFailed")
                elif prod_num <= data[f"{self.cat_stock}"][f"{self.com_stock}"][f"{self.pro_stock}"]["stock"]:
                    data[f"{self.cat_stock}"][f"{self.com_stock}"][f"{self.pro_stock}"]["stock"] -= prod_num
                    lol = data[f"{self.cat_stock}"][f"{self.com_stock}"][f"{self.pro_stock}"]["stock"]
                    os.remove(self.Path_To_Json)
                    with open(self.Path_To_Json,"w",encoding="utf-8") as f:
                        json.dump(data,f,indent=4)
                    self.welcome()
                    self.textarea.insert(END,f"\n {prod_num} products removed from stock of \"{self.pro_stock}\"\n New stock of \"{self.pro_stock}\" is {lol}")
                    self.textarea.insert(END,"\n Status: \t\t\tSuccess")
        prod_num = 0 
        self.cat_stock = ""
        self.com_stock = ""
        self.pro_stock = ""
        self.company_stock.set("")
        self.product_stock.set("")
        self.entry_category_stock.current(0)
        self.remove_prod_stock.set(0)

    #set  product stock
    def set_prod_to_stock(self):
        self.verify_stock()
        if self.is_checked_stock > 0:
            prod_num = int(self.entry_change_stock.get())
            if prod_num != 0:
                self.num_empty_stock(prod_num)
            if prod_num < 0:
                messagebox.showerror("Error","Given data is smaller than zero. Can't hold negative values")
                self.welcome()
                self.textarea.insert(END,"\n Operation field must be a number greater than zero(0)")
                self.textarea.insert(END,"\n Status: \t\t\tFailed")
            elif prod_num >= 0:
                op=messagebox.askyesno("Stock Update!",f"You want to update stock of {self.pro_stock} to {prod_num}")
                if op == 0:
                    messagebox.showerror("Error","Operation not done, Denied by user")
                    self.welcome()
                    self.textarea.insert(END,"\n Denied")
                    self.textarea.insert(END,"\n Status: \t\t\tFailed")
                elif op > 0:
                    if self.is_checked_stock > 0:
                        with open(self.Path_To_Json,"r",encoding="utf-8") as f:
                            data = json.load(f)
                            data[f"{self.cat_stock}"][f"{self.com_stock}"][f"{self.pro_stock}"]["stock"] = prod_num
                        os.remove(self.Path_To_Json)
                        with open(self.Path_To_Json,"w",encoding="utf-8") as f:
                            json.dump(data,f,indent=4)
                        self.welcome()
                        self.textarea.insert(END,f"\n current stock of \"{self.pro_stock}\" is {prod_num}\n Stock Updated!!")
                        self.textarea.insert(END,"\n Status: \t\t\tSuccess")
        prod_num = 0
        self.cat_stock =""
        self.com_stock = ""
        self.pro_stock = ""
        self.company_stock.set("")
        self.product_stock.set("")
        self.entry_category_stock.current(0)
        self.set_prod_stock.set(0)

    #Set new price
    def new_price_to_stock(self):
        self.verify_stock()
        if self.is_checked_stock > 0:
            try:
                prod_num = int(self.entry_price_stock.get())
            except ValueError:
                messagebox.showerror("Error","Given data must be a number")
                self.welcome()
                self.textarea.insert(END,"\n Operation field must be a number")
                self.textarea.insert(END,"\n Status: \t\t\tFailed")
                prod_num = 0
                self.cat_stock =""
                self.com_stock = ""
                self.pro_stock = ""
                self.company_stock.set("")
                self.product_stock.set("")
                self.entry_category_stock.current(0)
                self.set_price_stock.set(0)
                return
            self.num_empty_stock(prod_num)
            if self.is_checked_stock > 0:   
                if prod_num < 0:
                    messagebox.showerror("Error","Given data is smaller than zero. Can't hold negative values")
                    self.welcome()
                    self.textarea.insert(END,"\n Operation field must be a number less than zero(0)")
                    self.textarea.insert(END,"\n Status: \t\t\tFailed")
                elif prod_num > 0:
                    op=messagebox.askyesno("Stock Update!",f"You want to update price of {self.pro_stock} to {prod_num}")
                    if op == 0:
                        messagebox.showerror("Error","Operation not done, Denied by user")
                        self.welcome()
                        self.textarea.insert(END,"\n Denied")
                        self.textarea.insert(END,"\n Status: \t\t\tFailed")
                    elif op > 0:
                        with open(self.Path_To_Json,"r",encoding="utf-8") as f:
                            data = json.load(f)
                            data[f"{self.cat_stock}"][f"{self.com_stock}"][f"{self.pro_stock}"]["price"] = prod_num
                        os.remove(self.Path_To_Json)
                        with open(self.Path_To_Json,"w",encoding="utf-8") as f:
                            json.dump(data,f,indent=4)
                        self.welcome()
                        self.textarea.insert(END,f"\n current price of \"{self.pro_stock}\" is {prod_num}\n Stock Updated!!")
                        self.textarea.insert(END,"\n Status: \t\t\tSuccess")
        prod_num = 0
        self.cat_stock =""
        self.com_stock = ""
        self.pro_stock = ""
        self.company_stock.set("")
        self.product_stock.set("")
        self.entry_category_stock.current(0)
        self.set_price_stock.set(0)

    #Show all companies Function
    def show_all_to_companies(self):
        lol = []
        with open(self.Path_To_Json,"r",encoding="utf-8") as f:
            data = json.load(f)
        try:
            for k,v in data["Seeds"].items():
                lol.append(k)
        except KeyError:
            messagebox.showerror("Error","There are no categories in the database")
            self.welcome()
            self.textarea.insert(END,f"\n No categories found in the database")
            self.textarea.insert(END,"\n Status: \t\t\tSuccess")
            return
        if lol != []:
            self.welcome()
            self.textarea.insert(END,"\n Success: \t\tSuccess")
            self.textarea.insert(END,"\nNames of all companies are")
            lol.sort()
            wow = 0
            for i in lol:
                wow += 1
                self.textarea.insert(END,f"\n{wow}- {i}")
            self.textarea.insert(END,"\n\nCompleted !!")
    #Show  all products by category
    def show_all_products_to_category(self):
        lol = []
        lol1 = []
        prod_name = self.entry_show_all_products_cat.get()
        if prod_name == "" or prod_name == "Select Option":
            messagebox.showerror("Error","Please Select a Category")
            self.welcome()
            self.textarea.insert(END,"\n No Category Selected")
            self.textarea.insert(END,"\n Status: \t\t\tFailed")
        else:
            with open(self.Path_To_Json,"r",encoding="utf-8") as f:
                data = json.load(f)  
            for k,v in data[f"{prod_name}"].items():
                lol.append(k)
            if lol == []:
                messagebox.showerror("Error","There are no companies in the database")
                self.welcome()
                self.textarea.insert(END,"\n No Companies in the database")
                self.textarea.insert(END,"\n Status: \t\t\tFailed")
            else:
                for i in lol:
                    for k , v in data[f"{prod_name}"][i].items():
                        try:
                            tmp_stock = data[f"{prod_name}"][i][k]["stock"]
                        except KeyError:
                            data[f"{prod_name}"][i][k]["stock"] = 0
                            tmp_stock = data[f"{prod_name}"][i][k]["stock"]
                        try:
                            tmp_price = data[f"{prod_name}"][i][k]["price"]
                        except KeyError:
                            data[f"{prod_name}"][i][k]["price"] = 0
                            tmp_price = data[f"{prod_name}"][i][k]["price"]
                        temp = f"{k} :\t\t{tmp_stock}\t{tmp_price}\t\t{i}"
                        lol1.append(temp)
                if lol1 == []:
                    messagebox.showerror("Error","There are no Products in the database")
                    self.welcome()
                    self.textarea.insert(END,"\n No Products in the database")
                    self.textarea.insert(END,"\n Status: \t\t\tFailed")
                else:
                    self.welcome()
                    self.textarea.insert(END,"\n Status: \t\tSuccess")
                    self.textarea.insert(END,f"\nNames of all Products of category \"{prod_name}\" are:")
                    self.textarea.insert(END,"\nProducts  \t\tStock \t Price \t\t Company")
                    lol1.sort()
                    noob = 0
                    for www in lol1:
                        noob += 1
                        self.textarea.insert(END,f"\n{noob}- {www}")
                    self.textarea.insert(END,"\n\nCompleted!!")

        self.entry_show_all_products_cat.current(0)

    #Show all products by company
    def show_all_products_to_company(self):
        lol = []
        hardcoded_tmp = ["Seeds","Fertilizers","Sprays and Pesticides","Miscellaneous"]
        prod_name = self.show_all_products_com_misc.get()
        if prod_name == "":
            messagebox.showerror("Error","Please Select a Company")
            self.welcome()
            self.textarea.insert(END,"\n No Company Selected")
            self.textarea.insert(END,"\n Status: \t\t\tFailed")
        else:
            with open(self.Path_To_Json,"r",encoding="utf-8") as f:
                data = json.load(f)
            try:
                data["Seeds"][f"{prod_name}"]
            except KeyError:
                messagebox.showerror("ERROR","The specified company does not exist, Please check your spelling and punctuation and try again")
                self.welcome()
                self.textarea.insert(END,f"\n \"{prod_name}\" company not found in database")
                self.textarea.insert(END,"\n Status: \t\t\tFailed")
                self.show_all_products_com_misc.set("")
                return
            for i in hardcoded_tmp:
                for k ,v in data[i][prod_name].items():
                    try:
                        tmp_stock = data[i][prod_name][k]["stock"]
                    except KeyError:
                        data[i][prod_name][k]["stock"] = 0
                        tmp_stock = data[i][prod_name][k]["stock"]
                    try:
                        tmp_price = data[i][prod_name][k]["price"]
                    except KeyError:
                        data[i][prod_name][k]["price"] = 0
                        tmp_price = data[i][prod_name][k]["price"]
                    temp = f"{k} :\t\t{tmp_stock}\t{tmp_price}\t\t{i}"
                    lol.append(temp)
            if lol == []:
                    messagebox.showerror("Error","There are no Products in the database")
                    self.welcome()
                    self.textarea.insert(END,"\n No Products in the database")
                    self.textarea.insert(END,"\n Status: \t\t\tFailed")
            else:
                self.welcome()
                self.textarea.insert(END,"\n Status: \t\tSuccess")
                self.textarea.insert(END,f"\nNames of all Products of company \"{prod_name}\" are:")
                self.textarea.insert(END,"\nProducts  \t\tStock \t Price \t\t Category")
                lol.sort()
                noob = 0
                for www in lol:
                    noob += 1
                    self.textarea.insert(END,f"\n{noob}- {www}")
                    self.textarea.insert(END,"\n\nCompleted!!")
            
        self.show_all_products_com_misc.set("")
    #Bill generator function
    def bill_generate_go(self):
        self.root.destroy()
        os.system("python D:\\files\\billing.py")
        

    #Clear Function
    def clear(self):
        self.add_company.set("")
        self.remove_company.set("")
        self.rename_company_first.set("")
        self.rename_company_second.set("")
        self.is_checked_prod = 1
        self.add_prod.set("")
        self.remove_prod.set("")
        self.company_prod.set("")
        self.cat_prod = ""
        self.com_prod = ""
        self.check_stock_prod.set("")
        self.entry_category_prod.current(0)
        self.is_checked_stock = 1
        self.add_prod_stock.set(0)
        self.cat_stock = ""
        self.remove_prod_stock.set(0)
        self.set_prod_stock.set(0)
        self.cat_stock =""
        self.com_stock = ""
        self.pro_stock = ""
        self.company_stock.set("")
        self.product_stock.set("")
        self.entry_category_stock.current(0)
        self.set_price_stock.set(0)
        self.entry_show_all_products_cat.current(0)
        self.show_all_products_com_misc.set("")
        self.entry_add_company.set("")
        self.entry_remove_company.set("")
        self.entry_change_company.set("")
        self.entry_company_prod.set("")
        self.entry_company_stock.set("")
        self.entry_show_all_products_com.set("") 
        self.search_loan_name.set("")
        self.minus_loan.set(0)
        self.welcome()

    #Backup Function
    def backup_jsondata(self):
        wow = datetime.now()
        wow_string = wow.strftime("%d.%m.%Y")
        with open(self.Path_To_Json,"r",encoding="utf-8") as f:
            data = json.load(f)
        try:
            with open("D:\\files\\important files\\backup\\" + wow_string +"_stock"+ ".txt","x",encoding="utf-8") as wow:
                json.dump(data,wow,indent=4)
        except FileExistsError:
            pass

        with open(self.Path_To_Customer_data,"r",encoding="utf-8") as f:
            lol = json.load(f)
        try:
            with open("D:\\files\\important files\\backup\\" + wow_string + "_customer"+".txt","x",encoding="utf-8") as wow:
                json.dump(lol,wow,indent=4)
        except FileExistsError:
            pass

        with open(self.Path_To_Loan_data,"r",encoding="utf-8") as f:
            lmao = json.load(f)
        try:
            with open("D:\\files\\important files\\backup\\" + wow_string +"_loan"+ ".txt","x",encoding="utf-8") as wow:
                json.dump(lmao,wow,indent=4)
        except FileExistsError:
            pass
    
    #Selcect * from companies function
    #1- add company combobox
    def company_key_press(self,event=""):
        here_list = []
        prod_name = event.widget.get()
        if prod_name != "":
            with open(self.Path_To_Json,"r",encoding="utf-8") as f:
                data = json.load(f)
            for k,v in data["Seeds"].items():
                if prod_name.lower() in k.lower():
                    here_list.append(k)
            here_list.sort()
            event.widget.config(value=here_list)
    #2 add products
    def product_key_press(self,event=""):
        tmp_list = ["Seeds","Fertilizers","Sprays and Pesticides","Miscellaneous"]
        tmp2 = []
        here_list = []
        prod_name = event.widget.get()
        if prod_name != "":
            with open(self.Path_To_Json,"r",encoding="utf-8") as f:
                data = json.load(f)
            for k,v in data["Seeds"].items():
                tmp2.append(k)
            for cat in tmp_list:
                for com in tmp2:
                    for prodk,v in data[cat][com].items():
                        if prod_name.lower() in prodk.lower():
                            here_list.append(prodk)
            here_list.sort()
            event.widget.config(value=here_list)
                
    def search_loan_and_others(self,event=""):
        prod_name = event.widget.get()
        here_list = []
        prod_name = prod_name.lower()
        if prod_name != "":
            with open(self.Path_To_Loan_data,"r",encoding="utf-8") as f:
                data = json.load(f)
            for k, v  in data["loan"].items():
                if prod_name in k.lower():
                    here_list.append(k)
            event.widget.config(value=here_list)
        elif prod_name == "":
            event.widget.config(value="")

    def search_loan_btn_function(self):
        prod_name = self.search_loan_name.get()
        prod_name = prod_name.lower()
        with open(self.Path_To_Loan_data,"r",encoding="utf-8") as f:
            data = json.load(f)
        try:
            data["loan"][prod_name]
        except KeyError:
            messagebox.showerror("Error","The username entered does not exist. Please check your spellings , Punctuation and try again")
            self.welcome()
            self.textarea.insert(END,f"\n No user found with name of {prod_name} in the database")
            self.textarea.insert(END,"\n Status: \t\t\tFailed")
            self.search_loan_name.set("")
            return
        phone = data["loan"][prod_name]["phone"]
        address = data["loan"][prod_name]["address"]
        cust_id = data["loan"][prod_name]["customer_id"]
        total_loan = data["loan"][prod_name]["Total Loan"]
        self.welcome()
        self.textarea.insert(END,f"\n Name: \t\t{prod_name}")
        self.textarea.insert(END,f"\n Phone: \t\t{phone}")
        self.textarea.insert(END,f"\n Address: \t\t{address}")
        self.textarea.insert(END,f"\n Customer ID: \t\t{cust_id}")
        self.textarea.insert(END,f"\n Total Credit: \t\t{total_loan}")
        self.textarea.insert(END,"\n=======================================================")
        self.textarea.insert(END,"\n=======================================================")
        for k,v in data["loan"][prod_name]["purchase"].items():
            self.textarea.insert(END,f"\n\tBill No:\t\t{k}")
            for newk ,newv in v.items():
                self.textarea.insert(END,f"\n\t{newk}: \t\t{newv}")
            self.textarea.insert(END,"\n=======================================================")
        self.search_loan_name.set("")

    def minus_loan_on_search(self,event=""):
        prod_name = self.entry_search_loan.get()
        try:
            int(prod_name)
        except ValueError:
            try:
                self.minus_loan.set(prod_name.replace(prod_name[-1],""))
            except IndexError:
                self.minus_loan.set(0)

    def minus_btn_on_search(self):
        prod_name = self.search_loan_name.get()
        prod_name = prod_name.lower()
        loan_minus = int(self.entry_search_loan.get())
        with open(self.Path_To_Loan_data,"r",encoding="utf-8") as f:
            data = json.load(f)
        try:
            data["loan"][prod_name]
        except KeyError:
            messagebox.showerror("Error","The username entered does not exist. Please check your spellings , Punctuation and try again")
            self.welcome()
            self.textarea.insert(END,f"\n No user found with name of {prod_name} in the database")
            self.textarea.insert(END,"\n Status: \t\t\tFailed")
            self.minus_loan.set(0)
            self.search_loan_name.set("")
            return
        total_loan = data["loan"][prod_name]["Total Loan"]
        if loan_minus > total_loan:
            messagebox.showerror("Error","The Entered  amount is greater than customer's actual Credit")
            self.welcome()
            self.textarea.insert(END,f"\n The entered amount {str(loan_minus)} is greater than\n actual Credit which is {total_loan}")
            self.textarea.insert(END,"\n Status: \t\t\tFailed")
            self.minus_loan.set(0)
            self.search_loan_name.set("")
            return
        asker = askstring("Are You sure!!","This will minus the Credit amount of user\nand if amount is equal to total Credit , it will clear all Clear records of that customer\n Type \"yes\" to continue the process")
        try:
            asker.lower()
        except AttributeError:
            messagebox.showerror("Error","Operation not done, Denied by user")
            self.welcome()
            self.textarea.insert(END,"\n Denied")
            self.textarea.insert(END,"\n Status: \t\t\tFailed")
            self.minus_loan.set(0)
            self.search_loan_name.set("")
            return
        if asker.lower() != "yes":
            messagebox.showerror("Error","Operation not done, Denied by user")
            self.welcome()
            self.textarea.insert(END,"\n Denied")
            self.textarea.insert(END,"\n Status: \t\t\tFailed")
            self.minus_loan.set(0)
            self.search_loan_name.set("")
            return
        elif asker.lower() == "yes":
            if loan_minus == total_loan:
                data["loan"][prod_name]["Total Loan"] = 0
                data["loan"][prod_name]["purchase"] = {}
                hello = data["loan"][prod_name]["Total Loan"]
                self.welcome()
                self.textarea.insert(END,f"\n Done. Current Credit of {prod_name} is {hello}")
                self.textarea.insert(END,"\n Status: \t\t\tSuccess")
                self.minus_loan.set(0)
                self.search_loan_name.set("")
            elif loan_minus < total_loan:
                data["loan"][prod_name]["Total Loan"] -= loan_minus
                hello = data["loan"][prod_name]["Total Loan"]
                self.welcome()
                self.textarea.insert(END,f"\n Done. Current Credit of {prod_name} is {hello}")
                self.textarea.insert(END,"\n Status: \t\t\tSuccess")
                self.minus_loan.set(0)
                self.search_loan_name.set("")

        os.remove(self.Path_To_Loan_data)
        with open(self.Path_To_Loan_data,"w",encoding="utf-8") as f:
            json.dump(data,f,indent=4)

        
    #Functions Complete



root=Tk()
obj=Manage_App(root)
root.mainloop()


