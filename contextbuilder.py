import data_01_allgemein as allgemein
import data_02_hhsatzung as hhdaten
import data_03_ergebnis as erg
import data_05_LFAG as lfag
import numpy as np 
import pandas as pd
import pathlib
import docxtpl
import dataimport as di
import enviromentvar as env
from datetime import date


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
    bild2 = str(pathlib.Path.cwd() / "hhdaten/plots/flaechennutzung.png")
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
    "img_flaeche" : docxtpl.InlineImage(doc, bild2),			                        #Graph der Flächennutzung
    "quelleflaeche" : quelleflaeche                 #Woher stammen die Flächendaten

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

def hh_vorbericht_03_verlaufvj(df):
    pass


def hh_vorbericht_05_UebersichtErgHH(df, hhj, gde_bez):
    
    ergdict = erg.gesamtplan_erg(df)
    ergdict["hhj"] = hhj
    ergdict["gde_bez"] =gde_bez
    return ergdict

def hh_vorbericht_06_Ertraege(df, dferl, dfstk, dfod, dflfaghhj, dfew, hhj, mindiff, doc):

    """
    hhj:        Haushaltsjahr, Quelle environmentvar.py
    gde:        Gemeindenummer, Quelle environmentvar.py

    abweichung: Betrag um die ein Ansatz vom Vorjahresansatz abweichen soll um in der Tabelle aufgenommen zu werden


    steuertbl:  Daten für die tabellarische Darstellung der Steuern, 
    zuwtbl:     Daten für die tabellarische Darstellung der Zuweisungen und Transfererträge, 


    """
    
    img_Hebesatzentwicklung = str(pathlib.Path.cwd() / "hhdaten/plots/img_hebesatz_entwicklung.png")
    img_Steuerentwicklung = str(pathlib.Path.cwd() / "hhdaten/plots/img_steuer_entwicklung.png")

    steuertbl = erg.get_steuern(df=df, dferl=dferl)
    transfertbl = erg.get_umlagen(df=df, dferl=dferl, mindiff=mindiff)
    oerlegtbl = erg.get_oerE(df=df, dferl=dferl, mindiff=mindiff)
    privattbl = erg.get_prE(df=df, dferl=dferl, mindiff=mindiff)
    kostetbl = erg.get_kostE(df=df, dferl=dferl, mindiff=mindiff)
    sonstetbl = erg.get_sonstE(df=df, dferl=dferl, mindiff=mindiff)
    finetbl = erg.get_finE(df=df, dferl=dferl)


    hhj = env.hhj
    gde = env.gde

    stk = lfag.calculate_steuerkraft(dfstk)
    sza = lfag.sza(dfod=dfod, ew=lfag.einwohner(dfew, hhj=hhj), stk=stk)
    szb = lfag.szb(ew=lfag.einwohner(dfew, hhj=hhj), dfod=dfod, dflfaghhj=dflfaghhj, stk=stk["stkgesamt"], sza=sza["sza"])
    szzo = lfag.szzo(dfod=dfod, dflfaghhj = dflfaghhj, sza=sza["sza"], stk=stk["stkgesamt"] )
   
    ertrdict = {"steuertbl" : steuertbl,
                "transfertbl" : transfertbl,
                "oerlegtbl" : oerlegtbl,
                "privattbl" : privattbl,
                "kostetbl" : kostetbl,
                "sonstetbl" : sonstetbl,
                "finetbl" : finetbl,
                "hhj" : hhj,
                "hhj-1" : hhj-1, 
                "stk" : stk,
                "sza" : sza,
                "szb" : szb,
                "szzo" : szzo,
                "img_Hebesatzentwicklung" : docxtpl.InlineImage(doc,img_Hebesatzentwicklung),
                "img_Steuerentwicklung" : docxtpl.InlineImage(doc,img_Steuerentwicklung), 
                
                }

    return ertrdict


def hh_vorbericht_07_aufwand(df, dferl, mindiff, doc, dfumlagen, umlagesaetze, kfadict, umlageplanungsstellen):

    """
    hhj:        Haushaltsjahr, Quelle environmentvar.py
    gde:        Gemeindenummer, Quelle environmentvar.py

    abweichung: Betrag um die ein Ansatz vom Vorjahresansatz abweichen soll um in der Tabelle aufgenommen zu werden


    steuertbl:  Daten für die tabellarische Darstellung der Steuern, 
    zuwtbl:     Daten für die tabellarische Darstellung der Zuweisungen und Transfererträge, 


    """
    
    stk = kfadict["stk"]["stkgesamt"]
    sza = kfadict["sza"]["sza"]
    szzo = kfadict["szzo"]["endg_zuwZO"]
    

    img_persaufwandstruktur = str(pathlib.Path.cwd() / "hhdaten/plots/img_persaufwandstruktur.png")
    img_EntwicklungUmlagelast = str(pathlib.Path.cwd() / "hhdaten/plots/img_Umlagen.png")


    msdtbl = erg.get_msdA(df=df, dferl=dferl, mindiff=mindiff)
    umltranstbl = erg.get_UmlA(df=df, dferl=dferl, mindiff=mindiff)
    sozAtbl = erg.get_sozA(df=df, dferl=dferl, mindiff=mindiff)
    sonstAtbl = erg.get_sonstA(df=df, dferl=dferl, mindiff=mindiff)
    finAtbl = erg.get_finA(df=df, dferl=dferl, mindiff=mindiff)
    afa = erg.get_AfA(df=df, dferl=dferl),
    
    # die get_AfA Funktion gibt ein Tupel aus der [0]Liste der AfA Planungsstellen (list of dicts) und dem 
    # [1] dictionary der Absummierungen zurück
    hhj = env.hhj
    gde = env.gde
    #print(afa)
    #print(type(afa))
    

    aufwdict = {
                "msdtbl" : msdtbl,
                "umltranstbl" : umltranstbl,
                "sonstAtbl" : sonstAtbl,
                "sozAtbl" : sozAtbl,
                "finAtbl" : finAtbl,
               
                "hhj" : hhj,
                "hhj-1" : hhj-1, 
                "img_persaufwandsstruktur" : docxtpl.InlineImage(doc, img_persaufwandstruktur),
                "img_EntwicklungUmlagelast" : docxtpl.InlineImage(doc, img_EntwicklungUmlagelast), 
                
                "PersaufwHHJ" : erg.sum_personalaufwand(dfbew=df, dferl=dferl)[0],
                "PersaufwVJ" : erg.sum_personalaufwand(dfbew=df, dferl=dferl)[1],
                "abschreibungen" : afa[0][1], 

                "stk" : stk,
                "sza" : sza, 
                "szzo" : szzo,
                "umlgrl" : stk+sza+szzo,
                "umlSaKU" : umlagesaetze["Kreisumlage"]	,
                "umlLastKU" : df.loc[(df["hhs"] == umlageplanungsstellen["Kreisumlage"])] ["anshhj"].values.item(),
                "umlSaVGU"	: umlagesaetze["Verbandsgemeindeumlage"],
                "umlLastVGU" : df.loc[(df["hhs"] == umlageplanungsstellen["Verbandsgemeindeumlage"])]["anshhj"].values.item(),
                "umlSaSoU"	: umlagesaetze["SonderumlageGS"],
                "umlLastSoU" : df.loc[(df["hhs"] == umlageplanungsstellen["SonderumlageGS"])]["anshhj"].values.item(),

                }
    
                
    #print(aufwdict["abschreibungen"])
    return aufwdict

def hh_vorbereicht_08_gesamtfinanzplan(df):

    fd = erg.gesamtplan_fin(df)
    
    findict = {

    }

    return findict


def hh_vorbericht_09_invest(dfneu):
    # Filtern der Maßnahmen
    
    dfmn = dfneu.loc[(dfneu["mn"]!=0)&(dfneu["anshhj"]!=0)]
    #print("DFMN ")
    #print("_________________________________")   
    #print(dfmn)
    dfinve = dfmn.loc[(dfmn["sk"]>680000)&(dfmn["sk"]<690000)]
    dfinva = dfmn.loc[(dfmn["sk"]>780000)&(dfmn["sk"]<790000)]
    dfmn = pd.concat([dfinve, dfinva])
    dfmn = dfmn.sort_values(by=["hhs"])
    #dfa = dfmn.groupby(by=["produkt", "mn"])


    #x = dict(iter(dfa))

    x = dfmn.to_dict("index")
    pdict = {}
    mndict = {}
    produkte = []
    massnahmen = []

    #print(x)
    #print(f"x ist folgendes dict:{x}")

    for plstdat in x.values():
        if (plstdat["produkt"], plstdat["prbez"]) not in produkte:
            produkte.append((plstdat["produkt"], plstdat["prbez"]))
    
    #print(produkte)


    for plstdat in x.values():
        prmn = f"{plstdat['produkt']}-{plstdat['mn']}"
        t=[]
        t = [a[0] for a in massnahmen]
        
        if prmn not in t:
            massnahmen.append((prmn, plstdat["mn"], plstdat["txt"], plstdat["mnerl"]))
            
    
    #print(massnahmen)
    #print(produkte)
    #print(massnahmen)

    for produkt, prbez in produkte:
        #print(f"produkt ist gleich {produkt}")
        pdict[produkt] = {"produkt": produkt,
                        "prbez" :  prbez,
                        "massnahmen" : {}
                        }


        #print(f"nach Produkt hinzugefügt: \n \n {pdict}")
        for massnahme, mn, text, erlaeuterung in massnahmen:
            #print(f"MN: {massnahme} mnummer: {mn}, text: {text}, erl: {erlaeuterung}")
            eakt = 0
            evj = 0
            aakt = 0
            avj = 0
            #text = "" if text == pd.nan else text
            if text == 0: text = ""
            if erlaeuterung == 0: erlaeuterung = ""
            
            if massnahme[0:7] == produkt:
                #print(f"... MN .......{massnahme[0:7]}")
                pdict[produkt]["massnahmen"][massnahme] = {"massnahme" : mn,
                                                            "mnbez" : text,
                                                            "mnerl" : erlaeuterung,
                                                            "plst" : {}}
                
                #print(f"nach Maßnahme hinzugefügt: \n \n {pdict}")
                for plstdat in x.values():
                    if f"{plstdat['produkt']}-{plstdat['mn']}" == massnahme:
                        #print(massnahme)
                        #print(produkt)
                        pdict[produkt]["massnahmen"][massnahme]["plst"][plstdat['hhs']] = plstdat
                        #print(pdict)
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
                eakt = 0
                evj = 0
                aakt = 0
                avj = 0

    produkte = {"produkte" : pdict }
    
    return produkte

def hh_vorbericht_10_kredit(dfbew, dfschulden, dfliq, hhj, gde, doc):

    hhj = hhj
    gde = gde
    
    img_Liquiditaet = str(pathlib.Path.cwd() / "hhdaten/plots/img_liquiditaetsentwicklung.png")
    img_verschuldung = str(pathlib.Path.cwd() / "hhdaten/plots/img_schuldennominal.png")
    img_prokopfverschuldung = str(pathlib.Path.cwd() / "hhdaten/plots/img_schuldenprokopf.png")
 
    liqVJ = float(dfliq.loc[dfliq["hhj"]==hhj-1].bestand.iloc[0])
    invE = dfbew.loc[(dfbew["sk"]>680000)&(dfbew["sk"]<690000)].sum().anshhj
    invA = dfbew.loc[(dfbew["sk"]>780000)&(dfbew["sk"]<790000)].sum().anshhj
    
    #print(invA)
    #print(type(invA))
    saldoInv = invE - invA
    ordEZ = dfbew.loc[(dfbew["sk"]>600000)&(dfbew["sk"]<680000)].sum().anshhj
    ordAZ = dfbew.loc[(dfbew["sk"]>700000)&(dfbew["sk"]<780000)].sum().anshhj
    saldoOrdZ = ordEZ - ordAZ
    pmTilgung = dfbew.loc[(dfbew["sk"]>790000)&(dfbew["sk"]<792999)].sum().anshhj
    ffs = saldoOrdZ - pmTilgung
    tilgLiqKred = dfbew.loc[(dfbew["sk"]>794000)&(dfbew["sk"]<794999)].sum().anshhj
    aufnLiqKred = dfbew.loc[(dfbew["sk"]>694000)&(dfbew["sk"]<694999)].sum().anshhj
    kreditbedarf_inv = -1*saldoInv - ffs - aufnLiqKred + tilgLiqKred
    invkredvj = round(float(dfschulden.loc[dfschulden["hhj"] == hhj-1].invkred.iloc[0]), 2)
    invkredhhj = round(float(dfschulden.loc[dfschulden["hhj"] == hhj].invkred.iloc[0]), 2)
    liqkredvj = round(float(dfschulden.loc[dfschulden["hhj"] == hhj-1].liqkred.iloc[0]),2)
    liqkredhhj = round(float(dfschulden.loc[dfschulden["hhj"] == hhj].liqkred.iloc[0]), 2)
    kreditgesamtvj =  invkredvj + liqkredvj
    kreditgesamthhj =  invkredhhj + liqkredhhj


    krdict = {
        "hhj" : hhj, 
        "img_Liquiditaet" : docxtpl.InlineImage(doc, img_Liquiditaet),
        "img_verschuldung" : docxtpl.InlineImage(doc,img_verschuldung),
        "img_prokopfverschuldung" : docxtpl.InlineImage(doc, img_prokopfverschuldung),
        "liqVJ" : liqVJ,
        "invE" : invE,
        "invA" : invA,
        "saldoInv" : saldoInv,
        "ordEZ" : ordEZ,
        "ordAZ" : ordAZ,
        "saldoOrdZ" : saldoOrdZ,
        "pmTilgung" : pmTilgung,
        "ffs" : ffs,    
        "tilgLiqKred" : tilgLiqKred,
        "aufnLiqKred" : aufnLiqKred,
        "kreditbedarf_inv" : kreditbedarf_inv,
        "invkredvj" : invkredvj,
        "invkredhhj" : invkredhhj,
        "liqkredvj" : liqkredvj,
        "liqkredhhj" : liqkredhhj,
        "kreditgesamtvj" : kreditgesamtvj,
        "kreditgesamthhj" : kreditgesamthhj,
        } 

    return krdict

def hh_vorbericht_11_Pflichtanlagen(hhj, gde, doc,  dfffs, dferg, dfek, gdebez):
    
    img_je_entwicklung = str(pathlib.Path.cwd() / "hhdaten/plots/img_je_entwicklung.png")
    img_ek_entwicklung = str(pathlib.Path.cwd() / "hhdaten/plots/img_ek_entwicklung.png")
    
    je_hhj5vj = dferg.loc[(dferg["gde"]==gde) & (dferg["hhj"]==hhj-5)].Jahresergebnis.values.item() 
    je_hhj4vj = dferg.loc[(dferg["gde"]==gde) & (dferg["hhj"]==hhj-4)].Jahresergebnis.values.item()
    je_hhj3vj = dferg.loc[(dferg["gde"]==gde) & (dferg["hhj"]==hhj-3)].Jahresergebnis.values.item()
    je_hhj2vj = dferg.loc[(dferg["gde"]==gde) & (dferg["hhj"]==hhj-2)].Jahresergebnis.values.item()
    je_hhj1vj = dferg.loc[(dferg["gde"]==gde) & (dferg["hhj"]==hhj-1)].Jahresergebnis.values.item()
    je_hhj = dferg.loc[(dferg["gde"]==gde) & (dferg["hhj"]==hhj)].Jahresergebnis.values.item()
    je_hhj1pj = dferg.loc[(dferg["gde"]==gde) & (dferg["hhj"]==hhj+1)].Jahresergebnis.values.item()
    je_hhj2pj = dferg.loc[(dferg["gde"]==gde) & (dferg["hhj"]==hhj+2)].Jahresergebnis.values.item()
    je_hhj3pj = dferg.loc[(dferg["gde"]==gde) & (dferg["hhj"]==hhj+3)].Jahresergebnis.values.item()

       
    jeSummebisPlanjahr = je_hhj+je_hhj1vj+je_hhj2vj+je_hhj3vj+je_hhj4vj+je_hhj5vj
    summeErg = jeSummebisPlanjahr + je_hhj1pj+ je_hhj2pj + je_hhj3pj
   
    

    pfldict = {
        "hhj" : hhj,
        "gde" : gde,
        "gde_bez" : gdebez,
        # Ergebnisentwicklung
        "img_je_entwicklung" : docxtpl.InlineImage(doc, img_je_entwicklung),
        "je_hhj5vj" : je_hhj5vj, 
        "je_hhj4vj" :je_hhj4vj ,
        "je_hhj3vj" :je_hhj3vj ,
        "je_hhj2vj" :je_hhj2vj ,
        "je_hhj1vj" :je_hhj1vj ,
        "je_hhj" : je_hhj ,
        "je_hhj1pj" :je_hhj1pj, 
        "je_hhj2pj" :je_hhj2pj,
        "je_hhj3pj" :je_hhj3pj,
        "jeSummebisPlanjahr" : jeSummebisPlanjahr,
        "summeErg" : summeErg,
        
        # Finanzhaushalt
        "o_ao_zahl5vj"  : dfffs.loc[(dfffs["hhj"] == hhj -5)].saldo_ord.values.item() ,
        "o_ao_zahl4vj"  : dfffs.loc[(dfffs["hhj"] == hhj -4)].saldo_ord.values.item() ,
        "o_ao_zahl3vj"  : dfffs.loc[(dfffs["hhj"] == hhj -3)].saldo_ord.values.item() ,
        "o_ao_zahl2vj"  : dfffs.loc[(dfffs["hhj"] == hhj -2)].saldo_ord.values.item() ,
        "o_ao_zahl1vj" :  dfffs.loc[(dfffs["hhj"] == hhj -1)].saldo_ord.values.item() ,
        "o_ao_zahlhhj" :  dfffs.loc[(dfffs["hhj"] == hhj )].saldo_ord.values.item() ,
        "o_ao_zahl1pj"  : dfffs.loc[(dfffs["hhj"] == hhj +1)].saldo_ord.values.item() ,
        "o_ao_zahl2pj"  : dfffs.loc[(dfffs["hhj"] == hhj +2)].saldo_ord.values.item() ,
        "o_ao_zahl3pj"  : dfffs.loc[(dfffs["hhj"] == hhj +3)].saldo_ord.values.item() ,

        "pmTilg5vj"  : dfffs.loc[(dfffs["hhj"] == hhj -5)].pm_tilgung.values.item() ,
        "pmTilg4vj"  : dfffs.loc[(dfffs["hhj"] == hhj -4)].pm_tilgung.values.item() ,
        "pmTilg3vj"  : dfffs.loc[(dfffs["hhj"] == hhj -3)].pm_tilgung.values.item() ,
        "pmTilg2vj"  : dfffs.loc[(dfffs["hhj"] == hhj -2)].pm_tilgung.values.item() ,
        "pmTilg1vj"  : dfffs.loc[(dfffs["hhj"] == hhj -1)].pm_tilgung.values.item() ,
        "pmTilghhj" : dfffs.loc[(dfffs["hhj"] == hhj )].pm_tilgung.values.item() +dfffs.loc[(dfffs["hhj"] == hhj )].tilgungplan.values.item(),
        "pmTilg1pj"  : dfffs.loc[(dfffs["hhj"] == hhj +1)].pm_tilgung.values.item() +dfffs.loc[(dfffs["hhj"] == hhj+1 )].tilgungplan.values.item(),
        "pmTilg2pj"  : dfffs.loc[(dfffs["hhj"] == hhj +2)].pm_tilgung.values.item() +dfffs.loc[(dfffs["hhj"] == hhj+2 )].tilgungplan.values.item(),
        "pmTilg3pj"  : dfffs.loc[(dfffs["hhj"] == hhj +3)].pm_tilgung.values.item() +dfffs.loc[(dfffs["hhj"] == hhj+3 )].tilgungplan.values.item(),

        "finvortr5vj"  :dfffs.loc[(dfffs["hhj"] == hhj -5)].ffs2.values.item() ,
        "finvortr4vj"  :dfffs.loc[(dfffs["hhj"] == hhj -4)].ffs2.values.item() ,
        "finvortr3vj"  :dfffs.loc[(dfffs["hhj"] == hhj -3)].ffs2.values.item() ,
        "finvortr2vj"  :dfffs.loc[(dfffs["hhj"] == hhj -2)].ffs2.values.item() ,
        "finvortr1vj"  :dfffs.loc[(dfffs["hhj"] == hhj -1)].ffs2.values.item() ,
        "finvortrhhj"  :dfffs.loc[(dfffs["hhj"] == hhj )].ffs2.values.item()  ,
        "finvortr1pj"  :dfffs.loc[(dfffs["hhj"] == hhj +1)].ffs2.values.item() ,
        "finvortr2pj"  :dfffs.loc[(dfffs["hhj"] == hhj +2)].ffs2.values.item() ,
        "finvortr3pj"  :dfffs.loc[(dfffs["hhj"] == hhj +3)].ffs2.values.item() ,
        
        "opfinvortrhhj"  :dfffs.loc[(dfffs["hhj"] == hhj )].ffs1.values.item(),  
        "opfinvortr1pj"  :dfffs.loc[(dfffs["hhj"] == hhj +1)].ffs1.values.item() ,
        "opfinvortr2pj"  :dfffs.loc[(dfffs["hhj"] == hhj +2)].ffs1.values.item(), 
        "opfinvortr3pj"  :dfffs.loc[(dfffs["hhj"] == hhj +3)].ffs1.values.item() ,
        
        "pmTilghhj_neu" : dfffs.loc[(dfffs["hhj"] == hhj )].tilgungplan.values.item(),
        "pmTilg1pj_neu"	: dfffs.loc[(dfffs["hhj"] == hhj +1)].tilgungplan.values.item(),
        "pmTilg2pj_neu"	: dfffs.loc[(dfffs["hhj"] == hhj +2)].tilgungplan.values.item(), 
        "pmTilg3pj_neu" : dfffs.loc[(dfffs["hhj"] == hhj +3)].tilgungplan.values.item(),

        "pmTilghhj_alt" : dfffs.loc[(dfffs["hhj"] == hhj )].pm_tilgung.values.item() ,  
        "pmTilg1pj_alt"	: dfffs.loc[(dfffs["hhj"] == hhj +1)].pm_tilgung.values.item() ,
        "pmTilg2pj_alt"	: dfffs.loc[(dfffs["hhj"] == hhj +2)].pm_tilgung.values.item(), 
        "pmTilg3pj_alt" : dfffs.loc[(dfffs["hhj"] == hhj +3)].pm_tilgung.values.item() ,

        "zwsummfinvortr" : dfffs.loc[(dfffs["hhj"] <= hhj ) & (dfffs["hhj"] >= hhj -5)].ffs2.sum(),
        "summfinvortr" : dfffs.loc[(dfffs["hhj"] <= hhj+3 ) & (dfffs["hhj"] >= hhj -5)].ffs2.sum(),


        # Eigenkapitalentwicklung
        "img_ek_entwicklung" : img_ek_entwicklung,
        "ek_hhjv3" : dfek.loc[(dfek["hhj"]==hhj-3)].EK.values.item(),
        "ek_hhjv2" : dfek.loc[(dfek["hhj"]==hhj-2)].EK.values.item(),
        "ek_hhjv1" : dfek.loc[(dfek["hhj"]==hhj-1)].EK.values.item(), 
        "ek_hhj" : dfek.loc[(dfek["hhj"]==hhj)].EK.values.item(),
        "ek_hhjn1" : dfek.loc[(dfek["hhj"]==hhj+1)].EK.values.item(),
        "ek_hhjn2" : dfek.loc[(dfek["hhj"]==hhj+2)].EK.values.item(),
        "ek_hhjn3" : dfek.loc[(dfek["hhj"]==hhj+3)].EK.values.item()
    }

    

    return pfldict

if __name__ == "__main__":
    #print test hhsatzungcontext
    #print(hhsatzung(gde=60 , hhj=2023, xlsgrunddaten=str(pathlib.Path.cwd() / "hhdaten/grunddaten.xlsx"),xlsbewegung=str(pathlib.Path.cwd() / "hhdaten/bewegungsdaten.xlsx") ))

    #print test vorbericht-allgemein
    #print(hh_vorbericht_01_Allgemeines(di.hhdata_excelimport(xlsxfile= str(pathlib.Path.cwd() / "hhdaten/bewegungsdaten.xlsx"))))
    
    
    #print(hh_vorbericht_05_UebersichtErgHH(di.hhdata_excelimport(xlsxfile= str(pathlib.Path.cwd() / "hhdaten/bewegungsdaten.xlsx"))))
    #print("test")

    print(hh_vorbericht_06_Ertraege(df=di.hhdata_excelimport(xlsxfile= str(pathlib.Path.cwd() / "hhdaten/bewegungsdaten.xlsx")), dferl = di.erl_excelimport(str(pathlib.Path.cwd() / "hhdaten/bewegungsdaten.xlsx"))))