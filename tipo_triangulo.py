def eh_triangulo(lado1, lado2, lado3):
    # Verifica se os lados formam um triângulo válido
    return (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1)

def tipo_triangulo(lado1, lado2, lado3):
    # Classifica o tipo de triângulo
    if lado1 == lado2 == lado3:
        return "Triângulo equilátero (todos os lados são iguais)"
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        return "Triângulo isósceles (dois lados são iguais)"
    else:
        return "Triângulo escaleno (todos os lados são diferentes)"

def main():
    try:
        # Solicita ao usuário que insira os lados do triângulo
        lado1 = float(input("Digite o comprimento do primeiro lado: "))
        lado2 = float(input("Digite o comprimento do segundo lado: "))
        lado3 = float(input("Digite o comprimento do terceiro lado: "))
        
        # Verifica se os lados formam um triângulo
        if eh_triangulo(lado1, lado2, lado3):
            # Se formam um triângulo, determina o tipo
            resultado = tipo_triangulo(lado1, lado2, lado3)
            print(resultado)
        else:
            print("Os valores informados não formam um triângulo válido.")
    except ValueError:
        print("Por favor, insira valores numéricos válidos.")

# Executa o programa
if __name__ == "__main__":
    main()