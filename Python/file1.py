#exemplo
class Triangulo: #temos a forma do bolo, não o bolo ainda
    def __init__(self):
        self.b = 0
        self.h = 0
    def calc_area(self): #Método
        return self.b * self.h / 2

x = Triangulo()
#x.b = int(input("Digite a base do triângulo: "))
#x.h = int(input("Digite a altura do triângulo: "))

x.b = 10
x.h = 20
print(x.b) #10
print(x.h) #20
y = x
y.b = 30 #x e y, que são os mesmos, recebem o 30 no atributo b
y.h = 40 #x e y, que são os mesmos, recebem o 40 no atributo b
print(x.b) #não temos dois objetos, temos duas referências para um mesmo objeto #30
print(x.h) #40
z = Triangulo()
z.b = 50
z.h = 60
print(z.b)
print(z.h)
print("Atributos de x: ", x.b, x.h)
print("Área de x :", x.calc_area())

print("Atributos de y: ", y.b, y.h)
print("Área de y :", y.calc_area())

print("Atributos de z: ", z.b, z.h)
print("Área de z :", z.calc_area())