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
   '''
   takes grunddaten = dataframe form grunddaten.xlsx
   takes bewegungsdaten = Dataframe from bewegungsdaten.xlsx
   takes hhj = fiscal year from config
   takes gde = municipal corpus from config
   '''
   
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

   #print(dfergebnis)
   return dfergebnis

def ekstat(grunddaten, bewegungsdaten, hhj, gde):
   dfergebnis = ergstat(grunddaten=grunddaten, bewegungsdaten=bewegungsdaten, hhj=hhj, gde=gde)
   dfek = dfergebnis[["hhj", "EK"]]
   print(dfek)
   return dfek


def steuerstat(dfsteuer, bewegungsdaten, hhj, gde):
   '''
   takes dfsteuer = Dataframe from grunddaten.xlsx steuer roster.
   takes bewegungsdaten = Dataframe from bewegungsdaten.xlsx
   takes hhj = fiscal year from config
   takes gde = municipal corpus from config

   returns dataframe with rows by fiscal year (hhj-2 to hhj+3) and a column for each tax
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


def personalaufwandsstruktur(df, dfprod):
   dfpaw = df.loc[(df["sk"]>500000)&(df["sk"]<520000)]
   dfpaz = df.loc[(df["sk"]>700000)&(df["sk"]<720000)]

   dfprod= dfprod[["Produkt", "Bezeichnung"]]
   dfprod = dfprod.rename(columns={"Produkt" : "produkt", "Bezeichnung":"prbez"} )
   # print(dfprod)
   dfprod.info()
   df.info()
   dfpaw = dfpaw.merge(right = dfprod, how="left", left_on = "produkt", right_on = "produkt")
   dfpaz = dfpaz.merge(right = dfprod, how="left", left_on = "produkt", right_on = "produkt")

   dfsummierungaufwand = dfpaw.groupby(by="produkt", ).agg({"produkt":"first", "prbez" : "first", "anshhj" : "sum", "ansvj" : "sum", "rgergvvj" : "sum"})
   #dfsummierungaufwand.drop(["sk", "mn"], axis=1)
   #print(dfsummierungaufwand)
   dfsummierungaufwand = dfsummierungaufwand.loc[(dfsummierungaufwand['anshhj'] != 0) | (dfsummierungaufwand['ansvj'] != 0) & (dfsummierungaufwand['rgergvvj'] != 0)]


   dfsummierungauszahlung = dfpaz.groupby(by="produkt", ).agg("sum")
   #dfsummierungauszahlung.drop(["sk", "mn"], axis=1)

   return dfsummierungaufwand

def staffelung(sk):
   if sk < 410000:
      return 400
   if 410000 <= sk < 420000:
      return 410
   if 420000 <= sk < 430000:
      return 420
   if 430000 <= sk < 440000:
      return 430
   if 440000 <= sk < 442000 or 443000 <= sk < 450000:
      return 440
   if 442000 <= sk < 443000:
      return 442
   if 450000 <= sk < 460000:
      return 450
   if 460000 <= sk < 470000:
      return 460
   if 470000 <= sk < 480000:
      return 470
   if 480000 <= sk < 490000:
      return 480
   if 490000 <= sk < 500000:
      return 490

   if 500000 <= sk < 520000:
      return 500
   if 520000 <= sk < 530000:
      return 520
   if 530000 <= sk < 540000:
      return 530
   if 540000 <= sk < 550000:
      return 540
   if 550000 <= sk < 560000:
      return 550
   if 560000 <= sk < 570000:
      return 560
   if 570000 <= sk < 580000:
      return 570
   if 580000 <= sk < 590000:
      return 580
   if 590000 <= sk < 600000:
      return 590

def eart(staffelung):
   if staffelung < 50:
      return "e"
   else:
      return "a"

def ertragsstruktur(df):
   dferg = df.loc[(df["sk"] < 500000)]
   dferg["staffel"] = dferg["sk"].map(staffelung)
   dferg["eart"] = dferg["staffel"].map(eart)

   dftp = dferg[["hhs", "sk", "staffel", "eart", "anshhj"]]
   dftp = dftp.rename(columns={"anshhj" : "betrag"})
   dftp["p-re"] = "p"
   dftp["jahr"] = "Haushaltsjahr"

   dfe2 = dferg[["hhs", "sk", "staffel", "eart", "ansvj"]]
   dfe2 = dfe2.rename(columns={"ansvj" : "betrag"})
   dfe2["p-re"] = "p"
   dfe2["jahr"] = "Nachtrag/Plan Vorjahr"

   dfe3 = dferg[["hhs", "sk", "staffel", "eart", "rgergvvj"]]
   dfe3 = dfe3.rename(columns={"rgergvvj" : "betrag"})
   dfe3["p-re"] = "re"
   dfe3["jahr"] = "Rechnungserg. 2. Vorjahr"

   dftp = pd.concat([dftp, dfe2])
   dftp = pd.concat([dftp, dfe3])

   groupers = {
      400 : "Steuern",
      410 : "Transfererträge",
      420 : "Erträge der sozialen Sicherung",
      430 : "Gebühren",
      440 : "privatrechtl. Leistungsentgelte",
      442 : "Kostenerstattungen",
      450 : "Wertkorrekturen",
      460 : "sonstige Erträge",
      470 : "Finanzerträge",
      480 : "Erträge aus ILV",
      490 : "Andere Erträge"
   }

   dftp2 = dftp.groupby(["staffel", "jahr"], as_index=False).sum()
   dftp2.reset_index()
   dftp2["stbez"] = dftp2.staffel.apply(lambda x: groupers[x])


   for grouper in groupers:
      d = dftp2.loc[dftp2.staffel == grouper]
      x = []
      for hhj in d.jahr:
         if d.loc[ d.jahr == hhj]['betrag'].values == 0:
            x.append(0)
            print(f"{grouper}: x = {x}")
         else:
            break

         if x == [0,0,0]:
            
            dftp2 = dftp2.drop(dftp2[dftp2.staffel == grouper].index, axis=0)
   
   return dftp2

def aufwandsstruktur(df):
   dferg = df.loc[(df["sk"] > 500000) & (df["sk"] > 600000)]
   dferg["staffel"] = dferg["sk"].map(staffelung)
   dferg["eart"] = dferg["staffel"].map(eart)

   dftp = dferg[["hhs", "sk", "staffel", "eart", "anshhj"]]
   dftp = dftp.rename(columns={"anshhj" : "betrag"})
   dftp["p-re"] = "p"
   dftp["jahr"] = "Haushaltsjahr"

   dfe2 = dferg[["hhs", "sk", "staffel", "eart", "ansvj"]]
   dfe2 = dfe2.rename(columns={"ansvj" : "betrag"})
   dfe2["p-re"] = "p"
   dfe2["jahr"] = "Nachtrag/Plan Vorjahr"

   dfe3 = dferg[["hhs", "sk", "staffel", "eart", "rgergvvj"]]
   dfe3 = dfe3.rename(columns={"rgergvvj" : "betrag"})
   dfe3["p-re"] = "re"
   dfe3["jahr"] = "Rechnungserg. 2. Vorjahr"

   dftp = pd.concat([dftp, dfe2])
   dftp = pd.concat([dftp, dfe3])

   groupers = {
      500 : "Personal & Versorgungsaufwand",
      520 : "Aufwendungen für Sach- und Dienstleistungen",
      530 : "Abschreibungen",
      540 : "Zuwendungen und Transferaufwand",
      550 : "Aufwand der sozialen Sicherung",
      560 : "sonstiger Aufwand",
      570 : "Finanzaufwand",
      580 : "Aufwand aus ILV",
      590 : "Andere Aufwendungen"
   }

   dftp2 = dftp.groupby(["staffel", "jahr"], as_index=False).sum()
   dftp2.reset_index()
   dftp2["stbez"] = dftp2.staffel.apply(lambda x: groupers[x])


   for grouper in groupers:
      d = dftp2.loc[dftp2.staffel == grouper]
      x = []
      for hhj in d.jahr:
         if d.loc[ d.jahr == hhj]['betrag'].values == 0:
            x.append(0)
            print(f"{grouper}: x = {x}")
         else:
            break

         if x == [0,0,0]:
            
            dftp2 = dftp2.drop(dftp2[dftp2.staffel == grouper].index, axis=0)
   
   return dftp2


def createdfumlagen(df, dfumlagen, hhj):

   #dfus = dfumlagen[["kreisumlage_satz", "vg_umlage_satz"]]

   #dfumlagen = dfumlagen.drop(["kreisumlage_satz", "vg_umlage_satz"], axis = 1)

   dfu = dfumlagen.set_index('hhj').drop("gdenr", axis=1)

   umlagearten = dfu.columns.values.tolist()
   umlagearten.append("e_p")
   planungsstellenumlagen = ["6.1.1.0.543100", "6.1.1.0.544210", "6.1.1.0.544230", "2.1.1.1.541430",]
   dictumlagen = {umlagearten[i]:planungsstellenumlagen[i] for i in range(len(planungsstellenumlagen))}

   dfu['e_p'] = "e"

   
   #print(dictumlagen)

   jahre = [i for i in range(hhj-2, hhj+4)]
   #print(jahre)
   print(dfu)
   dfu2 = pd.DataFrame(columns=umlagearten, index=jahre)

   
   for umlageart in dictumlagen:
      dfz=df.loc[df['hhs']==dictumlagen[umlageart]]
      #print(dfz)
      
      dfu2.loc[hhj-2, umlageart] = dfz.iloc[0]['rgergvvj']
      dfu2.loc[hhj-2]['e_p'] = "e"
      dfu2.loc[hhj-1, umlageart] = dfz.iloc[0]['ansvj']
      dfu2.loc[hhj-1]['e_p'] = "p"
      dfu2.loc[hhj, umlageart] = dfz.iloc[0]['anshhj']
      dfu2.loc[hhj]['e_p'] = "p"
      dfu2.loc[hhj+1, umlageart] = dfz.iloc[0]['plan1']
      dfu2.loc[hhj+1]['e_p'] = "p"
      dfu2.loc[hhj+2, umlageart] = dfz.iloc[0]['plan2']
      dfu2.loc[hhj+2]['e_p'] = "p"
      dfu2.loc[hhj+3, umlageart] = dfz.iloc[0]['plan3']
      dfu2.loc[hhj+3]['e_p'] = "p"

   # doppelte Jahre aus dem dfu2 herauslöschen. Es wird davon ausgegangen dass die Ergebniswerte in der Bestandstabelle aktueller sind
   for year in dfu.index:
      if year in dfu2.index:
         dfu2.drop(index=year, inplace=True)

   dfu = pd.concat([dfu,dfu2], axis=0)

   #print(dfu)

   dfu['Gew.St.-Umlage'] = dfu['Gew.St.-Umlage'].astype(float)
   dfu['Grundschulumlage'] = dfu['Grundschulumlage'].astype(float)
   dfu['Kreisumlage'] = dfu['Kreisumlage'].astype(float)
   dfu['VGUmlage'] = dfu['VGUmlage'].astype(float)
   return dfu












