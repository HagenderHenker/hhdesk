import dataimport as di 
import contextbuilder as ctx
import data_04_statistics as stat
import docbuilder
import pathlib
import enviromentvar as env
import graphplotter as plot

gde = env.gde
hhj = env.hhj
grunddaten = env.grunddaten
bewegungsdaten = env.bewDat

hhstpl = env.hhstpl
vorb01tpl = env.vorb01tpl
vorb02tpl = env.vorb02tpl
vorb05tpl = env.vorb05tpl
vorb06tpl = env.vorb06tpl
quelleewdaten = env.quelleewdaten
quelleflaechendaten = env.quelleflaechendaten

if __name__ == "__main__":

    # create the dataframes for all further purposes from dataimport
    print("Creating Dataframes")
    # Import Bewegungsdaten
    dfbew = di.hhdata_excelimport(xlsxfile=bewegungsdaten)
    print("... Bewegungsdaten")
    dferl = di.erl_excelimport(xlsxfile=bewegungsdaten)
    print("... Erläuterungen")
    dfpro = di.prod_excelimport(xlsxfile=bewegungsdaten)
    print("... Produkte")
    dfmn = di.mn_excelimport(xlsxfile=bewegungsdaten)
    print("... Erläuterungen")
    print("Bewegungsdaten erfolgreich importiert")

    # Grunddaten
    dfgde = di.readgrunddatengde(xlsfile=grunddaten, gdenr=gde)
    print("... Gemeindegrunddaten")
    dfhhs = di.readgrunddatenhh(xlsfile=grunddaten, gdenr=gde, hhj=hhj)
    print("... Haushaltssatzungsdaten")
    dfewentw = di.readewstatistik_wohn(xlsfile=grunddaten, gdenr=gde, jahr=hhj-1)
    print("... Einwohnerstatistik")
    dfewalter = di.readewdatenaltersstruktur(xlsfile=grunddaten, gdenr=gde, hhj=hhj-1)
    print("... Einwohnerstatistik Altersstruktur")
    dfewu20 = di.readewdaten_u20(xlsfile=grunddaten, gdenr=gde, hhj=hhj-1)
    print("... Einwohnerstatistik Altersstruktur unter 20jährige")
    dfeweinschulung = di.readewdaten_u20(xlsfile=grunddaten, gdenr=gde, hhj=hhj-1)
    print("... Einwohnerstatistik Einschulung")
    dfflaeche = di.readflaechenstatistik(xlsfile=grunddaten, gdenr=gde, hhj=hhj-1)
    print("... Flächenstatistik")
    dfstkraft = di.readlfag_stkberechnung(xlsfile=grunddaten, gdenr=gde, hhj=hhj)
    print("... Steuerkraft")
    #dfekentwicklung und ergebnisentwicklung =
    dfergebnis = di.readergebnisEKstat(xlsfile=grunddaten, gdenr=gde, hhj=hhj)
    print("... Statistik der Jahresergebnisse und Eigenkapitalentwicklung")
    #dffinanzentwicklung = 
    dffinanz = di.readffsfinstatistik(xlsfile=grunddaten, gdenr=gde, hhj=hhj)
    print("... Statistik der freien Finanzspitze und der Finanzrechnungsdaten")
    dfhebesaetze = di.readhebesatzentwicklung(xlsfile=grunddaten, gdenr=gde)
    print("... Statistik der festgesetzten Hebesätze der Gemeinde")
    dfsteuer = di.readsteuerertraege(xlsfile=grunddaten, gdenr=gde, hhj=hhj)
    print("... Statistik der Steuererträge der Gemeinde Vorjahre")
    dfkred = di.readkred(xlsfile=grunddaten, gdenr=gde, hhj=hhj)
    print("... Schulden und Kassenbestände")
    #dfschuldenentwicklung
    

    #dfinvkredentwicklung

    #dfliqkredentwicklung

    #dfsteuerentwicklung
    dfstkraft = di.readlfag_stkberechnung(xlsfile=grunddaten, gdenr=gde, hhj=hhj)
    print("... Steuereinnahmen")

    # plotting graphs
    print("")
    print("===============================================")
    print("Start plotting")
    print("===============================================")
    print("")
    
    plot.plot_gr_popdev(stat.ewstatistic(dfewentw, gde=gde, hhj=hhj), gde=gde, hhj=hhj)
    print("... Einwohnerentwicklung Plot aufbereitet")
    #plot.plot_gr_altersgruppen(stat.ewstatistic(dfewentw, gde=gde, hhj=hhj), gde=gde, hhj=hhj)
    #print("... Einwohnerentwicklung Plot aufbereitet")
    #U20
    plot.plot_flaechenentwicklung(dfflaeche)
    print("... Flächenentwicklung, Plot aufbereitet")
    #
        
    plot.plot_ekentwicklung(stat.ekstat(bewegungsdaten=dfbew, grunddaten=dfergebnis, hhj=hhj, gde=gde))
    print("... Eigenkapitalentwickklung, Plot aufbereitet")

    plot.plot_ergebnisentwicklung(stat.ergstat(bewegungsdaten=dfbew, grunddaten=dfergebnis, hhj=hhj, gde=gde))
    print("... Entwicklung der Jahresergebnisse, Plot aufbereitet")

    plot.plot_hebesatzentwicklung(dfhebesaetze=dfhebesaetze)
    print("... Entwicklung der Hebesätze, Plot aufbereitet")
#
    plot.plot_steuerentwicklung(dfs=stat.steuerstat(dfsteuer=dfsteuer, bewegungsdaten=dfbew, hhj=hhj, gde=gde) )
    print("... Entwicklung der Steuererträge")

    plot.plot_liquiditaet(dfliq=stat.bestandsstat(dfbew=dfbew, dfkred=dfkred, hhj=hhj, gde=gde))
    print("... Entwicklung der Bestände")
    
    plot.plot_schuldenentwicklung(dfschulden=stat.kredstat(dfbew=dfbew, dfkred=dfkred, hhj=hhj, gde=gde))
    print("... Entwicklung der Schulden")

    plot.plot_schuldenprokopf(dfschulden=stat.kredstatprokopf(dfbew=dfbew, dfkred=dfkred, hhj=hhj, gde=gde))
    print("... Entwicklung der pro Kopf Verschuldung")


    # build "Haushaltssatzung"
    """
    contexthhsatzung = ctx.hhsatzung(gde = gde, hhj = hhj, xlsgrunddaten = grunddaten, xlsbewegung = bewegungsdaten)
    print("Daten für 'Haushaltssatzung' sind zusammengestellt")
    
    docbuilder.builddocx(template=hhstpl, context=contexthhsatzung, filename="00-Haushaltssatzung", gde=gde, hhj=hhj)
    print(f"Haushaltssatzung erstellt in Ordner: 'Ausgabe/{gde}/{hhj}")
    """
    # build "02_Vorbericht" 1. Abschnitt: Allgemeines

    #vorb01tpl_instanz = docbuilder.create_tpl_instance(vorb01tpl)
    #print("*** Templateinstanz Vorbericht 01 Allgemeines erzeugt")

    #contextvorb1 = ctx.hh_vorbericht_01_Allgemeines(
    #                                                dfhhs=dfhhs,dfgdegrunddaten = dfgde, 
    #                                                dfewentwicklung=dfewentw, 
    #                                                dfewaltersgliederung=dfewalter, 
    #                                                dfewalteru20= dfewu20, 
    #                                                dfflaeche=dfflaeche, 
    #                                                quelleewdaten=quelleewdaten, quelleflaeche=quelleflaechendaten,
    #                                                doc =  vorb01tpl_instanz
    #                                              )
    #print("Daten für Vorbericht 01 Allgemeines sind zusammengestellt")

    #docbuilder.builddocx(tpl=vorb01tpl_instanz, context=contextvorb1, filename="01-Vorb_Allgemeines", gde=gde, hhj=hhj)
    #print(f"Vorbericht 01 - Allgemeines erzeugt in Ordner: 'Ausgabe/{gde}/{hhj}")

    # build "03_Vorbericht" Information about closed year

    #vorb02tpl_instanz = docbuilder.create_tpl_instance(vorb02tpl)
    #contextvorb2_vvj = ctx.hh_vorbericht_02_verlaufvvj(df=dfbew)
    #print("Daten für Vorbericht 02 Bericht 2. Haushaltsvorjahr sind zusammengestellt ")
    #docbuilder.builddocx(tpl=vorb02tpl_instanz, context=contextvorb2_vvj, filename="02-Vorb_VVJ", gde=gde, hhj=hhj)
    #print(f"Vorbericht 02 - 2. Haushaltsvorjahr: 'Ausgabe/{gde}/{hhj}")

    # build "04_Vorbericht" Information about last year

    # build "05_Vorbericht" Gesamtergebnisplan

    # build "06_Vorbericht_aenderungenErtraege"

    
    vorb05tpl_instanz = docbuilder.create_tpl_instance(vorb05tpl)
    contextvorb05 = ctx.hh_vorbericht_06_Ertraege(df=dfbew, dferl=dferl, mindiff=env.mindiff)
    print("Daten für Vorbericht 06 'Veränderungen in den Erträgen' sind zusammengestellt ")
    docbuilder.builddocx(tpl=vorb05tpl_instanz, context=contextvorb05, filename="06-Vorb_Ertraege", gde=gde, hhj=hhj)
    print(f"Vorbericht 06 - Veränderung in den Erträgen: 'Ausgabe/{gde}/{hhj}")
    

    #build "07_Vorbericht" Aufwendungen im Ergebnishaushalt