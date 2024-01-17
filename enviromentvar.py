import pathlib

'''
***************** A C H T U N G *****************
ATTENTION ATTENTION ATTENTION ATTENTION ATTENTION 
*************************************************

Es ist wichtig, dass für die einzulesenden Dateien

bewegungsdaten.xlsx

und

grunddaten.xlsx

keine Veränderungen an der Struktur vorgenommen werden.
Daten MÜSSEN in der vorgegebenen Struktur eingegeben werden!

'''

# Gemeinde
gde = 60

# Haushaltsjahr
hhj = 2023


# Datei für die Bewegungsdaten des Haushaltsplans
bewDat = str(pathlib.Path.cwd() / "hhdaten/bewegungsdaten.xlsx")

# Datei für die Grunddaten des Haushaltsplans
grunddaten = str(pathlib.Path.cwd() / "hhdaten/grunddaten.xlsx")

# Templates Haushaltssatzung und Vorbericht
hhstpl = str(pathlib.Path.cwd() / "wordtemplates/hhs.docx")
vorb01tpl = str(pathlib.Path.cwd() / "wordtemplates/02_Vorbericht_Allgemeines.docx")
vorb02tpl = str(pathlib.Path.cwd() / "wordtemplates/03_VorberichtVVJ.docx")
vorb03tpl = str(pathlib.Path.cwd() / "wordtemplates/04_VorberichtVJ.docx")
vorb04tpl = str(pathlib.Path.cwd() / "wordtemplates/05_Vorbericht_uebersicht_erghh.docx")
vorb05tpl = str(pathlib.Path.cwd() / "wordtemplates/06_Vorbericht_aenderungenErtraege.docx")
vorb06tpl = str(pathlib.Path.cwd() / "wordtemplates/07_Vorbericht_aenderungenAufwand.docx")
vorb07tpl = str(pathlib.Path.cwd() / "wordtemplates/08_Vorbericht_ueb_FinHH.docx")
vorb08tpl = str(pathlib.Path.cwd() / "wordtemplates/09_Vorbericht_Invest.docx")
vorb10tpl = str(pathlib.Path.cwd() / "wordtemplates/10_Vorbericht_Kredit.docx")
vorb11tpl = str(pathlib.Path.cwd() / "wordtemplates/11_Vorb_Pflichtanlagen.docx")

# Quelle für die Flächenstatistik
quelleflaechendaten = "Statistisches Landesamt RLP, 2021"

# Quelle der Einwohnerstatistik
quelleewdaten = "Komwisberichte"

# Jahresabschluss VVJ

ja_erledigt_teilsatz = "derzeit nur vorläufig fertiggestellt." #Die Jahresrechnung für das Haushaltsjahr {{hhj-2}} ist {{ja_erledigt_teilsatz}}.
erlaeuterung_ergebnis_vvj = "Wesentliche Verbesserungen ergaben sich insbesondere durch gestiegene Steuereinnahmen."
erlaeuterung_finanz_vvj = "Wesentliche Verbesserungen ergaben sich durch die Verschiebung von Unterhaltungs- und Investitionsmaßnahmen"
ergueb = "vorl. Erg."

# Abweichungsgröße ab der eine gesonderte Erläuterung der Haushaltsstelle im VOrbericht erfolgt
mindiff = 1000

# Haushaltsstelle für die Einplanung der Tilgung für neue Plandarlehen
tilgung_plandarlehen = "6.1.2.1/9999.792511"
