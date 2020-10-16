import tkinter as tk
from tkinter import ttk
from tkinter import font as tkFont
import hobby_query_funcs as get_db_data
import calc_functions as calc

############################ CheckBox Class og functions fyrir aukahluti  Hobby útreikningar 
class aukahlutir_widget():
    def __init__(self, main_frame):
        self.aukahlutir = []
        self.aukahlutir_buttons(main_frame)

    class checkclass():
            def __init__(self, master, verð, text):
                self.verð = verð
                self.texti = text + ' -- Verð eu: ' + str(verð)
                self.hidden = True
                self.var = tk.IntVar()
                self.c = tk.Checkbutton(
                    master, 
                    text = self.texti,
                    variable = self.var,
                    command = self.cb)
            def cb(self):
                print( self.var.get())
                print( self.texti)

    def aukahlutir_callback(self, index):
            #global aukahlutir
            print(index)
            for item in self.aukahlutir:
                for i in item:
                    i.hidden = True
                    i.c.grid_remove()
                    i.c.master.grid_remove()
            for item in self.aukahlutir[index]:
                if(item.hidden == True):
                    item.hidden = False
                    item.c.grid()
                    item.c.master.grid(column=0, row=7)
    

    def sum_aukahlutir(self, array):
        tmp_sum = 0
        for items in array:
            for i in items:
                if(i.var.get() == 1):
                    tmp_sum = i.verð + tmp_sum
        return tmp_sum

    def aukahlutir_func(self, frame, column, get_price, get_lysing, aukahlutir_for_hjolhysi_array):
        tmp_array = []
        i = 0 # Fer yfir aukahluti á listanum sem eiga við tiltekna týpu af hjólhýsi
        k = 0 # þarf k fyrir checkbox sem búin verða til út frá fjölda aukahluta sem tilketið hljólhýsi getur tekið
        print(aukahlutir_for_hjolhysi_array)
        for n in aukahlutir_for_hjolhysi_array:
            if(n==1):
                tmp_array.append( self.checkclass(frame, get_price[i], get_lysing[i]))
                tmp_array[k].c.grid(column = column, row=6 + i)
                tmp_array[k].c.grid_remove()
                k += 1
            i +=1
        return tmp_array 

    #frame hjolhysi_tab
    def aukahlutir_checkbox_creation(self, main_frame, id, attribute, col, row):
        frame = tk.LabelFrame(main_frame, text = str(attribute) )
        frame.option_add("*Font", "helvetica 18")
        frame.grid( column = col, row = row)
        aukahlutir_array = list(map(int, getattr( get_db_data.get_aukahlutir_by_hjolhysi_id(id), attribute).split(' ')))
        return self.aukahlutir_func(frame, col, get_db_data.get_price_aukahlutir_by_tegund( str(attribute) ), get_db_data.get_lysing_aukahlutir_by_tegund( str(attribute) ), aukahlutir_array)

    def array_of_checkboxes(self, main_frame, nafn, flokkur):
        tmp_aukahlutir_tegundir = get_db_data.get_aukahlutir_tegund()
        tmp_arr = []
        i = 0
        for items in tmp_aukahlutir_tegundir:
            tmp_arr.append(
                self.aukahlutir_checkbox_creation( main_frame,get_db_data.get_hjolhysi_id_by_name_flokkur( nafn, flokkur ), items, 0 , 7))
            i += 1
        return tmp_arr

    #frame hjolhysi
    # Aukahlutir buttons
    def aukahlutir_buttons(self, main_frame):
        tmp_array = []
        aukahlutir_frame = tk.LabelFrame(main_frame,text = "Aukahlutir")
        aukahlutir_frame.grid(column=0,row=6)
        aukahlutir_frame.grid_configure(padx=8,pady=8)
        i = 0
        for items in get_db_data.get_aukahlutir_tegund():
            tmp_array.append(tk.Button( 
                aukahlutir_frame, 
                text = items, 
                command = lambda arg=i: self.aukahlutir_callback(  arg ))) 
            if(i<7):      
                tmp_array[i].grid(column=0 + i, row = 0)
                tmp_array[i].grid_configure(padx=4,pady=4)

            else:
                tmp_array[i].grid(column=0 + i - 7, row = 1)
                tmp_array[i].grid_configure(padx=4,pady=4)
            i += 1 
        return tmp_array

    def clear_aukahlutir(self):
        for item in self.aukahlutir:
            for i in item:
                i.c.destroy()
                i.c.master.destroy()

class text_box_int():
    def __init__(self, main_frame, text, label_col, label_row, tbox_col, tbox_row, x, y):
        self.value = tk.IntVar()
        self.frame = main_frame
        self.text = text
        label_frame = tk.Label( self.frame, text = self.text)
        label_frame.grid( column = label_col, row = label_row)
        label_frame.grid_configure( padx = x, pady = y)
        self.textbox = ttk.Entry( self.frame, width=12, textvariable = self.value)
        self.textbox.grid( column = tbox_col, row = tbox_row )

class text_box_string():
    def __init__(self, main_frame, text, label_col, label_row, tbox_col, tbox_row, x, y):
        self.value = tk.StringVar()
        self.frame = main_frame
        self.text = text
        self.label_frame = tk.Label( self.frame, text = self.text)
        self.label_frame.grid( column = label_col, row = label_row)
        self.label_frame.grid_configure( padx = x, pady = y)
        self.textbox = ttk.Entry( self.frame, width=12, textvariable = self.value)
        self.textbox.grid( column = tbox_col, row = tbox_row )

class button():
    def __init__(self, frame, text, width, col, row, command, x, y):
        self.frame = frame
        self.width = width
        self.command = command
        self.but = tk.Button(frame, text = text, width=width, command = self.command)
        self.but.grid_configure( padx = x, pady = y)
        self.but.grid( column=col, row=row )


class popup_menu():
    def __init__(self, main_frame, values, col, row, x, y):
        self.value = tk.StringVar()
        self.values = values
        self.current = 0
        self.popup = ttk.Combobox( main_frame, width = 10, height = 25, textvariable = self.value, state='readonly')
        self.popup['values'] = self.values
        self.popup.grid( column = col, row = row )
        self.popup.grid_configure( padx = x, pady = y )
        self.popup.current(self.current)

class velja_hjolhysi():
    def cat_callback(self,event):
            self.type.popup['values'] = get_db_data.get_all_hjolhysi_by_flokkar(self.cat.popup.get())
    def type_callback(self,event):
        get_price = get_db_data.get_hjolhysi_price_by_name_flokkur(self.type.popup.get(), self.cat.popup.get())
        self.verd_eu.textbox.delete(0, 'end')
        self.verd_eu.textbox.insert(0, get_db_data.get_hjolhysi_price_by_name_flokkur(self.type.popup.get(), self.cat.popup.get())) 
        self.lista_verd_eu.textbox.delete(0, 'end')
        self.fob_verd_eu.textbox.delete(0, 'end')
        self.verd_kr.textbox.delete(0, 'end')
        self.cif_verd_kr.textbox.delete(0, 'end')
        self.tollur_verd_kr.textbox.delete(0, 'end')
        self.vsk.textbox.delete(0, 'end')
        self.til_landsins.textbox.delete(0, 'end')
        self.lista_verd_eu.textbox.insert(0, calc.format_verð( calc.lista_verd(   get_price)) )
        self.fob_verd_eu.textbox.insert(0,   calc.format_verð( calc.fob_verd(     get_price) ) )
        self.verd_kr.textbox.insert(0,       calc.format_verð( calc.verd_kronur(  get_price, self.gengi.value.get()) ) )
        self.cif_verd_kr.textbox.insert(0,   calc.format_verð( calc.cif_verd(     get_price, self.gengi.value.get(), self.frakt.value.get()) ) )
        self.tollur_verd_kr.textbox.insert(0,calc.format_verð( calc.tollur_13(    get_price, self.gengi.value.get(), self.frakt.value.get()) ) )
        self.vsk.textbox.insert(0,           calc.format_verð( calc.vsk(          get_price, self.gengi.value.get(), self.frakt.value.get()) ) )
        self.til_landsins.textbox.insert(0,  calc.format_verð( calc.til_landsins( get_price, self.gengi.value.get(), self.frakt.value.get())) ) 
        self.aukahlutir_widget.clear_aukahlutir()
        self.aukahlutir_widget.aukahlutir = self.aukahlutir_widget.array_of_checkboxes(self.checkboxframe, self.type.popup.get(), self.cat.popup.get())
        self.aukahlutir_samtalsverd.textbox.delete(0, 'end')
        self.heildarverd_med_ollu.textbox.delete(0, 'end')

    #Reikna summu aukahluta
    def reikna_aukahluti_action(self):
        get_price = get_db_data.get_hjolhysi_price_by_name_flokkur(self.type.popup.get(), self.cat.popup.get())
        til_landsins = calc.til_landsins( get_price, self.gengi.value.get(), self.frakt.value.get())
        aukahlutir_heildarverð = self.aukahlutir_widget.sum_aukahlutir(self.aukahlutir_widget.aukahlutir )
        print(aukahlutir_heildarverð)
        aukahlutir_verð_isk = aukahlutir_heildarverð * self.gengi.value.get()
        print(aukahlutir_verð_isk)
        self.aukahlutir_samtalsverd.textbox.delete(0, 'end')
        self.heildarverd_med_ollu.textbox.delete(0, 'end')
        self.aukahlutir_samtalsverd.textbox.insert(0, calc.format_verð(   aukahlutir_verð_isk ))
        self.heildarverd_med_ollu.value.set( calc.format_verð( til_landsins + self.thjonustu_gjald.value.get() + aukahlutir_verð_isk  ) )
        print('Verð í krónum: ', aukahlutir_verð_isk)
    
    def __init__(self, main_frame, parent_frame, top, root):
        self.checkboxframe = parent_frame
        self.gengi = text_box_int( top, 'Gengi', label_col=0, label_row=0, tbox_col=0, tbox_row=1, x=8, y=8)
        self.frakt = text_box_int( top, 'Frakt', label_col=1, label_row=0, tbox_col=1, tbox_row=1, x=8, y=8)
        self.thjonustu_gjald = text_box_int( top, 'Þjónustugjald', label_col=2, label_row=0, tbox_col=2, tbox_row=1, x=8, y=8)
        self.cat  = popup_menu( main_frame, values = get_db_data.get_flokkar(), col = 0, row = 0, x = 8, y = 8)
        self.cat.popup.bind("<<ComboboxSelected>>", self.cat_callback)
        self.type = popup_menu( main_frame, values = ("Hjólhýsi"), col =  1, row = 0, x = 8, y = 8 )
        self.type.popup.bind("<<ComboboxSelected>>", self.type_callback)
        self.verd_eu = text_box_int( main_frame,'Verð í evrum',             label_col=2, label_row=0, tbox_col=3, tbox_row=0, x=8, y=8)
        self.lista_verd_eu = text_box_int( main_frame, 'Lisaverð eu',       label_col=0, label_row=1, tbox_col=0, tbox_row=2, x=8, y=8)
        self.fob_verd_eu = text_box_int( main_frame,'Fob verð eu',          label_col=1, label_row=1, tbox_col=1, tbox_row=2, x=8, y=8)
        self.verd_kr = text_box_int( main_frame, 'Verð í krónum',           label_col=2, label_row=1, tbox_col=2, tbox_row=2, x=8, y=8)
        self.cif_verd_kr = text_box_int( main_frame, 'Cif verð',            label_col=3, label_row=1, tbox_col=3, tbox_row=2, x=8, y=8)
        self.tollur_verd_kr = text_box_int( main_frame, '13% Tollur',       label_col=4, label_row=1, tbox_col=4, tbox_row=2, x=8, y=8)
        self.vsk = text_box_int( main_frame,   'VSK',                       label_col=5, label_row=1, tbox_col=5, tbox_row=2, x=8, y=8)
        self.til_landsins = text_box_int( main_frame, 'Verð til landsins',  label_col=6, label_row=1, tbox_col=6, tbox_row=2, x=8, y=8)
        self.gengi.value.set(160)
        self.frakt.value.set(260000)
        self.thjonustu_gjald.value.set(250000)
        self.aukahlutir_widget = aukahlutir_widget(parent_frame)
        self.reikna_verd = tk.Button(root, text = 'Reikna heildarverð með öllu ', command = self.reikna_aukahluti_action)
        self.reikna_verd.grid(column = 0, row = 12, sticky=tk.N)
        self.aukahlutir_samtalsverd = text_box_int( root, 'Heildarverð á Aukahlutum', label_col=0, label_row=13, tbox_col=0, tbox_row=14, x=8, y=8 )
        self.heildarverd_med_ollu = text_box_int( root, 'Heildarverð með þjónustugjaldi og aukahlutum', label_col=0, label_row=15, tbox_col=0, tbox_row=16, x=8, y=8 )
        print(self.gengi.value.get())

class skra_vv():  
    def __init__(self, frame):
        self.eiginnafn = text_box_string( frame,'Eiginnafn',       0,0,0,1,8,8)
        self.eftirnafn = text_box_string( frame,'Eftirnafn',       1,0,1,1,8,8)
        self.kt = text_box_string( frame,'Kennitala',              2,0,2,1,8,8)
        self.simi = text_box_string( frame,'Sími',                 3,0,3,1,8,8)
        self.email = text_box_string( frame,'Email',               4,0,4,1,8,8)
        self.heimilisfang = text_box_string( frame,'Heimilisfang', 5,0,5,1,8,8)
        self.postnumer = text_box_string( frame,'Póstnúmer',       6,0,6,1,8,8)
        self.skra_vv = tk.Button(frame, text = 'Skrá Viðskiptavin ', command = self.skra_vv_callback)
        self.skra_vv.grid_configure( padx = 8, pady = 8)
        self.skra_vv.grid( column=0, row=2 )
    def skra_vv_callback(self):
        get_db_data.bua_til_vidskiptavin(
            self.eiginnafn.value.get(), 
            self.eftirnafn.value.get(), 
            self.kt.value.get(), 
            self.simi.value.get(), 
            self.email.value.get(), 
            self.heimilisfang.value.get(), 
            self.postnumer.value.get() 
        )

class leita_vv():  
    def __init__(self, frame,birta_vv):
        self.birta_leit = birta_vv
        self.eiginnafn = text_box_string( frame,'Eiginnafn',  0,0,0,1,8,8)
        self.skra_vv = tk.Button(frame, text = 'Leita ', command = self.leita_vv_callback)
        self.skra_vv.grid_configure( padx = 8, pady = 8)
        self.skra_vv.grid( column=1, row=1 )
        self.birta = tk.Label(frame)
        self.birta.grid( column=0, row=3 )

    def format_birta_vv(self, array):
        tmp_dict = array[0]
        nafn = tmp_dict['eiginnafn'] +' '+ tmp_dict['eftirnafn']
        kt = tmp_dict['kennitala']
        simi = tmp_dict['sími']
        email = tmp_dict['email']
        heimilisfang = tmp_dict['heimilisfang']
        postnumer = tmp_dict['póstnúmer']    
        return (nafn + ' '+ kt + ' ' + simi + ' ' + email + ' ' + heimilisfang + ' ' + postnumer)  
    
    def leita_vv_callback(self):
        self.birta_leit.nafn.configure(text=(self.format_birta_vv( get_db_data.birta_vidskiptavin( self.eiginnafn.value.get()) )))
        self.birta_leit.breyta_vv.but.grid_remove()
        self.birta_leit.breyta_vv.but.grid(column=0, row=2)


class birta_vv():
    def __init__(self, mainframe):
        self.nafn = tk.Label(mainframe, text='this is a test nigguuzzzzz')
        self.nafn.grid( column=0, row=0 )
        self.kt = tk.Label(mainframe)
        self.kt.grid( column=0, row=1 )
        self.simi = tk.Label(mainframe)
        self.simi.grid( column=0, row=1 )
        self.email = tk.Label(mainframe)
        self.email.grid( column=0, row=2 )
        self.heimilisfang = tk.Label(mainframe)
        self.heimilisfang.grid( column=0, row=2 )
        self.pn = tk.Label(mainframe)
        self.pn.grid( column=0, row=1 )
        self.breyta_vv = button( mainframe, 'Breyta upplýsingum ', 20, 0, 2, self.breyta_vv_callback, 2, 2)
        self.breyta_vv.but.grid_remove()
    
    def breyta_vv_callback(self):
        print('breyta nigguzzz')
       
        

#################### Main window settings
win = tk.Tk()
win.title("Hjólhýsi.com")
# fonts for all widgets
win.option_add("*Font", "helvetica 18")
helv18 = tkFont.Font(family='Helvetica', size=18)
#size
win.columnconfigure(0, weight=1)
win.geometry("1200x900")
win.resizable(False, False)
####################
####################################### Main Window Tabs
tabControl = ttk.Notebook(win)
tabControl.grid(column=0, row=0)

vidskiptavinur_tab = ttk.Frame( tabControl )
hjolhysi_tab = ttk.Frame( tabControl )

tabControl.add(vidskiptavinur_tab, text='Viðskiptavinir')
tabControl.add(hjolhysi_tab, text='Hjólhýsi útreikningar')
####################

#################### Tab Hjólhýsa útreikningar 
stillingar_frame = tk.LabelFrame( hjolhysi_tab, text = "Stillingar")
stillingar_frame.grid(column = 0, row = 0)
stillingar_frame.grid_configure(padx=8,pady=8)

velja_hjolhysi_frame = tk.LabelFrame( hjolhysi_tab, text = "Velja Hjólhýsi")
velja_hjolhysi_frame.grid(column = 0, row = 4)
velja_hjolhysi_frame.grid_configure(padx=8,pady=8)

aukahlutir_frame = tk.LabelFrame( hjolhysi_tab, text = "Velja Aukhluti")
aukahlutir_frame.grid(column = 0, row = 5)
aukahlutir_frame.grid_configure(padx=8,pady=8)

velja_hjolhysi( velja_hjolhysi_frame, aukahlutir_frame, stillingar_frame, hjolhysi_tab )
#####################
#################### Tab Viðskiptavinir Tab
glugga_val = tk.LabelFrame( vidskiptavinur_tab)
glugga_val.grid(column = 0, row = 0)
glugga_val.grid_configure(padx=8,pady=8)
button( glugga_val , 'Skrá Viðskiptavin ', 20, 0, 0, lambda : print('yo'), 2, 2)
button( glugga_val , 'Finna ', 20, 1, 0, lambda : print('yo'), 2, 2)

skra_vv_frame = tk.LabelFrame( vidskiptavinur_tab, text = " Skrá Viðskiptavin ")
skra_vv_frame.grid(column = 0, row = 1)
skra_vv_frame.grid_configure(padx=8,pady=8) 
skra_vv( skra_vv_frame )

leita_vv_frame = tk.LabelFrame( vidskiptavinur_tab, text = " Birta upplýsingar um Viðskiptavin ",width=100)
leita_vv_frame.grid(column = 0, row = 2, sticky='nsew')

birta_leit_vv_frame = tk.LabelFrame( vidskiptavinur_tab, text = " Niðurstöður ",width=100)
birta_leit_vv_frame.grid(column = 0, row = 3, sticky='nsew')

birta_leit = birta_vv( birta_leit_vv_frame )

leita_vv_frame.grid_configure(padx=8,pady=8) 
leita_vv( leita_vv_frame, birta_leit )


win.mainloop()
