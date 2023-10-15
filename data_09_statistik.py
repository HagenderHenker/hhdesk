import pandas as pd 
import dataimport as di
import pathlib

def get_hebesatzentwicklung(df):
    pass

def get_alterstat(df):
    pass

def get_einzuschulendstat(df):
    pass

def get_u20stat(df):
    pass

def get_flaechen_stat(df):
    pass

def get_steuerist_stat(df):
    pass

def get_umlageist_stat(df):
    pass

def get_ek_entwicklung_stat(df):
    pass

def get_jahreserg_entw_stat(df):
    pass

def get_persA_produktverteilung_stat(df):
    
    """
    Takes DF  from "Bewegungsdaten.xlsx" and sums per "produkt" field to show the source of human resource cost 
    """
    df = df.loc[(df["sk"]<520000 ) & (df["sk"]>499999)]
    dfpersprod = df.groupby(["produkt"]).sum()
    print(dfpersprod)
    return dfpersprod
    
get_persA_produktverteilung_stat(di.hhdata_excelimport(xlsxfile=str(pathlib.Path.cwd() / "haushalt/hhdaten/bewegungsdaten.xlsx")))