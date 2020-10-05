import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
import hobby_query_funcs as get_db_data
import calc_functions as calc
import hobby_gui_callback_funcs as action_funcs

################ Global Vars

gengi = 160
frakt = 260000

################

win = tk.Tk()
win.title("Hobby verð útreikningar")
caravan_frame = ttk.LabelFrame(win,text = "Select Caravan")
caravan_frame.grid(column = 0, row = 0)

################ Callback funcs

#Action fyrir val á flokki
def caravan_cat_callbackFunc(event):
    #print(caravan_cat_pop_up.get())
    if(caravan_cat_pop_up.get() ==  "On Tour"):
        caravan_type_pop_up['values'] = get_db_data.get_all_hjolhysi_by_flokkar("On Tour")
    
    if(caravan_cat_pop_up.get() ==  "Deluxe"):
        caravan_type_pop_up['values'] = get_db_data.get_all_hjolhysi_by_flokkar("Deluxe")
    
    if(caravan_cat_pop_up.get() ==  "Deluxe Edition"):
        caravan_type_pop_up['values'] = get_db_data.get_all_hjolhysi_by_flokkar("Deluxe Edition")
    
    if(caravan_cat_pop_up.get() ==  "Excellent"):
        caravan_type_pop_up['values'] = get_db_data.get_all_hjolhysi_by_flokkar("Excellent")

    if(caravan_cat_pop_up.get() ==  "Prestige"):
        caravan_type_pop_up['values'] = get_db_data.get_all_hjolhysi_by_flokkar("Prestige")
    
    if(caravan_cat_pop_up.get() ==  "Premium"):
        caravan_type_pop_up['values'] = get_db_data.get_all_hjolhysi_by_flokkar("Premium")

#Action fyrir val á hjólhýsi - skilar útreikningum í viðeigandi textaglugga
def caravan_type_callbackFunc(event):
    print(caravan_type_pop_up.get())
    textbox.delete(0, 'end')
    textbox.insert(0, get_db_data.get_hjolhysi_price_by_name_flokkur(caravan_type_pop_up.get(), caravan_cat_pop_up.get())) 
    lista_verd_textbox.delete(0, 'end')
    fob_verd_textbox.delete(0, 'end')
    kronu_verd_textbox.delete(0, 'end')
    cif_verd_textbox.delete(0, 'end')
    tollur_verd_textbox.delete(0, 'end')
    vsk_verd_textbox.delete(0, 'end')
    tillands_verd_textbox.delete(0, 'end')
    lista_verd_textbox.insert(0,   calc.lista_verd(     get_db_data.get_hjolhysi_price_by_name_flokkur(caravan_type_pop_up.get(), caravan_cat_pop_up.get())) )
    fob_verd_textbox.insert(0,     calc.fob_verd(       get_db_data.get_hjolhysi_price_by_name_flokkur(caravan_type_pop_up.get(), caravan_cat_pop_up.get())) )
    kronu_verd_textbox.insert(0,   calc.verd_kronur(    get_db_data.get_hjolhysi_price_by_name_flokkur(caravan_type_pop_up.get(), caravan_cat_pop_up.get()), gengi) )
    cif_verd_textbox.insert(0,     calc.cif_verd(       get_db_data.get_hjolhysi_price_by_name_flokkur(caravan_type_pop_up.get(), caravan_cat_pop_up.get()), gengi, frakt) )
    tollur_verd_textbox.insert(0,  calc.tollur_13(      get_db_data.get_hjolhysi_price_by_name_flokkur(caravan_type_pop_up.get(), caravan_cat_pop_up.get()), gengi, frakt) )
    vsk_verd_textbox.insert(0,     calc.vsk(            get_db_data.get_hjolhysi_price_by_name_flokkur(caravan_type_pop_up.get(), caravan_cat_pop_up.get()), gengi, frakt) )
    tillands_verd_textbox.insert(0,calc.til_landsins(   get_db_data.get_hjolhysi_price_by_name_flokkur(caravan_type_pop_up.get(), caravan_cat_pop_up.get()), gengi, frakt) )
   
################################# Pop Up Menus

#Pop up menu Velja hjólhýsaflokk
caravan_cat = tk.StringVar()
caravan_cat_pop_up = ttk.Combobox(caravan_frame,width=12,textvariable=caravan_cat, state='readonly')
caravan_cat_pop_up['values'] = get_db_data.get_flokkar()
caravan_cat_pop_up.grid(column=0,row=0)
caravan_cat_pop_up.current(0)
#Bindings fyrir Pop up menu Velja hjólhýsaflokk
caravan_cat_pop_up.bind("<<ComboboxSelected>>", caravan_cat_callbackFunc)

#Pop up menu Velja hjólhýsi
caravan_type = tk.StringVar()
caravan_type_pop_up = ttk.Combobox(caravan_frame,width=12,textvariable=caravan_type , state='readonly')
caravan_type_pop_up['values'] = ("On Tour","Deluxe","Deluxe Edition","Excellent","Premium")
caravan_type_pop_up.grid(column=1,row=0)
caravan_type_pop_up.current(0)
#Bindings fyrir Pop up menu Velja hjólhýsi
caravan_type_pop_up.bind("<<ComboboxSelected>>", caravan_type_callbackFunc)
###################################



########################################## Labels
#Verð Evrur
verd_evrur_label = ttk.Label(caravan_frame,text="Verð í evrum: ")
verd_evrur_label.grid(column=2, row=0)

#Verð í evrum textbox
textvalue = tk.StringVar()
textbox = ttk.Entry(caravan_frame, width=12, textvariable=textvalue)
textbox.grid(column=3,row=0) 

#Lista verð
lista_verd_label = ttk.Label(caravan_frame,text="Lista verð Eu: ")
lista_verd_label.grid(column=0, row=1)

#Fob verð
fob_verd_label = ttk.Label(caravan_frame,text="Fob verð Eu: ")
fob_verd_label.grid(column=1, row=1)

#Verð í krónum label
kronu_verd_label = ttk.Label(caravan_frame,text="Verð í krónum: ")
kronu_verd_label.grid(column=2, row=1)

#CIF Verð í krónum label
cif_verd_label = ttk.Label(caravan_frame,text="CIF Verð Kr: ")
cif_verd_label.grid(column=3, row=1)

#13% tollur label
tollur_verd_label = ttk.Label(caravan_frame,text="13% Tollur Kr: ")
tollur_verd_label.grid(column=4, row=1)

#VSK label
vsk_verd_label = ttk.Label(caravan_frame,text="VSK: ")
vsk_verd_label.grid(column=5, row=1)

#Til Landsins label
tillands_verd_label = ttk.Label(caravan_frame,text="Til Landsins Kr: ")
tillands_verd_label.grid(column=6, row=1)

##########################################

########################################## Textfields listar niðurstöður útreikninga

#Listaverð textbox
lista_verd_value = tk.StringVar()
lista_verd_textbox = ttk.Entry(caravan_frame, width=12, textvariable=lista_verd_value)
lista_verd_textbox.grid(column=0,row=2) 


#Fob verð textbox
fob_verd_textvalue = tk.StringVar()
fob_verd_textbox = ttk.Entry(caravan_frame, width=12, textvariable=fob_verd_textvalue)
fob_verd_textbox.grid(column=1,row=2) 


#Verð í krónum textbox
kronu_verd_textvalue = tk.StringVar()
kronu_verd_textbox = ttk.Entry(caravan_frame, width=12, textvariable=kronu_verd_textvalue)
kronu_verd_textbox.grid(column=2,row=2) 


#CIF  textbox
cif_verd_textvalue = tk.StringVar()
cif_verd_textbox = ttk.Entry(caravan_frame, width=12, textvariable=cif_verd_textvalue)
cif_verd_textbox.grid(column=3,row=2) 


#13% tollur textbox
tollur_verd_textvalue = tk.StringVar()
tollur_verd_textbox = ttk.Entry(caravan_frame, width=12, textvariable=tollur_verd_textvalue)
tollur_verd_textbox .grid(column=4,row=2) 


#VSK textbox
vsk_verd_textvalue = tk.StringVar()
vsk_verd_textbox = ttk.Entry(caravan_frame, width=12, textvariable=vsk_verd_textvalue)
vsk_verd_textbox.grid(column=5,row=2) 


#Til Landsins textbox
tillands_verd_textvalue = tk.StringVar()
tillands_verd_textbox = ttk.Entry(caravan_frame, width=12, textvariable=tillands_verd_textvalue)
tillands_verd_textbox.grid(column=6,row=2) 

##########################################

# TO DO Checkbox virkni fyrir mögulega aukahluti

############################ CheckBox Class og func fyrir aukahluti
checkbox_frame = ttk.LabelFrame(win,text = "chassis frame")
checkbox_frame.grid(column = 0, row = 6)
class checkclass():
    def __init__(self, master, verð, text):
        self.aukahlutir = verð
        self.texti = text + '-- Verð: ' + str(verð)
        self.var = tk.IntVar()
        self.c = tk.Checkbutton(
            master, 
            text = self.texti,
            variable = self.var,
            command = self.cb)
    def cb(self):
        print( self.var.get())
        print( self.texti)

def aukahlutir_func( column, get_price, get_lysing):
    tmp_array = []
    i = 0
    for n in get_extra_list:
        if(n==1):
            tmp_array.append( checkclass(checkbox_frame, get_price[i], get_lysing[i]))
            tmp_array[i].c.grid(column = column, row=6 + i)
            i +=1
    return tmp_array 



checkbox_frame = ttk.LabelFrame(win,text = "chassis frame")
checkbox_frame.grid(column = 0, row = 6)

tmp_id = get_db_data.get_hjolhysi_id_by_name_flokkur('390-SF','On Tour')
get_extra_list = list(map(int, get_db_data.get_aukahlutir_by_hjolhysi_id(tmp_id).chassis.split(' ')))
chassis_aukahlutir = aukahlutir_func( 4, get_db_data.get_price_aukahlutir_by_tegund('chassis'), get_db_data.get_lysing_aukahlutir_by_tegund('chassis'))
##################################

win.mainloop()

# Aukahlutir







