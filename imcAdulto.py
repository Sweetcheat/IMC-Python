while True:
    try: 
       nome = input('Por favor, insira seu nome: ')
       if not nome.isalpha():
        raise ValueError("Nome deve conter somente letras.")
       break
    except ValueError as e:
        print(f'Erro:{e}')   

while True: 
    try:
       altura = float(input ("Informe sua altura. ex: 1.75: "))
       if 0.54 <= altura <= 2.25:
        break
       else:
        print ("Altura tem que ser entre 0.54cm e 2.25m.")
    except ValueError:
        print ("Por favor, insira somente números.")   

while True: 
    try:
       peso = float(input ("Informe seu peso em kg: "))
       if 20 <= peso <= 727:
        break
       else:
         print ("Peso tem que ser entre 20kg e 727kg.")
    except ValueError:
        print ("Por favor, insira somente números.")  

imc = peso / altura **2 

if imc < 18.5:
    classificacao = "Abaixo do peso"
elif 18.5 <= imc < 24.9:
    classificacao = "Peso normal"
elif 25 <= imc < 29.9:
    classificacao = "Sobrepeso"
elif 30 <= imc < 34.9:
    classificacao = "Obesidade grau 1"
elif 35 <= imc < 39.9:
    classificacao = "Obesidade grau 2"
else:
    classificacao = "Obesidade grau 3"

print(f"{nome}, seu IMC é: {imc:.2f}")
print(f"Classificação: {classificacao}")
input("Pressione qualquer tecla para fechar o programa...")