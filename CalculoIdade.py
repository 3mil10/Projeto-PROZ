import datetime

def obter_ano_nascimento():
    while True:
        try:
            ano_nascimento = int(input("Digite o ano de nascimento (1922-2021): "))
            if 1922 <= ano_nascimento <= 2021:
                return ano_nascimento
            else:
                print("Ano fora do intervalo permitido. Tente novamente.")
        except ValueError:
            print("Por favor, digite um número válido.")

def main():
    nome_completo = input("Digite seu nome completo: ")

    while True:
        try:
            ano_nascimento = obter_ano_nascimento()
            break
        except KeyboardInterrupt:
            print("\nPrograma encerrado pelo usuário.")
            return
        except Exception as e:
            print(f"Erro: {e}")

    try:
        ano_atual = datetime.datetime.now().year
        idade = ano_atual - ano_nascimento

        print(f"\nNome: {nome_completo}")
        print(f"Idade em 2022: {idade} anos")
    except KeyboardInterrupt:
        print("\nPrograma encerrado pelo usuário.")

if __name__ == "__main__":
    main()
