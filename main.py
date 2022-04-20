'''
Welcome to Python.
linha de comentário grande inicia e termina com aspas simples ou dupla
'''

# Python não usa função principal nem limitadores com { } nem ponto e virgula no final, como na linguagem C ou C++

# importando bibliotecas
import math,os

# aqui tem uma linha de comentário

# A função print() em Python OUTPUT

# mostrando uma mensagem de texto
print("Olá aluno! Bem-vindo ao curso de Python.")

# usando \n ou \t
print("Olá aluno!\n e aqui pula linha.")
print("Olá aluno!\t e aqui dá um espaço (tab).")

# mostrando o valor de uma variável dentro do print
nome1 = 'José da Silva'
print("Benvindo,",nome1)

# mostrando o valor de uma variável dentro do print (no meio do texto)
nome2 = input("Digite seu nome: ")
print("Olá "+nome2+"!. Bem-vindo ao Instituto Federal de São Paulo!\n")

# texto concatenado (juntando textos)
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

# ou assim:
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

# expressões matemáticas concatenadas (+)
x = 5
y = 10
print (x+y) # ou
print("A soma de ",x,"+",y,"=",x + y,"\n")

# comando de entrada INPUT
nome = str(input("Solicitando um nome (ou uma string):\n"))
n1 = int(input("Solicitando um valor inteiro:\n"))
n2 = float(input("Solicitando um valor real:\n"))

#usando a bliblioteca 'os' para o comando 'clear'
os.system('clear')
print ("Mostrando o conteúdo de uma variavel do tipo caracter (string):")
print ("Nome digitado é ",nome,"\n")
print ("Mostrando o conteúdo de uma variavel do tipo numerica:")
print ("Número inteiro é ",n1)
print ("Número real é ",n2)

#executando expressões matemáticas e biblioteca de matematica 'math'
print ('Expressões matemáticas:') 
soma = n1+n2
subt = n1-n2
mult = n1*n2
divs = n1/n2
mod = n1%2 
raiz = math.sqrt(n1)
pote = math.pow(n2,n1)
arba = math.floor(n2)   # arredoda para o proximo inteiro abaixo
arci = math.ceil(n2)    # arredoda para o proximo inteiro acima
mode = math.fmod(n1,2)  # faz o mod ou %
ang = float(input("Digite o valor de um angulo:\n"))
os.system('clear')
# seno,cosseno e tangente calculado em radianos e convertidi para graus
seno = math.sin(math.radians(ang))
coss = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))
print ("Resultado das expressões matemáticas:")
print ("Para n1=",n1," e n2=",n2,"\n")
print ("A soma é ",soma,"\nA subtração é ",subt,"\nA multiplicação é ",mult,"\nA divisão é ",divs)
print ("A raiz é ",raiz,"\nA potencia é ",pote,"\nArredondar para baixo é ",arba,"\nArredondar para cima é ",arci)
print ("O mod de n1%2 é ",mod)
print ("O mod de n1%2 usando a bliblioteca math é ",mode,"\n")
print (f"Seno é {seno:.2f}\nCosseno é {coss:.2f}\nTangente é {tang:.2f}")
print (f"O valor de π é {math.pi:.4f}")

# utilizando if, else e elif (else if)
print ("\nO if tem que usar : no final do comando e identação (tab) no if e else.")
print ("\nO if pode usar if, elif ou else.")
x = int(input("Digite um valor para X:\n"))
if (x==0):
    print("X é igual a 10")
elif (x>0):
    print("X é positivo")
else:
    print("X é negativo")

# verificando se número é par
if (x%2==0):
    print("O número ",x," é par")
else:
    print("O número ",x," é impar")

# verificar a hora e ver se é manhã, tarde ou  noite
z = int(input("Digite a hora atual (inteiro):\n"))
if (z<12):
  print("Manhã")
elif (z<18):
  print("Tarde")
else:
  print("Noite")

# verificando se número é impar e multiplo de 3
# para juntar condições use "and" ou "or"
y = int(input("Digite um valor qualquer inteiro:\n"))
if (y%2==1 and y%3==0):
  print("O número ",y," é impar e multiplo de 3")
else:
  print("O número ",y," está fora")
  
  
  



