def obter_estado(cpf):
    # Mapeamento dos dígitos para os estados
    estados = {
        '0': 'Distrito Federal',
        '1': 'São Paulo',
        '2': 'São Paulo',
        '3': 'Minas Gerais',
        '4': 'Rio de Janeiro',
        '5': 'Espírito Santo',
        '6': 'Bahia',
        '7': 'Sergipe',
        '8': 'São Paulo',
        '9': 'Paraná'
    }
    
    # O dígito que indica o estado é o penúltimo dígito do CPF
    digito_estado = cpf[-2]
    
    # Retorna o estado correspondente ao dígito
    return estados.get(digito_estado, 'Estado desconhecido')

def main():
    # Solicita ao usuário que insira o CPF
    cpf_input = input("Digite o número do CPF (com ou sem pontuação): ")
    
    # Remove caracteres não numéricos
    cpf = ''.join(filter(str.isdigit, cpf_input))
    
    # Verifica se o CPF tem exatamente 11 dígitos
    if len(cpf) != 11:
        print('CPF INVÁLIDO')
        return
    
    # Obtém o estado correspondente ao CPF
    estado = obter_estado(cpf)
    
    # Exibe a mensagem informando de qual estado o usuário é
    print(f'O CPF informado é do estado: {estado}')

# Executa o programa
if __name__ == "__main__":
    main()