import random
szam=[]
szam.append(random.randint(100,999))


def generalo():
    vezeteknev=input("Kérem a vezetéknevét!")
    keresztnev=input("Kérem a vezetéknevét!")
    felhasznalonev=vezeteknev[0]+keresztnev[0]+str(szam)
    return felhasznalonev
    print(felhasznalonev)


generalo()


