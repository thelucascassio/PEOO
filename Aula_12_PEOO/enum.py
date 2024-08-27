import enum

class Estacao(enum): #enum recebe apenas um valor listado
    outono = 1
    inverno = 2
    primavera = 3
    verao = 4

a = Estacao.outono
print(a, type(a)) #Estacao.outono
print(a.name) #outono


class Dia(enum.IntFlag): #intflag recebe potencias de 2. 2^3, 2^4
    domingo = 1 #intflag recebe mais de um valor listado
    segunda = 2
    terca = 4
    quarta = 8
    quinta = 16
    sexta = 32
    sabado = 64

d = Dia(0)
print(d)
d = Dia.terca
print(d)
d = Dia.terca | Dia.sexta
print(d, type(d))