def eh_triangulo(lado1, lado2, lado3):
    # Verifica se a soma de dois lados é maior que o terceiro
    return (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1)

def main():
    # Solicita ao usuário que insira os lados do triângulo
    try:
        lado1 = float(input("Digite o comprimento do primeiro lado: "))
        lado2 = float(input("Digite o comprimento do segundo lado: "))
        lado3 = float(input("Digite o comprimento do terceiro lado: "))
        
        # Verifica se os lados formam um triângulo
        if eh_triangulo(lado1, lado2, lado3):
            print(True)
        else:
            print(False)
    except ValueError:
        print("Por favor, insira valores numéricos válidos.")

# Executa o programa
if __name__ == "__main__":
    main()