

nome = "Rogerio";
sobreNome = "Andrade";

if(nome == "Rogerio"):
    print("\nAcesso Permitido");

if(nome != "Rogério"):
    print("\nAcesso Negado");

if(len(nome)==len(sobreNome)):
    print("Nome e sobrenome tem o mesmo tamanho;");
else:
    print("Nome e sobrenome nao tem o mesmo tamanho;");


if(len(nome)>len(sobreNome)):
    print("Nome e maior que sobrenome;");

elif(len(nome)<len(sobreNome)):
    print("Nome e menor que sobrenome;");

elif(len(nome)>=len(sobreNome)):
    print("Nome e maior ou igual sobrenome;");

elif(len(nome)<=len(sobreNome)):
    print("Nome e menor ou igual sobrenome;");


    
