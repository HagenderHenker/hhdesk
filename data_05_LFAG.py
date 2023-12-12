import dataimport as di
import pathlib
import pandas as pd

def calculate_steuerkraft(dflfagstk):

    print(dflfagstk)
    print(dflfagstk["grstb_IV_vvj"].values[0])

    grsta_4vvj = round((dflfagstk["grsta_IV_vvj"].values[0] - dflfagstk["ber_grsta_IV_vvj"].values[0])*10000/dflfagstk["hebesatz_grsta_IV_vvj"].values[0],0)/100
    grsta_1bis3vj = round((dflfagstk["grsta_I-III_vj"].values[0] - dflfagstk["ber_grsta_I-III_vj"].values[0])*10000/dflfagstk["hebesatz_grsta_I-III_vj"].values[0],0)/100
    #Grundzahl
    grzgrsta = grsta_4vvj + grsta_1bis3vj
    # Nivellierung
    nivgrsta = dflfagstk["nivellierungssatz_grsta"].values[0] 
    stkgrsta = grzgrsta * nivgrsta/100
    print(stkgrsta)
    
    grstb_4vvj = round((dflfagstk["grstb_IV_vvj"].values[0] - dflfagstk["ber_grstb_IV_vvj"].values[0])*10000/dflfagstk["hebesatz_grstb_IV_vvj"].values[0],0)/100
    grstb_1bis3vj = round((dflfagstk["grstb_I-III_vj"].values[0] - dflfagstk["ber_grstb_I-III_vj"].values[0])*10000/dflfagstk["hebesatz_grstb_I-III_vj"].values[0],0)/100
    grzgrstb = grstb_4vvj + grstb_1bis3vj
    nivgrstb = dflfagstk["nivellierungssatz_grsta"].values[0] 
    stkgrstb = grzgrstb * nivgrstb/100

    gewst_4vvj = round((dflfagstk["gewst_IV_vvj"].values[0] - dflfagstk["ber_gewst_IV_vvj"].values[0])*10000/dflfagstk["hebesatz_gewst_IV_vvj"].values[0],0)/100
    gewst_1bis3vj = round((dflfagstk["gewst_I-III_vj"].values[0] - dflfagstk["ber_gewst_I-III_vj"].values[0])*10000/dflfagstk["hebesatz_gewst_I-III_vj"].values[0],0)/100
    grzgewst = gewst_4vvj + gewst_1bis3vj
    nivgewst = dflfagstk["nivellierungssatz_gewst"].values[0] 
    stkgewst = grzgewst * nivgewst/100



    EkSt4vvj = dflfagstk["EkSt4vvj"].values[0]
    EkSt1bis3vj = dflfagstk["EkSt1bis3vj"].values[0]
    ekst = EkSt1bis3vj + EkSt4vvj
    
    USt4vvj = dflfagstk["USt4vvj"].values[0]
    USt1bis3vj = dflfagstk["USt1bis3vj"].values[0]		
    ust = USt1bis3vj + USt4vvj
    
    wgUSt4vvj = dflfagstk["wgUSt4vvj"].values[0]
    wgUSt1bis3vj = dflfagstk["wgUSt1bis3vj"].values[0]
    wgust = wgUSt1bis3vj + wgUSt4vvj

    stkdict = {
        "grsta_4vvjist" : dflfagstk["grsta_IV_vvj"].values[0],
        "ber_grsta_IV_vvj" : dflfagstk["ber_grsta_IV_vvj"].values[0],
        "hebesatz_grsta_IV_vvj" : dflfagstk["hebesatz_grsta_IV_vvj"].values[0],
        "grzgrsta4vvj" : grsta_4vvj, 
        "grsta_IbisIII_vj" : dflfagstk["grsta_I-III_vj"].values[0],
        "ber_grsta_IbisIII_vj" : dflfagstk["ber_grsta_I-III_vj"].values[0],
        "hebesatz_grsta_IbisIII_vj" : dflfagstk["hebesatz_grsta_I-III_vj"].values[0],
        "grzgrsta1bis3vj" : grsta_1bis3vj,
        "grzgrsta" : grzgrsta,
        "nivgrsta" : nivgrsta,
        "stkgrsta" : stkgrsta,

        "grstb_4vvjist" : dflfagstk["grstb_IV_vvj"].values[0],
        "ber_grstb_IV_vvj" : dflfagstk["ber_grstb_IV_vvj"].values[0],
        "hebesatz_grstb_IV_vvj" : dflfagstk["hebesatz_grstb_IV_vvj"].values[0],
        "grzgrstb4vvj" : grstb_4vvj, 
        "grstb_1bis3vjist" : dflfagstk["grstb_I-III_vj"].values[0],
        "ber_grstb_1bis3_vj" : dflfagstk["ber_grstb_I-III_vj"].values[0],
        "hebesatz_grstb_1bis3_vj" : dflfagstk["hebesatz_grstb_I-III_vj"].values[0],
        "grzgrstb1bis3vj" : grstb_1bis3vj,
        "grzgrstb" : grzgrstb,
        "nivgrstb" : nivgrstb,
        "stkgrstb" : stkgrstb,

        "gewst_4vvjist" : dflfagstk["gewst_IV_vvj"].values[0],
        "ber_gewst_IV_vvj" : dflfagstk["ber_gewst_IV_vvj"].values[0],
        "hebesatz_gewst_IV_vvj" : dflfagstk["hebesatz_gewst_IV_vvj"].values[0],
        "grzgewst4vvj" : gewst_4vvj, 
        "gewst_1bis3vjist" : dflfagstk["gewst_I-III_vj"].values[0],
        "ber_gewst_1bis3_vj" : dflfagstk["ber_gewst_I-III_vj"].values[0],
        "hebesatz_gewst_1bis3_vj" : dflfagstk["hebesatz_grstb_I-III_vj"].values[0],
        "grzgewst1bis3vj" : gewst_1bis3vj,
        "grzgewst" : grzgewst,
        "nivgewst" : nivgewst,
        "stkgewst" : stkgewst,

        "EkSt4vvj" : EkSt4vvj,	
        "EkSt1bis3vj" :EkSt1bis3vj,
        "ekst" : ekst,
        "USt4vvj" : USt4vvj,
    	"USt1bis3vj" : USt1bis3vj,
        "ust" : ust,
        "wgUSt4vvj" : wgUSt4vvj,
        "wgUSt1bis3vj" : wgUSt1bis3vj,
        "wgust" : wgust,
        "stkgesamt" : float(ekst + wgust+ ust+stkgewst+stkgrsta+stkgrstb)
        }

    return stkdict