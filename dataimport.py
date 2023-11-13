import pandas as pd
import numpy as np
import pathlib
from datetime import date

def hhdata_excelimport(xlsxfile):
    df = pd.read_excel(xlsxfile, 0, 
                   # decimal = ",",
                   # encoding = "latin1",
                   #thousands = ".",
                   names = ["hhs", "produkt", "mn", "sk", "bez", "th", "dk", "anshhj", "sollhhj", "ansvj", "sollvj", "planvvj", "rgergvvj", "rgergvj", "rgakt", "plan1", "plan2", "plan3", "ve"],
                   dtype= {"hhs": str,
                           "produkt": str,
                           "bez": str,
                           "th": str,
                           "dk": str} 
                   )

    return df

def hhdata_clipboardimport():
    df = pd.read_clipboard(
                   # decimal = ",",
                   # encoding = "latin1",
                   #thousands = ".",
                   names = ["hhs", "produkt", "mn", "sk", "bez", "th", "dk", "anshhj", "sollhhj", "ansvj", "sollvj", "planvvj", "rgergvvj", "rgergvj", "rgakt", "plan1", "plan2", "plan3", "ve"],
                   dtype= {"hhs": str,
                           "produkt": str,
                           "bez": str,
                           "th": str,
                           "dk": str} 
                   )
    return df

def mn_excelimport(xlsxfile):
    df = pd.read_excel(xlsxfile, 1)
    return df

def prod_excelimport(xlsxfile):
    df = pd.read_excel(xlsxfile, 2)
    return df

def erl_excelimport(xlsxfile):
    def hhssyntesize(dferl):
        if dferl["mn"] == 0:
            x = ""
        else:
            x = "/" + str(dferl["mn"]).zfill(4)

        return f"{dferl['produkt']}{x}.{str(int(dferl['sk']))}"


    df = pd.read_excel(xlsxfile, 3, 
                       names=["hh", "produkt", "mn", "sk", "erlNr", "erlTyp", "interneErl", "erl", "nicht uebertragbar"],
                       dtype ={"hh" : str,
                               "produkt" : str,
                                #"sk" : int,
                                "erl" : str})
    df.fillna(0, inplace= True)
    df["hhs"] = df.apply(hhssyntesize, axis=1) # Erzeugt eine Spalte Haushaltsstelle ("hhs")
    df["duplikat"] = df.duplicated(subset=['hhs'], keep = False) # fügt eine Spalte "Duplikat" ein
    
    df['erljoined'] = df.groupby('hhs')['erl'].transform(lambda x: ' '.join(x)) #die strings der ERläuterungszeilen, die Duplikate darstellen werden hier zusammengeführt.
    df = df.drop_duplicates(subset=["hhs"], keep="first")
    df = df.drop(["erl"], axis=1)
    df = df.rename(columns={"erljoined" : "erl" })
    return df

def readgrunddatengde(xlsfile, gdenr):
    df = pd.read_excel(xlsfile, sheet_name="gde",)
    dfgde = df.loc[(df["gdenr"] == gdenr)]
    return dfgde

def readgrunddatenhh(xlsfile, gdenr, hhj):
    df = pd.read_excel(xlsfile, 
                       sheet_name="hhdaten",
                       dtype = {"hebesatz_grsta" : int,
                                "hebesatz_grstb" : int,
                                "hebesatz_gewst" : int,
                                "hust_1" : int,
                                "hust_2" : int,    
                                "hust_3" : int,
                                "kred_zinslos" : int,
                                "ve_ohne_kredit" : int,
                                "vg" : bool}
                       )
    
    dfhh = df.loc[(df["gdenr"] == gdenr) & (df["hhj"] == hhj)]
    return dfhh

def hhsatzungekentwicklung(xlsfile, gdenr, hhj):
       df = pd.read_excel(xlsfile, sheet_name="JAWerte")
       dfhh = df.loc[(df["gdenr"] == gdenr) & (df["hhj"] == hhj)]
       return dfhh

def readewstatistik_wohn(xlsfile, gdenr, jahr):
    df = pd.read_excel(xlsfile, sheet_name="ew_wohn")
       
    dfewdata = df.loc[(df["gdenr"] == gdenr) & (df["datum"] <= np.datetime64(date(year=jahr, month = 6, day = 30))) &  (df["datum"] >= np.datetime64(date(year=jahr-10, month=6, day=30)))]
    
    return dfewdata


def readflaechenstatistik(xlsfile, gdenr, hhj):
    df = pd.read_excel(xlsfile, sheet_name="Flaeche")
    df = df.loc[(df.gdenr == gdenr)&(df.Datum == df.Datum.max())]
    df = df[(df.Grundeintrag)&(df.Nutzungsart != "Bodenfläche insgesamt")]

    return df 

def readhebesatzentwicklung(xlsfile, gdenr):
    df = pd.read_excel(xlsfile, sheet_name="hebesatze")
    df = df.loc[(df.gdenr == gdenr) ][["hhj", "gdenr", "grsta", "grstb", "gewst"]]
    return df

def readhundesteuersatzentwicklung(xlsfile, gdenr):
    df = pd.read_excel(xlsfile, sheet_name="hebesatze")
    df = df.loc[(df.gdenr == gdenr) ][["gdenr", "hust1", "hust2", "hust3", "hustgef"]]
    return df

def readewdatenaltersstruktur(xlsfile, gdenr, hhj):
    df = pd.read_excel(xlsfile, 
                       sheet_name="ew_alter",
                       )
    df.fillna(0,inplace=True)
    df = df.loc[(df.gdenr == gdenr)&(df.datum <= np.datetime64(date(year=hhj-1, month=6, day=30)))&(df.datum >= np.datetime64(date(year=hhj-3, month=6, day=30)))]
    return df

def readewdaten_u20(xlsfile, gdenr, hhj):
    df = pd.read_excel(xlsfile, sheet_name="e_u20")
    df = df.loc[(df.gdenr == gdenr)&(df.datum <= np.datetime64(date(year=hhj-1, month=6, day=30)))&(df.datum >= np.datetime64(date(year=hhj-3, month=6, day=30)))]
    return df    

def readlfag_stkberechnung(xlsfile, gdenr, hhj):
    df = pd.read_excel(xlsfile, sheet_name="STKRAFT") 
    return df

def readsteuerertraege(xlsfile, gdenr, hhj):
    df = pd.read_excel(xlsfile, sheet_name="steuer")
    df = df.loc[(df.gdenr == gdenr)]
    return df

def readergebnisEKstat(xlsfile, gdenr, hhj):
    df = pd.read_excel(xlsfile, sheet_name="ertrag")
    df = df.loc[(df.gdenr == gdenr)]
    return df

def readffsfinstatistik(xlsfile, gdenr, hhj):
    df = pd.read_excel(xlsfile, sheet_name="ffs")
    return df




if __name__ == "main": 
    #df = readewstatistik_wohn(xlsfile=str(pathlib.Path.cwd() / "hhdaten/grunddaten.xlsx"), gdenr=60, jahr=2022)
    #print(df)
    #df = (readgrunddatenhh(xlsfile=str(pathlib.Path.cwd() / "hhdaten/grunddaten.xlsx"), gdenr=60, hhj=2023))
    #df = readflaechenstatistik(xlsfile=str(pathlib.Path.cwd() / "hhdaten/grunddaten.xlsx"), gdenr=60, jahr=2023)
    #df = readhebesatzentwicklung(xlsfile=str(pathlib.Path.cwd() / "hhdaten/grunddaten.xlsx"), gdenr=60)
    df = readewdatenaltersstruktur(xlsfile=str(pathlib.Path.cwd() / "hhdaten/grunddaten.xlsx"), gdenr=60, hhj=2023)
    print(df)
    print(df.dtypes)








