import tkinter as tk
from tkinter import ttk
from tkinter import font as tkFont

import Widget_classes

# Test view
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry(("1200x800"))
        self.costumer = None
        self.manufacturer = None
        self.productCategory = None
        self.productModel = None
        self.product = None
        self.extras_category = None
        self.optional_extras = None
        self.btn_costumer = tk.Button(self, text="Viðskiptavinir", command=self.callback)
        self.btn_productCategory = tk.Button(self, text="Vöruflokkar", command=self.callback_2)
        self.btn_productModel = tk.Button(self, text="Vörumódel", command=self.callback_3)
        self.btn_product = tk.Button(self, text="Vörur", command=self.callback_4)
        self.btn_manufacturer = tk.Button(self, text="Framleiðendur", command=self.callback_5)
        self.btn_extras_category = tk.Button(self, text="Tegund Aukahlutir", command=self.callback_6)
        self.btn_optional_extras = tk.Button(self, text="Aukahlutir", command=self.callback_7)
        
        self.btn_costumer.grid(column=0,row=0)
        self.btn_productCategory.grid(column=1,row=0)
        self.btn_productModel.grid(column=2,row=0)
        self.btn_product.grid(column=3,row=0)
        self.btn_manufacturer.grid(column=4,row=0)
        self.btn_extras_category.grid(column=5,row=0)
        self.btn_optional_extras.grid(column=6,row=0)

    def callback(self):
        self.costumer = Widget_classes.Costumer_widget(self, 'Vipskiptavinir)
        self.costumer.grid(column=0,row=1)
        self.manufacturer.destroy()
        self.product.destroy()
        self.productCategory.destroy()
        self.productModel.destroy()
        self.extras_category.destroy()
        self.optional_extras.destroy()

    def callback_2(self):
        self.productCategory = Widget_classes.ProductCategory_widget(self, 'Vöruflokkar')
        self.productCategory.grid(column=0,row=1)
        self.manufacturer.destroy()
        self.costumer.destroy()
        self.product.destroy()
        self.productModel.destroy()
        self.extras_category.destroy()
        self.optional_extras.destroy()
    
    def callback_3(self):
        self.productModel = Widget_classes.ProductModel_widget(self, 'Vöru módel')
        self.productModel.grid(column=0,row=1) 
        self.costumer.destroy()
        self.manufacturer.destroy() 
        self.product.destroy()
        self.extras_category.destroy()
        self.optional_extras.destroy()

    def callback_4(self):
        self.product = Widget_classes.Product_widget(self, 'Vörur')
        self.product.grid(column=0,row=1)
        self.costumer.destroy()
        self.productCategory.destroy()
        self.productModel.destroy()
        self.manufacturer.destroy()
        self.extras_category.destroy()
        self.optional_extras.destroy()

    def callback_5(self):
        self.manufacturer = Widget_classes.Manufacturer_widget(self, 'Framleiðendur')
        self.manufacturer.grid(column=0,row=1)
        self.costumer.destroy()
        self.productCategory.destroy()
        self.productModel.destroy()
        self.product.destroy()
        self.extras_category.destroy()
        self.optional_extras.destroy()
    
    def callback_6(self):
        self.extras_category = Widget_classes.ExtrasCategory_widget(self, 'Aukahlutir tegundir')
        self.extras_category.grid(column=0,row=1)
        self.costumer.destroy()
        self.productCategory.destroy()
        self.productModel.destroy()
        self.product.destroy()
        self.optional_extras.destroy()
        self.manufacturer.destroy()
    
    def callback_7(self):
        self.optional_extras = Widget_classes.Extras_widget(self, 'Aukahlutir')
        self.optional_extras.grid(column=0,row=1)
        self.productCategory.destroy()
        self.productModel.destroy()
        self.product.destroy()
        self.manufacturer.destroy()
        self.extras_category.destroy()
        
    
if __name__ == "__main__":
    app = App()
    app.mainloop()
