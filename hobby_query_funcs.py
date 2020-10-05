from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from hjolhysi_database import Hobby_flokkar, Hobby_hjolhysi, Base, Aukahlutir, Hjolhysi_aukahlutir


engine = create_engine('sqlite:///hobby_hjolhysi.db')
# Bind the engine to the metadata of the Base class 
Base.metadata.bind = engine

# A DBSession() instance establishes all conversations with the database
DBSession = sessionmaker(bind=engine)

session = DBSession()

def get_flokkar():
    flokkar = session.query(Hobby_flokkar).all()
    flokkar_array = []
    for items in flokkar:
        flokkar_array.append(items.nafn)
    return flokkar_array

def get_all_hjolhysi_by_flokkar(flokkur):
    on_tour_hjolhysi = session.query(Hobby_hjolhysi).join(Hobby_flokkar).filter(Hobby_flokkar.nafn == flokkur).all()
    hjolhysi_array = []
    for item in on_tour_hjolhysi:
        hjolhysi_array.append(item.nafn)
    return hjolhysi_array

def get_all_hjolhysi_id_by_flokkar(flokkur):
    on_tour_hjolhysi = session.query(Hobby_hjolhysi).join(Hobby_flokkar).filter(Hobby_flokkar.nafn == flokkur).all()
    hjolhysi_array = []
    for item in on_tour_hjolhysi:
        hjolhysi_array.append(item.id)
    return hjolhysi_array

def get_hjolhysi_price_by_name(nafn):
    return session.query(Hobby_hjolhysi).filter(Hobby_hjolhysi.nafn==nafn).first().verð

def get_hjolhysi_price_by_name_flokkur(nafn, flokkur):
    return session.query(Hobby_hjolhysi).join(Hobby_flokkar).filter(Hobby_flokkar.nafn == flokkur).filter(Hobby_hjolhysi.nafn==nafn).first().verð

def get_hjolhysi_id_by_name_flokkur(nafn, flokkur):
    return session.query(Hobby_hjolhysi).join(Hobby_flokkar).filter(Hobby_flokkar.nafn == flokkur).filter(Hobby_hjolhysi.nafn==nafn).first().id

def get_aukahlutir(hjolhysi, aukahlutur_tegund):
    return 0


#ble = session.query(Hobby_hjolhysi).join(Hobby_flokkar).filter(Hobby_flokkar.nafn == 'On Tour').filter(Hobby_hjolhysi.nafn=='390-SF').first().verð
#print(get_hjolhysi_price_by_name_flokkur('390-SF','On Tour'))
#ble = session.query(Hjolhysi_aukahlutir).filter(Hjolhysi_aukahlutir.id==1).first()
#ble_join = session.query(Hjolhysi_aukahlutir).join(Hobby_hjolhysi).filter(Hobby_hjolhysi.id==1).one()

#print(get_hjolhysi_price_by_name('495-WFB'))
#print(get_all_hjolhysi_by_flokkar('On Tour'))

#### velja mögulega varahluti fyrir ákveðin hjólhýsi - getum náð í valmöguleika og hjólhýsið og eigind þess
"""
ble_join = session.query(Hjolhysi_aukahlutir).join(Hobby_hjolhysi).filter(Hobby_hjolhysi.id==1).one()
print(ble_join.hjolhysi.nafn)
print(ble_join.load_capacity) 

ble_join = session.query(Hjolhysi_aukahlutir).join(Hobby_hjolhysi).filter(Hobby_hjolhysi.id==2).one()
print(ble_join.hjolhysi.nafn)
print(ble_join.load_capacity) 
"""

def get_aukahlutir_by_hjolhysi_id(id):
    _this = session.query(Hjolhysi_aukahlutir).join(Hobby_hjolhysi).filter(Hobby_hjolhysi.id==id).first()
    return _this


def get_price_aukahlutir_by_tegund(tegund):
    tmp_arr = []
    tmp_query = session.query(Aukahlutir).filter(Aukahlutir.tegund==tegund).all()
    for items in tmp_query:
        tmp_arr.append(items.verð)
    return tmp_arr

def get_lysing_aukahlutir_by_tegund(tegund):
    tmp_arr = []
    tmp_query = session.query(Aukahlutir).filter(Aukahlutir.tegund==tegund).all()
    for items in tmp_query:
        tmp_arr.append(items.lysing)
    return tmp_arr

def get_aukahlutir_by_tegund(tegund):
    tmp_arr = []
    tmp_query = session.query(Aukahlutir).filter(Aukahlutir.tegund==tegund).all()
    for items in tmp_query:
        tmp_arr.append(items.lysing)
    return tmp_arr

def get_aukahlutir_tegund():
    tmp_arr = []
    tmp_query = session.query(Aukahlutir).distinct(Aukahlutir.tegund).group_by(Aukahlutir.tegund).all()
    for items in tmp_query:
        tmp_arr.append(items.tegund)
    return tmp_arr



#print(list(map(int, get_aukahlutir_by_hjolhysi_id(1).load_chassis.split(' '))))
#print(list(map(int, get_aukahlutir_by_hjolhysi_id(2).load_capacity.split(' '))))
#print(list(map(int, get_aukahlutir_by_hjolhysi_id(3).load_capacity.split(' '))))
#print(list(map(int, get_aukahlutir_by_hjolhysi_id(4).load_capacity.split(' '))))

#print(get_aukahlutir_by_tegund('chassis'))
#print(get_aukahlutir_tegund())
#núna þarf ég

# id af völdu hjólhýsi -- get_hjolhysi_id_by_name_flokkur
# nota þetta id og get_aukahlutir_by_hjolhysi_id fyrir array n
#tmp_id = get_hjolhysi_id_by_name_flokkur('390-SF','On Tour')
#print(list(map(int, get_aukahlutir_by_hjolhysi_id(tmp_id).chassis.split(' '))))
#print(get_lysing_aukahlutir_by_tegund('chassis'))
# array með lysingum
#  get_lysing_aukahlutir_by_tegund
# array með verðum
#  get_price_aukahlutir_by_tegund


