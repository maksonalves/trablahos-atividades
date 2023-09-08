'''print((lambda x, y: x * y)(y=5,x=7))

a = (lambda *args: sum(args))(7,5,6,7,8) #sum soma tudo que esta dentro do args

print(a)

soma = lambda *args: sum(args)

print(soma(7,8,9,5,6,2))'''

numero_par = lambda x: "par" if x % 2 == 0 else "impar"
num = int(input("digite um numero: "))
print(numero_par(num))

