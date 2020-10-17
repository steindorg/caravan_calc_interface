#################################### Útreikningarföll

def lista_verd(listaverd_eu):
    afsl_14_prosent =  ( listaverd_eu * ( -1 ) ) * 0.14
    listaverd_med_afsl = listaverd_eu + afsl_14_prosent
    return listaverd_med_afsl

def fob_verd(listaverd_eu):
    afsl_14_prosent =  ( listaverd_eu * ( -1 ) ) * 0.14
    listaverd_med_afsl = listaverd_eu + afsl_14_prosent
    afreiknadur_19_prosent_vsk = ( -( listaverd_med_afsl/119 ) * 19  )

    return round( listaverd_med_afsl + afreiknadur_19_prosent_vsk )

def verd_kronur(listaverd_eu, gengi):
    return fob_verd(listaverd_eu) * gengi

def cif_verd(listaverd_eu, gengi, frakt):
    tryggingar = verd_kronur(listaverd_eu, gengi) * 0.005
    return verd_kronur(listaverd_eu, gengi) + frakt + tryggingar

def tollur_13(listaverd_eu, gengi, frakt):
    return round(cif_verd(listaverd_eu, gengi, frakt) * 0.13)
    
def vsk(listaverd_eu, gengi, frakt):
    return round(( cif_verd(listaverd_eu, gengi, frakt) + tollur_13(listaverd_eu, gengi, frakt) ) * 0.24)

def til_landsins(listaverd_eu, gengi, frakt):
    verd_til_landsins = cif_verd(listaverd_eu, gengi, frakt) + tollur_13(listaverd_eu, gengi, frakt) + vsk(listaverd_eu, gengi,frakt)
    return round(verd_til_landsins)

def format_verð(number): 
    return ("{:,}".format(number))

def format_toInt(string): 
    return (int(string.replace(',', '')))

    

