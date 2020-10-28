import tkinter as tk
from tkinter import ttk
from tkinter import font as tkFont
import controller_crud as get_db_data
import re

#Test controller

class popup_menu():
    def __init__(self, main_frame, values, col, row, x, y):
        self.value = tk.StringVar()
        self.values = values
        self.current = 0
        self.popup = ttk.Combobox( main_frame, width = 10, height = 25, textvariable = self.value, state='readonly')
        self.popup['values'] = self.values
        self.popup.pack()
        self.popup.pack_configure( padx = x, pady = y )
        self.popup.current(self.current)

class button():
    def __init__(self, frame, text, width, side, command, x, y):
        self.frame = frame
        self.width = width
        self.command = command
        self.but = tk.Button(frame, text = text, width=width, command = self.command)
        self.but.pack(side=side)
        self.but.pack_configure( padx = x, pady = y )

class butt():
    def __init__(self, frame, text, width, col, row, command, x, y):
        self.frame = frame
        self.width = width
        self.command = command
        self.but = tk.Button(frame, text = text, width=width, command = self.command)
        self.but.grid_configure( padx = x, pady = y)
        self.but.grid( column=col, row=row )


class menu():
    def __init__(self, main_frame, values, col, row, x, y, width):
        self.value = tk.StringVar()
        self.values = values
        self.current = 0
        self.popup = ttk.Combobox( main_frame, width = width, height = 85, textvariable = self.value, state='readonly')
        self.popup['values'] = self.values
        self.popup.grid( column = col, row = row )
        self.popup.grid_configure( padx = x, pady = y )
        self.popup.current(self.current)


class Form_widget(tk.LabelFrame):
    def __init__(self, master, fields, title_name, **kwargs):
        super().__init__(master, text = title_name, padx = 10, pady = 10, **kwargs)
        self.fields = fields
        self.load_details = None
        self.frame = tk.Frame(self)
        self.entries = list(map(self.create_field, enumerate(self.fields)))
        self.frame.pack()

    def create_field(self, field):
        position, text = field
        label = tk.Label(self.frame, text=text)
        entry = tk.Entry(self.frame, width=25)
        label.grid(row=position, column=0, pady=5)
        entry.grid(row=position, column=1, pady=5)
        return entry

    # get user input frá user input form dálkum
    def get_details(self):
        values = [e.get() for e in self.entries]
        try:
            return values
        except ValueError as e:
            mb.showerror("Validation error", str(e), parent=self)

    def clear(self):
        for entry in self.entries:
            entry.delete(0, tk.END)

class Update_form(Form_widget):
    def __init__(self, master, title_name, fields, **kwargs):
        super().__init__(master, fields, title_name, **kwargs)
        self.btn_save = tk.Button(self, text = "Save")
        self.btn_delete = tk.Button(self, text = "Delete")
        self.fields = fields
        self.load_details = None

        self.btn_save.pack(side=tk.RIGHT, ipadx=5, padx=5, pady=5)
        self.btn_delete.pack(side=tk.RIGHT, ipadx=5, padx=5, pady=5)

    def bind_save(self, callback):
        print('bind_save')
        self.btn_save.config(command=callback)

    def bind_delete(self, callback):
        self.btn_delete.config(command=callback)

class Data_list_widget(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master)
        self.lb = tk.Listbox(self, **kwargs)
        scroll = tk.Scrollbar(self, command = self.lb.yview)

        self.lb.config(yscrollcommand = scroll.set)
        scroll.pack( side = tk.RIGHT, fill = tk.Y)
        self.lb.pack(side = tk.LEFT,  fill = tk.BOTH, expand=1)

        self.insert = None

    def delete(self, index):
        self.lb.delete(index, index)

    def update(self, data, index):
        self.delete(index)
        self.insert(data, index)

    def bind_doble_click(self, callback):
        handler = lambda _: callback(self.lb.curselection()[0])
        self.lb.bind("<Double-Button-1>", handler)

class Add_new_record(tk.Toplevel):
    def __init__(self, parent, title_name, fields ):
        super().__init__(parent)
        self.new_record = None
        self.parent = parent
        self.form = Form_widget(self, fields, title_name )
        self.btn_add = tk.Button(self, text = "Confirm", command = self.confirm )
        self.form.pack(padx = 10, pady = 10 )
        self.btn_add.pack(pady = 10 )

    def confirm(self):
        print('confirm')
        self.new_record = self.form.get_details()
        if self.new_record:
            print('destroy')
            self.parent.focus_set()
            self.destroy()
            

    def show(self):
        print('show')
        self.grab_set()
        self.wait_window()
        return self.new_record

class Costumer_widget(tk.Frame):
    def __init__(self, parent, title_name):
        super().__init__(parent)
        self.title = title_name
        self.selection = None
        self.list = Data_list_widget(self, height = 15, width=30)
        self.list.insert = self.insert
        self.form = Update_form(self, title_name,("eiginnafn", "eftirnafn", "kt", "símanúmer", "netfang","heimilisfang","postnumer"))

        self.form.load_details = self.load_details
        self.costumers = self.load_costumers()
        self.btn_new = tk.Button(self, text = "Add new " + title_name, command = self.add_costumer)
        for costumer in self.costumers:
            self.list.insert(costumer)
        self.list.pack(side=tk.LEFT, padx = 10, pady = 10)
        self.form.pack(side=tk.LEFT, padx = 10, pady = 10)   
        self.btn_new.pack(side=tk.BOTTOM, pady = 5)
        
        self.list.bind_doble_click(self.show_costumers)  
        self.form.bind_save(self.update_costumer)
        self.form.bind_delete(self.delete)

    def add_costumer(self):
        new_costumer = Add_new_record(self,
        self.title,("eiginnafn", "eftirnafn", "kt", "símanúmer", "netfang","heimilisfang","postnumer"))
        new_costumer.load_details = self.load_details
        values = new_costumer.show()
        added_new_costumer = get_db_data.bua_til_vidskiptavin( 
            eiginnafn = values[0],  
            eftirnafn = values[1], 
            kt = values[2], 
            simi = values[3], 
            netfang = values[4], 
            heimilisfang = values[5], 
            postnumer = values[6]  
            )
        self.costumers.append(added_new_costumer)
        self.list.insert(added_new_costumer)

    def update_costumer(self):
        if self.selection is None:
            return
        values = self.form.get_details()
        self.costumers = self.load_costumers()
        
        if values:
            costumer = get_db_data.breyta_viðskiptavin( 
                values[0], # eiginnafn 
                values[1], # eftirnafn
                values[2], # kt
                values[3], # Símanúmer
                values[4], # Netfang
                values[5], # Heimilisfang
                values[6]  # póstnúmer
                )
            self.costumers[self.selection]
            self.costumers = self.load_costumers()
            self.list.update(costumer, self.selection)

    def delete(self):
        print('check delete function through costumer id', self.costumers[self.selection].id )
        get_db_data.delete_costumer( self.costumers[self.selection].id )
        self.list.lb.delete(self.selection)

    def load_costumers(self):
        return get_db_data.birta_alla_vidskiptavini()
    
    def show_costumers(self, index):
        self.selection = index
        self.costumers = self.load_costumers()
        costumer = self.costumers[index]
        self.form.load_details(costumer)

    def insert(self, costumer, index = tk.END):
        text = "{}, {}".format(costumer.eiginnafn, costumer.eftirnafn)
        print(text)
        self.list.lb.insert(index, text)
    
    def load_details(self, costumer):
        values = (
            costumer.eiginnafn, 
            costumer.eftirnafn,
            costumer.kt, 
            costumer.símanúmer[0].símanúmer, 
            costumer.netföng[0].netfang, 
            costumer.heimilisföng[0].heimilisfang, 
            costumer.heimilisföng[0].póstnúmer)
        for entry, value in zip(self.form.entries, values):
            entry.delete(0, tk.END)
            entry.insert(0, value)

class Manufacturer_widget(tk.Frame):
    def __init__(self, parent, title_name):
        super().__init__(parent)
        self.title = title_name
        self.selection = None
        self.list = Data_list_widget(self, height = 6)
        self.list.insert = self.insert
        self.form = Update_form(self, title_name,("Nafn", "Tengiliður forn.", "Tengiliður eftirn.", "símanúmer", "netfang"))

        self.form.load_details = self.load_details
        self.manufacturers = self.load_manufacturers()
        self.btn_new = tk.Button(self, text = "Add new " + title_name, command = self.add_manufacturer)
        for manufacturer in self.manufacturers:
            self.list.insert(manufacturer)
        self.list.pack(side=tk.LEFT, padx = 10, pady = 10)
        self.form.pack(side=tk.LEFT, padx = 10, pady = 10)   
        self.btn_new.pack(side=tk.BOTTOM, pady = 5)
        
        self.list.bind_doble_click(self.show_manufacturers)  
        self.form.bind_save(self.update_manufacturer)
        self.form.bind_delete(self.delete)

    def add_manufacturer(self):
        new_manufacturer = Add_new_record(self,
        self.title,("Nafn", "Tengiliður forn.", "Tengiliður eftirn.", "símanúmer", "netfang"))
        new_manufacturer.load_details = self.load_details
        values = new_manufacturer.show()
        added_new_manufacturer = get_db_data.bua_til_framleiðanda( 
            nafn = values[0], 
            tengiliður_nafn = values[1],
            tengiliður_eftirnafn = values[2], 
            tengiliður_sími = values[3], 
            tengiliður_netfang = values[4],  
            )
        self.manufacturers.append(added_new_manufacturer)
        self.list.insert(added_new_manufacturer)

    def update_manufacturer(self):
        if self.selection is None:
            return
        values = self.form.get_details()
        self.costumers = self.load_manufacturers()
        
        if values:
            manufacturer = get_db_data.breyta_framleiðanda( 
                values[0], # nafn 
                values[1], # tengiliður nafn
                values[2], # tengiliður eftirnafn
                values[3], # Símanúmer
                values[4], # Netfang
                )
            self.manufacturers[self.selection]
            self.manufacturers = self.load_manufacturers()
            self.list.update(manufacturer, self.selection)

    def delete(self):
        print('check delete function through delete_manufacturer id', self.manufacturers[self.selection].id )
        get_db_data.delete_manufacturer( self.manufacturers[self.selection].id )
        self.list.lb.delete(self.selection)

    def load_manufacturers(self):
        return get_db_data.get_framleiðendur()
    
    def show_manufacturers(self, index):
        self.selection = index
        self.manufacturers = self.load_manufacturers()
        manufacturer = self.manufacturers[index]
        self.form.load_details(manufacturer)
        

    def insert(self, manufacturer, index = tk.END):
        text = "{}".format(manufacturer.nafn)
        print('test getting attributes', getattr(manufacturer, 'nafn'))
        self.list.lb.insert(index, text)
    
    def load_details(self, manufacturer):
        values = (
            manufacturer.nafn,
            manufacturer.tengiliðir[0].eiginnafn, 
            manufacturer.tengiliðir[0].eftirnafn,
            manufacturer.tengiliðir[0].símanúmer[0].símanúmer, 
            manufacturer.tengiliðir[0].netföng[0].netfang 
            )
        for entry, value in zip(self.form.entries, values):
            entry.delete(0, tk.END)
            entry.insert(0, value)

class ProductCategory_widget(tk.Frame):
    def __init__(self, parent, title_name):
        super().__init__(parent)
        self.title = title_name
        self.selection = None
        self.list = Data_list_widget(self, height = 6)
        self.list.insert = self.insert
        self.form = Update_form(self, title_name,("Nafn",))

        self.form.load_details = self.load_details
        self.productCategorys = self.load_productCategorys()
        self.btn_new = tk.Button(self, text = "Add new " + title_name, command = self.add_productCategory)
        for productCategory in self.productCategorys:
            self.list.insert(productCategory)
        self.list.pack(side=tk.LEFT, padx = 10, pady = 10)
        self.form.pack(side=tk.LEFT, padx = 10, pady = 10)   
        self.btn_new.pack(side=tk.BOTTOM, pady = 5)
        
        self.list.bind_doble_click(self.show_productCategorys)  
        self.form.bind_save(self.update_productCategory)
        self.form.bind_delete(self.delete)

    def add_productCategory(self):
        new_productCategory = Add_new_record(self, self.title, ("Nafn",) )
        new_productCategory.load_details = self.load_details
        values = new_productCategory.show()
        added_new_productCategory = get_db_data.bua_til_vöruflokk( nafn = values[0])
        self.productCategorys.append(added_new_productCategory)
        self.list.insert(added_new_productCategory)

    def update_productCategory(self):
        if self.selection is None:
            return
        values = self.form.get_details()
        self.productCategorys = self.load_productCategorys()
        
        if values:
            productCategory = get_db_data.breyta_vöruflokk( values[0] )# nafn 
            self.productCategorys[self.selection]
            self.productCategorys = self.load_productCategorys()
            self.list.update(productCategory, self.selection)

    def delete(self):
        print('check delete_productCategory id', self.productCategorys[self.selection].id )
        get_db_data.delete_productCategory( self.productCategorys[self.selection].id )
        self.list.lb.delete(self.selection)


    def load_productCategorys(self):
        return get_db_data.get_productCategories()
    
    def show_productCategorys(self, index):
        self.selection = index
        self.productCategorys = self.load_productCategorys()
        productCategory = self.productCategorys[index]
        self.form.load_details(productCategory)

    def insert(self, productCategory, index = tk.END):
        text = "{}".format(productCategory.nafn)
        print(text)
        self.list.lb.insert(index, text)
    
    def load_details(self, productCategory): 
        values = (productCategory.nafn,)
        for entry, value in zip(self.form.entries, values):
            entry.delete(0, tk.END)
            entry.insert(0, value)

class ProductModel_widget(tk.Frame):
    def __init__(self, parent, title_name):
        super().__init__(parent)
        self.title = title_name
        self.selection = None
        self.popup_manufacturer = popup_menu(self, get_db_data.get_framleiðendur_nafn(),     0, 0, 8, 8)
        self.popupmenu_productCategory = popup_menu(self, get_db_data.get_vöruflokkar(),0, 1, 8, 8)
        self.list = Data_list_widget(self, height = 6)
        self.list.insert = self.insert
        self.form = Update_form(self, title_name,("Nafn",))
        self.form.load_details = self.load_details
        self.productModels = self.load_productModels()
        self.btn_new = tk.Button(self, text = "Add new " + title_name, command = self.add_productModel)
        for productModel in self.productModels:
            self.list.insert(productModel)
        
        self.list.pack(side=tk.LEFT, padx = 10, pady = 10)
        self.form.pack(side=tk.LEFT, padx = 10, pady = 10)   
        self.btn_new.pack(side=tk.BOTTOM, pady = 5)
        
        self.list.bind_doble_click(self.show_productModels)  
        self.form.bind_save(self.update_productModel)
        self.form.bind_delete(self.delete)
        self.popupmenu_productCategory.popup.bind("<<ComboboxSelected>>", self.product_category_popup_callback)

    def add_productModel(self):
        new_productModel = Add_new_record(self,
        self.title, ("Nafn", ))
        new_productModel.load_details = self.load_details
        values = new_productModel.show()
        added_new_productModel = get_db_data.bua_til_vörutegund( 
            values[0], #Nafn
            self.popupmenu_productCategory.popup.get(), # Vöruflokkur
            self.popup_manufacturer.popup.get() # Framleiðandi
            )
        self.productModels.append(added_new_productModel)
        self.list.insert(added_new_productModel)

    def update_productModel(self):
        if self.selection is None:
            return
        values = self.form.get_details()
        self.productModels[self.selection].id
        
        if values:
            print(self.selection)
            productModel = get_db_data.breyta_vörutegund( 
                values[0], # nafn 
                self.popupmenu_productCategory.popup.get(), # Vöruflokkur
                self.popup_manufacturer.popup.get(), # Framleiðandi,
                self.productModels[self.selection].id
            )
            self.productModels[self.selection]
            self.productModels = self.load_productModels()
            self.list.update(productModel, self.selection)
    
    def delete(self):
        print('check productModel id', self.productModels[self.selection].id )
        get_db_data.delete_productModel( self.productModels[self.selection].id )
        self.list.lb.delete(self.selection)


    def load_productModels(self):
        return get_db_data.get_productModels_by_category(self.popupmenu_productCategory.popup.get())
    
    def show_productModels(self, index):
        self.selection = index
        self.productModels = self.load_productModels()
        productModel = self.productModels[index]
        self.form.load_details(productModel)

    def insert(self, productModel, index = tk.END):
        text = "{}".format(productModel.nafn)
        print(text)
        self.list.lb.insert(index, text)
    
    def load_details(self, productModel): 
        values = (productModel.nafn,)
        for entry, value in zip(self.form.entries, values):
            entry.delete(0, tk.END)
            entry.insert(0, value)
    
    def product_category_popup_callback(self, event):
        for productModel in self.productModels:
            self.list.lb.delete(0)
        self.productModels = self.load_productModels()
        for productModel in self.productModels:
            self.list.insert(productModel)
        
class Product_widget(tk.Frame):
    def __init__(self, parent, title_name):
        super().__init__(parent)
        self.title = title_name
        self.selection = None
        self.popupmenu_productCategory = popup_menu(self, get_db_data.get_vöruflokkar(),0, 0, 8, 8)
        self.popupmenu_productModel = popup_menu(self, get_db_data.get_productModels_by_category_nafn(self.popupmenu_productCategory.popup.get()), 0, 1, 8, 8)
        
        self.list = Data_list_widget(self, height = 6)
        self.list.insert = self.insert
        self.form = Update_form(self, title_name,("Nafn", "Verð"))
        self.form.load_details = self.load_details
        self.products = self.load_products()
        self.btn_new = tk.Button(self, text = "Add new " + title_name, command = self.add_product)
        for product in self.products:
            self.list.insert(product)
        

        self.list.pack(side=tk.LEFT, padx = 10, pady = 10)
        self.form.pack(side=tk.LEFT, padx = 10, pady = 10)   
        self.btn_new.pack(side=tk.BOTTOM, pady = 5)
        
        self.list.bind_doble_click(self.show_products)  
        self.form.bind_save(self.update_product)
        self.form.bind_delete(self.delete)
        self.popupmenu_productModel.popup.bind("<<ComboboxSelected>>", self.product_model_popup_callback)
        self.popupmenu_productCategory.popup.bind("<<ComboboxSelected>>", self.product_category_popup_callback)

    def add_product(self):
        new_product = Add_new_record(self,
        self.title, ("Nafn", "Verð" ))
        new_product.load_details = self.load_details
        values = new_product.show()
        print('values', values[0])
        print('values', values[1])
        print('self pop up get', self.popupmenu_productModel.popup.get())
        added_new_product = get_db_data.bua_til_vöru( 
            values[0], #Nafn
            values[1], #verð
            self.popupmenu_productModel.popup.get() # Vörutegund
            )
        self.products.append(added_new_product)
        self.list.insert(added_new_product)

    def update_product(self):
        if self.selection is None:
            return
        values = self.form.get_details()
        self.products[self.selection].id
        
        if values:
            product = get_db_data.breyta_vöru( 
                values[0], # nafn 
                values[1], # Vöruflokkur
                self.popupmenu_productModel.popup.get(), # Vörutegund,
                self.products[self.selection].id
            )
            self.products[self.selection]
            self.products = self.load_products()
            self.list.update(product, self.selection)

    def delete(self):
        print('check product id', self.products[self.selection].id )
        get_db_data.delete_product( self.products[self.selection].id )
        self.list.lb.delete(self.selection)


    def load_products(self):
        return get_db_data.get_products_by_productModel(self.popupmenu_productModel.popup.get())

    def show_products(self, index):
        self.selection = index
        self.products = self.load_products()
        product = self.products[index]
        self.form.load_details(product)

    def insert(self, product, index = tk.END):
        text = "{}".format(product.nafn)
        print(text)
        self.list.lb.insert(index, text)
    
    def load_details(self, product): 
        values = (product.nafn, product.verð)
        for entry, value in zip(self.form.entries, values):
            entry.delete(0, tk.END)
            entry.insert(0, value)
    
    def product_model_popup_callback(self, event):
        for product in self.products:
            self.list.lb.delete(0)
        self.products = self.load_products()
        for product in self.products:
            self.list.insert(product)

    def product_category_popup_callback(self, event):
        self.popupmenu_productModel.popup['values'] = get_db_data.\
            get_productModels_by_category_nafn( self.popupmenu_productCategory.popup.get() )
 
class ExtrasCategory_widget(tk.Frame):
    def __init__(self, parent, title_name):
        super().__init__(parent)
        self.title = title_name
        self.selection = None
        self.popupmenu_productCategory = popup_menu(self, get_db_data.get_vöruflokkar(),0, 0, 8, 8)
        self.list = Data_list_widget(self, height = 6)
        self.list.insert = self.insert
        self.form = Update_form(self, title_name,("Nafn",))
        self.form.load_details = self.load_details
        self.ExtrasCategorys = self.load_ExtrasCategorys()
        self.btn_new = tk.Button(self, text = "Add new " + title_name, command = self.add_ExtrasCategory)
        for ExtrasCategory in self.ExtrasCategorys:
            self.list.insert(ExtrasCategory)
        
        self.list.pack(side=tk.LEFT, padx = 10, pady = 10)
        self.form.pack(side=tk.LEFT, padx = 10, pady = 10)   
        self.btn_new.pack(side=tk.BOTTOM, pady = 5)
        
        self.list.bind_doble_click(self.show_ExtrasCategorys)  
        self.form.bind_save(self.update_ExtrasCategory)
        self.form.bind_delete(self.delete)
        self.popupmenu_productCategory.popup.bind("<<ComboboxSelected>>", self.product_category_popup_callback)

    def add_ExtrasCategory(self):
        new_ExtrasCategory = Add_new_record( self, self.title, ("Nafn", ))
        new_ExtrasCategory.load_details = self.load_details
        values = new_ExtrasCategory.show()
        added_new_ExtrasCategory = get_db_data.bua_til_aukahlut_tegund( 
            values[0], #Nafn
            self.popupmenu_productCategory.popup.get() # Vöruflokkur
            )
        self.ExtrasCategorys.append(added_new_ExtrasCategory)
        self.list.insert(added_new_ExtrasCategory)

    def update_ExtrasCategory(self):
        if self.selection is None:
            return
        values = self.form.get_details()
        self.ExtrasCategorys[self.selection].id
        
        if values:
            print(self.selection)
            ExtrasCategory = get_db_data.breyta_aukahlut_tegund( 
                values[0], # nafn 
                self.popupmenu_productCategory.popup.get(), # Vöruflokkur
                self.ExtrasCategorys[self.selection].id
            )
            self.ExtrasCategorys[self.selection]
            self.ExtrasCategorys = self.load_ExtrasCategorys()
            self.list.update(ExtrasCategory, self.selection)
    
    def delete(self):
        print('check ExtrasCategory id', self.ExtrasCategorys[self.selection].id )
        get_db_data.delete_extrasCategory( self.ExtrasCategorys[self.selection].id )
        self.list.lb.delete(self.selection)


    def load_ExtrasCategorys(self):
        return get_db_data.get_ExtrasCategorys_by_category(self.popupmenu_productCategory.popup.get())
    
    def show_ExtrasCategorys(self, index):
        self.selection = index
        self.ExtrasCategorys = self.load_ExtrasCategorys()
        ExtrasCategory = self.ExtrasCategorys[index]
        self.form.load_details(ExtrasCategory)

    def insert(self, ExtrasCategory, index = tk.END):
        text = "{}".format(ExtrasCategory.nafn)
        print(text)
        self.list.lb.insert(index, text)
    
    def load_details(self, ExtrasCategory): 
        values = (ExtrasCategory.nafn,)
        for entry, value in zip(self.form.entries, values):
            entry.delete(0, tk.END)
            entry.insert(0, value)
    
    def product_category_popup_callback(self, event):
        for ExtrasCategory in self.ExtrasCategorys:
            self.list.lb.delete(0)
        self.ExtrasCategorys = self.load_ExtrasCategorys()
        for ExtrasCategory in self.ExtrasCategorys:
            self.list.insert(ExtrasCategory)

class Extras_widget(tk.Frame):
    def __init__(self, parent, title_name):
        super().__init__(parent)
        self.title = title_name
        self.selection = None
        self.popupmenu_productCategory = popup_menu(self, get_db_data.get_vöruflokkar(),0, 1, 8, 8)
        self.popupmenu_extraCategory = popup_menu(self, 
            get_db_data.get_ExtrasCategorys_by_category_names(self.popupmenu_productCategory.popup.get()),0, 0, 8, 8)
        
        
        self.list = Data_list_widget(self, height = 6, width=55)
        self.list.insert = self.insert
        self.form = Update_form(self, title_name,("Lýsing", "Verð"))
        self.form.load_details = self.load_details
        self.extras = self.load_extras()
        self.btn_new = tk.Button(self, text = "Add new " + title_name, command = self.add_extra)
        for extra in self.extras:
            self.list.insert(extra)
        

        self.list.pack(side=tk.LEFT, padx = 10, pady = 10)
        self.form.pack(side=tk.LEFT, padx = 10, pady = 10)   
        self.btn_new.pack(side=tk.BOTTOM, pady = 5)
        
        self.list.bind_doble_click(self.show_extras)  
        self.form.bind_save(self.update_extra)
        self.form.bind_delete(self.delete)
        self.popupmenu_productCategory.popup.bind("<<ComboboxSelected>>", self.product_category_popup_callback)
        self.popupmenu_extraCategory.popup.bind("<<ComboboxSelected>>", self.popupmenu_extraCategory_callback)
    
    def add_extra(self):
        new_extra = Add_new_record(self, self.title, ("Lýsing", "Verð" ))
        new_extra.load_details = self.load_details
        values = new_extra.show()

        added_new_extra = get_db_data.bua_til_aukahlut( 
            values[0], #Nafn
            values[1], #verð
            self.popupmenu_extraCategory.popup.get() # Aukahlutur tegund
            )
        self.extras.append(added_new_extra)
        self.list.insert(added_new_extra)

    def update_extra(self):
        if self.selection is None:
            return
        values = self.form.get_details()
        self.extras[self.selection].id
        
        if values:
            extra = get_db_data.breyta_aukahlut( 
                values[0], # nafn 
                values[1], # Vöruflokkur
                self.popupmenu_extraCategory.popup.get(), # Aukahlutur tegund
                self.extras[self.selection].id
            )
            self.extras[self.selection]
            self.extras = self.load_extras()
            self.list.update(extra, self.selection)

    def delete(self):
        print('check ExtrasCategory id', self.extras[self.selection].id )
        get_db_data.delete_extras( self.extras[self.selection].id )
        self.list.lb.delete(self.selection)


    def load_extras(self):
        return get_db_data.get_extras_by_extraCategory_name(self.popupmenu_extraCategory.popup.get())

    def show_extras(self, index):
        self.selection = index
        self.extras = self.load_extras()
        extra = self.extras[index]
        self.form.load_details(extra)

    def insert(self, extra, index = tk.END):
        text = "{}".format(extra.lýsing)
        print(text)
        self.list.lb.insert(index, text)
    
    def load_details(self, extra): 
        values = (extra.lýsing, extra.verð)
        for entry, value in zip(self.form.entries, values):
            entry.delete(0, tk.END)
            entry.insert(0, value)
    
    def popupmenu_extraCategory_callback(self, event):
        for extra in self.extras:
            self.list.lb.delete(0)
        self.extras = self.load_extras()
        for extra in self.extras:
            self.list.insert(extra)
    
    def product_category_popup_callback(self, event):
        self.popupmenu_extraCategory.popup['values'] = get_db_data.\
            get_ExtrasCategorys_by_category_names(self.popupmenu_productCategory.popup.get())

class Orders_widget(tk.Frame):
    def __init__(self, parent, title_name):
        super().__init__(parent)
        self.title = title_name
        self.selection = None
        self.selection_itemOrder = None
        self.costumer_order = None
        self.list = Data_list_widget(self, height = 6)
        self.list.insert = self.insert
        self.costumers = self.load_costumers()
        
        for costumer in self.costumers:
            self.list.insert(costumer)
        
        self.list.grid(column=0,row=0, padx = 10, pady = 10)  
        self.list.bind_doble_click(self.get_costumers) 
        

        self.category = get_db_data.get_vöruflokkar()
        self.model =   ['Veldu Vöruflokk']
        self.product = ['Veldu vörumódel']
        self.order = [ ]
        self.added = None
        self.div_1 = tk.LabelFrame(self)
        self.div_1.grid(column=0,row=4)
        self.popupmenu_productCategory = menu(self.div_1, self.category, 0, 4, 8, 8, 25)
        self.popupmenu_productModel    = menu(self.div_1, self.model,    1, 4, 8, 8, 25) 
        self.popupmenu_product         = menu(self.div_1, self.product,  0, 6, 4, 8, 25)
        self.addProduct_but = butt(self.div_1,'Bæta vöru við pöntun', 25, 1, 6, self.add_product_callback, 2, 2)
        self.extra_cat = get_db_data.get_ExtrasCategorys_by_category\
            (self.popupmenu_productCategory.popup.get())
       
        self.popupmenu_extraCategory = menu(self, self.get_names( self.extra_cat ), 0, 8, 8, 8, 50)

        self.extras = get_db_data.get_extras_by_extraCategory_name(self.popupmenu_extraCategory.popup.get())
        self.popupmenu_extras = menu(self, self.get_description( self.extras ), 0, 9, 4, 8, 50)
        self.addExtras_but = butt(self,'Bæta aukahlut við pöntun',25,0,10, self.addExtras_callback,2,2)

        self.ordered_items = Data_list_widget(self, height = 7, width=60)
        self.ordered_items.grid(column=0,row=11, padx = 10, pady = 10)
        self.ordered_items.insert = self.insert_ordered_items
        self.ordered_items.bind_doble_click(self.get_order_item)

        self.deleteFromOrder = butt(self,'Eyða hlut úr pöntun', 20, 1, 11, self.delete_from_order,2,2)
        self.save_order = butt(self,'Vista Pöntun', 20, 2, 11, self.save_order, 2,2)
        #self.popupmenu_product =         menu(self, self.product,  0, 7, 8, 8, 50)
         
        self.popupmenu_productCategory.popup.bind( "<<ComboboxSelected>>", self.product_category_popup_callback)
        self.popupmenu_productModel.popup.bind(    "<<ComboboxSelected>>", self.product_model_popup_callback)
        self.popupmenu_product.popup.bind(         "<<ComboboxSelected>>", self.product_popup_callback)
        self.popupmenu_extraCategory.popup.bind(   "<<ComboboxSelected>>", self.extraCategory_popup_callback)

    def add_product_callback(self):
        self.costumer_order.vörur.append( self.product[ self.popupmenu_product.popup.current() ] )
        self.order.append( self.product[ self.popupmenu_product.popup.current() ] )
        self.insert_ordered_items(self.product[ self.popupmenu_product.popup.current() ] )
        print( self.product[ self.popupmenu_product.popup.current() ] )
        print( self.order )

    def addExtras_callback(self):
        extra = self.extras[ self.popupmenu_extras.popup.current()]
        text = "Aukahlutur: {}.    Verð:  {}".format(extra.lýsing, extra.verð)
        self.ordered_items.lb.insert(tk.END, text)

    def product_category_popup_callback(self, event):
        self.model = get_db_data.get_productModels_by_category(self.popupmenu_productCategory.popup.get())
        self.popupmenu_productModel.popup['values'] = self.get_names( self.model )
    
    def product_model_popup_callback(self, event):
        self.product = get_db_data.get_products_by_productModel(self.popupmenu_productModel.popup.get())
        self.popupmenu_product.popup['values'] = self.get_names( self.product)

    def extraCategory_popup_callback(self, event):
        self.extras = get_db_data.get_extras_by_extraCategory_name(self.popupmenu_extraCategory.popup.get())
        self.popupmenu_extras.popup['values'] = self.get_description( self.extras )
        """
        self.added = get_db_data.get_added_extrasToProduct_by_category(added_items, self.popupmenu_extraCategory.popup.get())
        self.popupmenu_added_items.popup['values'] = self.get_description( self.added ) 
        """
    
    def product_popup_callback(self,event):
        print('To Do')

    def load_costumers(self):
        return get_db_data.birta_alla_vidskiptavini()
    
    def get_costumers(self, index):
        self.selection = index
        self.costumers = self.load_costumers()
        self.costumer_order = self.costumers[index]
        print('costumer in load',costumer.vörur)
        #self.form.load_details(costumer)



    def get_order_item(self, index):
        self.selection_itemOrder = index
        #self.costumers = self.load_costumers()
        #costumer = self.costumers[index]
        #print('costumer in load',costumer)
        #self.form.load_details(costumer)

    def delete_from_order(self):
        self.order.pop( self.ordered_items.lb.curselection()[0] )
        self.ordered_items.lb.delete( self.ordered_items.lb.curselection()[0] )
        self.costumer_order.vörur.pop( self.ordered_items.lb.curselection()[0] )
        print(self.ordered_items.lb.curselection()[0] )

    def insert(self, costumer, index = tk.END):
        text = "{}, {}".format(costumer.eiginnafn, costumer.eftirnafn)
        self.list.lb.insert(index, text)

    def insert_ordered_items(self, items, index = tk.END):
        text = "Tegund: {}.  Nafn: {}.   Verð í evrum:   {} ".format(items.vörutegundir.nafn, items.nafn, items.verð)
        self.ordered_items.lb.insert(index, text)
    

    def save_order(self):
        get_db_data.make_order( self.costumer_order)

    def load_details(self, costumer):
        values = (
            costumer.eiginnafn, 
            costumer.eftirnafn,
            costumer.kt, 
            costumer.símanúmer[0].símanúmer, 
            costumer.netföng[0].netfang, 
            costumer.heimilisföng[0].heimilisfang, 
            costumer.heimilisföng[0].póstnúmer)
        for entry, value in zip(self.form.entries, values):
            entry.delete(0, tk.END)
            entry.insert(0, value)
    
    def get_names(self, input_data):
        out = [item.nafn for item in input_data]
        print( out )
        return out
    
    def get_description(self, input_data):
        out = [item.lýsing for item in input_data]
        print( out )
        return out

#Widget sem bætir Aukahlut við vöru eða aftengir aukahlut frá vöru
class ExtrasToProducts(tk.Frame):
    def __init__(self, parent, title_name):
        super().__init__(parent)
        
        self.title = title_name
        self.category = get_db_data.get_vöruflokkar()
        self.model = ['Veldu Vöruflokk']
        self.product = ['Veldu vörumódel']
        self.added = None
        self.popupmenu_productCategory = popup_menu(self, self.category,0, 0, 8, 8)
        self.popupmenu_productModel = popup_menu(self, self.model, 0, 1, 8, 8) 
        self.popupmenu_product = popup_menu(self, self.product, 0, 2, 8, 8)
        
        self.extra_cat = get_db_data.get_ExtrasCategorys_by_category(self.popupmenu_productCategory.popup.get())
       
        self.popupmenu_extraCategory = popup_menu(self, self.get_names( self.extra_cat ), 0, 3, 8, 8)
        self.extras = get_db_data.get_extras_by_extraCategory_name(self.popupmenu_extraCategory.popup.get())
        self.popupmenu_extras = popup_menu(self, self.get_description( self.extras ), 0, 4, 8, 8)
        self.popupmenu_added_items = popup_menu(self, ['Added items'], 0, 4, 8, 8)

        self.add_but = button(self,   'Bæta aukahlut við vöru',    20, 'left', self.addToProduct_callback,8,8)
        self.remove_but = button(self,'Aftengja aukahlut frá vöru',20, 'left', self.removeFromProduct_callback,8,8)
  
        self.popupmenu_added_items.popup.configure(width=60)
        self.popupmenu_extras.popup.configure(width=60)

        self.popupmenu_productCategory.popup.bind( "<<ComboboxSelected>>", self.product_category_popup_callback)
        self.popupmenu_productModel.popup.bind(    "<<ComboboxSelected>>", self.product_model_popup_callback)
        self.popupmenu_product.popup.bind(         "<<ComboboxSelected>>", self.product_popup_callback)
        self.popupmenu_extraCategory.popup.bind(   "<<ComboboxSelected>>", self.extraCategory_popup_callback)
        self.popupmenu_extras.popup.bind(          "<<ComboboxSelected>>", self.extras_popup_callback)
   
    def product_category_popup_callback(self, event):
        self.model = get_db_data.get_productModels_by_category(self.popupmenu_productCategory.popup.get())
        self.popupmenu_productModel.popup['values'] = self.get_names( self.model )

    def product_model_popup_callback(self, event):
        self.product = get_db_data.get_products_by_productModel(self.popupmenu_productModel.popup.get())
        print(self.product)
        self.popupmenu_product.popup['values'] = self.get_names( self.product)
    
    def product_popup_callback(self, event):
        added_items = self.product[ self.popupmenu_product.popup.current() ].aukahlutir
        added_by_cat = get_db_data.get_added_extrasToProduct_by_category(added_items, self.popupmenu_extraCategory.popup.get())
        self.popupmenu_added_items.popup['values'] = self.get_description( added_by_cat )
    
    def extraCategory_popup_callback(self, event):
        self.extras = get_db_data.get_extras_by_extraCategory_name(self.popupmenu_extraCategory.popup.get())
        self.popupmenu_extras.popup['values'] = self.get_description( self.extras )
        added_items = self.product[ self.popupmenu_product.popup.current() ].aukahlutir
        self.added = get_db_data.get_added_extrasToProduct_by_category(added_items, self.popupmenu_extraCategory.popup.get())
        self.popupmenu_added_items.popup['values'] = self.get_description( self.added ) 

    def extras_popup_callback(self, event):
        print(self.extras[ self.popupmenu_extras.popup.current() ])

    def addToProduct_callback(self):
        get_db_data.add_extras_to_product( 
            self.product[ self.popupmenu_product.popup.current() ], #Vara
            self.extras[ self.popupmenu_extras.popup.current() ] #Aukahlutur
            )
        added_items = self.product[ self.popupmenu_product.popup.current() ].aukahlutir
        self.added = get_db_data.get_added_extrasToProduct_by_category\
            (added_items, self.popupmenu_extraCategory.popup.get())
        self.popupmenu_added_items.popup['values'] = self.get_description( self.added )
    
    def removeFromProduct_callback(self):
        get_db_data.remove_extras_from_product(
            self.product[ self.popupmenu_product.popup.current() ], #Vara
            self.added[ self.popupmenu_added_items.popup.current() ] #Aukahlutur
        )
        added_items = self.product[ self.popupmenu_product.popup.current() ].aukahlutir
        self.added = get_db_data.get_added_extrasToProduct_by_category\
            (added_items, self.popupmenu_extraCategory.popup.get())
        self.popupmenu_added_items.popup['values'] = self.get_description( self.added )
    
    def get_names(self, input_data):
        out = [item.nafn for item in input_data]
        print( out )
        return out
    
    def get_description(self, input_data):
        out = [item.lýsing for item in input_data]
        print( out )
        return out









