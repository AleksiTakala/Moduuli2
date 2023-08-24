import math

Leivi = input('Anna leiviskät ')
Naula = input('Anna naulat ')
Luoti = input('Anna luodit ')

leivi = float(Leivi)
naula = float(Naula)
luoti = float(Luoti)

maaraL = leivi * 8.512
maaraN = naula * 0.4256
maaraLu = luoti * 0.0133

Yhte = int(maaraL + maaraN + maaraLu)
gram = maaraL + maaraN + maaraLu
Gram = (gram - Yhte)*1000
deci = round(Gram, 2)
print("Massa nykymittojen mukaan ")
print(Yhte, " Kilogrammaa ja " ,deci)

