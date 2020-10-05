from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from hjolhysi_database import Hobby_flokkar, Hobby_hjolhysi, Base, Aukahlutir, Hjolhysi_aukahlutir

engine = create_engine('sqlite:///hobby_hjolhysi.db')
# Bind the engine to the metadata of the Base class 
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

#Hobby flokkur_id
flokkur_id = ['On Tour','Deluxe','Deluxe Edition','Excellent', 'Prestige', 'Premium']
for item in flokkur_id:
    add_flokkur_id = Hobby_flokkar(nafn = item)
    session.add(add_flokkur_id)

#Varahlutir 

#CHASSIS
add_aukahlutir = Aukahlutir(
    tegund = 'chassis', 
    lysing = 'Alloy spare wheel black polished with holder', 
    verð = 481 )
session.add(add_aukahlutir)

add_aukahlutir = Aukahlutir(
    tegund = 'chassis', 
    lysing = 'Alloy spare wheel black polished with holder, instead of tyre repair set', 
    verð = 481 )
session.add(add_aukahlutir)

add_aukahlutir = Aukahlutir(
    tegund = 'chassis', 
    lysing = 'Spare wheel with holder, underfloor mounting', 
    verð = 345 )
session.add(add_aukahlutir)

add_aukahlutir = Aukahlutir(
    tegund = 'chassis', 
    lysing = 'Spare wheel with holder, instead of tyre repair set, underfloor mounting', 
    verð = 345 )
session.add(add_aukahlutir)

add_aukahlutir = Aukahlutir(
    tegund = 'chassis', 
    lysing = 'Load indicator on the jockey wheel', 
    verð = 159 )
session.add(add_aukahlutir)

add_aukahlutir = Aukahlutir(
    tegund = 'chassis', 
    lysing = 'Stabilisa on system KNOTT ETS Plus', 
    verð = 773 )
session.add(add_aukahlutir)

add_aukahlutir = Aukahlutir(
    tegund = 'chassis', 
    lysing = 'Hitch lock an -the  device WINTERHOFF “ROBSTOP', 
    verð = 161 )
session.add(add_aukahlutir)
###################################

#LOAD CAPACITY
add_aukahlutir = Aukahlutir(
    tegund = 'Load Capacity', 
    lysing = 'Decrease in load capacity without any technical modifications', 
    verð = 0 )
session.add(add_aukahlutir)

add_aukahlutir = Aukahlutir(
    tegund = 'Load Capacity', 
    lysing = 'Increase in load capacity without any technical modi ca ons', 
    verð = 0 )
session.add(add_aukahlutir)

add_aukahlutir = Aukahlutir(
    tegund = 'Load Capacity', 
    lysing = 'Increase in load capacity with technical modi ca on for single-axle vehicles, including black alloy rims', 
    verð = 995 )
session.add(add_aukahlutir)

add_aukahlutir = Aukahlutir(
    tegund = 'Load Capacity', 
    lysing = 'Increase in load capacity with technical modi ca on for single-axle vehicles', 
    verð = 391 )
session.add(add_aukahlutir)

add_aukahlutir = Aukahlutir(
    tegund = 'Load Capacity', 
    lysing = 'Increase in load capacity with technical modi ca on for tandem-axle vehicles', 
    verð = 495 )
session.add(add_aukahlutir)

add_aukahlutir = Aukahlutir(
    tegund = 'Load Capacity', 
    lysing = 'Increase in load capacity with technical modi ca on for single-axle vehicles, Premium', 
    verð = 563 )
session.add(add_aukahlutir)
###################################

#WHEEL RIMS
add_aukahlutir = Aukahlutir(
    tegund = 'Wheel Rims', 
    lysing = 'Alloy rims silver, up to model 560', 
    verð = 481 )
session.add(add_aukahlutir)

add_aukahlutir = Aukahlutir(
    tegund = 'Wheel Rims', 
    lysing = 'Alloy rims silver, from model 620', 
    verð = 725 )
session.add(add_aukahlutir)
add_aukahlutir = Aukahlutir(
    tegund = 'Wheel Rims', 
    lysing = 'Alloy rims black, polished, up to model 560', 
    verð = 604 )
session.add(add_aukahlutir)

add_aukahlutir = Aukahlutir(
    tegund = 'Wheel Rims', 
    lysing = 'Alloy rims black, polished, from model 620', 
    verð = 959 )
session.add(add_aukahlutir)
###################################

#WINDOW
add_aukahlutir = Aukahlutir(
    tegund = 'Window', 
    lysing = 'Front window with fully integrated pleated blackout blind and insect screen', 
    verð = 451 )
session.add(add_aukahlutir)
###################################

#Body
add_aukahlutir = Aukahlutir(
    tegund = 'Body', 
    lysing = 'Rear lights with dynamic indicator', 
    verð = 230 )
session.add(add_aukahlutir)

add_aukahlutir = Aukahlutir(
    tegund = 'Body', 
    lysing = 'Roof awning THULE OMNISTOR 6300, width 260 cm, pull-out depth 200 cm', 
    verð = 887 )
session.add(add_aukahlutir)

add_aukahlutir = Aukahlutir(
    tegund = 'Body', 
    lysing = 'Roof awning THULE OMNISTOR 6300, width 300 cm, pull-out depth 250 cm', 
    verð = 952 )
session.add(add_aukahlutir)

add_aukahlutir = Aukahlutir(
    tegund = 'Body', 
    lysing = 'Roof awning THULE OMNISTOR 6300, width 350 cm, pull-out depth 250 cm', 
    verð = 1085 )
session.add(add_aukahlutir)

add_aukahlutir = Aukahlutir(
    tegund = 'Body', 
    lysing = 'Roof awning THULE OMNISTOR 6300, width 400 cm, pull-out depth 250 cm', 
    verð = 1359 )
session.add(add_aukahlutir)

add_aukahlutir = Aukahlutir(
    tegund = 'Body', 
    lysing = 'Roof awning THULE OMNISTOR 6300, width 450 cm, pull-out depth 250 cm', 
    verð = 1534 )
session.add(add_aukahlutir)

add_aukahlutir = Aukahlutir(
    tegund = 'Body', 
    lysing = 'Roof awning THULE OMNISTOR 6300, width 500 cm, pull-out depth 250 cm', 
    verð = 1706 )
session.add(add_aukahlutir)


add_aukahlutir = Aukahlutir(
    tegund = 'Body', 
    lysing = 'Bicycle rack THULE, for drawbar, 2 bicycles, loading capacity 60 kg', 
    verð = 294 )
session.add(add_aukahlutir)

add_aukahlutir = Aukahlutir(
    tegund = 'Body', 
    lysing = 'Bicycle rack THULE, for rear, 2 bicycles, loading capacity 40 kg', 
    verð = 306 )
session.add(add_aukahlutir)

add_aukahlutir = Aukahlutir(
    tegund = 'Body', 
    lysing = 'Garage under bunk bed (not in conjunction with hot water heater ALDE, colouring board under children’s bed removed)', 
    verð = 666 )
session.add(add_aukahlutir)

add_aukahlutir = Aukahlutir(
    tegund = 'Body', 
    lysing = 'Locker door THETFORD with central locking, 752 x 310 mm, lockable (optional)', 
    verð = 248 )
session.add(add_aukahlutir)
###################################

#LIVING AREA
add_aukahlutir = Aukahlutir(
    tegund = 'Living Area', 
    lysing = 'Single-post lift table', 
    verð = 221 )
session.add(add_aukahlutir)

add_aukahlutir = Aukahlutir(
    tegund = 'Living Area', 
    lysing = 'Carpet in the living area, removable', 
    verð = 275 )
session.add(add_aukahlutir)
###################################

#UPHOLSTERY COMBINATIONS
add_aukahlutir = Aukahlutir(
    tegund = 'Upholstery combinations', 
    lysing = 'Carpet in the living area, removable', 
    verð = 219)
session.add(add_aukahlutir)
###################################

#KITCHEN
add_aukahlutir = Aukahlutir(
    tegund = 'Kitchen', 
    lysing = 'Combined hob / oven including grill THETFORD', 
    verð = 995)
session.add(add_aukahlutir)

add_aukahlutir = Aukahlutir(
    tegund = 'Kitchen', 
    lysing = 'Oven THETFORD with electric igni on, grill and interior light, 36 litres', 
    verð = 566)
session.add(add_aukahlutir)

add_aukahlutir = Aukahlutir(
    tegund = 'Kitchen', 
    lysing = 'Extractor hood DOMETIC including Hobby 10-stage speed control', 
    verð = 286)
session.add(add_aukahlutir)

add_aukahlutir = Aukahlutir(
    tegund = 'Kitchen', 
    lysing = 'Microwave DOMETIC, 20 litres', 
    verð = 317)
session.add(add_aukahlutir)
###################################

#SLEEPING AREA
add_aukahlutir = Aukahlutir(
    tegund = 'Sleeping Area', 
    lysing = 'Bed extension for single beds including cushion', 
    verð = 340)
session.add(add_aukahlutir)

add_aukahlutir = Aukahlutir(
    tegund = 'Sleeping Area', 
    lysing = 'Cold foam mattress, with 7 zones and slatted bed base for double bed and queen-size bed', 
    verð = 572)
session.add(add_aukahlutir)

add_aukahlutir = Aukahlutir(
    tegund = 'Sleeping Area', 
    lysing = 'Cold foam mattresses, with 7 zones and slatted bed base for single beds', 
    verð = 596)
session.add(add_aukahlutir)

add_aukahlutir = Aukahlutir(
    tegund = 'Sleeping Area', 
    lysing = 'Children’s bed, 3 tiers with guard and ladder', 
    verð = 430)
session.add(add_aukahlutir)

add_aukahlutir = Aukahlutir(
    tegund = 'Sleeping Area', 
    lysing = 'Children’s bed, 3 tiers including 3rd window, with guard and ladder', 
    verð = 490)
session.add(add_aukahlutir)

add_aukahlutir = Aukahlutir(
    tegund = 'Sleeping Area', 
    lysing = 'Bedspread', 
    verð = 196)
session.add(add_aukahlutir)

#WASHROOM
add_aukahlutir = Aukahlutir(
    tegund = 'Washroom', 
    lysing = 'Shower fitting and shower curtain for washroom with external washbasin', 
    verð = 160)
session.add(add_aukahlutir)

add_aukahlutir = Aukahlutir(
    tegund = 'Washroom', 
    lysing = 'Blackout blind including insect screen for washroom', 
    verð = 104)
session.add(add_aukahlutir)

add_aukahlutir = Aukahlutir(
    tegund = 'Washroom', 
    lysing = 'Clothes rail in the shower', 
    verð = 137)
session.add(add_aukahlutir)
###################################

#WATER GAS ELECTRICITY
add_aukahlutir = Aukahlutir(
    tegund = 'Water-gas-electricity', 
    lysing = 'Fresh water tank, 47 litres', 
    verð = 153)
session.add(add_aukahlutir)

add_aukahlutir = Aukahlutir(
    tegund = 'Water-gas-electricity', 
    lysing = 'TFT control panel for lighting system and tank, including CI-BUS', 
    verð = 188)
session.add(add_aukahlutir)

add_aukahlutir = Aukahlutir(
    tegund = 'Water-gas-electricity', 
    lysing = 'Exterior awning socket, including 230 V output, satellite / TV connection', 
    verð = 133)
session.add(add_aukahlutir)

add_aukahlutir = Aukahlutir(
    tegund = 'Water-gas-electricity', 
    lysing = 'Adapter 7 - 13 pole for passenger vehicle connecting cable', 
    verð = 35)
session.add(add_aukahlutir)

add_aukahlutir = Aukahlutir(
    tegund = 'Water-gas-electricity', 
    lysing = 'City water connection', 
    verð = 192)
session.add(add_aukahlutir)

add_aukahlutir = Aukahlutir(
    tegund = 'Water-gas-electricity', 
    lysing = 'External gas socket', 
    verð = 226)
session.add(add_aukahlutir)

add_aukahlutir = Aukahlutir(
    tegund = 'Water-gas-electricity', 
    lysing = 'Electric boiler TRUMA, 14 litres (locker door can be removed)', 
    verð = 449)
session.add(add_aukahlutir)

add_aukahlutir = Aukahlutir(
    tegund = 'Water-gas-electricity', 
    lysing = 'Water pump with additional switch', 
    verð = 48)
session.add(add_aukahlutir)

add_aukahlutir = Aukahlutir(
    tegund = 'Water-gas-electricity', 
    lysing = 'Autonomy package including charge controller with booster, battery, battery sensor and battery case', 
    verð = 645)
session.add(add_aukahlutir)

add_aukahlutir = Aukahlutir(
    tegund = 'Water-gas-electricity', 
    lysing = 'Prepara on for autonomy package including charge controller with booster, battery sensor and battery case', 
    verð = 350)
session.add(add_aukahlutir)

add_aukahlutir = Aukahlutir(
    tegund = 'Water-gas-electricity', 
    lysing = 'HOBBY-CONNECT, remote control for on-board technology using app', 
    verð = 741)
session.add(add_aukahlutir)

add_aukahlutir = Aukahlutir(
    tegund = 'Water-gas-electricity', 
    lysing = 'Wireless remote control for the lighting system with one handset', 
    verð = 161)
session.add(add_aukahlutir)

add_aukahlutir = Aukahlutir(
    tegund = 'Water-gas-electricity', 
    lysing = 'Dual USB charging socket', 
    verð = 55)
session.add(add_aukahlutir)

add_aukahlutir = Aukahlutir(
    tegund = 'Water-gas-electricity', 
    lysing = 'Dual USB charging socket and children’s bed lights including USB charging socket', 
    verð = 93)
session.add(add_aukahlutir)
###################################


#LIGHTING
add_aukahlutir = Aukahlutir(
    tegund = 'Lighting', 
    lysing = 'Ambient lighting, design dependent on model', 
    verð = 277)
session.add(add_aukahlutir)
###################################

#HEATING AIR CONDITIONING
add_aukahlutir = Aukahlutir(
    tegund = 'Heating-airconditioning', 
    lysing = 'Heating system TRUMA Combi 6 E, instead of Combi 4', 
    verð = 791)
session.add(add_aukahlutir)

add_aukahlutir = Aukahlutir(
    tegund = 'Heating-airconditioning', 
    lysing = 'Heating system TRUMA Combi 6 E, instead of Combi 6', 
    verð = 624)
session.add(add_aukahlutir)

add_aukahlutir = Aukahlutir(
    tegund = 'Heating-airconditioning', 
    lysing = 'Auxiliary electric heater TRUMA Ultraheat including CI-BUS', 
    verð = 454)
session.add(add_aukahlutir)

add_aukahlutir = Aukahlutir(
    tegund = 'Heating-airconditioning', 
    lysing = 'Underfloor heating up to model 540', 
    verð = 555)
session.add(add_aukahlutir)

add_aukahlutir = Aukahlutir(
    tegund = 'Heating-airconditioning', 
    lysing = 'Underfloor heating from model 545', 
    verð = 689)
session.add(add_aukahlutir)

add_aukahlutir = Aukahlutir(
    tegund = 'Heating-airconditioning', 
    lysing = 'Hot water heater ALDE COMPACT 3020 HE including CI-BUS', 
    verð = 2530)
session.add(add_aukahlutir)

add_aukahlutir = Aukahlutir(
    tegund = 'Heating-airconditioning', 
    lysing = 'Hot water underfloor heating for hot water heater ALDE', 
    verð = 1219)
session.add(add_aukahlutir)

add_aukahlutir = Aukahlutir(
    tegund = 'Heating-airconditioning', 
    lysing = 'Roof-mounted air conditioning unit DOMETIC FreshJet including CI-BUS, with heating function, without lighting, 2.2 KW', 
    verð = 1976)
session.add(add_aukahlutir)

add_aukahlutir = Aukahlutir(
    tegund = 'Heating-airconditioning', 
    lysing = 'Prepara on for roof-mounted air conditioning unit', 
    verð = 69)
session.add(add_aukahlutir)
###################################

#multimedia
add_aukahlutir = Aukahlutir(
    tegund = 'Multimedia', 
    lysing = 'Pull-out shelf for  flat screen TV including required connections, without video cables (Cinch)', 
    verð = 198)
session.add(add_aukahlutir)

add_aukahlutir = Aukahlutir(
    tegund = 'Multimedia', 
    lysing = 'Articulated TV bracket including required connections, without video cables (Cinch)', 
    verð = 234)
session.add(add_aukahlutir)

add_aukahlutir = Aukahlutir(
    tegund = 'Multimedia', 
    lysing = 'ATV aerial mast TELECO', 
    verð = 208)
session.add(add_aukahlutir)
###################################

#COUNTRY SPECIFICATIONS
add_aukahlutir = Aukahlutir(
    tegund = 'Country specifications', 
    lysing = 'Registra on documents', 
    verð = 139)
session.add(add_aukahlutir)


#ADD HJOLHYSI On Tour
add_hjolhysi = Hobby_hjolhysi(
    nafn = '390-SF', 
    verð = 15700, 
    flokkur_id = 1)
session.add(add_hjolhysi)

add_hjolhysi = Hobby_hjolhysi(
    nafn = '460-DL', 
    verð = 17640, 
    flokkur_id = 1)
session.add(add_hjolhysi)

add_hjolhysi = Hobby_hjolhysi(
    nafn = '470-KMF', 
    verð = 17980, 
    flokkur_id = 1)
session.add(add_hjolhysi)

add_hjolhysi = Hobby_hjolhysi(
    nafn = '470-UL', 
    verð = 18300, 
    flokkur_id = 1)
session.add(add_hjolhysi)
###################################

#Deluxe  

add_hjolhysi = Hobby_hjolhysi(
    nafn = '400-SFe', 
    verð = 17780, 
    flokkur_id = 2)
session.add(add_hjolhysi)

add_hjolhysi = Hobby_hjolhysi(
    nafn = '440-SF', 
    verð = 18190, 
    flokkur_id = 2)
session.add(add_hjolhysi)

add_hjolhysi = Hobby_hjolhysi(
    nafn = '455-UF', 
    verð = 17920, 
    flokkur_id = 2)
session.add(add_hjolhysi)

add_hjolhysi = Hobby_hjolhysi(
    nafn = '460-UFe', 
    verð = 19030, 
    flokkur_id = 2)
session.add(add_hjolhysi)

add_hjolhysi = Hobby_hjolhysi(
    nafn = '460-LU', 
    verð = 18650, 
    flokkur_id = 2)
session.add(add_hjolhysi)

add_hjolhysi = Hobby_hjolhysi(
    nafn = '460-SFf', 
    verð = 20280, 
    flokkur_id = 2)
session.add(add_hjolhysi)


add_hjolhysi = Hobby_hjolhysi(
    nafn = '490-KMF', 
    verð = 19600, 
    flokkur_id = 2)
session.add(add_hjolhysi)

add_hjolhysi = Hobby_hjolhysi(
    nafn = '495-UL', 
    verð = 18960, 
    flokkur_id = 2)
session.add(add_hjolhysi)

add_hjolhysi = Hobby_hjolhysi(
    nafn = '495-WFB', 
    verð = 21370, 
    flokkur_id = 2)
session.add(add_hjolhysi)

add_hjolhysi = Hobby_hjolhysi(
    nafn = '515-UHK', 
    verð = 22830, 
    flokkur_id = 2)
session.add(add_hjolhysi)

add_hjolhysi = Hobby_hjolhysi(
    nafn = '515-UHL', 
    verð = 22830, 
    flokkur_id = 2)
session.add(add_hjolhysi)

add_hjolhysi = Hobby_hjolhysi(
    nafn = '540-FU', 
    verð = 22200, 
    flokkur_id = 2)
session.add(add_hjolhysi)

add_hjolhysi = Hobby_hjolhysi(
    nafn = '540-UL' ,
    verð = 20290, 
    flokkur_id = 2)
session.add(add_hjolhysi)

add_hjolhysi = Hobby_hjolhysi(
    nafn = '540-UFF', 
    verð = 20430, 
    flokkur_id = 2)
session.add(add_hjolhysi)

add_hjolhysi = Hobby_hjolhysi(
    nafn = '540-KMFe', 
    verð = 21310, 
    flokkur_id = 2)
session.add(add_hjolhysi)

add_hjolhysi = Hobby_hjolhysi(
    nafn = '545-kmf',
    verð = 21690 , 
    flokkur_id = 2)
session.add(add_hjolhysi)

add_hjolhysi = Hobby_hjolhysi(
    nafn = '560-KMFe', 
    verð = 22210, 
    flokkur_id = 2)
session.add(add_hjolhysi)

add_hjolhysi = Hobby_hjolhysi(
    nafn = '650-KFU', 
    verð = 26150, 
    flokkur_id = 2)
session.add(add_hjolhysi)
###############################

#Deluxe Edition
add_hjolhysi = Hobby_hjolhysi(
    nafn = '460-UFe', 
    verð = 19460, 
    flokkur_id = 3)
session.add(add_hjolhysi)

add_hjolhysi = Hobby_hjolhysi(
    nafn = '490-KMF', 
    verð = 20580, 
    flokkur_id = 3)
session.add(add_hjolhysi)

add_hjolhysi = Hobby_hjolhysi(
    nafn = '495-UL', 
    verð = 19550, 
    flokkur_id = 3)
session.add(add_hjolhysi)

add_hjolhysi = Hobby_hjolhysi(
    nafn = '545-KMF', 
    verð = 22370, 
    flokkur_id = 3)
session.add(add_hjolhysi)

add_hjolhysi = Hobby_hjolhysi(
    nafn = '560 KMFe', 
    verð = 22680, 
    flokkur_id = 3)
session.add(add_hjolhysi)

add_hjolhysi = Hobby_hjolhysi(
    nafn = '650-KMFe', 
    verð = 24980, 
    flokkur_id = 3)
session.add(add_hjolhysi)
##############################

#Excellent
add_hjolhysi = Hobby_hjolhysi(
    nafn = '460-UFe', 
    verð = 20570, 
    flokkur_id = 4)
session.add(add_hjolhysi)

add_hjolhysi = Hobby_hjolhysi(
    nafn = '460-SFf', 
    verð = 21290, 
    flokkur_id = 4)
session.add(add_hjolhysi)

add_hjolhysi = Hobby_hjolhysi(
    nafn = '495-UFe', 
    verð = 21430, 
    flokkur_id = 4)
session.add(add_hjolhysi)

add_hjolhysi = Hobby_hjolhysi(
    nafn = '495-UL', 
    verð = 20660, 
    flokkur_id = 4)
session.add(add_hjolhysi)

add_hjolhysi = Hobby_hjolhysi(
    nafn = '495-WFB', 
    verð = 23010, 
    flokkur_id = 4)
session.add(add_hjolhysi)

add_hjolhysi = Hobby_hjolhysi(
    nafn = '540-FU', 
    verð = 23700, 
    flokkur_id = 4)
session.add(add_hjolhysi)

add_hjolhysi = Hobby_hjolhysi(
    nafn = '540-WLU', 
    verð = 22770, 
    flokkur_id = 4)
session.add(add_hjolhysi)

add_hjolhysi = Hobby_hjolhysi(
    nafn = '540-UL', 
    verð = 21700, 
    flokkur_id = 4)
session.add(add_hjolhysi)

add_hjolhysi = Hobby_hjolhysi(
    nafn = '540-UFf', 
    verð = 21760, 
    flokkur_id = 4)
session.add(add_hjolhysi)

add_hjolhysi = Hobby_hjolhysi(
    nafn = '560-CFe', 
    verð = 23890, 
    flokkur_id = 4)
session.add(add_hjolhysi)

add_hjolhysi = Hobby_hjolhysi(
    nafn = '560-LU', 
    verð = 23040, 
    flokkur_id = 4)
session.add(add_hjolhysi)

add_hjolhysi = Hobby_hjolhysi(
    nafn = '560-WFU', 
    verð = 25350, 
    flokkur_id = 4)
session.add(add_hjolhysi)

add_hjolhysi = Hobby_hjolhysi(
    nafn = '650-UMFe', 
    verð = 25300, 
    flokkur_id = 4)
session.add(add_hjolhysi)
##############################

#Prestige
add_hjolhysi = Hobby_hjolhysi(
    nafn = '495-UL', 
    verð = 21130, 
    flokkur_id = 5)
session.add(add_hjolhysi)

add_hjolhysi = Hobby_hjolhysi(
    nafn = '560-FC', 
    verð = 26030, 
    flokkur_id = 5)
session.add(add_hjolhysi)

add_hjolhysi = Hobby_hjolhysi(
    nafn = '560-LU', 
    verð = 23670, 
    flokkur_id = 5)
session.add(add_hjolhysi)

add_hjolhysi = Hobby_hjolhysi(
    nafn = '560-WLU', 
    verð = 24880, 
    flokkur_id = 5)
session.add(add_hjolhysi)

add_hjolhysi = Hobby_hjolhysi(
    nafn = '560-WFU', 
    verð = 25980, 
    flokkur_id = 5)
session.add(add_hjolhysi)

add_hjolhysi = Hobby_hjolhysi(
    nafn = '620-CL', 
    verð = 25470, 
    flokkur_id = 5)
session.add(add_hjolhysi)

add_hjolhysi = Hobby_hjolhysi(
    nafn = '660-WFC', 
    verð = 29140, 
    flokkur_id = 5)
session.add(add_hjolhysi)

add_hjolhysi = Hobby_hjolhysi(
    nafn = '720-UKFe', 
    verð = 29380, 
    flokkur_id = 5)
session.add(add_hjolhysi)

add_hjolhysi = Hobby_hjolhysi(
    nafn = '720-KWFU', 
    verð = 31500, 
    flokkur_id = 5)
session.add(add_hjolhysi)

add_hjolhysi = Hobby_hjolhysi(
    nafn = '720-WLC',
    verð = 31240, 
    flokkur_id = 5)
session.add(add_hjolhysi)

add_hjolhysi = Hobby_hjolhysi(
    nafn = '720-WQC', 
    verð = 31650, 
    flokkur_id = 5)
session.add(add_hjolhysi)
##############################
#Premium
add_hjolhysi = Hobby_hjolhysi(
    nafn = '495 UL', 
    verð = 24870, 
    flokkur_id = 6)
session.add(add_hjolhysi)

add_hjolhysi = Hobby_hjolhysi(
    nafn = '560 CFe', 
    verð = 28660, 
    flokkur_id = 6)
session.add(add_hjolhysi)

add_hjolhysi = Hobby_hjolhysi(
    nafn = '560 UL', 
    verð = 27330, 
    flokkur_id = 6)
session.add(add_hjolhysi)

add_hjolhysi = Hobby_hjolhysi(
    nafn = '650 UFf', 
    verð = 32040, 
    flokkur_id = 6)
session.add(add_hjolhysi)

add_hjolhysi = Hobby_hjolhysi(
    nafn = '650 UKFe', 
    verð = 32200 , 
    flokkur_id = 6)
session.add(add_hjolhysi)

add_hjolhysi = Hobby_hjolhysi(
    nafn = '660 WFU',
    verð = 32910, 
    flokkur_id = 6)
session.add(add_hjolhysi)
###############################

# Add aukahlutir
add_hjolhysi_aukahlutir = Hjolhysi_aukahlutir(
    hjolhysi_id = 1,
    chassis = '0 0 0 1 0 1 1',
    load_capacity = '1 1 0 1 0 0',
    wheel_rims = '1 0 1 0',
    window = '1',
    body = '1 1 0 0 0 0 0 1 1 0 0',
    living_area = '0 1',
    upholstery_combinations = '0',
    kitchen = '0 0 1 0',
    sleeping_area = '0 0 0 0 0 1',
    washroom = '0 0 0',
    water_gas_electricity = '1 1 1 1 1 1 1 1 1 1 1 1 1 0',
    lighting = '1',
    heating_air_condition = '0 0 1 1 0 0 0 1 1',
    multimedia = '0 1 1',
    country_specs = '1')
session.add(add_hjolhysi_aukahlutir)

#On Tour 2
add_hjolhysi_aukahlutir = Hjolhysi_aukahlutir(
    hjolhysi_id = 2,
    chassis = '0 0 0 1 0 1 1',
    load_capacity = '0 1 0 1 0 0',
    wheel_rims = '1 0 1 0',
    window = '1',
    body = '1 0 0 1 0 0 0 1 1 0 0',
    living_area = '1 1',
    upholstery_combinations = '0',
    kitchen = '0 0 1 0',
    sleeping_area = '1 0 0 0 0 1',
    washroom = '0 0 0',
    water_gas_electricity = '1 1 1 1 1 1 1 1 1 1 1 1 1 0',
    lighting = '1',
    heating_air_condition = '0 0 1 1 0 0 0 1 1',
    multimedia = '0 1 0',
    country_specs = '1')
session.add(add_hjolhysi_aukahlutir)

#On Tour 3
add_hjolhysi_aukahlutir = Hjolhysi_aukahlutir(
    hjolhysi_id = 3,
    chassis = '0 0 0 1 0 1 1',
    load_capacity = '1 0 0 1 0 0',
    wheel_rims = '1 0 1 0',
    window = '1',
    body = '1 0 0 1 0 0 0 1 1 0 0',
    living_area = '0 1',
    upholstery_combinations = '0',
    kitchen = '0 0 1 0',
    sleeping_area = '0 0 0 1 0 1',
    washroom = '0 0 0',
    water_gas_electricity = '1 1 1 1 1 1 1 1 1 1 1 1 0 1',
    lighting = '1',
    heating_air_condition = '0 0 1 1 0 0 0 1 1',
    multimedia = '0 1 1',
    country_specs = '1')
session.add(add_hjolhysi_aukahlutir)

#On Tour 4
add_hjolhysi_aukahlutir = Hjolhysi_aukahlutir(
    hjolhysi_id = 4,
    chassis = '0 0 0 1 0 1 1',
    load_capacity = '1 1 0 1 0 0',
    wheel_rims = '1 0 1 0',
    window = '1',
    body = '1 0 0 1 0 0 0 1 1 0 0',
    living_area = '1 1',
    upholstery_combinations = '0',
    kitchen = '0 0 1 0',
    sleeping_area = '1 0 0 0 0 1',
    washroom = '0 0 0',
    water_gas_electricity = '1 1 1 1 1 1 1 1 1 1 1 1 1 0',
    lighting = '1',
    heating_air_condition = '0 0 1 1 0 0 0 1 1',
    multimedia = '0 1 0',
    country_specs = '1')
session.add(add_hjolhysi_aukahlutir)

#Deluxe
add_hjolhysi_aukahlutir = Hjolhysi_aukahlutir(
    hjolhysi_id = 4,
    chassis = '0 0 0 0 1 0 0',
    load_capacity = '1 1 0 1 0 0',
    wheel_rims = '1 0 1 0',
    window = '1',
    body = '1 0 0 1 0 0 0 1 1 0 0',
    living_area = '1 1',
    upholstery_combinations = '0',
    kitchen = '0 0 1 0',
    sleeping_area = '1 0 0 0 0 1',
    washroom = '0 0 0',
    water_gas_electricity = '1 1 1 1 1 1 1 1 1 1 1 1 1 0',
    lighting = '1',
    heating_air_condition = '0 0 1 1 0 0 0 1 1',
    multimedia = '0 1 0',
    country_specs = '1')
session.add(add_hjolhysi_aukahlutir)

# TO DO
# Klára að harðkóða gögn

#Save inserts
session.commit()


