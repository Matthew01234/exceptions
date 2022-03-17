
from logging import exception


getal = input('Vul een getal boven de 0 in: ')
a = True
while a == True:
    try:
        getal = int(getal)
        if getal <= 0:
            raise exception
    except:
        print('Ik zei een getal boven de 0...')
        getal = (input('Vul een getal boven de 0 in: ' ))
    else: a = False
