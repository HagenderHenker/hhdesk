import data_01_allgemein as allgemein
import data_02_hhsatzung as hhdaten
import data_03_ergebnis as erg
import numpy as np 
import pandas as pd
import pathlib
import docxtpl
import dataimport as di
import enviromentvar as env


def hhsatzung(gde, hhj, xlsgrunddaten, xlsbewegung):
    #dictgde = allgemein.gdegrunddaten(xlsfilegrunddaten=xlsgrunddaten, gde=gde)
    dictgde = allgemein.gdegrunddaten(xlsfilegrunddaten=xlsgrunddaten, gde=60)
    dictbew = hhdaten.hhsatzungbewegung(gde = gde, hhj = hhj, hhbewfile=xlsbewegung)
    dicthhgd = hhdaten.hhsatzunggrunddatenhh(xlsfile = xlsgrunddaten, gdenr=gde, hhj=hhj)
    #print(f"dictgde: {dictgde}")
    #print(f"dictbew: {dictbew}")
    #print(f"dicthhgd: {dicthhgd}")    
    conhhsatzung = dictgde | dictbew | dicthhgd
    ekvvj = hhdaten.hhsatzungekvvj(gdenr=gde, hhj=hhj, xlsfile=xlsgrunddaten)/100
    ekvj = ekvvj + dictbew["saldo_vj"]
    ekhhj = ekvj + dictbew["erg_saldo"]
    ikred_verzinst = dictbew["ikred_aufnahme"] - dicthhgd["ikred_zinslos"]
    conhhsatzung["ek_vvj"] = ekvvj
    conhhsatzung["ek_vj"] = ekvj
    conhhsatzung["ek_hhj"] = ekhhj
    conhhsatzung["ikred_verzinst"] = ikred_verzinst
    return conhhsatzung

def hh_vorbericht_01_Allgemeines(dfhhs, dfgdegrunddaten, dfewentwicklung, dfewaltersgliederung, dfewalteru20, dfflaeche, quelleewdaten, quelleflaeche, doc):
    
    #dfgdegrunddaten.head()

    """
    gde_bez:			#Gemeindebezeichnung: zusammenfassung der Felder Gemeindetyp und 
    hhj:				#Haushaltsjahr für das ein Vorbericht erstellt wird
    gde_typ:			#Ortsgemeinde, Stadt, Verbandsgemeinde
    bm_typ:				#Ortsbürgermeister, Stadtbürgermeister, Bürgermeister
    hhj-1:				#Vorjahr der Haushaltsplanung
    EW_akt:				#Aktuelle Einwohnerzahl
    img_einwohnerentwicklung:	#Graph der Einwohnerentwicklung der letzten 10 Jahre
    img_altersstruktur:		#Graph, Alterspyramide der Einwohner/Bürger
    img_struktur_altersgruppebis20: #Graph der Einwohnerentwicklung bis 20 Jahre
    quelleewdaten:			#Woher stammen die Einwohnerdaten
    flaeche:			#Gesamtfläche der Gemeinde in km²
    img_flaeche:			#Graph der Flächennutzung
    quelleflaeche:			#Woher stammen die Flächendaten
    """
    #print(dfhhs)

    hhj = dfhhs["hhj"].values[0]
    #print(type(doc))
    #print(hhj)
    dfewakt = dfewentwicklung.loc[(dfewentwicklung["gdenr"] == 60) & (dfewentwicklung["datum"] == np.datetime64(f'{hhj-1}-06-30')) & (dfewentwicklung["wohnstatus"] == "Einwohner mit Hauptwohnung") ]
    ew_akt = dfewakt["maennl"].values[0] +dfewakt["weibl"].values[0]
    #print(ew_akt)
    #print(type(ew_akt))
    flaeche = dfflaeche["km²"].sum()
    bild1 = str(pathlib.Path.cwd() / "hhdaten/plots/bev-entw.png")
    #print(bild1)
    conhh_vorb_allg = {
    "gde_bez" : dfgdegrunddaten.gde_bez.values[0], 	#Gemeindebezeichnung: zusammenfassung der Felder Gemeindetyp und 
    "hhj" : hhj,				                    #Haushaltsjahr für das ein Vorbericht erstellt wird
    "gde_typ" : dfgdegrunddaten["gde_typ"].values[0],       #Ortsgemeinde, Stadt, Verbandsgemeinde
    "bm_typ" : dfgdegrunddaten["bm_typ"].values[0],			#Ortsbürgermeister, Stadtbürgermeister, Bürgermeister

    "hhj-1" : hhj-1,        				        #Vorjahr der Haushaltsplanung
    "EW_akt" : ew_akt,         		                #Aktuelle Einwohnerzahl
    "img_einwohnerentwicklung" : docxtpl.InlineImage(doc, bild1),               #Graph der Einwohnerentwicklung der letzten 10 Jahre
 #   "img_altersstruktur" : docxtpl.InlineImage(doc, pathlib.Path.cwd() / "hhdaten/plots/bev-entw.png"),               #Graph, Alterspyramide der Einwohner/Bürger
 #   "img_struktur_altersgruppebis20" : docxtpl.InlineImage(doc, pathlib.Path.cwd() / "hhdaten/plots/bev-entw.png"),             #Graph der Einwohnerentwicklung bis 20 Jahre
 #   "quelleewdaten" : quelleewdaten,                 #Woher stammen die Einwohnerdaten
    "flaeche" : flaeche,			                #Gesamtfläche der Gemeinde in km²
   # "img_flaeche" : docxtpl.InlineImage(doc, pathlib.Path.cwd() / "hhdaten/plots/bev-entw.png"),			                        #Graph der Flächennutzung
    #"quelleflaeche" : quelleflaeche                 #Woher stammen die Flächendaten

    }
    return conhh_vorb_allg

def hh_vorbericht_02_verlaufvvj(df):
    ergdict = erg.gesamtplan_vvj(df)

    ja_erledigt_teilsatz = env.ja_erledigt_teilsatz
    erlaeuterung_ergebnis_vvj = env.erlaeuterung_ergebnis_vvj                           #Erläuterungstext zum Ergebnishaushalt
    erlaeuterung_finanz_vvj = env.erlaeuterung_finanz_vvj
    vvj = env.hhj -2	                                #Haushaltsjahr -2
    ergueb = env.ergueb

    ergdict["ja_erledigt_teilsatz"] = ja_erledigt_teilsatz
    ergdict["erlaeuterung_ergebnis_vvj"] = erlaeuterung_ergebnis_vvj
    ergdict["erlaeuterung_finanz_vvj"] = erlaeuterung_finanz_vvj
    ergdict["vvj"] = vvj
    ergdict["hhj"] = env.hhj
    ergdict["ergueb"] = ergueb
    return ergdict


def hh_vorbericht_05_UebersichtErgHH(df):
    ergdict = erg.gesamtplan_erg(df)
    return ergdict

def hh_vorbericht_06_Ertraege(df, dferl, mindiff):

    """
    hhj:        Haushaltsjahr, Quelle environmentvar.py
    gde:        Gemeindenummer, Quelle environmentvar.py

    abweichung: Betrag um die ein Ansatz vom Vorjahresansatz abweichen soll um in der Tabelle aufgenommen zu werden


    steuertbl:  Daten für die tabellarische Darstellung der Steuern, 
    zuwtbl:     Daten für die tabellarische Darstellung der Zuweisungen und Transfererträge, 


    """
    
    steuertbl = erg.get_steuern(df=df, dferl=dferl)
    transfertbl = erg.get_umlagen(df=df, dferl=dferl, mindiff=mindiff)
    oerlegtbl = erg.get_oerE(df=df, dferl=dferl, mindiff=mindiff)
    privattbl = erg.get_prE(df=df, dferl=dferl, mindiff=mindiff)
    kostetbl = erg.get_kostE(df=df, dferl=dferl, mindiff=mindiff)
    sonstetbl = erg.get_sonstE(df=df, dferl=dferl, mindiff=mindiff)
    finetbl = erg.get_finE(df=df, dferl=dferl)


    hhj = env.hhj
    gde = env.gde
   
    ertrdict = {"steuertbl" : steuertbl,
                "transfertbl" : transfertbl,
                "oerlegtbl" : oerlegtbl,
                "privattbl" : privattbl,
                "kostetbl" : kostetbl,
                "sonstetbl" : sonstetbl,
                "finetbl" : finetbl,
                "hhj" : hhj,
                "hhj-1" : hhj-1, }

    return ertrdict



def hh_vorbericht_09_invest(dfneu):
    # Filtern der Maßnahmen
    
    dfmn = dfneu.loc[(dfneu["mn"]!=0)&(dfneu["anshhj"]!=0)]
    print(dfmn)
    dfinve = dfmn.loc[(dfmn["sk"]>680000)&(dfmn["sk"]<690000)]
    dfinva = dfmn.loc[(dfmn["sk"]>780000)&(dfmn["sk"]<790000)]

    #dfa = dfmn.groupby(by=["produkt", "mn"])


    #x = dict(iter(dfa))

    x = dfmn.to_dict("index")
    pdict = {}
    mndict = {}
    produkte = []
    massnahmen = []

    #print(x)
    print(f"x ist folgendes dict:{x}")
    for plstdat in x.values():
        if plstdat["produkt"] not in produkte:
            produkte.append((plstdat["produkt"], plstdat["prbez"]))


    for plstdat in x.values():
        prmn = f"{plstdat['produkt']}-{plstdat['mn']}"
        if prmn not in massnahmen:
            massnahmen.append((prmn, plstdat["mn"], plstdat["txt"], plstdat["mnerl"]))

    #print(produkte)
    #print(massnahmen)

    for produkt, prbez in produkte:
        pdict[produkt] = {"produkt": produkt,
                        "prbez" :  prbez,
                        "massnahmen" : {}
                        }



        for massnahme, mn, text, erlaeuterung in massnahmen:
            eakt = 0
            evj = 0
            aakt = 0
            avj = 0
            #text = "" if text == pd.nan else text
            if text == 0: text = ""
            if erlaeuterung == 0: erlaeuterung = ""

            if massnahme[0:7] == produkt:

                pdict[produkt]["massnahmen"][massnahme] = {"massnahme" : mn,
                                                            "mnbez" : text,
                                                            "mnerl" : erlaeuterung,
                                                            "plst" : {}}

            for plstdat in x.values():
                if f"{plstdat['produkt']}-{plstdat['mn']}" == massnahme:
                    pdict[produkt]["massnahmen"][massnahme]["plst"][plstdat['hhs']] = plstdat
                if 680000 < plstdat["sk"] < 690000:
                    eakt += plstdat["anshhj"]
                    evj += plstdat["ansvj"]
                if 780000 < plstdat["sk"] < 790000:
                    aakt += plstdat["anshhj"]
                    avj += plstdat["ansvj"]

            pdict[produkt]["massnahmen"][massnahme]["eakt"] = eakt
            pdict[produkt]["massnahmen"][massnahme]["aakt"] = aakt
            pdict[produkt]["massnahmen"][massnahme]["sakt"] = eakt - aakt
            pdict[produkt]["massnahmen"][massnahme]["evj"] = evj
            pdict[produkt]["massnahmen"][massnahme]["avj"] = avj
            pdict[produkt]["massnahmen"][massnahme]["svj"] = evj - avj

    produkte = {"produkte" : pdict }
    
    return produkte

if __name__ == "__main__":
    #print test hhsatzungcontext
    #print(hhsatzung(gde=60 , hhj=2023, xlsgrunddaten=str(pathlib.Path.cwd() / "hhdaten/grunddaten.xlsx"),xlsbewegung=str(pathlib.Path.cwd() / "hhdaten/bewegungsdaten.xlsx") ))

    #print test vorbericht-allgemein
    #print(hh_vorbericht_01_Allgemeines(di.hhdata_excelimport(xlsxfile= str(pathlib.Path.cwd() / "hhdaten/bewegungsdaten.xlsx"))))
    
    
    #print(hh_vorbericht_05_UebersichtErgHH(di.hhdata_excelimport(xlsxfile= str(pathlib.Path.cwd() / "hhdaten/bewegungsdaten.xlsx"))))
    #print("test")

    print(hh_vorbericht_06_Ertraege(df=di.hhdata_excelimport(xlsxfile= str(pathlib.Path.cwd() / "hhdaten/bewegungsdaten.xlsx")), dferl = di.erl_excelimport(str(pathlib.Path.cwd() / "hhdaten/bewegungsdaten.xlsx"))))