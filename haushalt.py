import dataimport as di 
import contextbuilder as ctx
import data_03_ergebnis as erg
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
vorb03tpl = env.vorb03tpl
vorb05tpl = env.vorb05tpl
vorb06tpl = env.vorb06tpl
vorb07tpl = env.vorb07tpl
vorb08tpl = env.vorb08tpl
vorb10tpl = env.vorb10tpl
vorb11tpl = env.vorb11tpl
quelleewdaten = env.quelleewdaten
quelleflaechendaten = env.quelleflaechendaten

if __name__ == "__main__":

    # create the dataframes for all further purposes from dataimport
    print("")
    print("===============================================")    
    print("Creating Dataframes")
    print("===============================================")
    print("")
    
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
    #hebesaetze
    dfhebesaetze = di.readhebesatzentwicklung(xlsfile=grunddaten, gdenr=gde)
    print("... Statistik der festgesetzten Hebesätze der Gemeinde")
    #steuerentwicklung
    dfsteuer = di.readsteuerertraege(xlsfile=grunddaten, gdenr=gde, hhj=hhj)
    print("... Statistik der Steuererträge der Gemeinde Vorjahre")
    dfumlagen = di.readumlagen(gdenr=gde, hhj=hhj, xlsfile=grunddaten)
    print("... Statistik der Umlagelast der Gemeinde Vorjahre")
    #kredit
    dfkred = di.readkred(xlsfile=grunddaten, gdenr=gde, hhj=hhj)
    print("... Schulden und Kassenbestände")
    #df LFAG Daten Haushaltsjahr (Orientierungsdaten)

    dfod = di.readlfagod(xlsfile=grunddaten, hhj=hhj)
    print("... LFAG Richtwerte Orientierungsdaten/Haushaltsrundschreiben")

    # steuerkraft
    dfstkraft = di.readlfag_stkberechnung(xlsfile=grunddaten, gdenr=gde, hhj=hhj)
    print("... Berechnung Steuerkraft")
    # LFAG Kalkulationsdaten (Gemeindunabhängig/Landeseinheitlich)
    dflfaghhj = di.readlfagHHJgde(xlsfile=grunddaten, hhj=hhj, gde=gde)
    print("... LFAG gemeindespezifische Daten")
    #Liquiditätsbestand
    dfliq = stat.bestandsstat(dfbew=dfbew, dfkred=dfkred, hhj=hhj, gde=gde)
    print("... Liquidität")
    dfschulden = stat.kredstat(dfbew=dfbew, dfkred=dfkred, hhj=hhj, gde=gde)

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

    plot.plot_Umlagen(dfu=stat.createdfumlagen(df=dfbew, dfumlagen=dfumlagen, hhj=hhj))
    print("... Entwicklung der Umlagebeträge (Asbolut)")    


    plot.plot_liquiditaet(dfliq=dfliq)
    print("... Entwicklung der Bestände")
    
    plot.plot_schuldenentwicklung(dfschulden=dfschulden)
    print("... Entwicklung der Schulden")

    plot.plot_schuldenprokopf(dfschulden=stat.kredstatprokopf(dfbew=dfbew, dfkred=dfkred, hhj=hhj, gde=gde))
    print("... Entwicklung der pro Kopf Verschuldung")

    plot.plot_persaufwandstruktur(dfsummierungaufwand=stat.personalaufwandsstruktur(df=dfbew, dfprod=dfpro))
    print("...Personalaufwandstruktur")

    plot.plot_ertragsstruktur(df=stat.ertragsstruktur(df=dfbew))
    print("...Ertragsstruktur")

    plot.plot_aufwandsstruktur(df=stat.ertragsstruktur(df=dfbew))
    print("...Aufwandstruktur")

   
    # plotting graphs
    print("")
    print("===============================================")
    print("Building docx Documents")
    print("===============================================")
    print("")

    # build "Haushaltssatzung"
    
    contexthhsatzung = ctx.hhsatzung(gde = gde, hhj = hhj, xlsgrunddaten = grunddaten, xlsbewegung = bewegungsdaten)
    print("... Daten für 'Haushaltssatzung' sind zusammengestellt")
    
    hhs = docbuilder.create_tpl_instance(template=hhstpl)
    docbuilder.builddocx(tpl=hhs, context=contexthhsatzung, filename="00-Haushaltssatzung", gde=gde, hhj=hhj)
    print(f"... Haushaltssatzung erstellt in Ordner: 'Ausgabe/{gde}/{hhj}")
    
    # build "02_Vorbericht" 1. Abschnitt: Allgemeines
    print(" ")
    print("----------------------------")
 
    vorb01tpl_instanz = docbuilder.create_tpl_instance(vorb01tpl)
    print("*** Templateinstanz Vorbericht 01 Allgemeines erzeugt")

    contextvorb1 = ctx.hh_vorbericht_01_Allgemeines(
                                                    dfhhs=dfhhs,dfgdegrunddaten = dfgde, 
                                                    dfewentwicklung=dfewentw, 
                                                    dfewaltersgliederung=dfewalter, 
                                                    dfewalteru20= dfewu20, 
                                                    dfflaeche=dfflaeche, 
                                                    quelleewdaten=quelleewdaten, quelleflaeche=quelleflaechendaten,
                                                    doc =  vorb01tpl_instanz
                                                  )
    print("Daten für Vorbericht 01 Allgemeines sind zusammengestellt")

    docbuilder.builddocx(tpl=vorb01tpl_instanz, context=contextvorb1, filename="01-Vorb_Allgemeines", gde=gde, hhj=hhj)
    print(f"Vorbericht 01 - Allgemeines erzeugt in Ordner: 'Ausgabe/{gde}/{hhj}")

    # build "03_Vorbericht" Information about closed year

    vorb02tpl_instanz = docbuilder.create_tpl_instance(vorb02tpl)
    print(" ")
    print("----------------------------")
    print("*** Templateinstanz Vorbericht 02 VVJ erzeugt")

    contextvorb2_vvj = ctx.hh_vorbericht_02_verlaufvvj(df=dfbew)
    print("...Daten für Vorbericht 02 Bericht 2. Haushaltsvorjahr sind zusammengestellt ")
    docbuilder.builddocx(tpl=vorb02tpl_instanz, context=contextvorb2_vvj, filename="02-Vorb_VVJ", gde=gde, hhj=hhj)
    print(f"...Vorbericht 02 - 2. Haushaltsvorjahr: 'Ausgabe/{gde}/{hhj}")
    """
    # build "04_Vorbericht" Information about last year
    print(" ")
    print("----------------------------")
    vorb03tpl_instanz = docbuilder.create_tpl_instance(vorb03tpl)
    print("*** Templateinstanz Vorbericht 03 VJ erzeugt")
    contextvorb2_vvj = ctx.hh_vorbericht_03_verlaufvj(df=dfbew)
    print("...Daten für Vorbericht 02 Bericht 2. Haushaltsvorjahr sind zusammengestellt ")
    docbuilder.builddocx(tpl=vorb02tpl_instanz, context=contextvorb2_vvj, filename="02-Vorb_VVJ", gde=gde, hhj=hhj)
    print(f"...Vorbericht 02 - 2. Haushaltsvorjahr: 'Ausgabe/{gde}/{hhj}")
    """

    #vorb03tpl_instanz = docbuilder.create_tpl_instance(vorb03tpl)



    # build "05_Vorbericht" Gesamtergebnisplan

    #vorb04tpl_instanz = docbuilder.create_tpl_instance(vorb04tpl)

    

    # build "06_Vorbericht_aenderungenErtraege"

    vorb05tpl_instanz = docbuilder.create_tpl_instance(vorb05tpl)
    print(" ")
    print("----------------------------")
    print("*** Templateinstanz Vorbericht 05 Ertrag erzeugt")
    contextvorb05 = ctx.hh_vorbericht_06_Ertraege(df=dfbew, dferl=dferl, mindiff=env.mindiff, dfew=dfewentw, dflfaghhj=dflfaghhj, dfod = dfod, dfstk=dfstkraft, hhj=hhj, doc=vorb05tpl_instanz)
    print("...Daten für Vorbericht 06 'Veränderungen in den Erträgen' sind zusammengestellt ")
    docbuilder.builddocx(tpl=vorb05tpl_instanz, context=contextvorb05, filename="06-Vorb_Ertraege", gde=gde, hhj=hhj)
    print(f"...Vorbericht 06 - Veränderung in den Erträgen: Ausgabe/{gde}/{hhj}")
    

    #build "07_Vorbericht" Aufwendungen im Ergebnishaushalt
    print(" ")
    print("----------------------------")
    vorb06tpl_instanz = docbuilder.create_tpl_instance(vorb06tpl)
    print("*** Templateinstanz Vorbericht 06 Aufwand erzeugt")

    kfadict = {
        "stk" : contextvorb05["stk"],
        "szzo": contextvorb05["szzo"],
        "sza" : contextvorb05["sza"],
        "szb" : contextvorb05["szb"],
    }

    #print(kfadict)
    contextvorb06 = ctx.hh_vorbericht_07_aufwand(df=dfbew, dferl=dferl, mindiff=env.mindiff, dfumlagen=dfstkraft, kfadict=kfadict, doc=vorb06tpl_instanz)
    print("...Daten für Vorbericht 07 'Veränderungen in den Aufwendungen' sind zusammengestellt ")
    docbuilder.builddocx(tpl=vorb06tpl_instanz, context=contextvorb06, filename="07-Vorb_Aufwand", gde=gde, hhj=hhj)
    print(f"...Vorbericht 07 - Veränderung in den Aufwendungen: Ausgabe/{gde}/{hhj}")



    #bulid "08_FinnHH" Abweichungen Finanzhaushalt



    #build "09_Invest" Investitionen
    print(" ")
    print("----------------------------")
    print("*** Templateinstanz Vorbericht 08 Invest erzeugt")
    vorb08tpl_instanz = docbuilder.create_tpl_instance(vorb08tpl)
    contextvorb08 = ctx.hh_vorbericht_09_invest(dfneu=erg.createinvest(df=dfbew, dfprod=dfpro, dfmnt=dfmn, dferl=dferl))
    print("Daten für Vorbericht 08 'Investitionen' sind zusammengestellt ")
    docbuilder.builddocx(tpl=vorb08tpl_instanz, context=contextvorb08, filename="08-Vorb_Invest", gde=gde, hhj=hhj)
    print(f"Vorbericht 08 - Investitionen: 'Ausgabe/{gde}/{hhj}")
    
    #build "10_Kredit" Kredite
   
    print(" ")
    print("----------------------------")
    print("*** Templateinstanz Vorbericht 10 Kredit")
    vorb10tpl_instanz = docbuilder.create_tpl_instance(vorb10tpl)
    contextvorb10 = ctx.hh_vorbericht_10_kredit(dfschulden=dfschulden, dfliq=dfliq, dfbew=dfbew, hhj=hhj, gde=gde, doc=vorb10tpl_instanz)
    print("Daten für Vorbericht 10 'Kredit und Bestand' sind zusammengestellt")
    docbuilder.builddocx(tpl=vorb10tpl_instanz, context=contextvorb10, filename="10-Vorb_Kredit", gde=gde, hhj=hhj)
    print(f"Vorbericht 10 - Kredit und Bestand: 'Ausgabe/{gde}/{hhj}")
   


    #build "11_Pflichtanlagen" Pflichtanlagen
    
    print(" ")
    print("----------------------------")
    print("*** Templateinstanz Vorbericht 11 Pflichtanlagen erzeugt")
    vorb11tpl_instanz = docbuilder.create_tpl_instance(vorb11tpl)
    contextvorb11 = ctx.hh_vorbericht_11_Pflichtanlagen(hhj=hhj, 
                                                        gde=gde, 
                                                        doc=vorb11tpl_instanz, 
                                                        dferg=stat.ergstat(bewegungsdaten=dfbew, grunddaten=dfergebnis, gde=gde, hhj=hhj),
                                                        dfbew=2, 
                                                        dffinanz=3, 
                                                        dfje=4, 
                                                        dfek = stat.ekstat(bewegungsdaten=dfbew, grunddaten=dfergebnis, hhj=hhj, gde=gde), )
    print("Daten für Vorbericht 11 'Pflichtanlagen' sind zusammengestellt ")
    docbuilder.builddocx(tpl=vorb11tpl_instanz, context=contextvorb11, filename="11-Vorb_Pflichtanlagen", gde=gde, hhj=hhj)
    print(f"Vorbericht 11- Pflichtanlagen: 'Ausgabe/{gde}/{hhj}")
    
    