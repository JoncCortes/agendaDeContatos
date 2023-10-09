# ====== AGENDA ======

AGENDA = {}


# ====== FUNÇÕES ======

def mostrar_contatos():
    if AGENDA:
        for contato in AGENDA:
            buscar_contato(contato)
            print('________________________________________')
    else:
        print('>>>>>> Agenda Vazia')


def buscar_contato(contato):
    try:
        print(' ')
        print('NOME:', contato)
        print('Telefone:', AGENDA[contato]['telefone'])
        print('Email:', AGENDA[contato]['email'])
        print('Endereço:', AGENDA[contato]['endereco'])
        print(' ')
    except KeyError:
        print('>>>>>> Contato inexistente!')
    except Exception as error:
        print(f'Um erro inesperado ocorreu! ERRO: {error}')


def ler_detalhes_contato():
    telefone = input('Digite o telefone do contato: ')
    email = input('Digite o Email do contato: ')
    endereco = input('Digite o endereço do contato: ')
    return telefone, email, endereco


def incluir_editar_contato(contato, telefone, email, endereco):

    AGENDA[contato] = {
    'telefone': telefone,
    'email': email,
    'endereco': endereco,
    }
    save()
    print(' ')
    print(f'>>>>>> Contato {contato} adicionado/editado com sucesso!')
    print(' ')


def excluir_contato(contato):
    try:
        AGENDA.pop(contato)
        save()
        print(' ')
        print(f'>>>>>> Contato {contato} excluido com sucesso!')
        print(' ')
    except KeyError:
        print('>>>>>> Contato inexistente!')
    except Exception as error:
        print(f'Um erro inesperado ocorreu! ERRO: {error}')


def save():
    exportar_contatos('database.csv')


def load():
    try:
        with open('database.csv', 'r') as file:
            linhas = file.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(',')
                contato = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]

                AGENDA[contato] = {
                'telefone': telefone,
                'email': email,
                'endereco': endereco,
                }
        print('>>>>>> Database carregado com sucesso')
        print(f'{(len(AGENDA))} contatos carregados.')
    except FileNotFoundError:
        print('>>>>>> Arquivo não encontrado')
    except Exception as error:
        print('>>>>>> Algum erro inesperado aconteceu')
        print(error)



def imprimir_menu():
    print('_________________________________________')
    print('[ 1 ] Mostrar todos os contatos')
    print('[ 2 ] Buscar contato')
    print('[ 3 ] Incluir contato')
    print('[ 4 ] Editar contato')
    print('[ 5 ] Excluir contato')
    print('[ 6 ] Exportar CSV')
    print('[ 7 ] Importar contatos CSV')
    print('[ 0 ] Fechar agenda')
    print('_________________________________________')


def exportar_contatos(filename):
    try:
        with open(filename, 'w') as file:
            for contato in AGENDA:
                telefone = AGENDA[contato]['telefone']
                email = AGENDA[contato]['email']
                endereco = AGENDA[contato]['endereco']
                file.write(f'{contato}, {telefone}, {email}, {endereco}\n')
        print('>>>>>> Agenda exportada com sucesso!')
    except Exception as error:
        print('>>>>>> Algum erro ocorreu')
        print(error)


def importar_contatos(filename):
    try:
        with open(filename, 'r') as file:
            linhas = file.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(',')
                contato = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]

                incluir_editar_contato(contato, telefone, email, endereco)
    except FileNotFoundError:
        print('>>>>>> Arquivo não encontrado')
    except Exception as error:
        print('>>>>>> Algum erro inesperado aconteceu')
        print(error)

# ====== INICIO DO PROGRAMA ======

load()
while True:
    imprimir_menu()

    opcao = input('Escolha uma opção: ')
    print('_________________________________________')
    if opcao == '1':
        mostrar_contatos()

    elif opcao == '2':
        contato = input('Digite o nome do contato: ')
        buscar_contato(contato)

    elif opcao == '3':
        contato = input('Digite o nome do contato: ')
        try:
            AGENDA[contato]
            print('>>>>>> Contato já existente')
        except KeyError:
            telefone, email, endereco = ler_detalhes_contato()
            incluir_editar_contato(contato, telefone, email, endereco)

    elif opcao == '4':
        contato = input('Digite o nome do contato: ')
        try:
            AGENDA[contato]
            print('>>>>>> Editando:', contato)
            telefone, email, endereco = ler_detalhes_contato()
            incluir_editar_contato(contato, telefone, email, endereco)
        except KeyError:
            print('>>>>>> Contato inexistente')

    elif opcao == '5':
        contato = input('Digite o nome do contato: ')
        excluir_contato(contato)

    elif opcao == '6':
        filename = input('Digite o nome do arquivo.csv para exportar: ')
        exportar_contatos(filename)

    elif opcao == '7':
        filename = input('Digite o nome do arquivo.CSV para importar: ')
        importar_contatos(filename)

    elif opcao == '0':
        print('>>>>>> Fechando programa')
        break

    else:
        print('>>>>>> Opção invalida')

