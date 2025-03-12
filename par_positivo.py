def eh_par_e_positivo(numero):
    # Verifica se o número é par e positivo
    return numero > 0 and numero % 2 == 0

def main():
    try:
        # Solicita ao usuário que insira um número
        numero = float(input("Digite um número: "))
        
        # Verifica se o número é par e positivo
        if eh_par_e_positivo(numero):
            print(True)
        else:
            print(False)
    except ValueError:
        print("Por favor, insira um número válido.")

# Executa o programa
if __name__ == "__main__":
    main()