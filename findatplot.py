import matplotlib.pyplot as plt
import seaborn as sns

import data_09_statistik as stat
import pandas as pd 
import numpy as np


def hebesatzentwicklung(df):
    ''' 
    Entwicklung der Hebesätze
    this function creates a lineplot of the development of the taxrates (Realsteuerhebesätze)
    for Grundsteuer A, Grundsteuer B and Gewerbesteuer
    It takes a Dataframe created in "data_09_statistik.py" from the /hhdaten/grunddaten.xlsx
    '''


def ertragsstruktur(df):
    def staffelung(sk):
        if sk < 410000:
            return 40
        if 410000 <= sk < 420000:
            return 41
        if 420000 <= sk < 430000:
            return 42
        if 430000 <= sk < 440000:
            return 43
        if 440000 <= sk < 442000 or 443000 <= sk < 450000:
            return 44
        if 442000 <= sk < 443000:
            return 442
        if 450000 <= sk < 460000:
            return 45
        if 460000 <= sk < 470000:
            return 46
        if 470000 <= sk < 480000:
            return 47
        if 480000 <= sk < 490000:
            return 48
        if 490000 <= sk < 500000:
            return 49

        if 500000 <= sk < 520000:
            return 50
        if 520000 <= sk < 530000:
            return 52
        if 530000 <= sk < 540000:
            return 53
        if 540000 <= sk < 550000:
            return 54
        if 550000 <= sk < 560000:
            return 55
        if 560000 <= sk < 570000:
            return 56
        if 570000 <= sk < 580000:
            return 57
        if 580000 <= sk < 590000:
            return 58
        if 590000 <= sk < 600000:
            return 59

    def eart(staffelung):
        if staffelung < 50:
            return "e"
        else:
            return "a"
    
    df.dtypes
    dferg = df.loc[(df["sk"] < 500000)]
    dferg["staffel"] = dferg["sk"].map(staffelung)
    dferg["eart"] = dferg["staffel"].map(eart)

    dftp = dferg[["hhs", "sk", "staffel", "eart", "anshhj"]]
    dftp = dftp.rename(columns={"anshhj" : "betrag"})
    dftp["p-re"] = "p"
    dftp["jahr"] = "hhj"

    dfe2 = dferg[["hhs", "sk", "staffel", "eart", "ansvj"]]
    dfe2 = dfe2.rename(columns={"ansvj" : "betrag"})
    dfe2["p-re"] = "p"
    dfe2["jahr"] = "vj"

    dfe3 = dferg[["hhs", "sk", "staffel", "eart", "rgergvvj"]]
    dfe3 = dfe3.rename(columns={"rgergvvj" : "betrag"})
    dfe3["p-re"] = "re"
    dfe3["jahr"] = "vvj"

    dftp = dftp.append(dfe2)
    dftp = dftp.append(dfe3)

    fig, ax = plt.subplots(figsize = ( 5, 3))

    groupers = {
        40 : "Steuern",
        41 : "Transfererträge",
        42 : "Erträge der sozialen Sicherung",
        43 : "Gebühren",
        44 : "privatrechtl. Leistungsentgelte",
        442 : "Kostenerstattungen",
        45 : "Wertkorrekturen",
        46 : "sonstige Erträge",
        47 : "Finanzerträge",
        48 : "Erträge aus ILV",
        49 : "Andere Erträge"
    }


    dftp2 = dftp.groupby(["staffel", "jahr"], as_index=False).sum()
    dftp2.reset_index()
    print(dftp2)

    sns.barplot(data=dftp2,
                x= "staffel",
                y="betrag",
                hue="jahr",
                ax = ax)

    ax.set_xlabel("Ertragsart", size= 14)
    ax.set_ylabel("Volumen in Mio€", size = 14 )
    ax.set_title("Erträge", size = 20)

