import dataimport as di
import pandas as pd
import numpy as np
import pathlib

"""
class Gemeinde:
   
    #he "Gemeinde" class is used to store the repeatedly used key data for the municipal authority
    #for which the budget is drawn up
   
    def __init__(self, gde_nr, gde_name, gde_typ, bm_name, bm_typ, vg):
        self.gde_nr = gde_nr
        self.gde_name = gde_name
        self.gde_typ = gde_typ
        self.bm_name = bm_name
        self.bm_typ = bm_typ
        self.vg = vg
        self.gde_bez = f"{self.gde_typ} {self.gde_name}"

    @ staticmethod
    def readgrunddaten(xlsfile, gdenr):
        df = pd.read_excel(xlsfile, sheet_name="gde",)
        print(df.head())
        dfgde = df.loc[(df["gdenr"] == gdenr)]
        return dfgde

class Haushalt:
 
    #Repeatedly used data for the budget itself. 


    def __init__(self, gde, hhj, hebesatz_grsta, hebesatz_grstb, hebesatz_gewst, hust_1, hust_2, hust_3, hust_gef, kredzinslos, ve_ohne_kredit, wg_invest, planodernachtrag, beschluss_vorjahr,beschluss_vorvorjahr ,vvj_abgeschlossen=False, ja_vvj_beschluss):
        self.gde_nr = gde
        self.hhj = hhj
        self.vj = hhj - 1
        self.vvj = hhj - 2
        self.hhj1 = hhj + 1
        self.hhj2 = hhj + 2
        self.hhj3 = hhj + 3
        self.hebesatz_grsta = hebesatz_grsta
        self.hebesatz_grstb = hebesatz_grstb
        self.hebesatz_gewst = hebesatz_gewst
        self.hust_1 = hust_1
        self.hust_2= hust_2
        self.hust_3 = hust_3
        self.hust_gef = hust_gef
        self.kredzinslos = kredzinslos
        self.ve_ohne_kredit = ve_ohne_kredit
        self.wg_invest = wg_invest
        self.beschluss_vorjahr = beschluss_vorjahr
        self.beschluss_vorvorjahr = beschluss_vorvorjahr
        self.vvj_abgeschlossen = vvj_abgeschlossen
        self.planodernachtrag = planodernachtrag

    @staticmethod
    def readgrunddaten(xlsfile, gdenr, hhj):
        df = pd.read_excel(xlsfile, sheet_name="hhdaten",)
        print(df.head())
        dfhh = df.loc[(df["gdenr"] == gdenr) & (df["hhj"] == hhj)]
        return dfhh




xls = str(pathlib.Path.cwd() / "hhdaten/grunddaten.xlsx")
gemnr = 60
hhj = 2023

gde = Gemeinde(gde_nr = Gemeinde.readgrunddaten(xls, gemnr)["gdenr"],
               gde_name = Gemeinde.readgrunddaten(xls, gemnr)["gde_ort"],
               gde_typ = Gemeinde.readgrunddaten(xls, gemnr)["gde_typ"],
               bm_name= Gemeinde.readgrunddaten(xls, gemnr)["bm_name"],
               bm_typ = Gemeinde.readgrunddaten(xls, gemnr)["bm_typ"],
               vg = Gemeinde.readgrunddaten((xls, gemnr)["vg"])
                )
               
print(gde.gde_bez)

hh = Haushalt( 
                gde_nr = Haushalt.readgrunddaten(xls, gemnr, hhj)["gde"],
                hhj = Haushalt.readgrunddaten(xls, gemnr, hhj)["hhj"],
                hebesatz_grsta = Haushalt.readgrunddaten(xls, gemnr, hhj)["grst_a"],
                hebesatz_grstb = Haushalt.readgrunddaten(xls, gemnr, hhj)["grst_b"],
                hebesatz_gewst = Haushalt.readgrunddaten(xls, gemnr, hhj)["gewst"],
                hust_1 = Haushalt.readgrunddaten(xls, gemnr, hhj)["hust_1"],
                hust_2 = Haushalt.readgrunddaten(xls, gemnr, hhj)["hust_2"],
                hust_3 = Haushalt.readgrunddaten(xls, gemnr, hhj)["hust_3"],
                hust_gef = Haushalt.readgrunddaten(xls, gemnr, hhj)["hust_gef"],
                kredzinslos = Haushalt.readgrunddaten(xls, gemnr, hhj)["hust_gef"] 
                ve_ohne_kredit = Haushalt.readgrunddaten(xls, gemnr, hhj)["hust_gef"] 
                wg_invest = Haushalt.readgrunddaten(xls, gemnr, hhj)["hust_gef"] 
                planodernachtrag = Haushalt.readgrunddaten(xls, gemnr, hhj)["hust_gef"] 
                beschluss_vorjahr = Haushalt.readgrunddaten(xls, gemnr, hhj)["hust_gef"]
                beschluss_vorvorjahr = Haushalt.readgrunddaten(xls, gemnr, hhj)["hust_gef"]
                vvj_abgeschlossen = 
                ja_vvj_beschluss =


)
"""

def gdegrunddaten(xlsfilegrunddaten, gde):
    df = di.readgrunddatengde(xlsfile=xlsfilegrunddaten, gdenr=gde)
    dic = df.to_dict()
    gdedict = {}
    for key in dic:
        gdedict[key] = str(list(dic[key].values())[0])
    return gdedict


