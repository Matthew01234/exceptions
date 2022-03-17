from logging import exception
print ('(-----------------------------------------------)')
print ('+   Sollicitatieformulier "Circusdirecteur"     +')
print ('(-----------------------------------------------)')
print (' Er wordt u een aantal relevante vragen gesteld...')
print (' Gelieve die naar eer en geweten in te vullen')
print (' Als blijkt dat u aan de criteria voldoet dan komt \n u in aanmerking voor een serieus sollicitatiegesprek!')
print (' Ontspan maar blijf wakker, hier komen de vragen!')
print ('(-----------------------------------------------)')

naam = input ('Wat is je voor naam?: ').lower()
try:
     if naam != 'matthew':
        raise exception
except: 
        print('wat een kut naam')
        exit()


lengte = input ('Wat is je lengte?: ')
gender = input ('man / vrouw: ')
if (gender == 'man'):
        snor = input ('Hoe breed is je snor?: ')
            
if (gender == 'vrouw'):
        haarkleur = input ('Is je haar rood? ja/nee: ')
        if (haarkleur == 'ja'):
                lengtehaar = input ('hoelang is je haar?: ')

gewicht = input ('Hoe zwaar ben je?: ')
try:
     if gewicht > 200:
        raise exception
except: 
        print('Ga sporten inplaats van solliciteren')
        exit()

diploma = input ('In bezit van een Diploma MBO-4 ondernemen? ja/nee: ')
praktijk = input ('Meer dan 4 jaar praktijkervaring met dieren-dressuur \nOf meer dan 5 jaar ervaring met jongleren \nOf meer dan 3 jaar praktijkervaring met acrobatiek? ja/nee: ')
rijbewijs = input ('In bezit van een geldig Vrachtwagen rijbewijs? ja/nee: ')
hoed = input ('In bezit van een hoge hoed? ja/nee: ')
certificaat = input ('In bezit van certificaat: “Overleven met gevaarlijk personeel” ja/nee: ')
kaas = input ('Hou je van kaas?: ')
worst = input ('Hou je van worst?: ')
boterham = input ('Hou je van een boterham?: ')
appel = input ('Hou je van appel?: ').lower
try:
     if appel == 'nee':
        raise exception
except: 
        print('an appel a day keeps the doctor away')
        exit()


  
if (int(lengte) > 150) and (int(gewicht) > 90) and (diploma == 'ja') and (praktijk == 'ja') and (rijbewijs == 'ja') and (hoed == 'ja') and (certificaat == 'ja') and (int(snor) > 10 or ((haarkleur == 'ja') and int(lengtehaar) > 20 )):
    print('Je kan op solli komen ')
else:
    print ('sorry deze baan is niet van toepassing')
