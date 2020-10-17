from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import update
from sqlalchemy.ext.declarative import declarative_base
import crud_exceptions as crud_exc
<<<<<<< HEAD
from hjolhysi_com_database import Base, Hobby_flokkar, Hobby_hjolhysi,  Aukahlutir, Hjolhysi_aukahlutir, Vidskiptavinir, Vidhengi, Heimilisfang
=======
from hjolhysi_database import Base, Hobby_flokkar, Hobby_hjolhysi,  Aukahlutir, Hjolhysi_aukahlutir, Vidskiptavinir, Vidhengi, Heimilisfang
>>>>>>> cc296bea6fdda4ce9c4deb21522bacdf3f99400b


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
 
def bua_til_vidskiptavin(eiginnafn, eftirnafn, kt, simi, email, heimilisfang, postnumer ):
    if(session.query(Vidskiptavinir).filter(Vidskiptavinir.kt==kt).all()):
        
        raise crud_exc.ItemAlreadyStored('"{}" Viðskiptavinur með þessa kennitölu er nú þegar á skrá!'.format(kt))
    
    else:
        bua_til_vv = Vidskiptavinir( 
            eiginnafn = "".join(eiginnafn.split() ),  
            eftirnafn = "".join(eftirnafn.split() ),  
            kt = "".join(kt.split()),  
            simi = "".join(simi.split()),  
            email = "".join(email.split()) 
            )
        hf = Heimilisfang( 
            heimilisfang = "".join(heimilisfang.split()), 
            postnumer = "".join(postnumer.split() ) ) 
        bua_til_vv.heimilisfang.append( hf )
        session.add_all( [ bua_til_vv, hf ] )
        session.commit()


def breyta__vidskiptavin(eiginnafn, eftirnafn, kt, simi, email, heimilisfang, postnumer):
    vv = session.query(Vidskiptavinir).filter(Vidskiptavinir.eiginnafn==eiginnafn).all()
    
    if vv:
        if(len(vv) == 1 ):
            vv[0].eiginnafn = eiginnafn
            vv[0].eftirnafn = eftirnafn
            vv[0].kt = kt
            vv[0].simi = simi
            vv[0].email = email
            #heimilisfang = session.query(Heimilisfang).join(Vidskiptavinir).filter(Vidskiptavinir.id==vv[0].id).first()
            vv[0].heimilisfang[0].postnumer = postnumer
            vv[0].heimilisfang[0].heimilisfang = heimilisfang
            #vv[0].heimilisfang.append( heimilisfang )
        
        else:
            return vv_allir
                 
    else:
        raise crud_exc.ItemAlreadyStored('"{}" Viðskiptavinur er ekki á skrá'.format(eiginnafn))

    session.commit()
    
def eyda_vidskiptavin(kt):
    vv = session.query(Vidskiptavinir).filter(Vidskiptavinir.kt==kt).all()
    if vv:
        heimilisfang = session.query(Heimilisfang).join(Vidskiptavinir).filter(Vidskiptavinir.kt==vv[0].kt).first()
        session.delete(heimilisfang)
        session.delete(vv[0])
        session.commit()
    else:
        raise crud_exc.ItemAlreadyStored(' Viðskiptavinur með kennitölu "{}" er ekki á skrá '.format(kt))
    return 0

def birta_alla_vidskiptavini():
    vv_listi = enumerate([ item for item in session.query(Vidskiptavinir).all()])
    tmp_array = []
    for i, k in vv_listi:
        tmp_array.append({
            'eiginnafn': k.eiginnafn, 
            'eftirnafn': k.eftirnafn,
            'kennitala': k.kt,  
            'sími': k.simi, 
            'email': k.email , 
            'heimilisfang': k.heimilisfang[0].heimilisfang,
            'póstnúmer': k.heimilisfang[0].postnumer  })
    return tmp_array

def birta_vidskiptavin(eiginnafn):
    vv = session.query(Vidskiptavinir).filter(Vidskiptavinir.eiginnafn==eiginnafn).all()
    print(len(vv))
    if vv:
        if(len(vv) == 1 ):
            tmp_array = []
            for k in vv:
                tmp_array.append({
                    'eiginnafn': k.eiginnafn, 
                    'eftirnafn': k.eftirnafn,
                    'kennitala': k.kt,  
                    'sími': k.simi, 
                    'email': k.email , 
                    'heimilisfang': k.heimilisfang[0].heimilisfang,
                    'póstnúmer': k.heimilisfang[0].postnumer  })
            return tmp_array
          
        
        else:
            tmp_array = []
            for k in vv:
                tmp_array.append({
                    'eiginnafn': k.eiginnafn, 
                    'eftirnafn': k.eftirnafn,
                    'kennitala': k.kt,  
                    'sími': k.simi, 
                    'email': k.email , 
                    'heimilisfang': k.heimilisfang[0].heimilisfang,
                    'póstnúmer': k.heimilisfang[0].postnumer  })
            return tmp_array
                 
    else:
        raise crud_exc.ItemAlreadyStored('"{}" Viðskiptavinur er ekki á skrá'.format(eiginnafn))



