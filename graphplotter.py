import pandas as pd
import numpy as np
import dataimport as di
import pathlib
import datetime as dt
import matplotlib.pyplot as plt
import seaborn as sns   


def gr_populationdevelopment(xlsfile, gde, hhj):
    data = di.readewstatistik_wohn(xlsfile=xlsfile, gdenr=gde, jahr=hhj-1)
    data["gesamt"] =  data["maennl"] + data["weibl"]
    data["jahr"] = pd.to_datetime(data["datum"]).dt.year


    #print(data)
    dn = data[["jahr", "gesamt"]].loc[data["wohnstatus"] == "Einwohner mit Hauptwohnung"]
    dn = dn.set_index("jahr", drop=True)
    return dn

"""
def plot_gr_popdev(xlsfile, gde, hhj):
    data = gr_populationdevelopment(xlsfile=xlsfile, gde=gde, hhj=hhj)
    fig = px.line(data_frame=data             )
    fig.show()
"""

def plot_gr_popdev(xlsfile, gde, hhj):
    data = gr_populationdevelopment(xlsfile=xlsfile, gde=gde, hhj=hhj)
    
    print(data)
    
    plt.plot(data['gesamt'], color='blue', marker='o')
    plt.title('Bevölkerungsentwicklung', fontsize=14)
    plt.xlabel('Jahr', fontsize=12)
    plt.yticks(np.arange(3000, 5000, step = 1000))
    plt.ylabel('Anzahl Einwohner', fontsize=12)
    plt.grid(True)


    for year in np.sort(data.index):
        plt.annotate(str(data.loc[year]["gesamt"]), xy=(year, data.loc[year]["gesamt"]), xytext=(year, (data.loc[year]["gesamt"])-120))

   
    plt.savefig(str(pathlib.Path.cwd() / "hhdaten/plots/bev-entw.png"))
    plt.show()

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







if __name__ == "__main__":
    #plot_gr_popdev(xlsfile=str(pathlib.Path.cwd() / "hhdaten/grunddaten.xlsx"), gde=60, hhj=2023)
    plot_flaechenentwicklung(di.readflaechenstatistik(xlsfile=str(pathlib.Path.cwd() / "hhdaten/grunddaten.xlsx"), gdenr=60, hhj=2023))
