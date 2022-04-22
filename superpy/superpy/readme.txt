Beste lezers,

Ik zal u kort uitleggen hoe superpy werkt.
1)koop een item:
enter in de terminal hetvolgende : 
python3 main.py buy --product-name Naam_van_het_item --price Prijs_van_item --expire-date vervaldatum_van_het_item --amount de_hoeveelheid
een voorbeeld:
python3 main.py buy --product-name orange --price 2 --expire-date 2022-04-30 --amount 5


2)verkoop een product
Enter in de terminal hetvolgende :
python3 main.py sell --product-name Naam_van_het_product --price Hoeveel_het_product_kost
een voorbeeld:
python3 main.py sell --product-name orange --price 2

3)export een bestand naar excel formaat
enter in het terminal het volgende:
python3 main.py export --import-file bestand naam van de csv file --export-file bestand naam van de excel bestand
Bijvoorbeeld:
python3 main.py export --import-file bought --export-file data1

Als het excel bestand al bestaat krijgt u een foutmelding
Mocht u graag willen weten welke csv bestanden in het programma staat kunt u de volgende command ingeven
python3 main.py files

Mocht u de geexporteerde data willen filteren op datum dan kunt u de command gebruiken
python3 main.py export --import-file bought --export-file data1 --start-date datum(YY-MM-DD) --end-date datum(YY-MM-DD) 
Bij --start-date kunt u de begin datum invoeren
en bij --end-date voert u de einddatum in
Bijvoorbeeld:
python3 main.py export --import-file stock --export-file data --start-date 2022-04-22 --end-date 2022-04-30



U kunt ook de bestandformaat aanpassen naar xlsx of naar csv
u kunt de argument --file-extension gebruiken een voorbeeld :
python3 main.py export --import-file stock --export-file data --start-date 2022-04-22 --end-date 2022-04-30 --file-extension csv

4)report
Als u een report van alle inventory wilt hebben dan kunt u deze command gebruiken
python3 main.py report --inventory

Als u een report wilt hebben van de sales dan kunt u het volgende invoeren
python3 main.py report --sales (zet hier in de datum welke gegevens u wilt inzien)
Als u alle data wilt inzien van de sales kunt u de volgende command gebruiken
python3 main.py report --sales all

Als u een report wilt hebben van de orders dan kunt u de volgende command gebruiken
python3 main.py report --orders (zet hier in de datum welke gegevens u wilt inzien)
Als u alle data wilt inzien van de orders kunt u de volgende command gebruiken
python3 main.py report --orders all

Als u een report wilt hebben van de revenue dan kunt u de volgende command gebruiken
python3 main.py report --revenue (zet hier in de datum welke gegevens u wilt inzien)
Je kan de de volgende gegevens in de revenue argument invoeren
today, tomorrow, yesterday of een datum als u een datum invoert dan moet u het doen in het volgende formaat jaar-maand

Als u een report wilt hebben van de profit dan kunt u de volgende command gebruiken
python3 main.py report --profit (zet hier in de datum welke gegevens u wilt inzien)
Je kan de de volgende gegevens in de revenue argument invoeren
today, tomorrow, yesterday of een datum als u een datum invoert dan moet u het doen in het volgende formaat jaar-maand


5)om de datum van het programma aan te passen kunt u de volgende command gebruiken
python3 main.py advancetime --days nummer --weeks nummer
u hoeft niet --days en --weeks te gebruiken het kan ook afzonderlijk een voorbeeld
python3 main.py advancetime --days 4