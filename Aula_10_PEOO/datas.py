import datetime
y =  datetime(2024, 8, 6)
print(y)
print(type(y))
z =  datetime(day=6, month=8, year=6)
print(z)
#quando colocamos a biblioteca/módulo, não precisamos repetir o datetime, mas no caso deste arquivo, precisamos
a =   now()
print(a)
# now() pode passar a informação de fuso horário, mas no today isso não é possível
date =   strptime("23/06/2023 09:30", "%d/%m/%Y %H:%M")
nasc = input("Digite o dia do seu nascimento (dd/mm/aaaa) ")
data =   strptime(nasc, "%d/%m/%Y") #strptime permitirá fazer contas
print(data)

hoje =   now()
print(hoje - data)

s = hoje.strftime("%A, %d, %b, %y") #o minúsuclo abrevia os nomes e números, quando possível
print(s)
print(type(s))