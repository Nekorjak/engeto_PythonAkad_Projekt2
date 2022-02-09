import datetime
from random import randrange


def hlavicka():
    """Pozdraví užitele a vypíše úvodní text"""

    uvitani_1 = "Hi there!"
    uvitani_2 = "I've generated a random 4 digit number for you."
    uvitani_3 = "Let's play a bulls and cows game."
    uvitani_4 = "Enter four unique numbers. Do not start with zero."
    uvitani_5 = "Write >quit< to end the game"
    oddelovac = '-' * len(uvitani_4)
    print(uvitani_1, oddelovac, uvitani_2, uvitani_3, oddelovac, uvitani_4, uvitani_5, oddelovac, sep='\n')


def pc_cisla() -> list:
    """Sada 4 nahodnych cisel v listu. Sada nezacina nulou
    a neobsahuje duplicitni hodnoty."""

    cisla_random = []
    while len(cisla_random) < 4:
        cislo = str(randrange(0, 10))
        if len(cisla_random) == 0 and cislo == '0':
            continue
        elif cislo in cisla_random:
            continue
        else:
            cisla_random.append(cislo)
    return cisla_random


def vstup_uzivatele() -> list:
    """Vyhodnoti , zda je sada ctyr cisel od uzivatele ve spravnem formatu.
    Dokud neni podminka splnena, je vstup znovu a znovu vyzadovan.
    """

    prepinac = 1
    while prepinac:
        vstup = (input('\n''Enter four numbers >>>'))
        if vstup == 'quit':
            print('Thanks for playing! Bye!')
            exit()
        if vstup.isnumeric() is False or len(vstup) != 4:
            print('Please, use four numbers.')
        if vstup[0] == '0':
            print('You cannot start with "0"')
        if len(vstup) == 4 and vstup[0] != '0' and vstup.isnumeric() is True:
            prepinac = 0
            return list(vstup)


def bulls_list(vstup_uzivatele_fix, pc_cisla_fix) -> list:
    """Tvori seznam uhodnutych bulls. Parametry jsou definvany v hlavni funkci hra()."""

    bulls_cisla = []
    for x, y in zip(vstup_uzivatele_fix, pc_cisla_fix):
        if x == y:
            bulls_cisla.append(x)
    return bulls_cisla


def cows_list(vstup_uzivatele_fix, pc_cisla_fix) -> list:
    """Tvori seznam uhodnutych cows. Parametry jsou definvany v hlavni funkci hra()."""

    cows_cisla = []
    for i in vstup_uzivatele_fix:
        if i in pc_cisla_fix:
            cows_cisla.append(i)
    return cows_cisla


def hodnoceni_hry(vstup_uzivatele_fix, pc_cisla_fix):
    """Vyhodnocuje stav bulls and cows. Dale hlida, zda hrac uhodl celou tajenku.
    Pokud ano, posila do hlavni funkce informaci win = True"""

    num_of_bulls = len(bulls_list(pc_cisla_fix, vstup_uzivatele_fix))
    num_of_cows = len(cows_list(pc_cisla_fix, vstup_uzivatele_fix)) - num_of_bulls

    if num_of_bulls != 4:
        if num_of_bulls == 1:
            print('1 bull')
        else:
            print(f'{num_of_bulls} bulls')
        if num_of_cows == 1:
            print('1 cow')
        else:
            print(f'{num_of_cows} cows')
    win = num_of_bulls == 4
    return win is True


def hra():
    """Pro usnadneni kontroly funkcnosti hry se na zacatku vytiskne cislo
    generovana pocitacem: print('PC vybral: ', pc_cisla_fix).
    Promenna 'pc_cisla_fix' prejima vstup od PC a zafixuje ho pro jednu hru.
    Promenna 'vstup_uzivatele_fix' prejima vstup od uzivatele a fixuje ho na jedno kolo ve hre.
    Funkce obsahuje mereni casu trvani hry"""

    hlavicka()
    pc_cisla_fix = pc_cisla()
    print('PC vybral: ', pc_cisla_fix)
    time_start = datetime.datetime.now().replace(microsecond=0)

    win = False
    while win is False:
        vstup_uzivatele_fix = vstup_uzivatele()
        win = hodnoceni_hry(vstup_uzivatele_fix, pc_cisla_fix)
    time_stop = datetime.datetime.now().replace(microsecond=0)
    print(f'CONGRATULATIONS!. YOU WIN"\nYour time is: {time_stop - time_start} ')


hra()
