import dataimport as di  
import pandas as pd
import pathlib


def gesamtplan_erg(df):
        
    # Summenermittlung für den Gesamtplan
    dic = {
    "e_p_steuern"	: df.loc[(df["sk"]<410000)]["anshhj"].sum(),
    "e_v_steuern"	: df.loc[(df["sk"]<410000)]["ansvj"].sum(),
    "e_re_steuern" : df.loc[(df["sk"]<410000)]["rgergvvj"].sum(),
    "e_p_tranfer"	: df.loc[(df["sk"]<420000) & (df["sk"]>410000)]["anshhj"].sum(),
    "e_v_tranfer"	: df.loc[(df["sk"]<420000) & (df["sk"]>410000)]["ansvj"].sum(),
    "e_re_tranfer" : df.loc[(df["sk"]<420000) & (df["sk"]>410000)]["rgergvvj"].sum(),
    "e_p_sozE" : df.loc[(df["sk"]<430000) & (df["sk"]>420000)]["anshhj"].sum(),
    "e_v_sozE"  : df.loc[(df["sk"]<430000) & (df["sk"]>420000)]["ansvj"].sum(),
    "e_re_sozE" : df.loc[(df["sk"]<430000) & (df["sk"]>420000)]["rgergvvj"].sum(),
    "e_p_oerLeist" : df.loc[(df["sk"]<440000) & (df["sk"]>430000)]["anshhj"].sum(),
    "e_v_oerLeist" : df.loc[(df["sk"]<440000) & (df["sk"]>430000)]["ansvj"].sum(),	
    "e_re_oerLeist" : df.loc[(df["sk"]<440000) & (df["sk"]>430000)]["rgergvvj"].sum(),
    "e_p_prLeist"	: df.loc[(df["sk"]<420000) & (df["sk"]>410000)]["anshhj"].sum(),
    "e_v_prLeist"	: df.loc[(df["sk"]<420000) & (df["sk"]>410000)]["ansvj"].sum(),
    "e_re_prLeist" : df.loc[(df["sk"]<420000) & (df["sk"]>410000)]["rgergvvj"].sum(),
    "e_p_koste"	: df.loc[(df["sk"]<420000) & (df["sk"]>410000)]["anshhj"].sum(),
    "e_v_koste"	: df.loc[(df["sk"]<420000) & (df["sk"]>410000)]["ansvj"].sum(),
    "e_re_koste": df.loc[(df["sk"]<420000) & (df["sk"]>410000)]["rgergvvj"].sum(),
    "e_p_sonstE"	: df.loc[(df["sk"]<420000) & (df["sk"]>410000)]["anshhj"].sum(),
    "e_v_sonstE" : df.loc[(df["sk"]<420000) & (df["sk"]>410000)]["ansvj"].sum(),
    "e_re_sonstE" : df.loc[(df["sk"]<420000) & (df["sk"]>410000)]["rgergvvj"].sum(),
    "e_p_summeE" : df.loc[(df["sk"]<470000)]["anshhj"].sum(),
    "e_v_summeE" : df.loc[(df["sk"]<470000)]["ansvj"].sum(),
    "e_re_summeE" : df.loc[(df["sk"]<470000)]["rgergvvj"].sum(),
    "e_p_pers" : df.loc[(df["sk"]<520000) & (df["sk"]>500000)]["anshhj"].sum(),
    "e_v_pers" : df.loc[(df["sk"]<520000) & (df["sk"]>500000)]["ansvj"].sum(),
    "e_re_pers" : df.loc[(df["sk"]<520000) & (df["sk"]>500000)]["rgergvvj"].sum(),
    "e_p_msd" : df.loc[(df["sk"]<530000) & (df["sk"]>520000)]["anshhj"].sum(),
    "e_v_msd" : df.loc[(df["sk"]<530000) & (df["sk"]>520000)]["ansvj"].sum(),
    "e_re_msd" : df.loc[(df["sk"]<530000) & (df["sk"]>520000)]["rgergvvj"].sum(),
    "e_p_afa" : df.loc[(df["sk"]<540000) & (df["sk"]>530000)]["anshhj"].sum(),	
    "e_v_afa" : df.loc[(df["sk"]<540000) & (df["sk"]>530000)]["ansvj"].sum(),
    "e_re_afa" : df.loc[(df["sk"]<540000) & (df["sk"]>530000)]["rgergvvj"].sum(),
    "e_p_umla" : df.loc[(df["sk"]<550000) & (df["sk"]>540000)]["anshhj"].sum(),
    "e_v_umla" : df.loc[(df["sk"]<550000) & (df["sk"]>540000)]["ansvj"].sum(),
    "e_re_umla" : df.loc[(df["sk"]<550000) & (df["sk"]>540000)]["rgergvvj"].sum(),
    "e_p_sozA" :df.loc[(df["sk"]<560000) & (df["sk"]>550000)]["anshhj"].sum(),
    "e_v_sozA" : df.loc[(df["sk"]<560000) & (df["sk"]>550000)]["ansvj"].sum(),
    "e_re_sozA" : df.loc[(df["sk"]<560000) & (df["sk"]>550000)]["rgergvvj"].sum(),
    "e_p_sonstA" : df.loc[(df["sk"]<570000) & (df["sk"]>560000)]["anshhj"].sum(),	
    "e_v_sonstA" : df.loc[(df["sk"]<570000) & (df["sk"]>560000)]["ansvj"].sum(),	
    "e_re_sonstA" : df.loc[(df["sk"]<570000) & (df["sk"]>560000)]["rgergvvj"].sum(),
    "e_p_summeA" : df.loc[(df["sk"]<570000) & (df["sk"]>500000)]["anshhj"].sum(),
    "e_v_summeA" : df.loc[(df["sk"]<570000) & (df["sk"]>500000)]["ansvj"].sum(),
    "e_re_summeA" : df.loc[(df["sk"]<570000) & (df["sk"]>500000)]["rgergvvj"].sum(),
    "e_p_saldolfd" : df.loc[(df["sk"]<470000) & (df["sk"]>400000)]["anshhj"].sum() - df.loc[(df["sk"]<570000) & (df["sk"]>500000)]["anshhj"].sum(),	
    "e_v_saldolfd" : df.loc[(df["sk"]<470000) & (df["sk"]>400000)]["ansvj"].sum() - df.loc[(df["sk"]<570000) & (df["sk"]>500000)]["ansvj"].sum(),	
    "e_re_saldolfd" : df.loc[(df["sk"]<470000) & (df["sk"]>400000)]["rgergvvj"].sum() - df.loc[(df["sk"]<570000) & (df["sk"]>500000)]["rgergvvj"].sum(),
    "e_p_finE" : df.loc[(df["sk"]<480000) & (df["sk"]>470000)]["anshhj"].sum(),
    "e_v_finE" : df.loc[(df["sk"]<480000) & (df["sk"]>470000)]["ansvj"].sum(),
    "e_re_finE" : df.loc[(df["sk"]<480000) & (df["sk"]>470000)]["rgergvvj"].sum(),
    "e_p_finA" : df.loc[(df["sk"]<580000) & (df["sk"]>570000)]["anshhj"].sum(),
    "e_v_finA" : df.loc[(df["sk"]<580000) & (df["sk"]>570000)]["ansvj"].sum(),
    "e_re_finA" : df.loc[(df["sk"]<580000) & (df["sk"]>570000)]["rgergvvj"].sum(),
    "e_p_finSaldo" : df.loc[(df["sk"]<480000) & (df["sk"]>470000)]["anshhj"].sum() - df.loc[(df["sk"]<580000) & (df["sk"]>570000)]["anshhj"].sum(),	
    "e_v_finSaldo" : df.loc[(df["sk"]<480000) & (df["sk"]>470000)]["ansvj"].sum() - df.loc[(df["sk"]<580000) & (df["sk"]>570000)]["ansvj"].sum(),	
    "e_re_finSaldo" : df.loc[(df["sk"]<480000) & (df["sk"]>470000)]["rgergvvj"].sum() - df.loc[(df["sk"]<580000) & (df["sk"]>570000)]["rgergvvj"].sum(),	
    "e_p_ordErg" : df.loc[(df["sk"]<480000) & (df["sk"]>400000)]["anshhj"].sum() - df.loc[(df["sk"]<580000) & (df["sk"]>500000)]["anshhj"].sum(),	
    "e_v_ordErg" : df.loc[(df["sk"]<480000) & (df["sk"]>400000)]["ansvj"].sum() - df.loc[(df["sk"]<580000) & (df["sk"]>500000)]["ansvj"].sum(),
    "e_re_ordErg" : df.loc[(df["sk"]<480000) & (df["sk"]>400000)]["rgergvvj"].sum() - df.loc[(df["sk"]<580000) & (df["sk"]>500000)]["rgergvvj"].sum(),
    "e_p_je" : df.loc[(df["sk"]<500000) & (df["sk"]>400000)]["anshhj"].sum() - df.loc[(df["sk"]<600000) & (df["sk"]>500000)]["anshhj"].sum(),
    "e_v_je" : df.loc[(df["sk"]<500000) & (df["sk"]>400000)]["ansvj"].sum() - df.loc[(df["sk"]<600000) & (df["sk"]>500000)]["ansvj"].sum(),
    "e_re_je" : df.loc[(df["sk"]<500000) & (df["sk"]>400000)]["rgergvvj"].sum() - df.loc[(df["sk"]<600000) & (df["sk"]>500000)]["rgergvvj"].sum(),
    }

    return(dic)

def gesamtplan_fin(df):

   ordslzvj2 = df.loc[(df["sk"]<669500) & (df["sk"]>600000)]["rgergvvj"].sum()- df.loc[(df["sk"]<770000) & (df["sk"]>700000)]["rgergvvj"].sum() +  df.loc[(df["sk"]<680000) & (df["sk"]>670000)]["rgergvvj"].sum()- df.loc[(df["sk"]<780000) & (df["sk"]>770000)]["rgergvvj"].sum()
   ordslzvj1 = df.loc[(df["sk"]<669500) & (df["sk"]>600000)]["ansvj"].sum() - df.loc[(df["sk"]<770000) & (df["sk"]>700000)]["ansvj"].sum() + df.loc[(df["sk"]<680000) & (df["sk"]>670000)]["ansvj"].sum() - df.loc[(df["sk"]<780000) & (df["sk"]>770000)]["ansvj"].sum()
   ordslzhhj = df.loc[(df["sk"]<669500) & (df["sk"]>600000)]["anshhj"].sum() - df.loc[(df["sk"]<770000) & (df["sk"]>700000)]["anshhj"].sum() + df.loc[(df["sk"]<680000) & (df["sk"]>670000)]["anshhj"].sum() - df.loc[(df["sk"]<780000) & (df["sk"]>770000)]["anshhj"].sum()
   ordslzpl1 = df.loc[(df["sk"]<669500) & (df["sk"]>600000)]["plan1"].sum() - df.loc[(df["sk"]<770000) & (df["sk"]>700000)]["plan1"].sum() + df.loc[(df["sk"]<680000) & (df["sk"]>670000)]["plan1"].sum() - df.loc[(df["sk"]<780000) & (df["sk"]>770000)]["plan1"].sum()
   ordslzpl2 = df.loc[(df["sk"]<669500) & (df["sk"]>600000)]["plan2"].sum() - df.loc[(df["sk"]<770000) & (df["sk"]>700000)]["plan2"].sum() + df.loc[(df["sk"]<680000) & (df["sk"]>670000)]["plan2"].sum() - df.loc[(df["sk"]<780000) & (df["sk"]>770000)]["plan2"].sum()
   ordslzpl3 = df.loc[(df["sk"]<669500) & (df["sk"]>600000)]["plan3"].sum() - df.loc[(df["sk"]<770000) & (df["sk"]>700000)]["plan3"].sum() + df.loc[(df["sk"]<680000) & (df["sk"]>670000)]["plan3"].sum() - df.loc[(df["sk"]<780000) & (df["sk"]>770000)]["plan3"].sum()

   aoslzvj2 = df.loc[(df["sk"]<669999) & (df["sk"]>669000)]["rgergvvj"].sum()- df.loc[(df["sk"]<769999) & (df["sk"]>769500)]["rgergvvj"].sum()
   aoslzvj1 = df.loc[(df["sk"]<669999) & (df["sk"]>669000)]["ansvj"].sum()- df.loc[(df["sk"]<769999) & (df["sk"]>769500)]["ansvj"].sum()
   aoslzhhj = df.loc[(df["sk"]<669999) & (df["sk"]>669000)]["anshhj"].sum()- df.loc[(df["sk"]<769999) & (df["sk"]>769500)]["anshhj"].sum()
   aoslzpl1 = df.loc[(df["sk"]<669999) & (df["sk"]>669000)]["plan1"].sum()- df.loc[(df["sk"]<769999) & (df["sk"]>769500)]["plan1"].sum()
   aoslzpl2 = df.loc[(df["sk"]<669999) & (df["sk"]>669000)]["plan2"].sum()- df.loc[(df["sk"]<769999) & (df["sk"]>769500)]["plan2"].sum()
   aoslzpl3 = df.loc[(df["sk"]<669999) & (df["sk"]>669000)]["plan3"].sum()- df.loc[(df["sk"]<769999) & (df["sk"]>769500)]["plan3"].sum()

   inv_slz_2vj = df.loc[(df["sk"]<690000) & (df["sk"]>680000)]["rgergvvj"].sum() - df.loc[(df["sk"]<790000) & (df["sk"]>780000)]["rgergvvj"].sum()
   inv_slz_1vj = df.loc[(df["sk"]<690000) & (df["sk"]>680000)]["ansvj"].sum() -  df.loc[(df["sk"]<790000) & (df["sk"]>780000)]["ansvj"].sum()
   inv_slz_hhj = df.loc[(df["sk"]<690000) & (df["sk"]>680000)]["anshhj"].sum() - df.loc[(df["sk"]<790000) & (df["sk"]>780000)]["anshhj"].sum() 
   inv_slz_1pj = df.loc[(df["sk"]<690000) & (df["sk"]>680000)]["plan1"].sum() -  df.loc[(df["sk"]<790000) & (df["sk"]>780000)]["plan1"].sum()
   inv_slz_2pj = df.loc[(df["sk"]<690000) & (df["sk"]>680000)]["plan2"].sum() -  df.loc[(df["sk"]<790000) & (df["sk"]>780000)]["plan2"].sum()
   inv_slz_3pj = df.loc[(df["sk"]<690000) & (df["sk"]>680000)]["plan3"].sum() -  df.loc[(df["sk"]<790000) & (df["sk"]>780000)]["plan3"].sum()

   findic = {
      "lfd_ez_2vj" : df.loc[(df["sk"]<670000) & (df["sk"]>600000)]["rgergvvj"].sum(),
      "lfd_ez_1vj" : df.loc[(df["sk"]<670000) & (df["sk"]>600000)]["ansvj"].sum(),
      "lfd_ez_hhjj" : df.loc[(df["sk"]<670000) & (df["sk"]>600000)]["anshhj"].sum(),
      "lfd_ez_1pj" : df.loc[(df["sk"]<670000) & (df["sk"]>600000)]["plan1"].sum(),
      "lfd_ez_2pj" : df.loc[(df["sk"]<670000) & (df["sk"]>600000)]["plan2"].sum(),
      "lfd_ez_3pj" : df.loc[(df["sk"]<670000) & (df["sk"]>600000)]["plan3"].sum(),
      "lfd_az_2vj" : df.loc[(df["sk"]<770000) & (df["sk"]>700000)]["rgergvvj"].sum(),
      "lfd_az_1vj" :  df.loc[(df["sk"]<770000) & (df["sk"]>700000)]["ansvj"].sum(),
      "lfd_az_hhj" : df.loc[(df["sk"]<770000) & (df["sk"]>700000)]["anshhj"].sum(),
      "lfd_az_1pj" :  df.loc[(df["sk"]<770000) & (df["sk"]>700000)]["plan1"].sum(),
      "lfd_az_2pj" :  df.loc[(df["sk"]<770000) & (df["sk"]>700000)]["plan2"].sum(),
      "lfd_az_3pj" :  df.loc[(df["sk"]<770000) & (df["sk"]>700000)]["plan3"].sum(),
      "lfd_slz_2vj" : df.loc[(df["sk"]<670000) & (df["sk"]>600000)]["rgergvvj"].sum()- df.loc[(df["sk"]<770000) & (df["sk"]>700000)]["rgergvvj"].sum(),
      "lfd_slz_1vj" :  df.loc[(df["sk"]<670000) & (df["sk"]>600000)]["ansvj"].sum() - df.loc[(df["sk"]<770000) & (df["sk"]>700000)]["ansvj"].sum(),
      "lfd_slz_hhj" : df.loc[(df["sk"]<670000) & (df["sk"]>600000)]["anshhj"].sum() - df.loc[(df["sk"]<770000) & (df["sk"]>700000)]["anshhj"].sum(),
      "lfd_slz_1pj" :  df.loc[(df["sk"]<670000) & (df["sk"]>600000)]["plan1"].sum() - df.loc[(df["sk"]<770000) & (df["sk"]>700000)]["plan1"].sum(),
      "lfd_slz_2pj" :  df.loc[(df["sk"]<670000) & (df["sk"]>600000)]["plan2"].sum() - df.loc[(df["sk"]<770000) & (df["sk"]>700000)]["plan2"].sum(),
      "lfd_slz_3pj" :  df.loc[(df["sk"]<670000) & (df["sk"]>600000)]["plan3"].sum() - df.loc[(df["sk"]<770000) & (df["sk"]>700000)]["plan3"].sum(),
      "fin_slz_2vj" : df.loc[(df["sk"]<680000) & (df["sk"]>670000)]["rgergvvj"].sum()- df.loc[(df["sk"]<780000) & (df["sk"]>770000)]["rgergvvj"].sum(),
      "fin_slz_1vj" : df.loc[(df["sk"]<680000) & (df["sk"]>670000)]["ansvj"].sum() - df.loc[(df["sk"]<780000) & (df["sk"]>770000)]["ansvj"].sum(),
      "fin_slz_hhj" : df.loc[(df["sk"]<680000) & (df["sk"]>670000)]["anshhj"].sum() - df.loc[(df["sk"]<780000) & (df["sk"]>770000)]["anshhj"].sum(),
      "fin_slz_1pj" : df.loc[(df["sk"]<680000) & (df["sk"]>670000)]["plan1"].sum() - df.loc[(df["sk"]<780000) & (df["sk"]>770000)]["plan1"].sum(),
      "fin_slz_2pj" : df.loc[(df["sk"]<680000) & (df["sk"]>670000)]["plan2"].sum() - df.loc[(df["sk"]<780000) & (df["sk"]>770000)]["plan2"].sum(),
      "fin_slz_3pj" : df.loc[(df["sk"]<680000) & (df["sk"]>670000)]["plan3"].sum() - df.loc[(df["sk"]<780000) & (df["sk"]>770000)]["plan3"].sum(),
      "ord_slz_2vj" : ordslzvj2,
      "ord_slz_1vj" : ordslzvj1,
      "ord_slz_hhj" : ordslzhhj,
      "ord_slz_1pj" : ordslzpl1,
      "ord_slz_2pj" : ordslzpl2,
      "ord_slz_3pj" : ordslzpl3,
      "ao_slz_2vj" : aoslzvj2,
      "ao_slz_1vj" : aoslzvj1,
      "ao_slz_hhj" : aoslzhhj,
      "ao_slz_1pj" : aoslzpl1,
      "ao_slz_2pj" : aoslzpl2,
      "ao_slz_3pj" : aoslzpl3,
      "inv_ez_2vj" : df.loc[(df["sk"]<690000) & (df["sk"]>680000)]["rgergvvj"].sum() ,
      "inv_ez_1vj" : df.loc[(df["sk"]<690000) & (df["sk"]>680000)]["ansvj"].sum(), 
      "inv_ez_hhj" : df.loc[(df["sk"]<690000) & (df["sk"]>680000)]["anshhj"].sum(),
      "inv_ez_1pj" : df.loc[(df["sk"]<690000) & (df["sk"]>680000)]["plan1"].sum(), 
      "inv_ez_2pj" : df.loc[(df["sk"]<690000) & (df["sk"]>680000)]["plan2"].sum(),
      "inv_ez_3pj" : df.loc[(df["sk"]<690000) & (df["sk"]>680000)]["plan3"].sum(),
      "inv_az_2vj" : df.loc[(df["sk"]<790000) & (df["sk"]>780000)]["rgergvvj"].sum(),
      "inv_az_1vj" : df.loc[(df["sk"]<790000) & (df["sk"]>780000)]["ansvj"].sum(),
      "inv_az_hhj" : df.loc[(df["sk"]<790000) & (df["sk"]>780000)]["anshhj"].sum(),
      "inv_az_1pj" : df.loc[(df["sk"]<790000) & (df["sk"]>780000)]["plan1"].sum(),
      "inv_az_2pj" : df.loc[(df["sk"]<790000) & (df["sk"]>780000)]["plan2"].sum(),
      "inv_az_3pj" : df.loc[(df["sk"]<790000) & (df["sk"]>780000)]["plan3"].sum(),
      "inv_slz_2vj" : df.loc[(df["sk"]<690000) & (df["sk"]>680000)]["rgergvvj"].sum() - df.loc[(df["sk"]<790000) & (df["sk"]>780000)]["rgergvvj"].sum(),
      "inv_slz_1vj" : df.loc[(df["sk"]<690000) & (df["sk"]>680000)]["ansvj"].sum() -  df.loc[(df["sk"]<790000) & (df["sk"]>780000)]["ansvj"].sum(),
      "inv_slz_hhj" : df.loc[(df["sk"]<690000) & (df["sk"]>680000)]["anshhj"].sum() - df.loc[(df["sk"]<790000) & (df["sk"]>780000)]["anshhj"].sum() ,
      "inv_slz_1pj" : df.loc[(df["sk"]<690000) & (df["sk"]>680000)]["plan1"].sum() -  df.loc[(df["sk"]<790000) & (df["sk"]>780000)]["plan1"].sum(),
      "inv_slz_2pj" : df.loc[(df["sk"]<690000) & (df["sk"]>680000)]["plan2"].sum() -  df.loc[(df["sk"]<790000) & (df["sk"]>780000)]["plan2"].sum(),
      "inv_slz_3pj" : df.loc[(df["sk"]<690000) & (df["sk"]>680000)]["plan3"].sum() -  df.loc[(df["sk"]<790000) & (df["sk"]>780000)]["plan3"].sum(),
      "finm_slz_2vj" : ,
      "finm_slz_1vj" : ,
      "finm_slz_hhj" : ,
      "finm_slz_1pj" : ,
      "finm_slz_2pj" : ,
      "finm_slz_3pj" : ,
      "kred_ez_2vj" : df.loc[(df["sk"]<700000) & (df["sk"]>690000)]["rgergvvj"].sum(),
      "kred_ez_1vj" : df.loc[(df["sk"]<700000) & (df["sk"]>690000)]["ansvj"].sum(), 
      "kred_ez_hhj" : df.loc[(df["sk"]<700000) & (df["sk"]>690000)]["anshhj"].sum(),
      "kred_ez_1pj" : df.loc[(df["sk"]<700000) & (df["sk"]>690000)]["plan1"].sum(),
      "kred_ez_2pj" : df.loc[(df["sk"]<700000) & (df["sk"]>690000)]["plan2"].sum(),
      "kred_ez_3pj" : df.loc[(df["sk"]<700000) & (df["sk"]>690000)]["plan3"].sum(),
      "kred_az_2vj" : df.loc[(df["sk"]<800000) & (df["sk"]>790000)]["rgergvvj"].sum(),
      "kred_az_1vj" : df.loc[(df["sk"]<800000) & (df["sk"]>790000)]["ansvj"].sum(),
      "kred_az_hhj" : df.loc[(df["sk"]<800000) & (df["sk"]>790000)]["anshhj"].sum(),
      "kred_az_1pj" : df.loc[(df["sk"]<800000) & (df["sk"]>790000)]["plan1"].sum(),
      "kred_az_2pj" : df.loc[(df["sk"]<800000) & (df["sk"]>790000)]["plan2"].sum(),
      "kred_az_3pj" : df.loc[(df["sk"]<800000) & (df["sk"]>790000)]["plan3"].sum(),
      "kred_ng_2vj" : df.loc[(df["sk"]<700000) & (df["sk"]>690000)]["rgergvvj"].sum()
      "kred_ng_1vj" : df.loc[(df["sk"]<700000) & (df["sk"]>690000)]["ansvj"].sum(), 
      "kred_ng_hhj" : df.loc[(df["sk"]<700000) & (df["sk"]>690000)]["anshhj"].sum(),
      "kred_ng_1pj" : df.loc[(df["sk"]<700000) & (df["sk"]>690000)]["plan1"].sum(),
      "kred_ng_2pj" : df.loc[(df["sk"]<700000) & (df["sk"]>690000)]["plan2"].sum(),
      "kred_ng_3pj" : df.loc[(df["sk"]<700000) & (df["sk"]>690000)]["plan3"].sum(),
 
      "kbv_slz_2vj" : df.loc[(df["sk"]<700000) & (df["sk"]>690000)]["rgergvvj"].sum() - df.loc[(df["sk"]<800000) & (df["sk"]>790000)]["rgergvvj"].sum(),
      "kbv_slz_1vj" : df.loc[(df["sk"]<700000) & (df["sk"]>690000)]["ansvj"].sum() - df.loc[(df["sk"]<800000) & (df["sk"]>790000)]["ansvj"].sum(),
      "kbv_slz_hhj" : df.loc[(df["sk"]<700000) & (df["sk"]>690000)]["anshhj"].sum() - df.loc[(df["sk"]<800000) & (df["sk"]>790000)]["anshhj"].sum(),
      "kbv_slz_1pj" : df.loc[(df["sk"]<700000) & (df["sk"]>690000)]["plan1"].sum() - df.loc[(df["sk"]<800000) & (df["sk"]>790000)]["plan1"].sum(),
      "kbv_slz_2pj" : df.loc[(df["sk"]<700000) & (df["sk"]>690000)]["plan2"].sum() - df.loc[(df["sk"]<800000) & (df["sk"]>790000)]["plan2"].sum(),
      "kbv_slz_3pj" : df.loc[(df["sk"]<700000) & (df["sk"]>690000)]["plan3"].sum() - df.loc[(df["sk"]<800000) & (df["sk"]>790000)]["plan3"].sum(),

      "ffs_2vj" : ordslzvj2 - df.loc[(df["sk"]<800000) & (df["sk"]>790000)]["rgergvvj"].sum(),
      "ffs_1vj" : ordslzvj1 - df.loc[(df["sk"]<800000) & (df["sk"]>790000)]["ansvj"].sum(),
      "ffs_hhj" : ordslzhhj - df.loc[(df["sk"]<800000) & (df["sk"]>790000)]["anshhj"].sum(),
      "ffs_1pj" : ordslzpl1 - df.loc[(df["sk"]<800000) & (df["sk"]>790000)]["plan1"].sum(),
      "ffs_2pj" : ordslzpl2 - df.loc[(df["sk"]<800000) & (df["sk"]>790000)]["plan2"].sum(),
      "ffs_3pj" : ordslzpl3 - df.loc[(df["sk"]<800000) & (df["sk"]>790000)]["plan3"].sum(),
   }
   findic

def gesamtplan_vvj(df):
   dic = {
      "lfdE_pl_vvj" : df.loc[(df["sk"]<470000)]["planvvj"].sum(),	                
      "lfdE_je_vvj" : df.loc[(df["sk"]<470000)]["rgergvvj"].sum(),	
      "lfdE_aw_vvj" : df.loc[(df["sk"]<470000)]["rgergvvj"].sum() - df.loc[(df["sk"]<470000)]["planvvj"].sum(),
      "lfdA_pl_vvj" : df.loc[(df["sk"]<570000) & (df["sk"]>500000)]["planvvj"].sum(),	
      "lfdA_je_vvj" : df.loc[(df["sk"]<570000) & (df["sk"]>500000)]["rgergvvj"].sum(),		
      "lfdA_aw_vvj" : df.loc[(df["sk"]<570000) & (df["sk"]>500000)]["rgergvvj"].sum() - df.loc[(df["sk"]<570000) & (df["sk"]>500000)]["planvvj"].sum(),	
      "lfdSaldo_pl_vvj" : 	df.loc[(df["sk"]<500000)]["planvvj"].sum() - df.loc[(df["sk"]<600000) & (df["sk"]>500000)]["planvvj"].sum(),	
      "lfdSaldo_je_vvj" : 	df.loc[(df["sk"]<500000)]["rgergvvj"].sum() - df.loc[(df["sk"]<600000) & (df["sk"]>500000)]["rgergvvj"].sum(),
      "lfdSaldo_aw_vvj" :  df.loc[(df["sk"]<500000)]["rgergvvj"].sum() - df.loc[(df["sk"]<500000)]["planvvj"].sum() - df.loc[(df["sk"]<600000) & (df["sk"]>500000)]["rgergvvj"].sum() - df.loc[(df["sk"]<600000) & (df["sk"]>500000)]["planvvj"].sum(),
      "zinsE_pl_vvj" : df.loc[(df["sk"]<480000) & (df["sk"]>470000)]["planvvj"].sum(),	
      "zinsE_je_vvj" : df.loc[(df["sk"]<480000) & (df["sk"]>470000)]["rgergvvj"].sum(),
      "zinsE_aw_vvj" : df.loc[(df["sk"]<480000) & (df["sk"]>470000)]["rgergvvj"].sum() - df.loc[(df["sk"]<580000) & (df["sk"]>570000)]["planvvj"].sum(),
      "zinsA_pl_vvj" : df.loc[(df["sk"]<580000) & (df["sk"]>570000)]["planvvj"].sum(),	
      "zinsA_je_vvj" : df.loc[(df["sk"]<580000) & (df["sk"]>570000)]["rgergvvj"].sum(),
      "zinsA_aw_vvj" : df.loc[(df["sk"]<580000) & (df["sk"]>570000)]["rgergvvj"].sum() - df.loc[(df["sk"]<580000) & (df["sk"]>570000)]["planvvj"].sum(),
      "zinsSaldo_pl_vvj" : df.loc[(df["sk"]<480000) & (df["sk"]>470000)]["planvvj"].sum() - df.loc[(df["sk"]<580000) & (df["sk"]>570000)]["planvvj"].sum(),		
      "zinsSaldo_je_vvj" :  df.loc[(df["sk"]<480000) & (df["sk"]>470000)]["rgergvvj"].sum() - df.loc[(df["sk"]<580000) & (df["sk"]>570000)]["rgergvvj"].sum(),
      "zinsSaldo_aw_vvj" : (df.loc[(df["sk"]<480000) & (df["sk"]>470000)]["rgergvvj"].sum() - df.loc[(df["sk"]<580000) & (df["sk"]>570000)]["planvvj"].sum()) - (df.loc[(df["sk"]<580000) & (df["sk"]>570000)]["rgergvvj"].sum() - df.loc[(df["sk"]<580000) & (df["sk"]>570000)]["planvvj"].sum()),
      "ordErg_pl_vvj" : df.loc[(df["sk"]<500000)]["planvvj"].sum() - df.loc[(df["sk"]<600000) & (df["sk"]>500000)]["planvvj"].sum() + df.loc[(df["sk"]<480000) & (df["sk"]>470000)]["planvvj"].sum() - df.loc[(df["sk"]<580000) & (df["sk"]>570000)]["planvvj"].sum(),
      "ordErg_je_vvj" : df.loc[(df["sk"]<500000)]["rgergvvj"].sum() - df.loc[(df["sk"]<600000) & (df["sk"]>500000)]["rgergvvj"].sum() + df.loc[(df["sk"]<480000) & (df["sk"]>470000)]["rgergvvj"].sum() - df.loc[(df["sk"]<580000) & (df["sk"]>570000)]["rgergvvj"].sum(),
      "ordErg_aw_vvj" : df.loc[(df["sk"]<500000)]["rgergvvj"].sum() - df.loc[(df["sk"]<500000)]["planvvj"].sum() - df.loc[(df["sk"]<600000) & (df["sk"]>500000)]["rgergvvj"].sum() - df.loc[(df["sk"]<600000) & (df["sk"]>500000)]["planvvj"].sum() + (df.loc[(df["sk"]<480000) & (df["sk"]>470000)]["rgergvvj"].sum() - df.loc[(df["sk"]<580000) & (df["sk"]>570000)]["planvvj"].sum()) - (df.loc[(df["sk"]<580000) & (df["sk"]>570000)]["rgergvvj"].sum() - df.loc[(df["sk"]<580000) & (df["sk"]>570000)]["planvvj"].sum()),
      "erg_pl_vvj" : df.loc[(df["sk"]<500000)]["planvvj"].sum() - df.loc[(df["sk"]<600000) & (df["sk"]>500000)]["planvvj"].sum() + df.loc[(df["sk"]<480000) & (df["sk"]>470000)]["planvvj"].sum() - df.loc[(df["sk"]<580000) & (df["sk"]>570000)]["planvvj"].sum(),
      "erg_je_vvj" : df.loc[(df["sk"]<500000)]["rgergvvj"].sum() - df.loc[(df["sk"]<600000) & (df["sk"]>500000)]["rgergvvj"].sum() + df.loc[(df["sk"]<480000) & (df["sk"]>470000)]["rgergvvj"].sum() - df.loc[(df["sk"]<580000) & (df["sk"]>570000)]["rgergvvj"].sum(),
      "erg_aw_vvj" : df.loc[(df["sk"]<500000)]["rgergvvj"].sum() - df.loc[(df["sk"]<500000)]["planvvj"].sum() - df.loc[(df["sk"]<600000) & (df["sk"]>500000)]["rgergvvj"].sum() - df.loc[(df["sk"]<600000) & (df["sk"]>500000)]["planvvj"].sum() + (df.loc[(df["sk"]<480000) & (df["sk"]>470000)]["rgergvvj"].sum() - df.loc[(df["sk"]<580000) & (df["sk"]>570000)]["planvvj"].sum()) - (df.loc[(df["sk"]<580000) & (df["sk"]>570000)]["rgergvvj"].sum() - df.loc[(df["sk"]<580000) & (df["sk"]>570000)]["planvvj"].sum()),
      "osf_pl_vvj" : df.loc[(df["sk"]<680000) & (df["sk"]>600000)]["planvvj"].sum() - df.loc[(df["sk"]<780000) & (df["sk"]>700000)]["planvvj"].sum(),	
      "osf_je_vvj" : df.loc[(df["sk"]<680000) & (df["sk"]>600000)]["rgergvvj"].sum() - df.loc[(df["sk"]<780000) & (df["sk"]>700000)]["rgergvvj"].sum(),	
      "osf_aw_vvj" : (df.loc[(df["sk"]<680000) & (df["sk"]>600000)]["rgergvvj"].sum() - df.loc[(df["sk"]<780000) & (df["sk"]>700000)]["rgergvvj"].sum()) - (df.loc[(df["sk"]<680000) & (df["sk"]>600000)]["planvvj"].sum() - df.loc[(df["sk"]<780000) & (df["sk"]>700000)]["planvvj"].sum()),
      "e1inv_pl_vvj" : df.loc[(df["sk"]<682000) & (df["sk"]>681000)]["planvvj"].sum(),
      "e1inv_je_vvj" : df.loc[(df["sk"]<682000) & (df["sk"]>681000)]["rgergvvj"].sum(),
      "e1inv_aw_vvj" : df.loc[(df["sk"]<682000) & (df["sk"]>681000)]["rgergvvj"].sum() - df.loc[(df["sk"]<682000) & (df["sk"]>681000)]["planvvj"].sum(),
      "e2inv_pl_vvj" : df.loc[(df["sk"]<683000) & (df["sk"]>682000)]["planvvj"].sum(),
      "e2inv_je_vvj" : df.loc[(df["sk"]<683000) & (df["sk"]>682000)]["rgergvvj"].sum(),
      "e2inv_aw_vvj" : df.loc[(df["sk"]<683000) & (df["sk"]>682000)]["rgergvvj"].sum() - df.loc[(df["sk"]<683000) & (df["sk"]>682000)]["planvvj"].sum(),
      "e3inv_pl_vvj" : df.loc[(df["sk"]<690000) & (df["sk"]>683000)]["planvvj"].sum(),
      "e3inv_je_vvj" : df.loc[(df["sk"]<690000) & (df["sk"]>683000)]["rgergvvj"].sum(),
      "e3inv_aw_vvj" : df.loc[(df["sk"]<690000) & (df["sk"]>683000)]["rgergvvj"].sum() - df.loc[(df["sk"]<690000) & (df["sk"]>683000)]["planvvj"].sum(),
      "esuminv_pl_vvj" : df.loc[(df["sk"]<690000) & (df["sk"]>680000)]["planvvj"].sum(),
      "esuminv_je_vvj" : df.loc[(df["sk"]<690000) & (df["sk"]>680000)]["rgergvvj"].sum(),
      "esuminv_aw_vvj" : df.loc[(df["sk"]<690000) & (df["sk"]>680000)]["rgergvvj"].sum() - df.loc[(df["sk"]<690000) & (df["sk"]>680000)]["planvvj"].sum(),
      "a1inv_pl_vvj" : df.loc[(df["sk"]<785000) & (df["sk"]>780000)]["planvvj"].sum(),
      "a1inv_je_vvj" : df.loc[(df["sk"]<785000) & (df["sk"]>780000)]["rgergvvj"].sum(),
      "a1inv_aw_vvj" : df.loc[(df["sk"]<785000) & (df["sk"]>780000)]["rgergvvj"].sum() - df.loc[(df["sk"]<785000) & (df["sk"]>780000)]["planvvj"].sum(),
      "a2inv_pl_vvj" : df.loc[(df["sk"]<786000) & (df["sk"]>785000)]["planvvj"].sum(),
      "a2inv_je_vvj" : df.loc[(df["sk"]<786000) & (df["sk"]>785000)]["rgergvvj"].sum(),
      "a2inv_aw_vvj" : df.loc[(df["sk"]<786000) & (df["sk"]>785000)]["rgergvvj"].sum() - df.loc[(df["sk"]<786000) & (df["sk"]>785000)]["planvvj"].sum(),
      "a3inv_pl_vvj" : df.loc[(df["sk"]<788000) & (df["sk"]>786000)]["planvvj"].sum(),
      "a3inv_je_vvj" : df.loc[(df["sk"]<788000) & (df["sk"]>786000)]["rgergvvj"].sum(),
      "a3inv_aw_vvj" : df.loc[(df["sk"]<788000) & (df["sk"]>786000)]["rgergvvj"].sum() - df.loc[(df["sk"]<788000) & (df["sk"]>786000)]["planvvj"].sum(),
      "a4inv_pl_vvj" : df.loc[(df["sk"]<790000) & (df["sk"]>789000)]["planvvj"].sum(),
      "a4inv_je_vvj" : df.loc[(df["sk"]<790000) & (df["sk"]>789000)]["rgergvvj"].sum(),
      "a4inv_aw_vvj" : df.loc[(df["sk"]<790000) & (df["sk"]>789000)]["rgergvvj"].sum() - df.loc[(df["sk"]<786000) & (df["sk"]>785000)]["planvvj"].sum(),
      "asuminv_pl_vvj" : df.loc[(df["sk"]<790000) & (df["sk"]>780000)]["planvvj"].sum(),
      "asuminv_je_vvj" : df.loc[(df["sk"]<790000) & (df["sk"]>780000)]["rgergvvj"].sum(),
      "asuminv_aw_vvj" : df.loc[(df["sk"]<790000) & (df["sk"]>780000)]["rgergvvj"].sum() - df.loc[(df["sk"]<790000) & (df["sk"]>780000)]["planvvj"].sum(),
      "saldoinv_pl_vvj" : df.loc[(df["sk"]<690000) & (df["sk"]>680000)]["planvvj"].sum()- df.loc[(df["sk"]<790000) & (df["sk"]>780000)]["planvvj"].sum(),
      "saldoinv_je_vvj" : df.loc[(df["sk"]<690000) & (df["sk"]>680000)]["rgergvvj"].sum()- df.loc[(df["sk"]<790000) & (df["sk"]>780000)]["rgergvvj"].sum(),
      "saldoinv_aw_vvj" : df.loc[(df["sk"]<690000) & (df["sk"]>680000)]["rgergvvj"].sum()- df.loc[(df["sk"]<790000) & (df["sk"]>780000)]["rgergvvj"].sum() - (df.loc[(df["sk"]<690000) & (df["sk"]>680000)]["planvvj"].sum()- df.loc[(df["sk"]<790000) & (df["sk"]>780000)]["planvvj"].sum()),
      "fin_dif_pl_vvj" : df.loc[(df["sk"]<690000) & (df["sk"]>600000)]["planvvj"].sum()- df.loc[(df["sk"]<790000) & (df["sk"]>700000)]["planvvj"].sum(),
      "fin_dif_je_vvj" : df.loc[(df["sk"]<690000) & (df["sk"]>600000)]["rgergvvj"].sum()- df.loc[(df["sk"]<790000) & (df["sk"]>700000)]["rgergvvj"].sum(),
      "fin_dif_aw_vvj" : df.loc[(df["sk"]<690000) & (df["sk"]>600000)]["rgergvvj"].sum()- df.loc[(df["sk"]<790000) & (df["sk"]>700000)]["rgergvvj"].sum() - (df.loc[(df["sk"]<690000) & (df["sk"]>600000)]["planvvj"].sum()- df.loc[(df["sk"]<790000) & (df["sk"]>700000)]["planvvj"].sum()),
      "ekred_pl_vvj" : df.loc[(df["sk"]<700000) & (df["sk"]>690000)]["planvvj"].sum(),
      "ekred_je_vvj" : df.loc[(df["sk"]<700000) & (df["sk"]>690000)]["rgergvvj"].sum(),
      "ekred_aw_vvj" : df.loc[(df["sk"]<700000) & (df["sk"]>690000)]["rgergvvj"].sum() - df.loc[(df["sk"]<700000) & (df["sk"]>690000)]["planvvj"].sum(),
      "akred_pl_vvj" : df.loc[(df["sk"]<800000) & (df["sk"]>790000)]["planvvj"].sum(),
      "akred_je_vvj" : df.loc[(df["sk"]<800000) & (df["sk"]>790000)]["rgergvvj"].sum(),
      "akred_aw_vvj" : df.loc[(df["sk"]<800000) & (df["sk"]>790000)]["rgergvvj"].sum() -df.loc[(df["sk"]<800000) & (df["sk"]>790000)]["planvvj"].sum(),
      "saldokred_pl_vvj" : df.loc[(df["sk"]<700000) & (df["sk"]>690000)]["planvvj"].sum()- df.loc[(df["sk"]<800000) & (df["sk"]>790000)]["planvvj"].sum(),
      "saldokred_je_vvj" : df.loc[(df["sk"]<700000) & (df["sk"]>690000)]["rgergvvj"].sum()- df.loc[(df["sk"]<800000) & (df["sk"]>790000)]["rgergvvj"].sum(),
      "saldokred_aw_vvj" : (df.loc[(df["sk"]<700000) & (df["sk"]>690000)]["rgergvvj"].sum() - df.loc[(df["sk"]<700000) & (df["sk"]>690000)]["planvvj"].sum()) - (df.loc[(df["sk"]<800000) & (df["sk"]>790000)]["rgergvvj"].sum() - df.loc[(df["sk"]<800000) & (df["sk"]>790000)]["planvvj"].sum()),
      "ffs_pl_vvj" : df.loc[(df["sk"]<680000) & (df["sk"]>600000)]["planvvj"].sum() - df.loc[(df["sk"]<780000) & (df["sk"]>700000)]["planvvj"].sum() - df.loc[(df["sk"]<800000) & (df["sk"]>790000)]["planvvj"].sum(),
      "ffs_je_vvj" : df.loc[(df["sk"]<680000) & (df["sk"]>600000)]["rgergvvj"].sum() - df.loc[(df["sk"]<780000) & (df["sk"]>700000)]["rgergvvj"].sum() - df.loc[(df["sk"]<800000) & (df["sk"]>790000)]["rgergvvj"].sum(),
      "ffs_aw_vvj" : df.loc[(df["sk"]<680000) & (df["sk"]>600000)]["rgergvvj"].sum() - df.loc[(df["sk"]<780000) & (df["sk"]>700000)]["rgergvvj"].sum() - df.loc[(df["sk"]<800000) & (df["sk"]>790000)]["rgergvvj"].sum() - df.loc[(df["sk"]<680000) & (df["sk"]>600000)]["planvvj"].sum() - df.loc[(df["sk"]<780000) & (df["sk"]>700000)]["planvvj"].sum() - df.loc[(df["sk"]<800000) & (df["sk"]>790000)]["planvvj"].sum()
   }
   return dic


def get_hhst_dict(df, dferl, minsk, maxsk):
    """
    Gibt ein dictionary nach Sachkonten gefiltert zurück  
    df = Dataframe mit den Haushaltsstellendaten
    dferl = Dataframe mit Erläuterungen
    minsk = kleinster Sachkontowert
    maxsk = größter Sachkontowert

    Return: gefilterter Dataframe wird in eine dict-liste umgewandelt
    """
    teildf = df.loc[df["sk"] < 410000]   
    #print(dferl)
    dferl["sk"] = dferl["sk"].fillna(0).astype("int")
    #print(dferl)
    dfnew = pd.merge(teildf, dferl, how = "left", left_on= ["produkt", "sk"], right_on=["produkt", "sk"])
    dfnew = dfnew.drop(["hh", "mn_y", "erlNr", "erlTyp", "nicht uebertragbar"], axis=1)
    #print(dfnew)
    st = dfnew[["hhs","sk", "produkt", "bez", "anshhj", "ansvj", "rgergvvj", "erl"]].to_dict('records')
    return st



def get_steuern(df, dferl):
   """
   Gibt ein dictionary zurück 
   """
   teildf = df.loc[df["sk"] < 410000] 
   dferl = dferl.drop("hhs", axis=1)
   #print(dferl)
   dferl["sk"] = dferl["sk"].fillna(0).astype("int")
   #print(dferl)
   dfnew = pd.merge(teildf, dferl, how = "left", left_on= ["produkt", "sk"], right_on=["produkt", "sk"])
   dfnew = dfnew.drop(["hh", "mn_y", "erlNr", "erlTyp", "nicht uebertragbar"], axis=1)
   dfnew["erl"] = dfnew["erl"].fillna(0)
   #print(dfnew)
   st = dfnew[["hhs","sk", "produkt", "bez", "anshhj", "ansvj", "rgergvvj", "erl"]].to_dict('records')
   return st

def get_umlagen(df, dferl, mindiff=0):
   """
   Gibt ein dictionary zurück 
   """

   df["ansdiff"] = df["anshhj"] - df["ansvj"]
   dferl = dferl.drop("hhs", axis=1)
   teildf = df.loc[(df["sk"]<420000) & (df["sk"]>410000)]

   teildf = teildf.loc[(teildf["ansdiff"] >= mindiff) | (teildf["ansdiff"] <= mindiff*-1) ]
   #teildf.info()
   #print(dferl)
   dferl["sk"] = dferl["sk"].fillna(0).astype("int")
   #print(dferl)
   dfnew = pd.merge(teildf, dferl, how = "left", left_on= ["produkt", "sk"], right_on=["produkt", "sk"])
   #print(dfnew)
   dfnew = dfnew.drop(["hh", "mn_y", "erlNr", "erlTyp", "nicht uebertragbar"], axis=1)
   dfnew["erl"] = dfnew["erl"].fillna(0)
   #print(dfnew)
   st = dfnew[["hhs","sk", "produkt", "bez", "anshhj", "ansvj", "rgergvvj", "erl"]].to_dict('records')
   #print(st)
   return st

def get_sozE(df, dferl, mindiff=0):
   df["ansdiff"] = df["anshhj"] - df["ansvj"]  
   dferl = dferl.drop("hhs", axis=1)
   teildf = df.loc[(df["sk"]<430000) & (df["sk"]>420000)]
   teildf = teildf.loc[(teildf["ansdiff"] >= mindiff) | (teildf["ansdiff"] <= mindiff*-1) ]
   dferl = dferl.drop("hhs", axis=1)
   #print(dferl)
   dferl["sk"] = dferl["sk"].fillna(0).astype("int")
   #print(dferl)
   dfnew = pd.merge(teildf, dferl, how = "left", left_on= ["produkt", "sk"], right_on=["produkt", "sk"])
   dfnew = dfnew.drop(["hh", "mn_y", "erlNr", "erlTyp", "nicht uebertragbar"], axis=1)
   dfnew["erl"] = dfnew["erl"].fillna(0)
   #print(dfnew)
   st = dfnew[["hhs","sk", "produkt", "bez", "anshhj", "ansvj", "rgergvvj", "erl"]].to_dict('records')
   return st

def get_oerE(df, dferl, mindiff=0):
   df["ansdiff"] = df["anshhj"] - df["ansvj"]  
   dferl = dferl.drop("hhs", axis=1)
   teildf = df.loc[(df["sk"]<440000) & (df["sk"]>430000)]
   teildf = teildf.loc[(teildf["ansdiff"] >= mindiff) | (teildf["ansdiff"] <= mindiff*-1) ]
   #teildf.info()
   #print(dferl)
   dferl["sk"] = dferl["sk"].fillna(0).astype("int")
   #print(dferl)
   dfnew = pd.merge(teildf, dferl, how = "left", left_on= ["produkt", "sk"], right_on=["produkt", "sk"])
   #print(dfnew)
   dfnew = dfnew.drop(["hh", "mn_y", "erlNr", "erlTyp", "nicht uebertragbar"], axis=1)
   dfnew["erl"] = dfnew["erl"].fillna(0)
   #print(dfnew)
   st = dfnew[["hhs","sk", "produkt", "bez", "anshhj", "ansvj", "rgergvvj", "erl"]].to_dict('records')
   #print(st)
   return st

def get_prE(df, dferl, mindiff=0):
   df["ansdiff"] = df["anshhj"] - df["ansvj"] 
   dferl = dferl.drop("hhs", axis=1) 
   teildf = df.loc[(df["sk"]<442000) & (df["sk"]>440000)]
   teildf = teildf.loc[(teildf["ansdiff"] >= mindiff) | (teildf["ansdiff"] <= mindiff*-1) ]
   #teildf.info()
   #print(dferl)
   dferl["sk"] = dferl["sk"].fillna(0).astype("int")
   #print(dferl)
   dfnew = pd.merge(teildf, dferl, how = "left", left_on= ["produkt", "sk"], right_on=["produkt", "sk"])
   #print(dfnew)
   dfnew = dfnew.drop(["hh", "mn_y", "erlNr", "erlTyp", "nicht uebertragbar"], axis=1)
   dfnew["erl"] = dfnew["erl"].fillna(0)
   #print(dfnew)
   st = dfnew[["hhs","sk", "produkt", "bez", "anshhj", "ansvj", "rgergvvj", "erl"]].to_dict('records')
   #print(st)
   return st

def get_kostE(df, dferl, mindiff=0):
   df["ansdiff"] = df["anshhj"] - df["ansvj"] 
   dferl = dferl.drop("hhs", axis=1) 
   teildf = df.loc[(df["sk"]<450000) & (df["sk"]>442000)]
   teildf = teildf.loc[(teildf["ansdiff"] >= mindiff) | (teildf["ansdiff"] <= mindiff*-1) ]
   #teildf.info()
   #print(dferl)
   dferl["sk"] = dferl["sk"].fillna(0).astype("int")
   #print(dferl)
   dfnew = pd.merge(teildf, dferl, how = "left", left_on= ["produkt", "sk"], right_on=["produkt", "sk"])
   #print(dfnew)
   dfnew = dfnew.drop(["hh", "mn_y", "erlNr", "erlTyp", "nicht uebertragbar"], axis=1)
   dfnew["erl"] = dfnew["erl"].fillna(0)
   #print(dfnew)
   st = dfnew[["hhs","sk", "produkt", "bez", "anshhj", "ansvj", "rgergvvj", "erl"]].to_dict('records')
   #print(st)
   return st

def get_sonstE(df, dferl, mindiff=0):
   df["ansdiff"] = df["anshhj"] - df["ansvj"] 
   dferl = dferl.drop("hhs", axis=1) 
   teildf = df.loc[(df["sk"]<470000) & (df["sk"]>460000)]
   teildf = teildf.loc[(teildf["ansdiff"] >= mindiff) | (teildf["ansdiff"] <= mindiff*-1) ]
   #teildf.info()
   #print(dferl)
   dferl["sk"] = dferl["sk"].fillna(0).astype("int")
   #print(dferl)
   dfnew = pd.merge(teildf, dferl, how = "left", left_on= ["produkt", "sk"], right_on=["produkt", "sk"])
   #print(dfnew)
   dfnew = dfnew.drop(["hh", "mn_y", "erlNr", "erlTyp", "nicht uebertragbar"], axis=1)
   dfnew["erl"] = dfnew["erl"].fillna(0)
   #print(dfnew)
   st = dfnew[["hhs","sk", "produkt", "bez", "anshhj", "ansvj", "rgergvvj", "erl"]].to_dict('records')
   #print(st)
   return st

def get_finE(df, dferl, mindiff=0):
   df["ansdiff"] = df["anshhj"] - df["ansvj"] 
   dferl = dferl.drop("hhs", axis=1) 
   teildf = df.loc[(df["sk"]<480000) & (df["sk"]>470000)]
   teildf = teildf.loc[(teildf["ansdiff"] >= mindiff) | (teildf["ansdiff"] <= mindiff*-1) ]
   #teildf.info()
   #print(dferl)
   dferl["sk"] = dferl["sk"].fillna(0).astype("int")
   #print(dferl)
   dfnew = pd.merge(teildf, dferl, how = "left", left_on= ["produkt", "sk"], right_on=["produkt", "sk"])
   #print(dfnew)
   dfnew = dfnew.drop(["hh", "mn_y", "erlNr", "erlTyp", "nicht uebertragbar"], axis=1)
   dfnew["erl"] = dfnew["erl"].fillna(0)
   #print(dfnew)
   st = dfnew[["hhs","sk", "produkt", "bez", "anshhj", "ansvj", "rgergvvj", "erl"]].to_dict('records')
   #print(st)
   return st

def get_persA(df, dferl):
   df["ansdiff"] = df["anshhj"] - df["ansvj"] 
   teildf = df.loc[(df["sk"]<520000) & (df["sk"]>500000)]
   dferl = dferl.drop("hhs", axis=1)
   #print(dferl)
   dferl["sk"] = dferl["sk"].fillna(0).astype("int")
   #print(dferl)
   dfnew = pd.merge(teildf, dferl, how = "left", left_on= ["produkt", "sk"], right_on=["produkt", "sk"])
   dfnew = dfnew.drop(["hh", "mn_y", "erlNr", "erlTyp", "nicht uebertragbar"], axis=1)
   dfnew["erl"] = dfnew["erl"].fillna(0)
   #print(dfnew)
   st = dfnew[["hhs","sk", "produkt", "bez", "anshhj", "ansvj", "rgergvvj", "erl"]].to_dict('records')
   return st

def get_msdA(df, dferl, mindiff=0):
   #dferl = dferl.drop("hhs", axis=1) 
   df["ansdiff"] = df["anshhj"] - df["ansvj"] 
   teildf = df.loc[(df["sk"]<530000) & (df["sk"]>520000)]
   #print(teildf)
   teildf = teildf.loc[(teildf["ansdiff"] >= mindiff) | (teildf["ansdiff"] <= mindiff*-1) ]
   #print("----------------------------------")
   #print(teildf)
   dferl = dferl.drop("hhs", axis=1)
      #print(dferl)
   dferl["sk"] = dferl["sk"].fillna(0).astype("int")
   #print(dferl)
   dfnew = pd.merge(teildf, dferl, how = "left", left_on= ["produkt", "sk"], right_on=["produkt", "sk"])
   dfnew = dfnew.drop(["hh", "mn_y", "erlNr", "erlTyp", "nicht uebertragbar"], axis=1)
   dfnew["erl"] = dfnew["erl"].fillna(0)
   #print(dfnew)
   st = dfnew[["hhs","sk", "produkt", "bez", "anshhj", "ansvj", "rgergvvj", "erl"]].to_dict('records')
   return st

def get_AfA(df, dferl, mindiff=0):
   teildf = df.loc[(df["sk"]<540000) & (df["sk"]>530000)]
   dferl = dferl.drop("hhs", axis=1)
      #print(dferl)
   dferl["sk"] = dferl["sk"].fillna(0).astype("int")
   #print(dferl)
   dfnew = pd.merge(teildf, dferl, how = "left", left_on= ["produkt", "sk"], right_on=["produkt", "sk"])
   dfnew = dfnew.drop(["hh", "mn_y", "erlNr", "erlTyp", "nicht uebertragbar"], axis=1)
   dfnew["erl"] = dfnew["erl"].fillna(0)
   #print(dfnew)
   summ = dfnew[["anshhj", "ansvj", "rgergvvj"]].sum()
   summ = summ.to_dict()
   st = dfnew[["hhs","sk", "produkt", "bez", "anshhj", "ansvj", "rgergvvj", "erl"]].to_dict('records')
   a = (st, summ)
   return a 

def get_UmlA(df, dferl, mindiff=0):
   teildf = df.loc[(df["sk"]<550000) & (df["sk"]>540000)]
   dferl = dferl.drop("hhs", axis=1)
   #print(dferl)
   dferl["sk"] = dferl["sk"].fillna(0).astype("int")
   #print(dferl)
   dfnew = pd.merge(teildf, dferl, how = "left", left_on= ["produkt", "sk"], right_on=["produkt", "sk"])
   dfnew = dfnew.drop(["hh", "mn_y", "erlNr", "erlTyp", "nicht uebertragbar"], axis=1)
   dfnew["erl"] = dfnew["erl"].fillna(0)
   #print(dfnew)
   st = dfnew[["hhs","sk", "produkt", "bez", "anshhj", "ansvj", "rgergvvj", "erl"]].to_dict('records')
   return st

def get_sozA(df, dferl, mindiff=0):
   df["ansdiff"] = df["anshhj"] - df["ansvj"] 
   teildf = df.loc[(df["sk"]<560000) & (df["sk"]>550000)]
   dferl = dferl.drop("hhs", axis=1)
   teildf = teildf.loc[(teildf["ansdiff"] >= mindiff) | (teildf["ansdiff"] <= mindiff*-1) ]
   #print(dferl)
   dferl["sk"] = dferl["sk"].fillna(0).astype("int")
   #print(dferl)
   dfnew = pd.merge(teildf, dferl, how = "left", left_on= ["produkt", "sk"], right_on=["produkt", "sk"])
   dfnew = dfnew.drop(["hh", "mn_y", "erlNr", "erlTyp", "nicht uebertragbar"], axis=1)
   dfnew["erl"] = dfnew["erl"].fillna(0)
   #print(dfnew)
   st = dfnew[["hhs","sk", "produkt", "bez", "anshhj", "ansvj", "rgergvvj", "erl"]].to_dict('records')
   return st

def get_sonstA(df, dferl, mindiff=0):
   df["ansdiff"] = df["anshhj"] - df["ansvj"] 
   teildf = df.loc[(df["sk"]<570000) & (df["sk"]>560000)]
   dferl = dferl.drop("hhs", axis=1)
   teildf = teildf.loc[(teildf["ansdiff"] >= mindiff) | (teildf["ansdiff"] <= mindiff*-1) ]
      #print(dferl)
   dferl["sk"] = dferl["sk"].fillna(0).astype("int")
   #print(dferl)
   dfnew = pd.merge(teildf, dferl, how = "left", left_on= ["produkt", "sk"], right_on=["produkt", "sk"])
   dfnew = dfnew.drop(["hh", "mn_y", "erlNr", "erlTyp", "nicht uebertragbar"], axis=1)
   dfnew["erl"] = dfnew["erl"].fillna(0)
   #print(dfnew)
   st = dfnew[["hhs","sk", "produkt", "bez", "anshhj", "ansvj", "rgergvvj", "erl"]].to_dict('records')
   return st

def get_finA(df, dferl, mindiff=0):
   teildf = df.loc[(df["sk"]<580000) & (df["sk"]>570000)]
   dferl = dferl.drop("hhs", axis=1)
      #print(dferl)
   dferl["sk"] = dferl["sk"].fillna(0).astype("int")
   #print(dferl)
   dfnew = pd.merge(teildf, dferl, how = "left", left_on= ["produkt", "sk"], right_on=["produkt", "sk"])
   dfnew = dfnew.drop(["hh", "mn_y", "erlNr", "erlTyp", "nicht uebertragbar"], axis=1)
   dfnew["erl"] = dfnew["erl"].fillna(0)
   #print(dfnew)
   st = dfnew[["hhs","sk", "produkt", "bez", "anshhj", "ansvj", "rgergvvj", "erl"]].to_dict('records')
   return st

def get_ilvE(df, dferl):
   teildf = df.loc[(df["sk"]<490000) & (df["sk"]>480000)]
      #print(dferl)
   dferl["sk"] = dferl["sk"].fillna(0).astype("int")
   #print(dferl)
   dfnew = pd.merge(teildf, dferl, how = "left", left_on= ["produkt", "sk"], right_on=["produkt", "sk"])
   dfnew = dfnew.drop(["hh", "mn_y", "erlNr", "erlTyp", "nicht uebertragbar"], axis=1)
   #print(dfnew)
   st = dfnew[["hhs","sk", "produkt", "bez", "anshhj", "ansvj", "rgergvvj", "erl"]].to_dict('records')
   return st

def get_ilfA(df, dferl):
   teildf = df.loc[(df["sk"]<590000) & (df["sk"]>580000)]
      #print(dferl)
   dferl["sk"] = dferl["sk"].fillna(0).astype("int")
   #print(dferl)
   dfnew = pd.merge(teildf, dferl, how = "left", left_on= ["produkt", "sk"], right_on=["produkt", "sk"])
   dfnew = dfnew.drop(["hh", "mn_y", "erlNr", "erlTyp", "nicht uebertragbar"], axis=1)
   #print(dfnew)
   st = dfnew[["hhs","sk", "produkt", "bez", "anshhj", "ansvj", "rgergvvj", "erl"]].to_dict('records')
   return st

def createinvest(df, dfprod, dfmnt, dferl):
   
   dferl.columns = ["hh", "produkt", "mn", "sk", "erlnr", "erltyp", "intern", "nü", "hhs", "duplikat", "erl"]
   dfmnt.columns = ["produkt", "mn", "txt", "konsum", "anzPSt"]
   #print(dfprod)
   dfprod = dfprod[["Produkt", "Bezeichnung"]]
   dfprod = dfprod.rename(columns={"Produkt" : "produkt", "Bezeichnung" : "prbez"}) 
   dferl['erljoined'] = dferl.groupby('hhs')['erl'].transform(lambda x: ' '.join(x))
   #dfmnt = dfmnt.rename(columns={"Maßnahme" : "mn", "Produkt" : "produkt"})
   dfmnt.columns = ["produkt", "mn", "txt", "konsum", "anzPSt"]

   dfprod = dfprod.rename(columns={"Produkt" : "produkt"})

   #print(f"______________________________")
   #print(f"erläuterungen vor bereinigung ")
   #print(f"==============================")

   #dferl.info()

   # löschen der Duplikate
   dferl = dferl.drop_duplicates(subset=["hhs"], keep="first")
   # drop der erläuterungsspalte
   #print(f"______________________________")
   #print(f"erläuterungen nach bereinigung")
   #print(f"==============================")
   #dferl.info()

   # umbenenen der erljoined in erl
   dferl = dferl.drop(["erl"], axis=1)
   dferl = dferl.rename(columns={"erljoined" : "erl" })

   #print(f"Erläuterungen: \n {dfdup}")

   dfneu = pd.merge(left=df, right=dfmnt, how="left",
                  left_on=["produkt", "mn"],
                  right_on=["produkt", "mn"]
                  )
   
   #dfneu.info()
   dfneu = pd.merge(left=dfneu,
                  right=dfprod,
                  how="left",
                  left_on=["produkt"],
                  right_on=["produkt"],
                  )
   #print(f"Merge Produkttext: {dfneu}")
   dfneu = pd.merge(left=dfneu,
                  right=dferl,
                  how="left",
                  left_on=["produkt", "mn", "sk"],
                  right_on=["produkt", "mn", "sk"]
                  )
   #print(f"Merge Erläuterungstext: {dfneu}")
   dferl2 = dferl.loc[dferl["sk"]==0]
   dfneu = pd.merge(left=dfneu,
                  right=dferl2,
                  how="left",
                  left_on=["produkt", "mn"],
                  right_on=["produkt", "mn"]
                  )
   dfneu = dfneu.rename(columns={"sk_x": "sk", "erl_x": "pserl","erl_y": "mnerl", "hhs" : "hhsmn", "hhs_x": "hhs"})#, "hhs_x": "hhs"
   dfneu = dfneu.drop(["sk_y", "hhs_y", "duplikat_y", "duplikat_x"  ], axis=1)

   dfneu = dfneu.fillna(0)

   dfneu.iloc[ :, [0,16,17,18,19,20,21,22,23,24]]

   return dfneu

def sum_personalaufwand(dfbew, dferl):
   teildf = dfbew.loc[(dfbew["sk"]<520000) & (dfbew["sk"]>500000)]
   dferl = dferl.drop("hhs", axis=1)
   #print(dferl)
   dferl["sk"] = dferl["sk"].fillna(0).astype("int")
   #print(dferl)
   dfnew = pd.merge(teildf, dferl, how = "left", left_on= ["produkt", "sk"], right_on=["produkt", "sk"])
   dfnew = dfnew.drop(["hh", "mn_y", "erlNr", "erlTyp", "nicht uebertragbar"], axis=1)
   summe = (dfnew.anshhj.sum(), dfnew.ansvj.sum())
   return summe




if __name__ == "__main__":
   # print(gesamtplan_erg(xlsfile=str(pathlib.Path.cwd() / "haushalt/hhdaten/bewegungsdaten.xlsx"), hhj=2023, gde=60))
   print(gesamtplan_vvj(di.hhdata_excelimport(xlsxfile=str(pathlib.Path.cwd() / "hhdaten/bewegungsdaten.xlsx"))))