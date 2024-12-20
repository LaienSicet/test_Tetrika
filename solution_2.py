import requests
from bs4 import BeautifulSoup
import csv
import time
import random

stroka = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'

s = 0# это не обязательно, однако спокойнее знать, что происходит. =)
slovar = dict()


def rekyrsiv_parsing(adres):
    'считает количество животных на каждой странице, а затем рекурсивно открывает следующую страницу'
    global s, slovar
    inf = requests.get(adres).text
    inf_1 = BeautifulSoup(inf, 'lxml')
    inf_2 = inf_1.find_all(class_="mw-category-group")

    for i in inf_2[2::]:

        kl = i.find('h3').text
        zn = len(i.find_all('a'))

        if kl in slovar:
            slovar[kl] += zn
        else:
            slovar[kl] = zn

    s += 1# это не обязательно, однако спокойнее знать, что происходит. =)
    dalhe = inf_1.find('a', string='Следующая страница')
    if dalhe:
        print(f'страница {s}. продолжаем.')# это не обязательно, однако спокойнее знать, что происходит. =)
        adres_1 = 'https://ru.wikipedia.org' + dalhe.get('href')
        time.sleep(random.randint(0, 2))
        rekyrsiv_parsing(adres_1)
    else:
        print(f'готово!\nвсего обработано {s} страниц.')# это не обязательно, однако спокойнее знать, что происходит. =)



rekyrsiv_parsing(stroka)

with open('beasts.csv', 'w', encoding='utf-8') as fa:
    write = csv.writer(fa)
    for i in slovar:
        write.writerow([i, slovar[i]])

