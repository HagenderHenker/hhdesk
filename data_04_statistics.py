import dataimport as di
import pathlib
import pandas as pd

"""
Provide the statistics Data needed for the document
Datamangling for the graphplotter.py 
"""

def ewstatistic(xlsfile, gde, hhj):
   pass 





def ekstat(grunddaten, bewegungsdaten, hhj, gde):
   
   dfergebnis = grunddaten
   
   dfergebnis["p_e"] = "e"
   df2 = bewegungsdaten.loc[(bewegungsdaten["sk"] < 500000)][["anshhj", "ansvj", "plan1", "plan2", "plan3"]].sum()
   df3 = bewegungsdaten.loc[(bewegungsdaten["sk"] > 500000) & (bewegungsdaten["sk"]<600000)][["anshhj", "ansvj", "plan1", "plan2", "plan3"]].sum()

   eK = dfergebnis["EK"].loc[dfergebnis["hhj"]==hhj-1].values


   if (dfergebnis.loc[dfergebnis["hhj"] == hhj-1 ]["p_e"].values != "e"):
      dfergebnis.loc[len(dfergebnis.index)] = [gde, hhj-1, df2.ansvj, df3.ansvj, (df2.ansvj-df3.ansvj), (eK+(df2.ansvj-df3.ansvj)).item(),"p"][0]
      dfergebnis["EK"].loc[dfergebnis["hhj"] == hhj-1].dtype
      eK = eK+int((df2.plan3-df3.plan3))

   if (dfergebnis.loc[dfergebnis["hhj"] == hhj ]["p_e"].values != "e") or (dfergebnis.loc[dfergebnis["hhj"] == hhj ]["p_e"].size <= 0):
      dfergebnis.loc[len(dfergebnis.index)] = [gde, hhj, df2.anshhj, df3.anshhj, (df2.anshhj-df3.anshhj), (eK+(df2.anshhj-df3.anshhj)).item(), "p"]
      eK = eK+(df2.plan3-df3.plan3)

   if dfergebnis.loc[dfergebnis["hhj"] == hhj+1 ]["p_e"].values != "e" or dfergebnis.loc[dfergebnis["hhj"] == hhj+1 ]["p_e"].size <= 0:
      dfergebnis.loc[len(dfergebnis.index)] = [gde, hhj+1, df2.plan1, df3.plan1, (df2.plan1-df3.plan1), (eK+(df2.plan1-df3.plan1)).item(), "p"]
      eK = eK+(df2.plan3-df3.plan3)

   if dfergebnis.loc[dfergebnis["hhj"] == hhj+2 ]["p_e"].values != "e" or dfergebnis.loc[dfergebnis["hhj"] == hhj+2 ]["p_e"].size <= 0:
      dfergebnis.loc[len(dfergebnis.index)] = [gde, hhj+2, df2.plan2, df3.plan2, (df2.plan2-df3.plan2), (eK+(df2.plan2-df3.plan2)).item(), "p"]
      eK = eK+(df2.plan3-df3.plan3)

   if dfergebnis.loc[dfergebnis["hhj"] == hhj+3 ]["p_e"].values != "e" or dfergebnis.loc[dfergebnis["hhj"] == hhj+3 ]["p_e"].size <= 0:
      dfergebnis.loc[len(dfergebnis.index)] = [gde, hhj+3, df2.plan3, df3.plan3, (df2.plan3-df3.plan3), (eK+(df2.plan3-df3.plan3)).item(), "p"]
      eK = eK+(df2.plan3-df3.plan3)

   dfek = dfergebnis[["hhj", "EK"]]

   return dfek


















def get_steuern(df, dferl):
   teildf = df.loc[df["sk"] < 410000]   
   #print(dferl)
   dferl["sk"] = dferl["sk"].fillna(0).astype("int")
   #print(dferl)
   dfnew = pd.merge(teildf, dferl, how = "left", left_on= ["produkt", "sk"], right_on=["produkt", "sk"])
   dfnew = dfnew.drop(["hh", "mn_y", "erlNr", "erlTyp", "nicht uebertragbar"], axis=1)
   #print(dfnew)
   st = dfnew[["hhs","sk", "produkt", "bez", "anshhj", "ansvj", "rgergvvj", "erl"]].to_dict('records')
   return st

def get_umlagen(df, dferl, mindiff=0):
   df["ansdiff"] = df["anshhj"] - df["ansvj"]
   teildf = df.loc[(df["sk"]<420000) & (df["sk"]>410000)]
   teildf = teildf.loc[(teildf["ansdiff"] > 4999) | (teildf["ansdiff"]) < -4999 ]
   #print(dferl)
   dferl["sk"] = dferl["sk"].fillna(0).astype("int")
   #print(dferl)
   dfnew = pd.merge(teildf, dferl, how = "left", left_on= ["produkt", "sk"], right_on=["produkt", "sk"])
   dfnew = dfnew.drop(["hh", "mn_y", "erlNr", "erlTyp", "nicht uebertragbar"], axis=1)
   #print(dfnew)
   st = dfnew[["hhs","sk", "produkt", "bez", "anshhj", "ansvj", "rgergvvj", "erl"]].to_dict('records')
   return st

def get_sozE(df, dferl):
   teildf = df.loc[(df["sk"]<430000) & (df["sk"]>420000)]
   #print(dferl)
   dferl["sk"] = dferl["sk"].fillna(0).astype("int")
   #print(dferl)
   dfnew = pd.merge(teildf, dferl, how = "left", left_on= ["produkt", "sk"], right_on=["produkt", "sk"])
   dfnew = dfnew.drop(["hh", "mn_y", "erlNr", "erlTyp", "nicht uebertragbar"], axis=1)
   #print(dfnew)
   st = dfnew[["hhs","sk", "produkt", "bez", "anshhj", "ansvj", "rgergvvj", "erl"]].to_dict('records')
   return st

def get_oerE(df, dferl):
   teildf = df.loc[(df["sk"]<440000) & (df["sk"]>430000)]
      #print(dferl)
   dferl["sk"] = dferl["sk"].fillna(0).astype("int")
   #print(dferl)
   dfnew = pd.merge(teildf, dferl, how = "left", left_on= ["produkt", "sk"], right_on=["produkt", "sk"])
   dfnew = dfnew.drop(["hh", "mn_y", "erlNr", "erlTyp", "nicht uebertragbar"], axis=1)
   #print(dfnew)
   st = dfnew[["hhs","sk", "produkt", "bez", "anshhj", "ansvj", "rgergvvj", "erl"]].to_dict('records')
   return st

def get_prE(df, dferl):
   teildf = df.loc[(df["sk"]<442000) & (df["sk"]>440000)]
      #print(dferl)
   dferl["sk"] = dferl["sk"].fillna(0).astype("int")
   #print(dferl)
   dfnew = pd.merge(teildf, dferl, how = "left", left_on= ["produkt", "sk"], right_on=["produkt", "sk"])
   dfnew = dfnew.drop(["hh", "mn_y", "erlNr", "erlTyp", "nicht uebertragbar"], axis=1)
   #print(dfnew)
   st = dfnew[["hhs","sk", "produkt", "bez", "anshhj", "ansvj", "rgergvvj", "erl"]].to_dict('records')
   return st

def get_kostE(df, dferl):
   teildf = df.loc[(df["sk"]<450000) & (df["sk"]>443000)]
      #print(dferl)
   dferl["sk"] = dferl["sk"].fillna(0).astype("int")
   #print(dferl)
   dfnew = pd.merge(teildf, dferl, how = "left", left_on= ["produkt", "sk"], right_on=["produkt", "sk"])
   dfnew = dfnew.drop(["hh", "mn_y", "erlNr", "erlTyp", "nicht uebertragbar"], axis=1)
   #print(dfnew)
   st = dfnew[["hhs","sk", "produkt", "bez", "anshhj", "ansvj", "rgergvvj", "erl"]].to_dict('records')
   return st

def get_sonstE(df, dferl):
   teildf = df.loc[(df["sk"]<470000) & (df["sk"]>460000)]
      #print(dferl)
   dferl["sk"] = dferl["sk"].fillna(0).astype("int")
   #print(dferl)
   dfnew = pd.merge(teildf, dferl, how = "left", left_on= ["produkt", "sk"], right_on=["produkt", "sk"])
   dfnew = dfnew.drop(["hh", "mn_y", "erlNr", "erlTyp", "nicht uebertragbar"], axis=1)
   #print(dfnew)
   st = dfnew[["hhs","sk", "produkt", "bez", "anshhj", "ansvj", "rgergvvj", "erl"]].to_dict('records')
   return st

def get_finE(df, dferl):
   teildf = df.loc[(df["sk"]<480000) & (df["sk"]>470000)]
      #print(dferl)
   dferl["sk"] = dferl["sk"].fillna(0).astype("int")
   #print(dferl)
   dfnew = pd.merge(teildf, dferl, how = "left", left_on= ["produkt", "sk"], right_on=["produkt", "sk"])
   dfnew = dfnew.drop(["hh", "mn_y", "erlNr", "erlTyp", "nicht uebertragbar"], axis=1)
   #print(dfnew)
   st = dfnew[["hhs","sk", "produkt", "bez", "anshhj", "ansvj", "rgergvvj", "erl"]].to_dict('records')
   return st

def get_persA(df, dferl):
   teildf = df.loc[(df["sk"]<520000) & (df["sk"]>500000)]
      #print(dferl)
   dferl["sk"] = dferl["sk"].fillna(0).astype("int")
   #print(dferl)
   dfnew = pd.merge(teildf, dferl, how = "left", left_on= ["produkt", "sk"], right_on=["produkt", "sk"])
   dfnew = dfnew.drop(["hh", "mn_y", "erlNr", "erlTyp", "nicht uebertragbar"], axis=1)
   #print(dfnew)
   st = dfnew[["hhs","sk", "produkt", "bez", "anshhj", "ansvj", "rgergvvj", "erl"]].to_dict('records')
   return st

def get_msdA(df, dferl):
   teildf = df.loc[(df["sk"]<530000) & (df["sk"]>520000)]
      #print(dferl)
   dferl["sk"] = dferl["sk"].fillna(0).astype("int")
   #print(dferl)
   dfnew = pd.merge(teildf, dferl, how = "left", left_on= ["produkt", "sk"], right_on=["produkt", "sk"])
   dfnew = dfnew.drop(["hh", "mn_y", "erlNr", "erlTyp", "nicht uebertragbar"], axis=1)
   #print(dfnew)
   st = dfnew[["hhs","sk", "produkt", "bez", "anshhj", "ansvj", "rgergvvj", "erl"]].to_dict('records')
   return st

def get_AfA(df, dferl):
   teildf = df.loc[(df["sk"]<540000) & (df["sk"]>530000)]
      #print(dferl)
   dferl["sk"] = dferl["sk"].fillna(0).astype("int")
   #print(dferl)
   dfnew = pd.merge(teildf, dferl, how = "left", left_on= ["produkt", "sk"], right_on=["produkt", "sk"])
   dfnew = dfnew.drop(["hh", "mn_y", "erlNr", "erlTyp", "nicht uebertragbar"], axis=1)
   #print(dfnew)
   st = dfnew[["hhs","sk", "produkt", "bez", "anshhj", "ansvj", "rgergvvj", "erl"]].to_dict('records')
   return st

def get_UmlA(df, dferl):
   teildf = df.loc[(df["sk"]<550000) & (df["sk"]>540000)]
   #print(dferl)
   dferl["sk"] = dferl["sk"].fillna(0).astype("int")
   #print(dferl)
   dfnew = pd.merge(teildf, dferl, how = "left", left_on= ["produkt", "sk"], right_on=["produkt", "sk"])
   dfnew = dfnew.drop(["hh", "mn_y", "erlNr", "erlTyp", "nicht uebertragbar"], axis=1)
   #print(dfnew)
   st = dfnew[["hhs","sk", "produkt", "bez", "anshhj", "ansvj", "rgergvvj", "erl"]].to_dict('records')
   return st

def get_sozA(df, dferl):
   teildf = df.loc[(df["sk"]<560000) & (df["sk"]>550000)]
   #print(dferl)
   dferl["sk"] = dferl["sk"].fillna(0).astype("int")
   #print(dferl)
   dfnew = pd.merge(teildf, dferl, how = "left", left_on= ["produkt", "sk"], right_on=["produkt", "sk"])
   dfnew = dfnew.drop(["hh", "mn_y", "erlNr", "erlTyp", "nicht uebertragbar"], axis=1)
   #print(dfnew)
   st = dfnew[["hhs","sk", "produkt", "bez", "anshhj", "ansvj", "rgergvvj", "erl"]].to_dict('records')
   return st

def get_sonstA(df, dferl):
   teildf = df.loc[(df["sk"]<570000) & (df["sk"]>560000)]
      #print(dferl)
   dferl["sk"] = dferl["sk"].fillna(0).astype("int")
   #print(dferl)
   dfnew = pd.merge(teildf, dferl, how = "left", left_on= ["produkt", "sk"], right_on=["produkt", "sk"])
   dfnew = dfnew.drop(["hh", "mn_y", "erlNr", "erlTyp", "nicht uebertragbar"], axis=1)
   #print(dfnew)
   st = dfnew[["hhs","sk", "produkt", "bez", "anshhj", "ansvj", "rgergvvj", "erl"]].to_dict('records')
   return st

def get_finA(df, dferl):
   teildf = df.loc[(df["sk"]<580000) & (df["sk"]>570000)]
      #print(dferl)
   dferl["sk"] = dferl["sk"].fillna(0).astype("int")
   #print(dferl)
   dfnew = pd.merge(teildf, dferl, how = "left", left_on= ["produkt", "sk"], right_on=["produkt", "sk"])
   dfnew = dfnew.drop(["hh", "mn_y", "erlNr", "erlTyp", "nicht uebertragbar"], axis=1)
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

print(get_steuern(df= di.hhdata_excelimport(xlsxfile= str(pathlib.Path.cwd() / "hhdaten/bewegungsdaten.xlsx")), dferl=di.erl_excelimport(xlsxfile= str(pathlib.Path.cwd() / "hhdaten/bewegungsdaten.xlsx"))))
#print(get_umlagen(di.hhdata_excelimport(xlsxfile= str(pathlib.Path.cwd() / "hhdaten/bewegungsdaten.xlsx"))))