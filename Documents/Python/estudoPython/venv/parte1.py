#Estudo Python
#1-Variaveis
'''
nome = 'Rogerio'
numInteiro = 10
numFloat = 2.5

#2-variavel com Seleção
nomeTipo = str('Rogerio')
numInteiroTipo = int(10)
numFloatTipo = float(2.5)

print("\n1-Print variavel \n")

print(nome);
print(numInteiro);
print(numFloat)

print("\n2-Print variavel com Selecao\n")

print(nomeTipo);
print(numInteiroTipo);
print(numFloatTipo);

print("\n3-Print variavel com Frutas - Mesma linha declracao\n")

fruta1,fruta2,fruta3 = "maca","banana","uva"

print(fruta1)
print(fruta2)
print(fruta3)

print("\n4-Print variavel com Frutas -Atribhuições sequenciais\n")
fruta1=fruta2=fruta3= "Jaca"
print(fruta3)

print("\n5-Print variavel com Frutas - extraindo variaveis de uma lista\n")
frutas = ["cereja","melancia","limao"]
x,y,z = frutas

print(x)
print(y)
print(z)

print("\n6-Print tipos de variaveis\n")

print(type(nome))
print(type(numInteiro))
print(type(numFloat))

print("\n7-Print tipos de variaveis com selecao\n")

print(type(nomeTipo))
print(type(numInteiroTipo))
print(type(numFloatTipo))

print("\n8-Print tipos concatenar\n")

print("Nome: "+ nome)
print("Nome: "+ nome +" escoheu a fruta: "+fruta1+" Qtd: " + str(numInteiro)+ " Peso de :"+str(numFloat))
print("Nome: "+ nome +" do tipo :"+ str((type(nome))))

'''
'''
print("\n9-Variavel global e local\n")
#declarei a variavel fora da funcao
x = "variavelGlobal"
y= "Variavel Global2"
#criei a funcao
def minhaFuncao():
    print(x)
#acionei a funcao
minhaFuncao()


def funcaoSoma():
    soma = 10+2
    print(str(soma))

def funcaoSub():
    subtracao = 10-2
    print(str(subtracao))

funcaoSoma()
funcaoSub()

#A variavel apenas é acionada dentro da função
#print(str(soma))
#print(str(subtracao))

#Variavel global e aceita em todo programa

print(str(x))
print(str(y))
'''
'''
print("\n10-Definicao de Tipo de dado\n")

a = "Hello World"
b = 20
c = 20.5
d = 1j
e = ["maca","banana","Abacaxi"]
f = ("maca","banana","Abacaxi")
g = range(6)
h = {"maca","banana","Abacaxi"}
i = frozenset({"apple", "banana", "cherry"})
j = True

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(h))
print(type(i))
print(type(j))

print("\n11-Conversao Tipo\n")

k = float(b)
print(k)
print(type(k))

print("\n12-Numero Aleatorio\n")

#importacao_modulo_biblioteca
import random
print(random.randrange(1,20))

print("\n13-Multilinha String\n")

l="""----Menu----
A)cadastro
B)Edicao
C)Deletar"""

print(l)

print("\n14-String Matrizes\n")

m = "Rogerio"
print(m)
print(m[0],m[1],m[2])

print("\n15-Tamanho da String\n")
print(len(m))

print("\n16-Busca de palavra no texto\n")

texto = "A programacao em Python e otima"
print("Python" in texto)

print("\n17-Busca de texto com condicional\n")
texto = "A programacao em Python e otima"
if "Python" in texto:
    print("Sim, existe a palavra")

if "CSS" not in texto:
    print("Nao, existe a palavra")

print("\n18-Busca de texto por selecao\n")
print(texto[0:9])
print(texto[:9])
print(texto[9:])

print("\n19-Metodos Strings\n")

print(texto.upper())
print(texto.lower())
print(texto.strip())
print(texto.replace("Python","LARAVEL"))
print(texto.split(","))

print("\n20-Metodos Strings Format\n")
age = 36
txt = "Meu nome e Rogerio tenho {} anos" # inserir no texto as chaves e sinalizar no metodo a variavel declrada  
print(txt.format(age))

qtd = 3
pedacos = 567
preco = 49.935
myOrder = "Eu quero {} laranjas, dividido em {} pedacos com o valor de {}."
print(myOrder.format(qtd,pedacos,preco))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

print("\n21-Fuga no Python\n")
txt = "We are the so-called \"Vikings\" from the north."
print("Meu \\nome \ne Rogerio \rtenho \tqual \bsera \fo motivo")

print("""
Method	Description
1)capitalize()	Converts the first character to upper case
2)casefold()	Converts string into lower case
3)center()	Returns a centered string
4)count()	Returns the number of times a specified value occurs in a string
5)encode()	Returns an encoded version of the string
6)endswith()	Returns true if the string ends with the specified value
7)expandtabs()	Sets the tab size of the string
8)find()	Searches the string for a specified value and returns the position of where it was found
9)format()	Formats specified values in a string
10)format_map()	Formats specified values in a string
11)index()	Searches the string for a specified value and returns the position of where it was found
12)isalnum()	Returns True if all characters in the string are alphanumeric
13)isalpha()	Returns True if all characters in the string are in the alphabet
14)isdecimal()	Returns True if all characters in the string are decimals
15)isdigit()	Returns True if all characters in the string are digits
16)isidentifier()	Returns True if the string is an identifier
17)islower()	Returns True if all characters in the string are lower case
18)isnumeric()	Returns True if all characters in the string are numeric
19)isprintable()	Returns True if all characters in the string are printable
20)isspace()	Returns True if all characters in the string are whitespaces
21)istitle()	Returns True if the string follows the rules of a title
22)isupper()	Returns True if all characters in the string are upper case
23)join()	Joins the elements of an iterable to the end of the string
24)ljust()	Returns a left justified version of the string
25)lower()	Converts a string into lower case
26)lstrip()	Returns a left trim version of the string
27)maketrans()	Returns a translation table to be used in translations
28)partition()	Returns a tuple where the string is parted into three parts
29)replace()	Returns a string where a specified value is replaced with a specified value
30)rfind()	Searches the string for a specified value and returns the last position of where it was found
31)rindex()	Searches the string for a specified value and returns the last position of where it was found
32)rjust()	Returns a right justified version of the string
33)rpartition()	Returns a tuple where the string is parted into three parts
34)rsplit()	Splits the string at the specified separator, and returns a list
35)rstrip()	Returns a right trim version of the string
36)split()	Splits the string at the specified separator, and returns a list
37)splitlines()	Splits the string at line breaks and returns a list
38)startswith()	Returns true if the string starts with the specified value
39)strip()	Returns a trimmed version of the string
40)swapcase()	Swaps cases, lower case becomes upper case and vice versa
41)title()	Converts the first character of each word to upper case
42)translate()	Returns a translated string
43)upper()	Converts a string into upper case
44)zfill()	Fills the string with a specified number of 0 values at the beginning""")
'''
'''
print("\n22-Booleano\n")
print(10>9)
print(10==9)
print(10<9)

a = 200
b = 33

if b > a:
    print("b e maior que a")
else:
    print("a e maior que b")

def functionBolean():
    return True
print(functionBolean())

print(isinstance(a,float))
print("O valor e do tipo float :") 
'''
'''
print("\n23 - Operadores Aritmeticos\n")

print(10+5)
w=5+5
print(w)

x = 20
y = 3

adicao = x+y
subtracao = x-y
multiplicacao = x*y
divisao = x/y
restoMod = x%y
exponencial = x**y
divisaoInteiro = x//y
print("\n")
print(adicao)
print(subtracao)
print(multiplicacao)
print(divisao)
print(restoMod)
print(exponencial)
print(divisaoInteiro)

print("\n24 - Operadores Atribuicao\n")


print("\n25 - Operadores Atribuicao\n")

print(x==y)
print(x!=y)
print(x>y)
print(x<y)
print(x>=y)
print(x<=y)

print("\n26 - Operadores logicos\n")

print(x>10 and x<30)
print(x>10 or x<30)
print(not(x>10 and x<30))

print("\n27 - Operadores de asociação\n")
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
print(x is y)
print(x == y)
'''
'''
print("\n28 - Listas\n")

lista = ["maca","banana","laranja"]
print(lista)
print(lista[0])
print(lista[1])
print(lista[2])

print(len(lista))
print(type(lista))
lista2 = list(("laranja","banana","maca"))
print(lista2)
print(lista2[0])
print(lista2[1])
print(lista2[2])

print(lista[0:2])
print(lista[-2])

#alterando um item da lista
lista[0] = "Melancia"
print(lista)

#alterando trecho da lista
lista[0:2] = ["Caju","Tomate"]
print(lista)
#Metodo inserir
lista.insert(3,"Melancia")
print(lista)

#inserindo item ao final da lista
lista.append("limao")
print(lista)

#inserindo  conjunto de itens de outra lista

lista.extend(lista2)
print(lista)

#Removendo itens da lista

lista.remove("Tomate")
print(lista)

lista.pop(1)
print(lista)

del lista[2]
print(lista)

lista.clear()
print(lista)
'''
'''
print("\n29 - Listas e loops \n")
frutas = ["Abacaxi","Manga","limao"]
for x in frutas:
    print(x)


for i in range(len(frutas)):
    print(frutas[i])
'''
'''
print("\n30 - Listas e loops \n")

#formando o dicionario
pessoa = {
    "Nome": "Rogerio",
    "Idade": 39,
    "Altura": 1.78,
    "Ano Nascimento": 1981 ,
    "Profissao": "Contador",
}
print(pessoa)

#consultabndo elemento do CFBundleInfoDictionaryVersion

pessoaNome = pessoa["Nome"]
pessoaIdade = pessoa["Idade"]
print(pessoaNome)
print(pessoaIdade)

x = pessoa.get("Nome")
print(x)

y = pessoa.values()
print(y)

#alterando elemento do CFBundleInfoDictionaryVersion

pessoa["Idade"] = 40

print(pessoa)

pessoa.update({"Profissao": "Desenvolvedor"})
print(pessoa)

#adicionado elemento do CFBundleInfoDictionaryVersion

pessoa["Empresa"] = "RA7"
print(pessoa)

#Deletando elemento do CFBundleInfoDictionaryVersion
pessoa.pop("Empresa")
print(pessoa)

del pessoa["Ano Nascimento"]
print(pessoa)

pessoa.clear()
print(pessoa)

'''
'''
print("\n31 - If - Else \n")

a = input("Digite um numero A:  ")
b = input("Digite um numero B:  ")

if a > b:
    print("Numero A e maior que o numero B")
elif a < b:
    print("Numero A e menor que o numero B")
else :
    print("Numero A e igual o numero B")
'''
'''
print("\n32 - While  - Break\n")

i = 0

while i < 6:
    print(i)
    i=i+1
'''
'''
i=0
i2 = 0

while i < 6:
    print(i)
    if i == 3:
        break
    i=i+1
'''
'''
while i2 < 6:
    i2 = i2+1
    if i2 == 3:
        continue
    print(i2)
'''
'''
i = 0
while i < 6:
    print(i)
    i = i + 1
else:
    print("i e maiorr que 6 agora")
'''


'''
numero1 = input("Digite numero 1 :  ")
numero2 = input("Digite numero 2 :  ")

escolha = input("Escolha a operacao")


print("\n99 - Entrada\n")

nome = input("Digite seu nome:  ")
print("Nome digitado foi: "+ nome)
'''