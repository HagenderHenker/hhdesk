import pandas as pd
import numpy as np
import dataimport as di
import pathlib
import datetime as dt
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns  
import data_04_statistics as statdf 

mpl.rcParams['lines.linewidth']=2
mpl.rcParams['axes.labelcolor']="darkgreen"
mpl.rcParams['axes.titlecolor']="darkgreen"
mpl.rcParams['axes.edgecolor']="darkgreen"
mpl.rcParams['xtick.color']="darkgreen"
mpl.rcParams['xtick.labelcolor']="darkgreen"
mpl.rcParams['ytick.color']="darkgreen"
mpl.rcParams['ytick.labelcolor']="darkgreen"

def plot_gr_popdev(data, gde, hhj):
        
    #print(data)
    
    plt.plot(data['gesamt'], color='darkgreen', marker='o')
    plt.title('Bevölkerungsentwicklung')
    plt.xlabel('Jahr')
    plt.yticks(np.arange(3000, 5000, step = 1000))
    plt.ylabel('Anzahl Einwohner', fontsize=12)
 
    for year in np.sort(data.index):
        plt.annotate(str(data.loc[year]["gesamt"]), xy=(year, data.loc[year]["gesamt"]), xytext=(year, (data.loc[year]["gesamt"])-120))

  
    plt.savefig(str(pathlib.Path.cwd() / "hhdaten/plots/bev-entw.png"))
    #plt.show()
    plt.close()


def plot_gr_altersgruppen(df):
    plt.figure(figsize=(8,5))
    df = df[(df.Grundeintrag)&(df.Nutzungsart != "Bodenfläche insgesamt")]



def plot_flaechenentwicklung(df):
    plt.figure(figsize=(8,5)) 
    #df = pd.read_excel("Fläche.xlsx")
    df = df[(df.Grundeintrag)&(df.Nutzungsart != "Bodenfläche insgesamt")]
    #print(df)

    plt.rcParams.update({'axes.ymargin': 0.1})

    colors4 = ["coral", "darkgrey", "forestgreen", "skyblue"]
    colors9 = ["coral", "firebrick", "tomato", "lightsalmon", "darkgrey", "tan", "lawngreen", "forestgreen", "lightskyblue"]
    labels = df.Nutzungsart
    
    plot = sns.barplot(x = "Nutzungsart", y="km²", data=df[["Nutzungsart", "km²"]], palette = colors9)
    #print(plot)
    plt.xticks(rotation=30, ha="right")

    for bar in plot.patches:
        plot.annotate(format(bar.get_height(), '.2f'),
                   (bar.get_x() + bar.get_width() / 2,
                    bar.get_height()), ha='center', va='center',
                   size=8, xytext=(0, 8),
                   textcoords='offset points')

    plt.title("Flächennutzung")
    plt.tight_layout()
 

    plt.savefig(str(pathlib.Path.cwd() / "hhdaten/plots/flaechennutzung.png"))
    plt.close()




# FINANZDADTENPLOTS
'''
The following plots are primarily Plots from the /hhdaten/bewegungsdaten.xlsx
mixed with some of the Grunddaten.xlsx dataframes
'''
def plot_ekentwicklung(dfek):

    '''
    Takes 
    dfertaufek: 
    dfbek:  Dataframe from data_04_statistics.py
    gde:    municipal corpus from config
    hhj:    budgetary year from config

    '''

    highest = int(int((dfek.max()[1].item())/1000000)*1000000)+1000000
    lowest = int(int((dfek.min()[1].item())/1000000)*1000000)-1000000

    y = range(lowest, highest, 1000000)
    z = [x/1000000 for x in y]

    fig, ax1 = plt.subplots(figsize = ( 6, 3.6))
    ax1.plot(dfek["EK"], color="darkgreen", marker="^", zorder=2)
    ax1.set_title("Entwicklung des Eigenkapitals")
    ax1.set_ylabel("Eigenkapital in Mio €")
    ax1.set_xlabel("Haushaltsjahr")
    ax1.set_ylim(top=highest, bottom=lowest)
    ax1.set_xticks(dfek.index)
    ax1.set_yticks(y)
    ax1.set_xticklabels(dfek["hhj"], rotation = 40)
    ax1.set_yticklabels([x/1000000 for x in y])

    plt.savefig(str(pathlib.Path.cwd() / "hhdaten/plots/img_ek_entwicklung.png"))
    plt.close()





def plot_hebesatzentwicklung(dfhebesaetze):
    ''' 
    Entwicklung der Hebesätze
    this function creates a lineplot of the development of the taxrates (Realsteuerhebesätze)
    for Grundsteuer A, Grundsteuer B and Gewerbesteuer
    It takes a Dataframe created in "data_09_statistik.py" from the /hhdaten/grunddaten.xlsx
    '''

    font = {"family" : "sans-serif",
        "color" : "darkgreen",
        "size" : 8
    	}

    fig, ax1 = plt.subplots(figsize = ( 6, 3.6))

    grsta = ax1.plot(dfhebesaetze["grsta"], color="darkgreen", marker="^", zorder=3, label="Grundsteuer A")
    grstb = ax1.plot(dfhebesaetze["grstb"], color="limegreen", marker="o", zorder=1, label="Grundsteuer B")
    gewst = ax1.plot(dfhebesaetze["gewst"], color="yellowgreen", marker="*", zorder=2, label="Gewerbesteuer")
    ax1.set_title("Entwicklung der Realsteuerhebesätze")
    ax1.set_ylabel("Hebesatz in %")
    ax1.set_xlabel("Haushaltsjahr")
    #ax1.set_ylim(top=highest, bottom=lowest)
    ax1.set_xticks(dfhebesaetze.index)
    #ax1.set_yticks(y)
    ax1.set_xticklabels(dfhebesaetze["hhj"], rotation = 40, fontdict=font)
    ax1.legend(handles=[grsta, grstb, gewst], labels=["Grundsteuer A", "Grundsteuer B", "Gewerbesteuer"])
    #ax1.set_yticklabels([x/1000000 for x in y])
    plt.savefig(str(pathlib.Path.cwd() / "hhdaten/plots/img_hebesatz_entwicklung.png"))
    plt.close()


def plot_ergebnisentwicklung(dfergebnis):
    def colorizer(jevalue):
        if jevalue > 0:
            s = "lawngreen"
        elif jevalue == 0:
            s = "black"
        else:
            s = "darkgreen"
        return s

    highest = int(int((dfergebnis[['Gesamtbetrag Erträge', 'Gesamtbetrag Aufwendungen']].max()[1].item())/1000000)*1000000)+1000000
    


    # Entwicklung Jahresergebnisse
    dfergebnis.dropna(axis=0, how="any", inplace=True)


    xmarken = ([x for x in range(len(dfergebnis["hhj"].index))])
    #print(xmarken)
    dfergebnis.index = xmarken
    #print(dfergebnis)

    dfertaufw = dfergebnis[["hhj", "Gesamtbetrag Erträge", "Gesamtbetrag Aufwendungen"]]
    #dfertaufw = dfertaufw.dropna(axis=0, how="any", inplace=True)

    dfergsaldo = dfergebnis[["hhj","Jahresergebnis"]]
    #dfertaufw

    fig, ax1 = plt.subplots(figsize = ( 6, 3.6))
    ax2 = ax1.twinx()

    custompalette = []

    dfergsaldo["color"] = dfergsaldo["Jahresergebnis"].apply(func=colorizer, )
    #print(dfergsaldo)
    custompalette = dfergsaldo["color"].tolist()
    sns.barplot(data = dfergsaldo, x="hhj", y="Jahresergebnis", palette = custompalette, zorder = 3)

    #wo fängt plan an?
    #vlinex = dfergebnis[dfergebnis.p_e == "p"].iloc[0].hhj
    #plt.vlines(x=5, color = "forestgreen", ymin=0, ymax=1)


    #print(plt.subplot())
    #q = sns.pointplot(data=dfertaufw, x="hhj", y="Gesamtbetrag Erträge", color="lawngreen", ax = ax1)
    #r = sns.pointplot(data=dfertaufw, x="hhj", y="Gesamtbetrag Aufwendungen", color="darkgreen", ax = ax1)

    ax1.plot(dfertaufw["Gesamtbetrag Erträge"], color="lawngreen", marker="o", zorder=1)
    ax1.plot(dfertaufw["Gesamtbetrag Aufwendungen"], color="darkgreen", marker="^", zorder=2)


    ax1.set_title("Entwicklung der Jahresergebnisse")
    ax1.set_ylabel("Ertrag und Aufwand in Mio €")
    ax1.set_xlabel("Haushaltsjahr")
    ax1.set_ylim(top=highest, bottom=0)
    ax1.set_xticks(xmarken)
    ax1.set_xticklabels(dfergsaldo["hhj"], rotation = 30)

    ax2.set_ylabel("Jahresergebnis in Mio €", )
    ax2.set_ylim(top=6000000)


    #wo fängt plan an?
    try:
        vlinex = dfergebnis[dfergebnis.p_e == "p"].index[0]
        plt.axvline(x=vlinex-0.5, color = "forestgreen", label="Planwerte")
        ax2.annotate("Planwerte", xy= (vlinex, 5000000), )
    except:
        pass


    ax2.set_xticks(xmarken)
    plt.axhline(y=0, color="black")
    plt.ticklabel_format(style='sci', axis='y', useMathText="True", )

    plt.savefig(str(pathlib.Path.cwd() / "hhdaten/plots/img_je_entwicklung.png"))
    #plt.show()
    plt.close()


def plot_steuerentwicklung(dfs):

    fdlabelsmall = {"family" : "sans-serif",
        "color" : "darkgreen",
        "size" : 8
        }

    fdaxlabel = {"family" : "sans-serif",
            "color" : "darkgreen",
            "size" : 12
    }

    fdtitle = {"family" : "sans-serif",
            "color" : "darkgreen",
            "size" : 16
    }

    firstplan = dfs["e_p"].loc[dfs["e_p"]== "p"]
    xplan = firstplan.index.min()
    xplan = xplan-0.5

    ind = dfs.index

    counter=0

    for i in ind:
        counter = counter+1
        if i > xplan:
            break



    ax = dfs.plot(kind="bar",
                stacked=True,
                colormap="Greens",
                figsize = (6, 5),

                )
    ax.legend(loc="lower center", ncols=4, bbox_to_anchor=(0.5 , -0.4),  labelcolor ="darkgreen"   )

    ax.spines[["left", "top", "bottom", "right"]].set_color("darkgreen")

    plt.title("Entwicklung der Steuererträge", fontdict=fdtitle)
    plt.xlabel(xlabel="Haushaltsjahr", fontdict=fdaxlabel)
    plt.ylabel(ylabel="Volumen in Mio €", fontdict=fdaxlabel)
    plt.xticks(rotation = 30, color="darkgreen" )
    plt.yticks(color="darkgreen")
    plt.axvline(x=counter-1.5 , color = "forestgreen", label="Planwerte")
    plt.tight_layout()
    plt.savefig(str(pathlib.Path.cwd() / "hhdaten/plots/img_steuer_entwicklung.png"))
    plt.close()

def plot_liquiditaet(dfliq):
    
    firstplan = dfliq["e_p"].loc[(dfliq["e_p"]== "p")]
    xplan = firstplan.index.min()
    xplan = xplan-0.5

    #fig, ax1 = plt.subplots(figsize = ( 6, 3.6))

    ymax = round(dfliq.bestand.max()/100000)*100000+100000
    ymin = round(dfliq.bestand.min()/100000)*100000-100000

    y = [value for value in range(ymin, ymax, 100000)]
    x = list(dfliq.hhj)
    yticklabels = [value/1000 for value in y]
    annotation = list(dfliq.bestand)

    ax = dfliq.bestand.plot(x=x, y=y, kind='bar', stacked=False, title='Bestände bei der Verbandsgemeindekasse', color='darkgreen')
    plt.xlabel(xlabel='Haushaltsjahr')
    plt.xticks(dfliq.index,labels=x, rotation=30)
    plt.ylabel(ylabel='Bestand in Tsd€')
    plt.yticks(y, labels=yticklabels)
    plt.axvline(x=xplan, color = "forestgreen")
    plt.text(x=xplan + 0.3, y=max(y)-50000, s='Planwerte'  )

    plt.savefig(str(pathlib.Path.cwd() / "hhdaten/plots/img_liquiditaetsentwicklung.png"))
    plt.close()


def plot_schuldenentwicklung(dfschulden):
    firstplan = dfschulden["e_p"].loc[dfschulden["e_p"]== "p"]
    xplan = firstplan.index.min()
    xplan = xplan-0.5

    #fig, ax1 = plt.subplots(figsize = ( 6, 3.6))

    #print(dfschulden[['invkred', 'liqkred']])

    ax = dfschulden[['hhj', 'invkred', 'liqkred']].plot.bar(x='hhj', stacked=True, title='Kreditschulden', color=['darkgreen', 'lawngreen']) 
    ax.legend(['Investitionskredit', 'Liquiditätskredite'])
    plt.xlabel(xlabel='Haushaltsjahr')
    plt.xticks(dfschulden.index, labels=dfschulden.hhj, rotation=30)
    plt.ylabel(ylabel='Schulden in Mio€')
    #plt.yticks(y, labels=yticklabels)
    plt.axvline(x=xplan, color = "forestgreen")
    dfschulden['schulden'] = dfschulden['invkred']+dfschulden['liqkred']
    y = round(max(dfschulden['schulden'])/1000000)*1000000+500000
    plt.text(x=xplan + 0.3, y=y, s='Planwerte'  )
    plt.savefig(str(pathlib.Path.cwd() / "hhdaten/plots/img_schuldennominal.png"))
    plt.close()


def plot_schuldenprokopf(dfschulden):
    #fig, ax1 = plt.subplots(figsize = ( 6, 3.6))

    #print(dfschulden[['invkredprokopf', 'liqkredprokopf']])
    firstplan = dfschulden["e_p"].loc[dfschulden["e_p"]== "p"]
    xplan = firstplan.index.min()
    xplan = xplan-0.5
    ax = dfschulden[['hhj', 'invkredprokopf', 'liqkredprokopf']].plot.bar(x='hhj', stacked=True, title='Kreditschulden pro Kopf', color=['darkgreen', 'lawngreen'])
    ax.legend(['Investitionskredit', 'Liquiditätskredite'])
    plt.xlabel(xlabel='Haushaltsjahr')
    plt.xticks(dfschulden.index, labels=dfschulden.hhj, rotation=30)
    plt.ylabel(ylabel='Schulden in €')
    #plt.yticks(y, labels=yticklabels)
    plt.axvline(x=xplan, color = "forestgreen")
    dfschulden['schuldenpk'] = dfschulden['invkredprokopf']+dfschulden['liqkredprokopf']
    y = round(max(dfschulden['schuldenpk'])/50)*50+30
    plt.text(x=xplan + 0.3, y=y, s='Planwerte'  )
    plt.savefig(str(pathlib.Path.cwd() / "hhdaten/plots/img_schuldenprokopf.png"))
    plt.close()

def plot_persaufwandstruktur(dfsummierungaufwand):
    fig, ax = plt.subplots(figsize = ( 6, 7))
    sns.light_palette("seagreen", as_cmap=True)
    sns.barplot(data=dfsummierungaufwand,
                x= "prbez",
                y="anshhj",
                palette = "Greens",
                ax = ax
            )


    ax.set_ylabel("Volumen in Mio€", size = 14 )
    ax.set_xlabel("bei Produkt", size = 14 )
    ax.set_title("Personalaufwand", size = 20)

    plt.ticklabel_format(style='sci', axis='y', useMathText="True")
    plt.xticks(rotation=50, ha="right")
    plt.tight_layout()
    plt.savefig(str(pathlib.Path.cwd() / "hhdaten/plots/img_persaufwandstruktur.png"))
    plt.close()

def plot_ertragsstruktur(df):
    fig, ax = plt.subplots(figsize = ( 10, 6))
    sns.barplot(data=df,
            x= "stbez",
            y="betrag",
            hue="jahr",
            palette="Greens",
            ax = ax)
    plt.xticks(rotation= 45, ha = 'right')
    ax.set_xlabel("Ertragsart", size= 14)
    ax.set_ylabel("Volumen in Mio€", size = 14 )
    ax.set_title("Erträge", size = 20)
    plt.savefig(str(pathlib.Path.cwd() / "hhdaten/plots/img_ertragsstruktur.png"))
    plt.close()


def plot_aufwandsstruktur(df):
    fig, ax = plt.subplots(figsize = ( 10, 6))
    sns.barplot(data=df,
            x= "stbez",
            y="betrag",
            hue="jahr",
            palette="Greens",
            ax = ax)
    plt.xticks(rotation= 30, ha = 'right')
    ax.set_xlabel("Aufwandsart", size= 14)
    ax.set_ylabel("Volumen in Mio€", size = 14 )
    ax.set_title("Aufwand", size = 20)
    plt.savefig(str(pathlib.Path.cwd() / "hhdaten/plots/img_aufwandstruktur.png"))
    plt.close()

def plot_Umlagen(dfu):
    
    firstplan = dfu["e_p"].loc[dfu["e_p"]== "p"]
    xplan = firstplan.index.min()
    xplan = xplan-0.5

    ind = dfu.index

    counter=0

    for i in ind:
        #print(f"counter: {i}")
        counter = counter+1
        if i > xplan:
            break

    ax = dfu.plot(kind="bar",
                stacked=True,
                colormap="Greens",
                figsize = (6, 5),

                )
    ax.legend(loc="lower center", ncols=4, bbox_to_anchor=(0.5 , -0.4),  labelcolor ="darkgreen"   )

    ax.spines[["left", "top", "bottom", "right"]].set_color("darkgreen")

    plt.title("Entwicklung der Umlagelasten", )
    plt.xlabel(xlabel="Haushaltsjahr", )
    plt.ylabel(ylabel="Volumen in Mio €", )
    plt.xticks(rotation = 30, color="darkgreen" )
    plt.yticks(color="darkgreen")
    plt.axvline(x=counter-1.5 , color = "forestgreen", label="Planwerte")
    ymax = dfu.sum(axis=1, numeric_only=True).max()
    print("ymax_ ",ymax)
    plt.text(x=counter-1, y=ymax, s='Planwerte' )
    plt.tight_layout()


    plt.savefig(str(pathlib.Path.cwd() / "hhdaten/plots/img_Umlagen.png"))
    plt.close()

    


if __name__ == "__main__":
    #plot_gr_popdev(xlsfile=str(pathlib.Path.cwd() / "hhdaten/grunddaten.xlsx"), gde=60, hhj=2023)
    #plot_flaechenentwicklung(di.readflaechenstatistik(xlsfile=str(pathlib.Path.cwd() / "hhdaten/grunddaten.xlsx"), gdenr=60, hhj=2023))
    pass