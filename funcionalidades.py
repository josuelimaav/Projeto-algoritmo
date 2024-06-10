def validarcampo(texto):
    while True:
        valor = input(texto)
        if valor == '':
            print('\n\033[0;31mCampo obrigatório. Digite novamente!.\033[m\n')
        else:
            return valor



def interface01():
    print('-------------------------------')
    print('| 1- Cadastrar Administrador  |')
    print('| 2- Cadastrar Usuário        |')
    print('| 3- Login                    |')
    print('-------------------------------')


def interface02():
    print('---------------------------')
    print('| 1- Login Administrador  |')
    print('| 2- Login Usuário        |')
    print('---------------------------')



def interface03():
    print('---------------------------------------')
    print('| 1- Adicionar Filmes                 |')
    print('| 2- Buscar Filmes                    |')
    print('| 3- Atualizar Filmes                 |')
    print('| 4- Remover Filmes                   |')
    print('| 5- Atualizar credenciais dos filmes |')
    print('| 6- Exibir estatísticas de compras   |')
    print('| 0- Fazer logoff                     |')
    print('--------------------------------------\n')



def interface04():
    print('-------------------------------------')
    print("| 1- alterar preços dos ingressos   |")
    print("| 2- alterar horários dos filmes    |")
    print("| 3- alterar salas                  |")
    print("| 4- alterar capacidades das salas  |")
    print('-------------------------------------')



def interface05():
    print('--------------------------------------------')
    print('| 1- Total de ingressos vendidos por filme |')
    print('| 2- Total de ingressos vendidos ao todo   |')
    print('| 3- Ver ultimas avaliações dos filmes     |')
    print('| 4- Valor total arrecardado               |')
    print('--------------------------------------------\n')



def interface06():
    print('---------------------------------------')
    print('| 1- Comprar ingressos                |')
    print('| 0- voltar                           |')
    print('---------------------------------------\n')



def interface07():
    print('------------------------------------')
    print('| 1- Ação                          |')
    print('| 2- Comédia                       |')
    print('| 3- Terror                        |')
    print('| 4- Drama                         |')
    print('| 5- Fantasia                      |')
    print('| 0- Fazer logof                   |')
    print('------------------------------------')



def ingressos_vendidos_por_filme(Filme, total):
    with open('projeto.txt', 'a') as file:
        file.write(f'Filme: {Filme}\n')
        file.write(f'Ingressos vendidos: {total}\n')



def ingressos_clientes(cliente, filme, total, valor):
    with open('projeto.txt.txt', 'a') as file:
        file.write(f'Cliente: {cliente}\n')
        file.write(f'Filme: {filme}\n')
        file.write(f'Ingressos comprados: {total}\n')
        file.write(f'Valor total: {valor}\n')



