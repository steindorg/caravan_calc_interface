import tkinter as tk
from tkinter import ttk
from tkinter import font as tkFont

import Widget_controller_classes as Widget_classes

# Test view
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry(("1400x1200"))
        self.option_add("*Font", "helvetica 22")
        self.choices_frame = tk.LabelFrame(self,text='Navigation')
        self.choices_frame.grid(column=0,row=0)
        self.current_frame = Widget_classes.Costumer_widget(self, 'Vipskiptavinir')
        self.costumer = None
        self.manufacturer = None
        self.productCategory = None
        self.productModel = None
        self.product = None
        self.extras_category = None
        self.optional_extras = None
        self.extras_ToProducts = None
        self.makeOrder = None

        self.btn_costumer = tk.Button(self.choices_frame, text="Viðskiptavinir",           command=self.callback)
        self.btn_productCategory = tk.Button(self.choices_frame, text="Vöruflokkar",       command=self.callback_2)
        self.btn_productModel = tk.Button(self.choices_frame, text="Vörumódel",            command=self.callback_3)
        self.btn_product = tk.Button(self.choices_frame, text="Vörur",                     command=self.callback_4)
        self.btn_manufacturer = tk.Button(self.choices_frame, text="Framleiðendur",        command=self.callback_5)
        self.btn_extras_category = tk.Button(self.choices_frame, text="Tegund Aukahlutir", command=self.callback_6)
        self.btn_optional_extras = tk.Button(self.choices_frame, text="Aukahlutir",        command=self.callback_7)
        self.btn_extras_ToProducts= tk.Button(self.choices_frame, text="Aukahlutir-Vörur", command=self.callback_8)
        self.btn_makeOrder = tk.Button(self.choices_frame, text="Gera Pöntun",             command=self.callback_9)
        
        self.btn_costumer.grid(column=0,row=0,padx=8,pady=4)
        self.btn_productCategory.grid(column=1,row=0 ,padx=8,pady=4)
        self.btn_productModel.grid(column=2,row=0,padx=8,pady=4)
        self.btn_product.grid(column=3,row=0,padx=8,pady=4)
        self.btn_manufacturer.grid(column=4,row=0,padx=8,pady=4)
        self.btn_extras_category.grid(column=5,row=0,padx=8,pady=4)
        self.btn_optional_extras.grid(column=6,row=0,padx=8,pady=4)
        self.btn_extras_ToProducts.grid(column=7,row=0,padx=8,pady=4)
        self.btn_makeOrder.grid(column=8,row=0,padx=8,pady=4)

    def callback(self):
        self.current_frame.destroy()
        self.costumer = Widget_classes.Costumer_widget(self, 'Vipskiptavinir')
        self.costumer.grid(column=0,row=1)
        self.current_frame = self.costumer

    def callback_2(self):
        self.current_frame.destroy()
        self.productCategory = Widget_classes.ProductCategory_widget(self, 'Vöruflokkar')
        self.productCategory.grid(column=0,row=1)
        self.current_frame = self.productCategory
    
    def callback_3(self):
        self.current_frame.destroy()
        self.productModel = Widget_classes.ProductModel_widget(self, 'Vöru módel')
        self.productModel.grid(column=0,row=1) 
        self.current_frame = self.productModel
       

    def callback_4(self):
        self.current_frame.destroy()
        self.product = Widget_classes.Product_widget(self, 'Vörur')
        self.product.grid(column=0,row=1)
        self.current_frame = self.product
  

    def callback_5(self):
        self.current_frame.destroy()
        self.manufacturer = Widget_classes.Manufacturer_widget(self, 'Framleiðendur')
        self.manufacturer.grid(column=0,row=1)
        self.current_frame = self.manufacturer

    def callback_6(self):
        self.current_frame.destroy()
        self.extras_category = Widget_classes.ExtrasCategory_widget(self, 'Aukahlutir tegundir')
        self.extras_category.grid(column=0,row=1)
        self.current_frame = self.extras_category 

    
    def callback_7(self):
        self.current_frame.destroy()
        self.optional_extras = Widget_classes.Extras_widget(self, 'Aukahlutir')
        self.optional_extras.grid(column=0,row=1)
        self.current_frame = self.optional_extras

    def callback_8(self):
        self.current_frame.destroy()
        self.extras_ToProducts = Widget_classes.ExtrasToProducts(self, "Aukahlutir-Vörur")
        self.extras_ToProducts.grid(column=0,row=1)
        self.current_frame = self.extras_ToProducts
    
    def callback_9(self):
        self.current_frame.destroy()
        self.makeOrder = Widget_classes.Orders_widget(self, "Pantanir")
        self.makeOrder.grid(column=0,row=1)
        self.current_frame = self.makeOrder 
       
      
    
if __name__ == "__main__":
    app = App()
    app.mainloop()
