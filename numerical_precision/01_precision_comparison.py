###############################################################################
#Aufgabe01
###############################################################################

import sympy as sy
import decimal as dec

zahlen = [10**2,10**3,10**4,3*10**4]

# Standard-Gleitkomm
def harmonika1(n):
    s=0
    for i in range(1,n):
        s= s+(1/i)
    return s

for n in zahlen:
    print(harmonika1(n))


#Mantisse fünfstellig
def harmonika2(n):
    dec.getcontext().prec = 5
    s=0
    for i in range(1,n):
        s= dec.Decimal(s)+dec.Decimal(1/i)
    return s

for n in zahlen:
    print(harmonika2(n))

#Mantisse vierstellig
def harmonika3(n):
    dec.getcontext().prec = 5
    s=0
    for i in range(1,n):
        s= sy.Rational(s)+sy.Rational(1/i)
    return s

for n in zahlen:
    print(harmonika3(n))

print(harmonika2(1000))
