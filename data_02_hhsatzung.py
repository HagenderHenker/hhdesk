
import dataimport as di
import pandas as pd
import numpy as np
import pathlib

#def readgrunddatenhh(xlsfile, gdenr, hhj):
#    df = pd.read_excel(xlsfile, sheet_name="hhdaten",)
#    #print(df.head())
#    dfhh = df.loc[(df["gdenr"] == gdenr) & (df["hhj"] == hhj)]
#    return dfhh

#df.head()
#dfert = df.loc[df["sk"]<500000]
#dfert.head()

def hhsatzunggrunddatenhh(xlsfile, gdenr, hhj):
        df = di.readgrunddatenhh(gdenr=gdenr, hhj=hhj, xlsfile=xlsfile)
        dic = df.to_dict()
        gddict = {}
        for key in dic:
                gddict[key] = list(dic[key].values())[0]
        return gddict
        

def hhsatzungekvvj(xlsfile, gdenr, hhj):
        df = di.hhsatzungekentwicklung(xlsfile=xlsfile, gdenr=gdenr, hhj=hhj-2)
        ek = int(df["ek_eb"]*100)
        print(f"Eigenkapital: {ek}")

        return ek




def hhsatzungbewegung(gde, hhj, hhbewfile):

        df = di.hhdata_excelimport(xlsxfile= hhbewfile)
        
        ertrag_gesamt = df.loc[(df["sk"]<500000)]["anshhj"].sum()
        aufwand_gesamt = df.loc[(df["sk"]<600000) & (df["sk"]>500000)]["anshhj"].sum()
        erg_saldo = ertrag_gesamt - aufwand_gesamt

        saldo_vj = df.loc[(df["sk"]<500000)]["ansvj"].sum() - df.loc[(df["sk"]<600000) & (df["sk"]>500000)]["ansvj"].sum()

        lfd_ez = df.loc[(df["sk"]<670000) & (df["sk"]>600000)]["anshhj"].sum()
        lfd_az = df.loc[(df["sk"]<770000) & (df["sk"]>700000)]["anshhj"].sum()
        lfd_saldo = lfd_ez - lfd_az

        fin_ez = df.loc[(df["sk"]<680000) & (df["sk"]>670000)]["anshhj"].sum()
        fin_az = df.loc[(df["sk"]<780000) & (df["sk"]>770000)]["anshhj"].sum()
        fin_saldo = fin_ez - fin_az

        ord_ez = lfd_ez + fin_ez
        ord_az = lfd_az + fin_az
        ord_saldo = ord_ez - ord_az

        inv_ez = df.loc[(df["sk"]<690000) & (df["sk"]>680000)]["anshhj"].sum()
        inv_az = df.loc[(df["sk"]<790000) & (df["sk"]>780000)]["anshhj"].sum()
        inv_saldo = inv_ez - inv_az

        ft_ez = df.loc[(df["sk"]<700000) & (df["sk"]>690000)]["anshhj"].sum()
        ft_az = df.loc[(df["sk"]<800000) & (df["sk"]>790000)]["anshhj"].sum()
        ft_saldo = ft_ez - ft_az

        ikred_aufnahme = df.loc[(df["sk"]<693000) & (df["sk"]>692000)]["anshhj"].sum()
        ve_gesamt = df["ve"].sum()

        if erg_saldo >= 0:
                bez_erg_saldo = "Jahresüberschuss" 
        else:
                bez_erg_saldo = "Jahresfehlbetrag"

        datacollection = {
                        "hhj" : hhj,
                        "ertrag_gesamt" : ertrag_gesamt,
                        "aufwand_gesamt" : aufwand_gesamt,
                        "erg_saldo" : erg_saldo,
                        "saldo_vj" : saldo_vj,
                        "lfd_ez" : lfd_ez,
                        "lfd_az" : lfd_az,
                        "lfd_saldo" : lfd_saldo,
                        "fin_ez" : fin_ez,
                        "fin_az" : fin_az,
                        "fin_saldo" :fin_saldo,
                        "ord_ez" : ord_ez,
                        "ord_az" : ord_az,
                        "ord_saldo" : ord_saldo,
                        "inv_ez" : inv_ez,
                        "inv_az" : inv_az,
                        "inv_saldo" : inv_saldo,
                        "ft_ez" : ft_ez,
                        "ft_az" : ft_az,
                        "ft_saldo" : ft_saldo,
                        "ikred_aufnahme" : ikred_aufnahme,
                        "ve_gesamt" : ve_gesamt,
                        "bez_erg_saldo" : bez_erg_saldo
                   }
        return datacollection














#if __name__ == "__main__":
       # hhsatzungekvvj(xlsfile=str(pathlib.Path.cwd() / "hhdaten/grunddaten.xlsx"), gdenr=60, hhj=2023)
        # print(hhsatzungbewegung(gde=60, hhj=2023, hhbewfile= str(pathlib.Path.cwd() / "hhdaten/bewegungsdaten.xlsx")))
