import os
import sys
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

#Base
Base = declarative_base()


class Framleiðandi(Base):
    __tablename__ = 'framleiðandi'
    id = Column(Integer, primary_key=True)
    nafn = Column(String(50), nullable=False)
    vörutegundir = relationship("Vörutegund", back_populates='framleiðandi', cascade="all, delete, delete-orphan")
    tengiliðir =  relationship("Tengiliður", back_populates='framleiðandi', cascade="all, delete, delete-orphan")
    
    def __repr__(self):
        return "<Framleiðandi(nafn='%s')>" % (self.nafn)

class Tengiliður(Base):
    __tablename__ = 'tengiliður'
    id = Column(Integer, primary_key=True)
    eiginnafn = Column(String(250), nullable=False)
    eftirnafn = Column(String(250), nullable=False)
    netföng = relationship("Netfang", back_populates='tengiliður', cascade="all, delete, delete-orphan")
    símanúmer = relationship("Símanúmer", back_populates='tengiliður', cascade="all, delete, delete-orphan")
    framleiðandi_id = Column(Integer, ForeignKey('framleiðandi.id'))
    framleiðandi = relationship("Framleiðandi", back_populates='tengiliðir')

    def __repr__(self):
        return "<Tengiliður(eiginnafn='%s', eftirnafn='%s')>" % (self.eiginnafn, self.eftirnafn)


class Vöruflokkar(Base):
    __tablename__ = 'vöruflokkar'
    id = Column(Integer, primary_key=True)
    nafn = Column(String(50), nullable=False)
    vörutegundir = relationship("Vörutegund", back_populates='vöruflokkur', cascade="all, delete, delete-orphan")
    aukahlutir_tegundir = relationship("Aukahlutir_tegund", back_populates='vöruflokkur', cascade="all, delete, delete-orphan")
    
    def __repr__(self):
        return "<Vörutegund(nafn='%s')>" % (self.nafn)

class Vörutegund(Base):
    __tablename__ = 'vörutegund'
    id = Column(Integer, primary_key=True)
    nafn = Column(String(50), nullable=False)
    vöruflokkur_id = Column(Integer, ForeignKey('vöruflokkar.id')) 
    framleiðandi_id = Column(Integer, ForeignKey('framleiðandi.id'))
    framleiðandi = relationship("Framleiðandi", back_populates="vörutegundir")
    vöruflokkur = relationship("Vöruflokkar", back_populates="vörutegundir")
    vörur = relationship("Vara", back_populates="vörutegundir")
    
    def __repr__(self):
        return "<Vörutegund(nafn='%s')>" % (self.nafn)


class Viðskiptavinir(Base):
    __tablename__ = 'viðskiptavinir'
    id = Column(Integer, primary_key=True)
    eiginnafn = Column(String(250), nullable=False)
    eftirnafn = Column(String(250), nullable=False)
    kt = Column(String(10), nullable=False)
    heimilisföng = relationship("Heimilisfang", back_populates='viðskiptavinur', cascade="all, delete, delete-orphan")
    netföng = relationship("Netfang", back_populates='viðskiptavinur', cascade="all, delete, delete-orphan")
    símanúmer = relationship("Símanúmer", back_populates='viðskiptavinur', cascade="all, delete, delete-orphan")
    vörur = relationship("Vara", secondary="pantanir", back_populates='viðskiptavinir')

    def __repr__(self):
        return "<Viðskiptavinir(eiginnafn='%s', eftirnafn='%s', kt='%s')>" % (self.eiginnafn, self.eftirnafn, self.kt)

class Vara(Base):
    __tablename__ = 'vara'
    id = Column(Integer, primary_key=True)
    nafn = Column(String(50), nullable=False)
    verð = Column(String(50), nullable=False)
    vöruflokkur_id = Column(Integer, ForeignKey('vöruflokkar.id'))
    vörutegund_id = Column(Integer, ForeignKey('vörutegund.id'))
    vörutegundir =  relationship("Vörutegund", back_populates='vörur')
    aukahlutir =  relationship("Aukahlutir", back_populates='vörur')
    viðskiptavinir = relationship("Viðskiptavinir", secondary="pantanir", back_populates='vörur')
    
    def __repr__(self):
        return "<Vara(nafn='%s', verð='%s')>" % (self.nafn, self.verð)

class Pantanir(Base):
    __tablename__ = 'pantanir'
    id = Column(Integer, primary_key=True)
    viðskiptavinur_id = Column(Integer,ForeignKey('viðskiptavinir.id'))
    vara_id = Column(Integer, ForeignKey('vara.id'))
    def __repr__(self):
        return "<Pantanir(viðskiptavinur_id='%s', vara_id='%s')>" % (self.viðskiptavinur_id, self.vara_id)

class Aukahlutir_tegund(Base):
    __tablename__ = 'aukahlutir_tegund'
    id = Column(Integer, primary_key=True)
    nafn = Column(String(50), nullable=False)
    vöruflokkur_id = Column(Integer, ForeignKey('vöruflokkar.id'))
    vöruflokkur = relationship("Vöruflokkar", back_populates='aukahlutir_tegundir')
    aukahlutir = relationship("Aukahlutir", back_populates='aukahlutur_tegund', cascade="all, delete, delete-orphan")
    
    def __repr__(self):
        return "<Aukahlutir_tegund(nafn='%s')>" % (self.nafn)


class Aukahlutir(Base):
    __tablename__ = 'aukahlutir'
    id = Column(Integer, primary_key=True)
    lýsing = Column(String(250), nullable=False)
    verð = Column(String(50), nullable=False)
    aukahlutur_tegund_id = Column(Integer, ForeignKey('aukahlutir_tegund.id'))
    aukahlutur_tegund = relationship("Aukahlutir_tegund", back_populates='aukahlutir')
    vara_id = Column(Integer, ForeignKey('vara.id'))
    vörur = relationship("Vara", back_populates='aukahlutir')
    
    def __repr__(self):
        return "<Aukahlutir(lýsing='%s', verð='%s')>" % (self.lýsing, self.verð)


class Heimilisfang(Base):
    __tablename__ = 'heimilisfang'
    id = Column(Integer, primary_key=True)
    heimilisfang = Column(String(250), nullable=False)
    póstnúmer = Column(String(3), nullable=False)
    viðskiptavinur_id = Column(Integer, ForeignKey('viðskiptavinir.id'))
    viðskiptavinur = relationship("Viðskiptavinir", back_populates="heimilisföng")

    def __repr__(self):
        return "<Heimilisfang(heimilisfang='%s', póstnúmer='%s')>" % (self.heimilisfang, self.póstnúmer)

class Netfang(Base):
    __tablename__ = 'netfang'
    id = Column(Integer, primary_key=True)
    netfang = Column(String(250), nullable=False)
    viðskiptavinur_id = Column(Integer, ForeignKey('viðskiptavinir.id'))
    viðskiptavinur = relationship("Viðskiptavinir", back_populates="netföng")
    tengiliður_id = Column(Integer, ForeignKey('tengiliður.id'))
    tengiliður = relationship("Tengiliður", back_populates="netföng")

    def __repr__(self):
        return "<Netfang(netfang='%s')>" % (self.netfang)

class Símanúmer(Base):
    __tablename__ = 'símanúmer'
    id = Column(Integer, primary_key=True)
    símanúmer = Column(String(7), nullable=False)
    viðskiptavinur_id = Column(Integer, ForeignKey('viðskiptavinir.id'))
    viðskiptavinur = relationship("Viðskiptavinir", back_populates="símanúmer")
    tengiliður_id = Column(Integer, ForeignKey('tengiliður.id'))
    tengiliður = relationship("Tengiliður", back_populates="símanúmer")

    def __repr__(self):
        return "<Símanúmer(símanúmer='%s')>" % (self.símanúmer)

# Create an engine that stores data in the local directory's
engine = create_engine('sqlite:///test_relations.db')

# Create all tables in the engine: "Create Table" statements in raw SQL.
Base.metadata.create_all(engine)

