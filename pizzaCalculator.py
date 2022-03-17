#Matthew Penhoat's Pizza calculator

from logging import exception


pizzaklein= 5
pizzanormaal= 9
pizzagroot= 13

print('Welkom bij Matthew Pizzas, Hier kunt u bestellen!')
a = True
Hoeveelheidklein = (input('Hoeveel kleine pizzas wilt u?: ' ))
while a == True:
    try:
        Hoeveelheidklein = int(Hoeveelheidklein)
        if Hoeveelheidklein <= 0:
            raise exception
    except:
        print('Sorry dit moet een heel cijfer zijn')
        Hoeveelheidklein = (input('Hoeveel kleine pizzas wilt u?: ' ))
    else: a = False



b = True
Hoeveelheidnormaal = (input('Hoeveel normale pizzas wilt u?: ' ))
while b == True:
    try:
        Hoeveelheidnormaal = int(Hoeveelheidnormaal)
        if Hoeveelheidnormaal <= 0:
            raise exception
    except:
        print('Sorry dit moet een heel cijfer zijn')
        Hoeveelheidnormaal = (input('Hoeveel normale pizzas wilt u?: ' ))
    else: b = False


c = True
Hoeveelheidgroot = (input('Hoeveel grote pizzas wilt u?: ' ))
while c == True:
    try:
        Hoeveelheidgroot = int(Hoeveelheidgroot)
        if Hoeveelheidgroot <= 0:
            raise exception
    except:
        print('Sorry dit moet een heel cijfer zijn')
        Hoeveelheidgroot = (input('Hoeveel grote pizzas wilt u?: ' ))
    else: c = False


prijsklein = Hoeveelheidklein * pizzaklein
prijsnormaal = Hoeveelheidnormaal * pizzanormaal
prijsgroot = Hoeveelheidgroot * pizzagroot
prijstotaal = prijsklein + prijsnormaal + prijsgroot

print ('Bestel Bon')
print ('-----------------------------------------')
print ('Kleine pizza: €' + str(prijsklein))
print ('Normale pizza: €'  + str(prijsnormaal))
print ('Grote pizza: €' + str(prijsgroot))
print ('Totaalprijs: €' + str(prijstotaal))
print ('Bedankt voor uw bestelling!')
print ('-----------------------------------------')