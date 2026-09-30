"""30 esercizi Python - versione .py
Ricostruita dal notebook fornito, mantenendo i nomi richiesti dagli esercizi.
"""

import math
import random
import re
from datetime import date


# ============================================================
# Esercizio 1
# Crea una funzione area_cerchio() che restituisca l'area di un cerchio.
# ============================================================
def area_cerchio(raggio):
    return math.pi * raggio ** 2


# ============================================================
# Esercizio 2
# Restituisce l'ipotenusa dati i due cateti.
# ============================================================
def ipotenusa(cateto_a, cateto_b):
    return math.sqrt(cateto_a ** 2 + cateto_b ** 2)


# ============================================================
# Esercizio 3
# Genera un intero casuale compreso tra minimo e massimo inclusi.
# ============================================================
def rand(minimo, massimo):
    return random.randint(minimo, massimo)


# ============================================================
# Esercizio 4
# Stampa tutti i numeri da first a last inclusi.
# ============================================================
def printNums(first=0, last=100):
    for numero in range(first, last + 1):
        print(numero)


# ============================================================
# Esercizio 5
# Trasforma un nome nelle sue iniziali. Es. "Tizio Caio" -> "T.C."
# ============================================================
def iniziali(nome):
    parole = nome.split()
    return "".join(parola[0].upper() + "." for parola in parole)


# ============================================================
# Esercizio 6
# Verifica se tre numeri possono essere i lati di un triangolo.
# ============================================================
def isTriangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    return (
        abs(b - c) < a < b + c
        and abs(a - c) < b < a + c
        and abs(a - b) < c < a + b
    )


# ============================================================
# Esercizio 7
# Congettura di Collatz.
# ============================================================
def collatz(n):
    risultato = [n]
    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
        risultato.append(n)
    return risultato


# ============================================================
# Esercizio 8
# FizzBuzz da 1 a 100.
# ============================================================
def fizz_buzz():
    for numero in range(1, 101):
        if numero % 15 == 0:
            print("FizzBuzz")
        elif numero % 3 == 0:
            print("Fizz")
        elif numero % 5 == 0:
            print("Buzz")
        else:
            print(numero)


# ============================================================
# Esercizio 9
# Restituisce i primi n numeri della successione di Fibonacci.
# ============================================================
def fibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]

    risultato = [0, 1]
    while len(risultato) < n:
        risultato.append(risultato[-1] + risultato[-2])
    return risultato


# ============================================================
# Esercizio 10
# Verifica se n è un numero primo.
# ============================================================
def isPrime(n):
    if n < 2:
        return False
    for divisore in range(2, int(math.sqrt(n)) + 1):
        if n % divisore == 0:
            return False
    return True


# ============================================================
# Esercizio 11
# Stampa i numeri tra minimo e massimo; se multipli di n1/n2/n3,
# stampa la relativa frase. La priorità è n1, poi n2, poi n3.
# ============================================================
def multipli(minimo, massimo, n1, n2, n3):
    for numero in range(minimo, massimo + 1):
        if numero % n1 == 0:
            print(f"{numero} é un multiplo di {n1}")
        elif numero % n2 == 0:
            print(f"{numero} é un multiplo di {n2}")
        elif numero % n3 == 0:
            print(f"{numero} é un multiplo di {n3}")
        else:
            print(numero)


# ============================================================
# Esercizio 12
# Se la somma dei tre numeri è pari restituisce la somma,
# altrimenti restituisce la media.
# ============================================================
def sommaMedia(n1, n2, n3):
    somma = n1 + n2 + n3
    if somma % 2 == 0:
        return somma
    return somma / 3


# ============================================================
# Esercizio 13
# Calcola quanti giorni mancano al prossimo Capodanno.
# ============================================================
def giorni_a_capodanno():
    oggi = date.today()
    prossimo_capodanno = date(oggi.year + 1, 1, 1)
    return (prossimo_capodanno - oggi).days


# ============================================================
# Esercizio 14
# Calcola il fattoriale in maniera iterativa.
# ============================================================
def fattoriale(n):
    if n < 0:
        raise ValueError("Il fattoriale non è definito per numeri negativi")

    risultato = 1
    for numero in range(1, n + 1):
        risultato *= numero
    return risultato


# ============================================================
# Esercizio 15
# Genera una lista di n interi casuali tra minimo e massimo.
# ============================================================
def randomNumbers(n, minimo, massimo):
    risultato = []
    for _ in range(n):
        risultato.append(random.randint(minimo, massimo))
    return risultato


# ============================================================
# Esercizio 16
# Genera n interi casuali tra 1 e 100 e conserva solo quelli pari.
# ============================================================
def randomNumbersPari(n):
    risultato = []
    for _ in range(n):
        numero = random.randint(1, 100)
        if numero % 2 == 0:
            risultato.append(numero)
    return risultato


# ============================================================
# Esercizio 17
# Calcola la media e i valori inferiori alla media.
# ============================================================
def printLowerThanAverage(arr):
    if not arr:
        raise ValueError("La lista non può essere vuota")

    media = sum(arr) / len(arr)
    minori = []
    for numero in arr:
        if numero < media:
            minori.append(numero)

    print(f"media = {media}, valori minori = {minori}")
    return media, minori


# ============================================================
# Esercizio 18
# Conta le cifre di un intero con massimo 4 cifre.
# ============================================================
def nCifre(n):
    valore = abs(n)
    if valore > 9999:
        return "numero troppo grande o troppo piccolo"
    if valore < 10:
        return "1 cifra"
    if valore < 100:
        return "2 cifre"
    if valore < 1000:
        return "3 cifre"
    return "4 cifre"


# ============================================================
# Esercizio 19
# Esegue un'operazione elemento per elemento tra due liste.
# ============================================================
def riduci(arr1, arr2, operazione):
    risultato = []

    for a, b in zip(arr1, arr2):
        if operazione == "addizione":
            risultato.append(a + b)
        elif operazione == "sottrazione":
            risultato.append(a - b)
        elif operazione == "moltiplicazione":
            risultato.append(a * b)
        elif operazione == "divisione":
            risultato.append(a / b)
        else:
            raise ValueError("Operazione non riconosciuta")

    return risultato


# ============================================================
# Esercizio 20
# Restituisce la parola più lunga di una stringa.
# ============================================================
def longerWord(string):
    parole = string.split()
    if not parole:
        return ""

    risultato = parole[0]
    for parola in parole[1:]:
        if len(parola) > len(risultato):
            risultato = parola
    return risultato


# ============================================================
# Esercizio 21
# Conta le vocali presenti in una stringa.
# ============================================================
def contaVocali(stringa):
    vocali = "aeiouAEIOU"
    conta = 0
    for carattere in stringa:
        if carattere in vocali:
            conta += 1
    return conta


# ============================================================
# Esercizio 22
# Somma tutti i naturali da 1 a n usando la formula di Gauss.
# ============================================================
def sommaNaturali(n):
    return n * (n + 1) // 2


# ============================================================
# Esercizio 23
# Restituisce True se la somma degli elementi è pari.
# ============================================================
def isEven(array):
    return sum(array) % 2 == 0


# ============================================================
# Esercizio 24
# Restituisce il secolo corrispondente a un anno.
# ============================================================
def century(anno):
    return (anno - 1) // 100 + 1


# ============================================================
# Esercizio 25
# Traduce un booleano in "Yes" / "No".
# ============================================================
def boolTranslate(valore_bool):
    return "Yes" if valore_bool else "No"


# ============================================================
# Esercizio 26
# Restituisce [numero_positivi, somma_negativi].
# ============================================================
def countPositivesSumNegatives(array):
    if not array:
        return []

    positivi = 0
    somma_negativi = 0

    for numero in array:
        if numero > 0:
            positivi += 1
        elif numero < 0:
            somma_negativi += numero

    return [positivi, somma_negativi]


# ============================================================
# Esercizio 27
# Verifica manualmente se el è presente nella lista.
# ============================================================
def includes(array, el):
    for elemento in array:
        if elemento == el:
            return True
    return False


# ============================================================
# Esercizio 28
# Restituisce l'indice di el, oppure -1 se non è presente.
# ============================================================
def indexOf(array, el):
    for indice, elemento in enumerate(array):
        if elemento == el:
            return indice
    return -1


# ============================================================
# Esercizio 29
# Disegna un istogramma usando asterischi.
# ============================================================
def istogramma(array):
    for numero in array:
        print("*" * numero)
        print()


# ============================================================
# Esercizio 30
# Verifica se una stringa è palindroma ignorando spazi,
# punteggiatura e differenze tra maiuscole e minuscole.
# ============================================================
def isPalindrome(string):
    stringa_pulita = re.sub(r"[^A-Za-z0-9]", "", string).lower()
    return stringa_pulita == stringa_pulita[::-1]


# ============================================================
# TEST DEL NOTEBOOK
# ============================================================
if __name__ == "__main__":
    assert area_cerchio(2) == 12.566370614359172
    print("Esercizio 1 Corretto")

    assert ipotenusa(3, 4) == 5
    print("Esercizio 2 Corretto")

    test = rand(1, 3)
    assert test in (1, 2, 3)
    print("Esercizio 3 Corretto")

    # Esercizio 4: decommenta per vedere i numeri da 0 a 100
    # printNums(0, 100)

    assert iniziali("Tizio Caio") == "T.C."
    print("Esercizio 5 Corretto")

    assert isTriangle(1, 1, 1) is True
    assert isTriangle(1, 99, 1) is False
    print("Esercizio 6 Corretto")

    assert collatz(10) == [10, 5, 16, 8, 4, 2, 1]
    print("Esercizio 7 Corretto")

    # Esercizio 8: decommenta per eseguire FizzBuzz
    # fizz_buzz()

    assert fibonacci(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    print("Esercizio 9 Corretto")

    assert isPrime(37) is True
    assert isPrime(83) is True
    assert isPrime(85) is False
    print("Esercizio 10 Corretto")

    # Esercizio 11: decommenta per visualizzare l'output
    # multipli(0, 10, 3, 2, 5)

    assert sommaMedia(1, 2, 3) == 6
    assert sommaMedia(3, 3, 3) == 3
    print("Esercizio 12 Corretto")

    print(f"Esercizio 13: mancano {giorni_a_capodanno()} giorni a Capodanno")

    assert fattoriale(5) == 120
    assert fattoriale(9) == 362880
    print("Esercizio 14 Corretto")

    test = randomNumbers(100, 3, 5)
    for numero in test:
        assert 3 <= numero <= 5
    print("Esercizio 15 Corretto")

    test = randomNumbersPari(100)
    for numero in test:
        assert numero % 2 == 0
    print("Esercizio 16 Corretto")

    # Esercizio 17: esempio
    # printLowerThanAverage([3, 5, 10, 2, 8])

    assert nCifre(2) == "1 cifra"
    assert nCifre(33) == "2 cifre"
    assert nCifre(478) == "3 cifre"
    print("Esercizio 18 Corretto")

    assert riduci(
        [3, 7, 2, 5, 8, 1, 2, 5, 6, 4],
        [9, 3, 1, 4, 7, 6, 5, 10, 1, 5],
        "addizione",
    ) == [12, 10, 3, 9, 15, 7, 7, 15, 7, 9]
    print("Esercizio 19 Corretto")

    assert longerWord("ciao a tutti") == "tutti"
    print("Esercizio 20 Corretto")

    assert contaVocali("ciAo") == 3
    print("Esercizio 21 Corretto")

    assert sommaNaturali(4) == 10
    assert sommaNaturali(10) == 55
    print("Esercizio 22 Corretto")

    assert isEven([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) is True
    assert isEven([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) is False
    print("Esercizio 23 Corretto")

    assert century(2024) == 21
    assert century(1999) == 20
    print("Esercizio 24 Corretto")

    assert boolTranslate(False) == "No"
    assert boolTranslate(True) == "Yes"
    print("Esercizio 25 Corretto")

    assert countPositivesSumNegatives(
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
    ) == [10, -65]
    print("Esercizio 26 Corretto")

    assert includes([20, "banana", True], "banana") is True
    print("Esercizio 27 Corretto")

    assert indexOf([20, "banana", True], "banana") == 1
    assert indexOf([20, "banana", True], "pesca") == -1
    print("Esercizio 28 Corretto")

    # Esercizio 29: decommenta per visualizzare l'istogramma
    # istogramma([3, 7, 9, 5])

    assert isPalindrome("Ab ./B a") is True
    assert isPalindrome("Hackademy") is False
    print("Esercizio 30 Corretto")
