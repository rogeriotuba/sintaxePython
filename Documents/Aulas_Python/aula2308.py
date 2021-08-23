
num1 = int(input("Digite numero 1:   "));
num2 = int(input("Digite numero 2:   "));


print("1-soma\n2-Subtracao\n3-Multiplicacao\n4-Divisao");
operacao = int(input("Digite a operacao a ser utilizada:  "));

if(operacao==1):
    soma = num1 + num2;
    print(soma);
elif(operacao==2):
    subrtracao = num1 - num2;
    print(subrtracao);
elif(operacao==3):
    multiplicacao= num1 * num2;
    print(multiplicacao);
elif(operacao==4):
    divisao = num1 / num2;
    print(divisao);
    