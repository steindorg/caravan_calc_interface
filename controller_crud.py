from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import update
from sqlalchemy.ext.declarative import declarative_base
import crud_exceptions as crud_exc
from hjolhysi_com_database import Base, Viðskiptavinir, Heimilisfang, Netfang, Símanúmer, Framleiðandi, Vöruflokkar, Vörutegund, Vara, Tengiliður, Aukahlutir, Aukahlutir_tegund, Pantanir
from sqlalchemy import inspect

engine = create_engine('sqlite:///test_relations.db')
# Bind the engine to the metadata
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()


#Crud og database fyrirspurnir - Brainstorm

def get_vöruflokkur_nafn( nafn ):
    if session.query(Vöruflokkar).filter(Vöruflokkar.nafn==nafn).first():
        return session.query(Vöruflokkar).filter(Vöruflokkar.nafn==nafn).first()
    else:
        raise crud_exc.ItemNotStored('"{}" Vöruflokkur er ekki á skrá'.format( nafn ))

def get_productCategories():
    return session.query(Vöruflokkar).all()

def get_vörutegund_nafn( nafn ):
    if session.query(Vörutegund).filter(Vörutegund.nafn==nafn).first():
        return session.query(Vörutegund).filter(Vörutegund.nafn==nafn).first()
    else:
        raise crud_exc.ItemNotStored('"{}" Vörutegund er ekki á skrá'.format( nafn ))

def get_vörutegundir_by_vöruflokkur( nafn ):
    tmp_arr = []
    get_all = session.query(Vörutegund).join(Vöruflokkar).\
        filter(Vöruflokkar.nafn == nafn).all()
    if get_all:
        for item in get_all:
            tmp_arr.append(item.nafn)
        return tmp_arr 
    else:
        raise crud_exc.ItemNotStored('"{}" Vöruflokkur er ekki á skrá'.format( nafn ))

def get_productModels_by_category(name):
    return session.query(Vörutegund).join(Vöruflokkar).filter(Vöruflokkar.nafn == name).all()

def get_productModels_by_category_nafn(name):
    return [item.nafn for item in session.query(Vörutegund).join(Vöruflokkar).filter(Vöruflokkar.nafn == name).all()]

def get_attributes_vörur_by_vörutegund( vörutegund, attribute ):
    tmp_arr = []
    get_all = session.query(Vara).join(Vörutegund).\
        filter(Vörutegund.nafn == vörutegund ).all()
    if get_all:
        for item in get_all:
            tmp_arr.append( getattr( item, attribute ) ) 
        return tmp_arr
    else:
        raise crud_exc.ItemNotStored('"{}" Vörutegund er ekki á skrá'.format( nafn ))

def get_products_by_productModel( productModel ):
    return session.query(Vara).join(Vörutegund).filter(Vörutegund.nafn == productModel ).all()

def get_products_by_productModel_nafn( productModel ):
    return [item.nafn for item in session.query(Vara).join(Vörutegund).filter(Vörutegund.nafn == productModel ).all()]



def get_values_aukahlutir_by_tegund_array(tegund, attribute):
    tmp_arr = []
    get_all = session.query(Aukahlutir).join(Aukahlutir_tegund).\
        filter(Aukahlutir_tegund.nafn == tegund ).all()
    if get_all:
        for item in get_all:
            tmp_arr.append( getattr( item, attribute ) ) 
        return tmp_arr
    else:
        raise crud_exc.ItemNotStored('"{}" Tegund aukahlutar er ekki á skrá'.format( tegund ))

def get_framleiðandi_nafn(nafn):
    if session.query(Framleiðandi).filter(Framleiðandi.nafn==nafn).first():
        return session.query(Framleiðandi).filter(Framleiðandi.nafn==nafn).first()
    else:
        raise crud_exc.ItemNotStored('"{}" Framleiðandi er ekki á skrá'.format( nafn ))

def get_framleiðendur():
    if session.query(Framleiðandi).all():
        return session.query(Framleiðandi).all()
    else:
        raise crud_exc.ItemNotStored('"{}" Engir framleiðendur til á skrá'.format( '' ))
def get_framleiðendur_nafn():
    return [x.nafn for x in session.query(Framleiðandi).all()]

def get_vöruflokkar():
    vf = session.query(Vöruflokkar).all()
    tmp_arr = []
    if vf:
        for item in vf:
            tmp_arr.append(item.nafn )       
        return tmp_arr
    else:
        raise crud_exc.ItemNotStored('"{}" Engir Vöruflokkar til á skrá'.format( '' ))


def get_vara_by_tegund(vara, tegund):
    vara = session.query(Vara).join(Vörutegund).\
        filter(Vörutegund.nafn == tegund ).filter(Vara.nafn==vara).first()
    if vara:
        return vara
    else:
        raise crud_exc.ItemNotStored('"{}" Vara er ekki á skrá'.format( tegund ))

def get_attr_vara_by_tegund(vara, tegund, attribute):
    vara = session.query(Vara).join(Vörutegund).\
        filter(Vörutegund.nafn == tegund ).filter(Vara.nafn==vara).first()
    if vara:
        return getattr(vara, attribute)
    else:
        raise crud_exc.ItemNotStored('"{}" Vara er ekki á skrá'.format( tegund ))

def get_aukahlutur_tegund(nafn):
    if session.query(Aukahlutir_tegund).filter(Aukahlutir_tegund.nafn==nafn).first():
        return session.query(Aukahlutir_tegund).filter(Aukahlutir_tegund.nafn==nafn).first()
    else:
        raise crud_exc.ItemNotStored('"{}" Tegund er ekki á skrá'.format( nafn ))

def get_all_aukahlutur_tegund():
        return session.query(Aukahlutir_tegund).all()

def get_extras_by_extraCategory_name(name):
    return session.query(Aukahlutir).join(Aukahlutir_tegund).filter(Aukahlutir_tegund.nafn==name).all()

def get_extra_by_name_extraCategory_name(extra_name, cat_name):
    return session.query(Aukahlutir).join(Aukahlutir_tegund)\
        .filter(Aukahlutir_tegund.nafn==name).all()


def get_extras_by_extraCategory_get_by_lysing(name):
    return [item.lýsing for item in session.query(Aukahlutir).join(Aukahlutir_tegund).filter(Aukahlutir_tegund.nafn==name).all()]


#print( session.query(Aukahlutir).join(Aukahlutir_tegund).filter(Aukahlutir_tegund.nafn=='Chassis').all()  )

def get_aukahlutir_vara_flokkur_tegund( nafn, tegund, aukahlutur_tegund):
    vara = get_vara_by_tegund( nafn,tegund )
    #print(vara.aukahlutir)
    tmp_arr = []
    for item in vara.aukahlutir:
        if( item.aukahlutur_tegund.nafn == aukahlutur_tegund):
            tmp_arr.append( { 'Lýsing': item.lýsing, 'Verð': item.verð } )
        else:
            tmp_arr = 'Aukahlutur ekki til fyrir þessa tegund af vöru'
    return tmp_arr

def get_aukahlutir_vara_flokkur_tegund( nafn, tegund, aukahlutur_tegund):
    vara = get_vara_by_tegund( nafn,tegund )
    #print(vara.aukahlutir)
    tmp_arr = []
    for item in vara.aukahlutir:
        if( item.aukahlutur_tegund.nafn == aukahlutur_tegund):
            tmp_arr.append( {'Lýsing': item.lýsing, 'Verð': item.verð } )
  
        else:
            tmp_arr = 'Aukahlutur ekki til fyrir þessa tegund af vöru'
    return tmp_arr



# CRUD
def bua_til_framleiðanda(nafn, tengiliður_nafn, tengiliður_eftirnafn, tengiliður_sími, tengiliður_netfang):
    if(session.query(Framleiðandi).filter(Framleiðandi.nafn==nafn).all()):

        raise crud_exc.ItemAlreadyStored('"{}" Framleiðandi er nú þegar á skrá!'.format(nafn))
    
    add_framleiðandi = Framleiðandi( nafn = nafn)
    add_framleiðandi.tengiliðir = [ Tengiliður(
        eiginnafn = tengiliður_nafn,
        eftirnafn = tengiliður_eftirnafn
        )]
    add_framleiðandi.tengiliðir[0].netföng = [ Netfang( netfang = tengiliður_netfang) ]
    add_framleiðandi.tengiliðir[0].símanúmer = [ Símanúmer( símanúmer = tengiliður_sími) ]
    print(add_framleiðandi.tengiliðir)
    session.add( add_framleiðandi  )   
    session.commit()
    return add_framleiðandi

def breyta_framleiðanda(nafn, tengiliður_nafn, tengiliður_eftirnafn, tengiliður_sími, tengiliður_netfang):
    fr = session.query(Framleiðandi).filter(Framleiðandi.nafn==nafn).first()
    if fr:
        fr.nafn = nafn
        fr.tengiliðir[0].eiginnafn = tengiliður_nafn
        fr.tengiliðir[0].eftirnafn = tengiliður_eftirnafn
        fr.tengiliðir[0].netföng[0].netfang = tengiliður_netfang
        fr.tengiliðir[0].símanúmer[0].símanúmer = tengiliður_sími
                 
    else:
        raise crud_exc.ItemNotStored('"{}" Framleiðandi er ekki á skrá'.format(nafn))

    session.commit()
    return fr

def delete_manufacturer(rowid):
    fr = session.query(Framleiðandi).filter(Framleiðandi.id==rowid).first()
    if fr:
        session.delete(fr)
        session.commit()            
    else:
        raise crud_exc.ItemNotStored('"{}" Framleiðandi er ekki á skrá'.format(fr.nafn))

def birta_framleiðanda(nafn):
    fr = session.query(Framleiðandi).filter(Framleiðandi.nafn==nafn).all()
    if fr:
        if(len(fr) == 1 ):
            tmp_array = []
            for k in fr:
                tmp_array.append({
                    'nafn': k.nafn,
                    'tengiliður eiginnafn': k.tengiliðir[0].eiginnafn, 
                    'tengiliður eftirnafn': k.tengiliðir[0].eftirnafn, 
                    'sími': k.tengiliðir[0].símanúmer[0].símanúmer, 
                    'email': k.tengiliðir[0].netföng[0].netfang
                    })
            return tmp_array[0]            
    else:
        raise crud_exc.ItemNotStored('"{}" Framleiðandi er ekki á skrá'.format(nafn))
   
def bua_til_vöruflokk(nafn):
    if(session.query(Vöruflokkar).filter(Vöruflokkar.nafn==nafn).all()):  
        raise crud_exc.ItemAlreadyStored('"{}" Vöruflokkur er nú þegar á skrá!'.format(nafn))
    
    add_vöruflokkur = Vöruflokkar( nafn = nafn)
    session.add( add_vöruflokkur  )   
    session.commit()
    return add_vöruflokkur

def breyta_vöruflokk(nafn):
    vf= session.query(Vöruflokkar).filter(Vöruflokkar.nafn==nafn).first()
    if vf:
        vf.nafn = nafn             
    else:
        raise crud_exc.ItemNotStored('"{}" Vöruflokkur er ekki á skrá'.format(nafn))

    session.commit()
    return vf

def delete_productCategory(rowid):
    vf = session.query(Vöruflokkar).filter(Vöruflokkar.id==rowid).first()
    if vf:
        session.delete( vf )
        session.commit()            
    else:
        raise crud_exc.ItemNotStored('"{}" Vöruflokkur er ekki á skrá'.format(vf.nafn))

def birta_vöruflokk(nafn):
    vf = session.query(Vöruflokkar).filter(Vöruflokkar.nafn==nafn).all()
    if vf:
        if(len(vf) == 1 ):
            tmp_array = []
            for k in vf:
                tmp_array.append({
                    'nafn': k.nafn,
                    })
            return tmp_array[0]            
    else:
        raise crud_exc.ItemNotStored('"{}" Vöruflokkur er ekki á skrá'.format(nafn))

def bua_til_vörutegund(nafn, vöruflokkur, framleiðandi):
    if(session.query(Vörutegund).filter(Vörutegund.nafn==nafn).all()): 
        raise crud_exc.ItemAlreadyStored('"{}" Vörutegund er nú þegar á skrá!'.format(nafn))
    
    add_vörutegund = Vörutegund( nafn = nafn)
    add_vörutegund.framleiðandi = get_framleiðandi_nafn( framleiðandi ) 
    add_vörutegund.vöruflokkur =  get_vöruflokkur_nafn( vöruflokkur ) 
    session.add( add_vörutegund  )   
    session.commit()
    return add_vörutegund

def breyta_vörutegund(nafn, vöruflokkur, framleiðandi, rowid):
    vt = session.query(Vörutegund).filter(Vörutegund.id==rowid).first()
    print(vt)
    vt.nafn = nafn
    vt.framleiðandi = get_framleiðandi_nafn( framleiðandi )
    vt.vöruflokkur  = get_vöruflokkur_nafn( vöruflokkur )              

    session.commit()
    return vt

def delete_productModel(rowid):
    vt = session.query(Vörutegund).filter(Vörutegund.id==rowid).first()
    if vt:
        session.delete( vt )
        session.commit()            
    else:
        raise crud_exc.ItemNotStored('"{}" Vörutegund er ekki á skrá'.format(vt.nafn))

def birta_vörutegundir():
    vt = session.query(Vörutegund).filter(Vörutegund.nafn==nafn).all()
    if vt:
        tmp_array = []
        for k in vt:
            tmp_array.append({
                'nafn': k.nafn,
                })
        return tmp_array            
    else:
        raise crud_exc.ItemNotStored('"{}" Vörutegund er ekki á skrá'.format(nafn))


def bua_til_vöru(nafn, verð, vörutegund):
    if session.query(Vara).join(Vörutegund).\
        filter(Vörutegund.nafn == vörutegund).filter(Vara.nafn==nafn).all():
        raise crud_exc.ItemAlreadyStored('"{}" Vara er nú þegar á skrá!'.format(nafn))
    
    add_tegund = session.query( Vörutegund ).filter( Vörutegund.nafn == vörutegund ).first()
    vara = Vara(nafn = nafn, verð = verð )
    add_tegund.vörur.append( vara )
    session.add( add_tegund )
    session.commit()
    return vara


def breyta_vöru(nafn, verð, vörutegund, rowid):
    vara = session.query(Vara).join(Vörutegund).filter(Vörutegund.nafn == vörutegund).filter(Vara.id==rowid).first()
    if vara:
        vara.nafn = nafn
        vara.verð = verð
        vara.vörutegundir = get_vörutegund_nafn( vörutegund )              
    else:
        raise crud_exc.ItemNotStored('"{}" Vara er ekki á skrá'.format(nafn))

    session.commit()
    return vara

def delete_product(rowid):
    vara = session.query(Vara).filter(Vara.id==rowid).first()
    session.delete( vara )
    session.commit()

def birta_vörur(nafn,vörutegund):
    vara = session.query(Vara).join(Vörutegund).filter(Vörutegund.nafn == vörutegund).all()
    if vara:
        tmp_array = []
        for k in vara:
            tmp_array.append({
                'nafn': k.nafn,
                'verð': k.verð,
                })
        return tmp_array            
    else:
        raise crud_exc.ItemNotStored('"{}" Vörutegund er ekki á skrá'.format(nafn))


def bua_til_aukahlut_tegund(nafn, vöruflokkur):
    if session.query(Aukahlutir_tegund).filter(Aukahlutir_tegund.nafn==nafn).all():
        raise crud_exc.ItemAlreadyStored('"{}" Tegund er nú þegar á skrá'.format(nafn))

    add_tegund = Aukahlutir_tegund(nafn=nafn)
    add_tegund.vöruflokkur = get_vöruflokkur_nafn( vöruflokkur )
    session.add( add_tegund  )
    session.commit()
    return add_tegund

def get_ExtrasCategorys_by_category(category):
    tegundir = session.query(Aukahlutir_tegund).join(Vöruflokkar).filter(Vöruflokkar.nafn==category).all()
    return tegundir

def get_ExtrasCategorys_by_category_names(category):
    tegundir = session.query(Aukahlutir_tegund).join(Vöruflokkar).filter(Vöruflokkar.nafn==category).all()
    return [item.nafn for item in tegundir]


def breyta_aukahlut_tegund(nafn, vöruflokkur, rowid):
    tegund = session.query(Aukahlutir_tegund).filter(Aukahlutir_tegund.id==rowid).first()
    if tegund:
        tegund.nafn = nafn
        tegund.vöruflokkur = get_vöruflokkur_nafn( vöruflokkur )              
    else:
        raise crud_exc.ItemNotStored('"{}" Tegund aukahlutar er ekki á skrá'.format(nafn))
    session.commit()
    return tegund

def delete_extrasCategory(rowid):
    tegund = session.query(Aukahlutir_tegund).filter(Aukahlutir_tegund.id==rowid).first()
    if tegund:
        session.delete( tegund )
        session.commit()              
    else:
        raise crud_exc.ItemNotStored('"{}" Tegund aukahlutar er ekki á skrá'.format(rowid))

def birta_aukahluti_vara(vara, vörutegund, aukahlutur_tegund ):
    get_aukahlutir_vara_flokkur_tegund( vara, vörutegund, aukahlutur_tegund)

def bua_til_aukahlut(lýsing, verð, tegund):
    add_aukahlutur = Aukahlutir( lýsing = lýsing, verð = verð)
    add_aukahlutur.aukahlutur_tegund = get_aukahlutur_tegund( tegund )
    session.add( add_aukahlutur )
    session.commit()
    return add_aukahlutur

def breyta_aukahlut(lýsing, verð, tegund, rowid):
    aukahlutur = session.query(Aukahlutir).filter(Aukahlutir.id==rowid).all()
    if aukahlutur:
        aukahlutur.lýsing = lýsing
        aukahlutur.verð = verð
        aukahlutur.aukahlutur_tegund = get_aukahlutur_tegund( tegund )
    else:
        raise crud_exc.ItemNotStored('"{}" aukahlutur með id ekki á skrá'.format(rowid))
    session.commit()
    return aukahlutur

def delete_extras(rowid):
    aukahlutur = session.query(Aukahlutir).filter(Aukahlutir.id==rowid).first()
    if tegund:
        session.delete( aukahlutur )
        session.commit()              
    else:
        raise crud_exc.ItemNotStored('"{}" Aukahlutur er ekki á skrá'.format(rowid))

"""
def add_extras_to_product(vara, vörutegund, tegund):
    add_to_vara = session.query(Vara).join(Vörutegund).\
        filter(Vörutegund.nafn == vörutegund).filter(Vara.nafn == vara).first() 
    if add_to_vara:
        # Fill here functionality
        add_to_vara.aukahlutir =  get_aukahlutur_tegund( tegund ).aukahlutir 
        session.commit()
    
    else:
        raise crud_exc.ItemNotStored ('"{}" Vara er ekki til á skrá!'.format(vara))
"""

def add_extras_to_product(product, extra):
    get_ids = [item.id for item in product.aukahlutir]
    for item in get_ids:
        if(item==extra.id):
            print('This Product allready has this optional extra')
            return
    product.aukahlutir.append(extra)
    session.commit()

def remove_extras_from_product(product, extra):
    get_ids = [item.id for item in product.aukahlutir]
    i=0
    for item in get_ids:
        if(item==extra.id):
            print('Remove optional extra from product at index', i)
            product.aukahlutir.pop(i)
            session.commit()
        i+=1

def get_added_extrasToProduct_by_category(extras, category):
    tmp_arr = []
    for item in extras:
        if(item.aukahlutur_tegund.nafn==category):
            tmp_arr.append( item )
    return tmp_arr

def make_order(costumer ):
    if costumer:
        session.commit()
    else:
        raise crud_exc.ItemNotStored('"{}" Viðskiptavinur er ekki á skrá'.format(eiginnafn))

print(session.query(Pantanir).all())
#print(session.query(Viðskiptavinir).filter(Viðskiptavinir.id==1).first().vörur)
#print(session.query(Pantanir).filter(Pantanir.viðskiptavinir.eiginnafn=='Halldór').all())

def bua_til_vidskiptavin(eiginnafn, eftirnafn, kt, simi, netfang, heimilisfang, postnumer ):
    if(session.query(Viðskiptavinir).filter(Viðskiptavinir.kt==kt).all()):
        
        raise crud_exc.ItemAlreadyStored('"{}" Viðskiptavinur með þessa kennitölu er nú þegar á skrá!'.format(kt))
    
    else:
        add_user = Viðskiptavinir( 
            eiginnafn = "".join(eiginnafn.split() ),  
            eftirnafn = "".join(eftirnafn.split() ),  
            kt = "".join(kt.split()))
            
        add_user.heimilisföng = [ Heimilisfang(
            heimilisfang = "".join(heimilisfang.split()),  
            póstnúmer = "".join(postnumer.split() ) 
            )]

        add_user.símanúmer = [ Símanúmer( símanúmer = "".join(simi.split()))]
        
        add_user.netföng = [Netfang( netfang = "".join(netfang.split()))]
        
        session.add( add_user  )
        
        session.commit()
    return add_user


def breyta_viðskiptavin(eiginnafn, eftirnafn, kt, simi, email, heimilisfang, postnumer):
    vv = session.query(Viðskiptavinir).filter(Viðskiptavinir.kt==kt).first()
    if vv:
        vv.eiginnafn = eiginnafn
        vv.eftirnafn = eftirnafn
        vv.kt = kt
        vv.símanúmer[0].símanúmer = simi
        vv.netföng[0].netfang = email
        vv.heimilisföng[0].póstnúmer = postnumer
        vv.heimilisföng[0].heimilisfang = heimilisfang
                 
    else:
        raise crud_exc.ItemNotStored('"{}" Viðskiptavinur er ekki á skrá'.format(eiginnafn))

    session.commit()
    return vv

"""
def birta_alla_vidskiptavini():
    vv_listi = enumerate([ item for item in session.query(Viðskiptavinir).all()])
    tmp_array = []
    for i, k in vv_listi:
        tmp_array.append({
            'eiginnafn': k.eiginnafn, 
            'eftirnafn': k.eftirnafn,
            'kennitala': k.kt,  
            'sími': k.símanúmer[0].símanúmer, 
            'email': k.netföng[0].netfang , 
            'heimilisfang': k.heimilisföng[0].heimilisfang,
            'póstnúmer': k.heimilisföng[0].póstnúmer  })
    return tmp_array
 """ 

def birta_alla_vidskiptavini():
    return session.query(Viðskiptavinir).all() 
  
def birta_vidskiptavin(eiginnafn):
    vv = session.query(Viðskiptavinir).filter(Viðskiptavinir.eiginnafn==eiginnafn).all()
    if vv:
        if(len(vv) == 1 ):
            tmp_array = []
            for k in vv:
                tmp_array.append({
                    'eiginnafn': k.eiginnafn, 
                    'eftirnafn': k.eftirnafn,
                    'kennitala': k.kt,  
                    'sími': k.símanúmer[0].símanúmer, 
                    'email': k.netföng[0].netfang , 
                    'heimilisfang': k.heimilisföng[0].heimilisfang,
                    'póstnúmer': k.heimilisföng[0].póstnúmer  })
            return tmp_array[0]
          
        
        else:
            tmp_array = []
            for k in vv:
                tmp_array.append({
                    'eiginnafn': k.eiginnafn, 
                    'eftirnafn': k.eftirnafn,
                    'kennitala': k.kt,  
                    'sími': k.símanúmer[0].símanúmer, 
                    'email': k.netföng[0].netfang , 
                    'heimilisfang': k.heimilisföng[0].heimilisfang,
                    'póstnúmer': k.heimilisföng[0].póstnúmer  })
            return tmp_array
                 
    else:
        raise crud_exc.ItemNotStored('"{}" Viðskiptavinur er ekki á skrá'.format(eiginnafn))

def delete_costumer(rowid):
    vv = session.query(Viðskiptavinir).filter(Viðskiptavinir.id==rowid).first()
    if vv:
        session.delete(vv)
        session.commit()
        print("Eyði Viðskiptavin", vv.eiginnafn)

    else:
        raise crud_exc.ItemNotStored(' Viðskiptavinur " {}" er ekki á skrá '.format(vv.eiginnafn))
    return 0

#a_dict = get_aukahlutir_vara_flokkur_tegund('SF 390','On Tour','Chassis')[0]
#print( a_dict.get('Lýsing') )

#print( get_attr_vara_by_tegund('SF 390', 'On Tour','verð') )


############### Test Records
#breyta_viðskiptavin( "Halldór", "Jónsson", "2805807109", "8212651", "dude@gmail.com", "Mávahlíð 181", "105")
#print(birta_vidskiptavin("Jóna"))
#eyda_vidskiptavin("2811104378")
#print(session.query(Vara).all())
#vv = session.query(Viðskiptavinir).get(1)
#vara = session.query(Vara).get(1)
#vv.vörur = [ vara ]
#print(vv.vörur[0].verð)
#print(vv)
#bua_til_vidskiptavin( "Halldór", "Jónsson", "2805807109", "8212651", "dude@gmail.com", "Mávahlíð 11", "105")
"""
bua_til_vöruflokk('Hjólhýsi')
bua_til_vöruflokk('Hjólhýsa Drif')
bua_til_vöruflokk('Tjöld')
bua_til_framleiðanda('Trigano','Nina', 'Hansen','3456789', 'ert@doo.com', ' Hanover', '2345-3455')
bua_til_framleiðanda('Hobby','Sonia', 'Schmidt','345458', 'ss@hobby.com', 'Hambourg', 'e945-t455')
bua_til_vörutegund('On Tour', 'Hjólhýsi','Hobby' )
bua_til_vörutegund('Deluxe', 'Hjólhýsi','Hobby' )
bua_til_vörutegund('Deluxe Edition', 'Hjólhýsi','Hobby' )
bua_til_vörutegund('Excellent', 'Hjólhýsi','Hobby' )
bua_til_vörutegund('Prestige', 'Hjólhýsi','Hobby' )
bua_til_vörutegund('Premium', 'Hjólhýsi','Hobby' )
bua_til_vöru('SF 390', '15700', 'On Tour')

bua_til_aukahlut_tegund('Chassis', 'Hjólhýsi')
bua_til_aukahlut_tegund('Load Capacity', 'Hjólhýsi')
bua_til_aukahlut_tegund('Wheel Rims', 'Hjólhýsi')
bua_til_aukahlut_tegund('Window', 'Hjólhýsi')
bua_til_aukahlut_tegund('Body', 'Hjólhýsi')
bua_til_aukahlut_tegund('Living Area', 'Hjólhýsi')
bua_til_aukahlut_tegund('Upholstery Combinations', 'Hjólhýsi')
bua_til_aukahlut_tegund('Kitchen', 'Hjólhýsi')
bua_til_aukahlut_tegund('Sleeping Area', 'Hjólhýsi')
bua_til_aukahlut_tegund('Washroom', 'Hjólhýsi')
bua_til_aukahlut_tegund('Water Gas Electricity', 'Hjólhýsi')
bua_til_aukahlut_tegund('Lighting', 'Hjólhýsi')
bua_til_aukahlut_tegund('Heating Air Conditioning', 'Hjólhýsi')
bua_til_aukahlut_tegund('Multimedia', 'Hjólhýsi')
bua_til_aukahlut_tegund('Contry Specifications', 'Hjólhýsi')


bua_til_aukahlut('Alloy spare wheel black polished with holder', '481', 'Chassis')
bua_til_aukahlut('Alloy spare wheel black polished with holder, instead of tyre repair set', '481', 'Chassis')
bua_til_aukahlut('Spare wheel with holder, underfloor mounting', '345', 'Chassis')
bua_til_aukahlut('Spare wheel with holder, instead of tyre repair set, underfloor mounting', '345', 'Chassis')
bua_til_aukahlut('Load indicator on the jockey wheel', '159', 'Chassis')
bua_til_aukahlut('Stabilisation system KNOTT ETS Plus', '773', 'Chassis')
bua_til_aukahlut('Hitch lock anti-theft device WINTERHOFF (ROBSTOP)', '161', 'Chassis')

bua_til_aukahlut('Decrease in load capacity without any technical modifications', '0', 'Load Capacity')
bua_til_aukahlut('Increase in load capacity without any technical modifications', '0', 'Load Capacity')
bua_til_aukahlut('Increase in load capacity with technical modification for single-axle vehicles, including black alloy rims', '995', 'Load Capacity')
bua_til_aukahlut('Increase in load capacity with technical modification for single-axle vehicles', '391', 'Load Capacity')
bua_til_aukahlut('Increase in load capacity with technical modification for tandem-axle vehicles', '495', 'Load Capacity')
bua_til_aukahlut('Increase in load capacity with technical modification for single-axle vehicles, Premium', '563', 'Load Capacity')

bua_til_aukahlut('Alloy rims silver, up to model 560', '481', 'Wheel Rims')
bua_til_aukahlut('Alloy rims silver, from model 620', '725', 'Wheel Rims')
bua_til_aukahlut('Alloy rims black, polished, up to model 560', '604', 'Wheel Rims')
bua_til_aukahlut('Alloy rims black, polished, from model 620', '959', 'Wheel Rims')

bua_til_aukahlut('Front window with fully integrated pleated blackout blind and insect screen', '451', 'Window')

bua_til_aukahlut('Rear lights with dynamic indicator', '230', 'Body')
bua_til_aukahlut('Roof awning THULE OMNISTOR 6300, width 260 cm, pull-out depth 200 cm', '887', 'Body')
bua_til_aukahlut('Roof awning THULE OMNISTOR 6300, width 300 cm, pull-out depth 250 cm', '952', 'Body')
bua_til_aukahlut('Roof awning THULE OMNISTOR 6300, width 350 cm, pull-out depth 250 cm', '1085', 'Body')
bua_til_aukahlut('Roof awning THULE OMNISTOR 6300, width 400 cm, pull-out depth 250 cm', '1359', 'Body')
bua_til_aukahlut('Roof awning THULE OMNISTOR 6300, width 450 cm, pull-out depth 250 cm', '1534', 'Body')
bua_til_aukahlut('Roof awning THULE OMNISTOR 6300, width 500 cm, pull-out depth 250 cm', '1706', 'Body')
bua_til_aukahlut('Bicycle rack THULE, for drawbar, 2 bicycles, loading capacity 60 kg', '294', 'Body')
bua_til_aukahlut('Bicycle rack THULE, for rear, 2 bicycles, loading capacity 40 kg', '306', 'Body')
bua_til_aukahlut('Garage under bunk bed (not in conjunction with hot water heater ALDE, colouring board under children’s bed removed)', '666', 'Body')
bua_til_aukahlut('Locker door THETFORD with central locking, 752 x 310 mm, lockable (optional)', '248', 'Body')

bua_til_aukahlut('Single-post lift table', '221', 'Living Area')
bua_til_aukahlut('Carpet in the living area, removable', '275', 'Living Area')
bua_til_aukahlut('Carpet in the living area, removable', '219', 'Upholstery Combinations')

bua_til_aukahlut('Combined hob / oven including grill THETFORD', '995', 'Kitchen')
bua_til_aukahlut('Oven THETFORD with electric ignition, grill and interior light, 36 litres', '566', 'Kitchen')
bua_til_aukahlut('Extractor hood DOMETIC including Hobby 10-stage speed control', '286', 'Kitchen')
bua_til_aukahlut('Microwave DOMETIC, 20 litres', '317', 'Kitchen')

bua_til_aukahlut('Bed extension for single beds including cushion', '340', 'Sleeping Area')
bua_til_aukahlut('Cold foam mattress, with 7 zones and slatted bed base for double bed and queen-size bed', '572', 'Sleeping Area')
bua_til_aukahlut('Cold foam mattresses, with 7 zones and slatted bed base for single beds', '596', 'Sleeping Area')
bua_til_aukahlut('Children’s bed, 3 tiers with guard and ladder', '430', 'Sleeping Area')
bua_til_aukahlut('Children’s bed, 3 tiers including 3rd window, with guard and ladder', '490', 'Sleeping Area')
bua_til_aukahlut('Bedspread', '196', 'Sleeping Area')

bua_til_aukahlut('Shower fitting and shower curtain for washroom with external washbasin', '160', 'Washroom')
bua_til_aukahlut('Blackout blind including insect screen for washroom', '104', 'Washroom')
bua_til_aukahlut('Clothes rail in the shower', '137', 'Washroom')


bua_til_aukahlut('Fresh water tank, 47 litres', '153', 'Water Gas Electricity')
bua_til_aukahlut('TFT control panel for lighting system and tank, including CI-BUS', '188', 'Water Gas Electricity')
bua_til_aukahlut('Exterior awning socket, including 230 V output, satellite / TV connection', '133', 'Water Gas Electricity')
bua_til_aukahlut('Adapter 7 - 13 pole for passenger vehicle connecting cable', '35', 'Water Gas Electricity')
bua_til_aukahlut('City water connection', '192', 'Water Gas Electricity')
bua_til_aukahlut('External gas socket', '226', 'Water Gas Electricity')
bua_til_aukahlut('Electric boiler TRUMA, 14 litres (locker door can be removed)', '449', 'Water Gas Electricity')
bua_til_aukahlut('Water pump with additional switch', '48', 'Water Gas Electricity')
bua_til_aukahlut('Autonomy package including charge controller with booster, battery, battery sensor and battery case', '645', 'Water Gas Electricity')
bua_til_aukahlut('Prepara on for autonomy package including charge controller with booster, battery sensor and battery case', '350', 'Water Gas Electricity')
bua_til_aukahlut('HOBBY-CONNECT, remote control for on-board technology using app', '741', 'Water Gas Electricity')
bua_til_aukahlut('Wireless remote control for the lighting system with one handset', '161', 'Water Gas Electricity')
bua_til_aukahlut('Dual USB charging socket', '55', 'Water Gas Electricity')
bua_til_aukahlut('Dual USB charging socket and children’s bed lights including USB charging socket', '93', 'Water Gas Electricity')

bua_til_aukahlut('Ambient lighting, design dependent on model', '277', 'Lighting')

bua_til_aukahlut('Heating system TRUMA Combi 6 E, instead of Combi 4', '791', 'Heating Air Conditioning')
bua_til_aukahlut('Heating system TRUMA Combi 6 E, instead of Combi 6', '624', 'Heating Air Conditioning')
bua_til_aukahlut('Auxiliary electric heater TRUMA Ultraheat including CI-BUS', '454', 'Heating Air Conditioning')
bua_til_aukahlut('Underfloor heating up to model 540', '555', 'Heating Air Conditioning')
bua_til_aukahlut('Underfloor heating from model 545', '689', 'Heating Air Conditioning')
bua_til_aukahlut('Hot water heater ALDE COMPACT 3020 HE including CI-BUS', '2530', 'Heating Air Conditioning')
bua_til_aukahlut('Hot water underfloor heating for hot water heater ALDE', '1219', 'Heating Air Conditioning')
bua_til_aukahlut('Roof-mounted air conditioning unit DOMETIC FreshJet including CI-BUS, with heating function, without lighting, 2.2 KW', '1976', 'Heating Air Conditioning')
bua_til_aukahlut('Prepara on for roof-mounted air conditioning unit', '69', 'Heating Air Conditioning')

bua_til_aukahlut('Pull-out shelf for  flat screen TV including required connections, without video cables (Cinch)', '198', 'Multimedia')
bua_til_aukahlut('Articulated TV bracket including required connections, without video cables (Cinch)', '234', 'Multimedia')
bua_til_aukahlut('ATV aerial mast TELECO', '208', 'Multimedia')

bua_til_aukahlut('Registra on documents', '139', 'Contry Specifications')
"""

########## END of test records




