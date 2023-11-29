import dataimport as di
import pathlib
import pandas as pd

"""
Provide the statistics Data needed for the document
Datamangling for the graphplotter.py 
"""

def ewstatistic(data, gde, hhj):
   # data = di.readewstatistik_wohn(xlsfile=xlsfile, gdenr=gde, jahr=hhj-1)
   data["gesamt"] =  data["maennl"] + data["weibl"]
   data["jahr"] = pd.to_datetime(data["datum"]).dt.year


    #print(data)
   dn = data[["jahr", "gesamt"]].loc[data["wohnstatus"] == "Einwohner mit Hauptwohnung"]
   dn = dn.set_index("jahr", drop=True)
   return dn





def ergstat(grunddaten, bewegungsdaten, hhj, gde):
   
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

   return dfergebnis

def ekstat(grunddaten, bewegungsdaten, hhj, gde):
   dfergebnis = ergstat(grunddaten=grunddaten, bewegungsdaten=bewegungsdaten, hhj=hhj, gde=gde)
   dfek = dfergebnis[["hhj", "EK"]]
   return dfek


def steuerstat(dfsteuer, bewegungsdaten, hhj, gde):
   '''
   takes dfsteuer = Dataframe from grunddaten.xlsx steuer roster.
   takes bewegungsdaten = Dataframe from bewegungsdaten.xlsx
   takes hhj = fiscal year from config
   takes gde = municipal corpus from config
   '''

   dfs = dfsteuer.set_index('hhj').drop("gdenr", axis=1)

   steuerarten = dfs.columns.values.tolist()
   steuerarten.append("e_p")
   sksteuern = [401100, 401200, 401300, 402100, 402200, 403300, 405210]
   dictsteuern = {steuerarten[i]:sksteuern[i] for i in range(len(sksteuern))}

   dfs['e_p'] = "e"

   #print(dfs)
   #print(dictsteuern)

   jahre = [i for i in range(hhj-2, hhj+4)]
   #print(jahre)

   dfs2 = pd.DataFrame(columns=steuerarten, index=jahre)


   for steuerart in dictsteuern:
      dfz=bewegungsdaten.loc[bewegungsdaten['sk']==dictsteuern[steuerart]]
      #print(dfz)
      dfs2.loc[hhj-2, steuerart] = dfz.iloc[0]['rgergvvj']
      dfs2.loc[hhj-2]['e_p'] = "e"
      dfs2.loc[hhj-1, steuerart] = dfz.iloc[0]['ansvj']
      dfs2.loc[hhj-1]['e_p'] = "p"
      dfs2.loc[hhj, steuerart] = dfz.iloc[0]['anshhj']
      dfs2.loc[hhj]['e_p'] = "p"
      dfs2.loc[hhj+1, steuerart] = dfz.iloc[0]['plan1']
      dfs2.loc[hhj+1]['e_p'] = "p"
      dfs2.loc[hhj+2, steuerart] = dfz.iloc[0]['plan2']
      dfs2.loc[hhj+2]['e_p'] = "p"
      dfs2.loc[hhj+3, steuerart] = dfz.iloc[0]['plan3']
      dfs2.loc[hhj+3]['e_p'] = "p"

   dfs = pd.concat([dfs,dfs2], axis=0)

   return dfs

def kredbestandstatistic(dfkred, df, hhj, gde):
   '''
   takes dfkred = Dataframe from grunddaten.xlsx, kred roster.
   takes bewegungsdaten = Dataframe from bewegungsdaten.xlsx
   takes hhj = fiscal year from config
   takes gde = municipal corpus from config
   
   Returns  Pandas Dataframe "dfkred" build from past years and 
            adds the planned years from bewegungsdaten. dfkred contains
            data for municipal credits and account balance

   The result is used in kredstat(), kredstatprokopf() and bestandstat()
   '''

   dfkred['e_p'] = ""


   if not dfkred.loc[dfkred['e_p'] == "p"].empty:
      dfkred.loc[dfkred['e_p'] == "p"].drop(axis=1, inplace=True)

   dfkred['e_p']='e'

   last_e = dfkred['hhj'].max()
   first_plan = last_e + 1

   # Ermittlung Nettokreditaufnahme Investiv

   ikA= df.loc[(df['sk'] > 690000) & (df['sk']< 700000) & (df['produkt'] == '6.1.2.1' )&(df['sk'] !=694440)&(df['sk'] !=694442)][['rgergvvj', 'ansvj', 'anshhj', 'plan1', 'plan2', 'plan3']].sum()
   ikTil = df.loc[(df['sk'] > 790000) & (df['sk']< 800000) & (df['produkt'] == '6.1.2.1' )&(df['sk'] !=796440)&(df['sk'] !=794430)][['rgergvvj', 'ansvj', 'anshhj', 'plan1', 'plan2', 'plan3']].sum()
   nettokrA = pd.DataFrame(data={'rgergvvj' : (ikA['rgergvvj'] - ikTil['rgergvvj']),  'ansvj' : (ikA['ansvj'] - ikTil['ansvj']), 'anshhj' : (ikA['anshhj'] - ikTil['anshhj']), 'plan1' : (ikA['plan1'] - ikTil['plan1']), 'plan2' : (ikA['plan2'] - ikTil['plan2']), 'plan3' : (ikA['plan3'] - ikTil['plan3'])  }, index=[0])
   # Ermittlung Bestandsveränderung

   ezohnelv = df.loc[(df['sk'] > 600000) & (df['sk']< 700000) & (df['sk']!= 694440) & (df['sk'] !=694442)][['rgergvvj', 'ansvj', 'anshhj', 'plan1', 'plan2', 'plan3']].sum()
   azohnelv = df.loc[(df['sk'] > 700000) & (df['sk']< 800000) & (df['sk'] !=796440) & (df['sk'] !=794430)][['rgergvvj', 'ansvj', 'anshhj', 'plan1', 'plan2', 'plan3']].sum()
   zsaldo_woliq = pd.DataFrame(data={'rgergvvj' : (ezohnelv['rgergvvj'] - azohnelv['rgergvvj']),  'ansvj' : (ezohnelv['ansvj'] - azohnelv['ansvj']), 'anshhj' : (ezohnelv['anshhj'] - azohnelv['anshhj']), 'plan1' : (ezohnelv['plan1'] - azohnelv['plan1']), 'plan2' : (ezohnelv['plan2'] - azohnelv['plan2']), 'plan3' : (ezohnelv['plan3'] - azohnelv['plan3'])  }, index=[0])
   #kontrollezaz = df.loc[(df['sk']== 694440) | (df['sk'] ==694442 ) | (df['sk'] ==796440) | (df['sk'] ==794430)]

   if not dfkred.loc[dfkred['e_p'] == "p"].empty:
      dfkred.loc[dfkred['e_p'] == "p"].drop(axis=1, inplace=True)
 
   if first_plan - hhj == -1:
      dfkred = pd.concat([dfkred, pd.DataFrame(
                        {'gdenr':gde,
                        'hhj':first_plan,
                        'invkred': int(nettokrA['ansvj'])+int(dfkred.loc[dfkred['hhj'] == hhj-2]['invkred'].values),
                        'bestand': int(dfkred.loc[dfkred['hhj'] == hhj - 2]['bestand']) + int(zsaldo_woliq['ansvj']),
                        'liqkred' : int(dfkred.loc[dfkred['hhj'] == hhj - 2]['liqkred']) + int(zsaldo_woliq['ansvj'])*-1 if int(dfkred.loc[dfkred['hhj'] == hhj - 2]['bestand']) + int(zsaldo_woliq['ansvj']) <0 else 0 ,
                        'vbkggvgkasse' : int(dfkred.loc[dfkred['hhj'] == hhj - 2]['vbkggvgkasse']) + int(zsaldo_woliq['ansvj']) if int(dfkred.loc[dfkred['hhj'] == hhj - 2]['bestand']) + int(zsaldo_woliq['ansvj']) <0 else 0 ,
                        'fordggvgkasse' : int(dfkred.loc[dfkred['hhj'] == hhj - 2]['fordggvgkasse']) + int(zsaldo_woliq['ansvj']) if int(dfkred.loc[dfkred['hhj'] == hhj - 2]['bestand']) + int(zsaldo_woliq['ansvj']) >0 else 0 ,
                        'Einwohner' : dfkred.loc['Einwohner'][hhj-2],
                        'e_p' : 'p'}, index=[len(dfkred.index)+1])], 
                        ignore_index = True)

   dfkred = pd.concat([dfkred, pd.DataFrame(
               {'gdenr':gde,
               'hhj':hhj,
               'invkred': int(nettokrA['anshhj'])+int(dfkred.loc[dfkred['hhj'] == hhj-1]['invkred'].values),
               'bestand': int(dfkred.loc[dfkred['hhj'] == hhj - 1]['bestand']) + int(zsaldo_woliq['anshhj']),
               'liqkred' : int(dfkred.loc[dfkred['hhj'] == hhj - 1]['liqkred']) + int(zsaldo_woliq['anshhj'])*-1 if int(dfkred.loc[dfkred['hhj'] == hhj - 1]['bestand']) + int(zsaldo_woliq['anshhj']) <0 else 0 ,
               'vbkggvgkasse' : int(dfkred.loc[dfkred['hhj'] == hhj - 1]['vbkggvgkasse']) + int(zsaldo_woliq['anshhj']) if int(dfkred.loc[dfkred['hhj'] == hhj - 1]['bestand']) + int(zsaldo_woliq['anshhj']) <0 else 0 ,
               'fordggvgkasse' : int(dfkred.loc[dfkred['hhj'] == hhj - 1]['fordggvgkasse']) + int(zsaldo_woliq['anshhj']) if int(dfkred.loc[dfkred['hhj'] == hhj - 1]['bestand']) + int(zsaldo_woliq['anshhj']) >0 else 0 ,
               'Einwohner' : dfkred.loc[dfkred['hhj'] == hhj-1]['Einwohner'].values[0],
               'e_p' : 'p'},
               index = [len(dfkred.index)+1] )], 
               ignore_index = True)

   dfkred = pd.concat([dfkred, pd.DataFrame(
               {'gdenr':gde,
               'hhj':hhj+1,
               'invkred': int(nettokrA['plan1'])+int(dfkred.loc[dfkred['hhj'] == hhj]['invkred'].values),
               'bestand': int(dfkred.loc[dfkred['hhj'] == hhj ]['bestand']) + int(zsaldo_woliq['plan1']),
               'liqkred' : int(dfkred.loc[dfkred['hhj'] == hhj ]['liqkred']) + int(zsaldo_woliq['plan1'])*-1 if int(dfkred.loc[dfkred['hhj'] == hhj ]['bestand']) + int(zsaldo_woliq['plan1']) <0 else 0 ,
               'vbkggvgkasse' : int(dfkred.loc[dfkred['hhj'] == hhj ]['vbkggvgkasse']) + int(zsaldo_woliq['plan1']) if int(dfkred.loc[dfkred['hhj'] == hhj ]['bestand']) + int(zsaldo_woliq['plan1']) <0 else 0 ,
               'fordggvgkasse' : int(dfkred.loc[dfkred['hhj'] == hhj ]['fordggvgkasse']) + int(zsaldo_woliq['plan1']) if int(dfkred.loc[dfkred['hhj'] == hhj ]['bestand']) + int(zsaldo_woliq['plan1']) >0 else 0 ,
               'Einwohner' :  dfkred.loc[dfkred['hhj'] == hhj-1]['Einwohner'].values[0],
               'e_p' : 'p'},
               index=[len(dfkred.index) + 1])], 
               ignore_index = True)

   dfkred = pd.concat([dfkred, pd.DataFrame(
               {'gdenr':gde,
               'hhj':hhj+2,
               'invkred': int(nettokrA['plan2'])+int(dfkred.loc[dfkred['hhj'] == hhj+1]['invkred'].values),
               'bestand': int(dfkred.loc[dfkred['hhj'] == hhj +1]['bestand']) + int(zsaldo_woliq['plan2']),
               'liqkred' : int(dfkred.loc[dfkred['hhj'] == hhj +1]['liqkred']) + int(zsaldo_woliq['plan2'])*-1 if int(dfkred.loc[dfkred['hhj'] == hhj +1]['bestand']) + int(zsaldo_woliq['plan2']) <0 else 0 ,
               'vbkggvgkasse' : int(dfkred.loc[dfkred['hhj'] == hhj +1]['vbkggvgkasse']) + int(zsaldo_woliq['plan2']) if int(dfkred.loc[dfkred['hhj'] == hhj +1]['bestand']) + int(zsaldo_woliq['plan2']) <0 else 0 ,
               'fordggvgkasse' : int(dfkred.loc[dfkred['hhj'] == hhj +1]['fordggvgkasse']) + int(zsaldo_woliq['plan2']) if int(dfkred.loc[dfkred['hhj'] == hhj +1]['bestand']) + int(zsaldo_woliq['plan2']) >0 else 0 ,
               'Einwohner' :  dfkred.loc[dfkred['hhj'] == hhj-1]['Einwohner'].values[0],
               'e_p' : 'p'},
               index=[len(dfkred.index) + 1])]
               , ignore_index = True)

   dfkred = pd.concat([dfkred, pd.DataFrame(
               {'gdenr':gde,
               'hhj':hhj+3,
               'invkred': int(nettokrA['plan3'])+int(dfkred.loc[dfkred['hhj'] == hhj+2]['invkred'].values),
               'bestand': int(dfkred.loc[dfkred['hhj'] == hhj + 2]['bestand']) + int(zsaldo_woliq['plan3']),
               'liqkred' : int(dfkred.loc[dfkred['hhj'] == hhj + 2]['liqkred']) + int(zsaldo_woliq['plan3'])*-1 if int(dfkred.loc[dfkred['hhj'] == hhj + 2]['bestand']) + int(zsaldo_woliq['plan3']) <0 else 0 ,
               'vbkggvgkasse' : int(dfkred.loc[dfkred['hhj'] == hhj + 2]['vbkggvgkasse']) + int(zsaldo_woliq['plan3']) if int(dfkred.loc[dfkred['hhj'] == hhj + 2]['bestand']) + int(zsaldo_woliq['plan3']) <0 else 0 ,
               'fordggvgkasse' : int(dfkred.loc[dfkred['hhj'] == hhj + 2]['fordggvgkasse']) + int(zsaldo_woliq['plan3']) if int(dfkred.loc[dfkred['hhj'] == hhj + 2]['bestand']) + int(zsaldo_woliq['plan3']) >0 else 0 ,
               'Einwohner' :  dfkred.loc[dfkred['hhj'] == hhj-1]['Einwohner'].values[0],
               'e_p' : 'p'},
               index=[len(dfkred.index) + 1])], 
               ignore_index = True)
      
   return dfkred

def kredstat(dfkred, dfbew, hhj, gde):
   '''
   uses kredbestandstatistic(dfkred, df, hhj, gde)
   to modify the returned dataframe for the creation of the credit-nominal plot
   in graphplotter.py schuldenentwicklung()
   '''
   df = kredbestandstatistic(dfkred, dfbew, hhj, gde)
   df = df[['hhj','invkred', 'liqkred', "e_p" ]]
   return df

def kredstatprokopf(dfkred, dfbew, hhj, gde):
   '''
   uses kredbestandstatistic(dfkred, df, hhj, gde)
   to modify the returned dataframe for the creation of the credit-nominal plot
   in graphplotter.py schuldenentwicklung()
   '''
   df = kredbestandstatistic(dfkred, dfbew, hhj, gde)
   df = df[['hhj','invkred', 'liqkred', 'Einwohner', "e_p"]]
   df['invkredprokopf'] = df['invkred']/df['Einwohner']
   df['liqkredprokopf'] = df['liqkred']/df['Einwohner']
   return df


def bestandsstat(dfkred, dfbew, hhj, gde):
   '''
   uses kredbestandstatistic(dfkred, df, hhj, gde)
   to modify the returned dataframe for the creation of the credit-nominal plot
   in graphplotter.py schuldenentwicklung()
   '''
   df = kredbestandstatistic(dfkred, dfbew, hhj, gde)
   df = df[['hhj','bestand', "e_p"]]
   return df


































































"""
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
"""