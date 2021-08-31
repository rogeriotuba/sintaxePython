#Estrutura de repetição infinita
while True:
  print("Hello world!")

#tab indenta shif + tab desindenta
'''i = 0
step = 5
while i < step:
  print("Hello world!") 
  #i = i+1
  i += 1
'''

choveu = False
while choveu != True:
  clima = input("Como está o tempo? ")
  if ('ch' in clima):
    choveu = True

sol = True
while sol == True:
  clima = input("Como esta o tempo?  ")
  if('sol' not in clima):
    print("Pega o guarda chuva!!")
    sol = False
  else:
    print("Bora pra praia!")

i = 10
while True:
  print("Hello world!")
  i -= 1
  if (i == 0):
    break
