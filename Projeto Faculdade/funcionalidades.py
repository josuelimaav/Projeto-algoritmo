def validarcampo(texto):
    while True:
        valor = input(texto)
        if valor == '':
            print('\n\033[0;31mCampo obrigatório. Digite novamente!.\033[m\n')
        else:
            return valor




def cadastro_de_adm(lista):

    print('\n=-=-=-=-=-= Cadastro de Administrador =-=-=-=-=-=\n')

    while True:
        admin = validarcampo('Admin: ')

        if admin in lista:
            print('\n\033[0;31mEste Administrador já existe!\033[m\n')
        else:
            email = validarcampo('E-mail: ')

            if '@' not in email or '.com' not in email:
                print('\n\033[0;31mE-mail inválido!\033[m\n')
            else:
                print('\n\033[0;32mE-mail verificado com sucesso!\033[m\n')
                while True:
                    senha = validarcampo('Senha: ')
                    confirmarsenha = validarcampo('Confirmar senha: ')

                    if senha == confirmarsenha:
                        print('\n\033[0;32mCadastro feito com sucesso!\033[m\n')
                        lista[admin] = confirmarsenha
                        return  # Usamos return para sair da função após o cadastro bem-sucedido
                    else:
                        print('\n\033[0;31mAs senhas não coincidem, tente novamente!\033[m\n')




def cadastro_de_usuario(lista):
    print('\n=-=-=-=-=-= Cadastro de Usuário =-=-=-=-=-=\n')
    while True:
        usuario = validarcampo('Usuário: ')

        if usuario in lista:
            print('\n\033[0;31mEste Usuário ja existe!\033[m\n')

        else:
            email = validarcampo('E-mail: ')

            if '@' not in email and '.com' not in email:
                print('\n\033[0;31mE-mail inválido!\033[m\n')

            else:
                print('\n\033[0;32mE-mail verificado com sucesso!\033[m\n')
                while True:
                    senha = validarcampo('Senha: ')
                    confirmarsenha = validarcampo('confirmar senha: ')

                    if senha == confirmarsenha:
                        print('\n\033[0;32mCadastro feito com sucesso!\033[m\n')
                        lista[usuario] = confirmarsenha
                        break
                    else:
                        print('\n\033[0;31mAs senhas não coinincidem, tente novamente!\033[m\n')

        break





def pagina_de_administrador(filmes, ingressos_comprados, lista_ingressos, valor_arrecardado):
    while True:
        print('\033[1;34m__--__ Administração do Cinema __--__\033[m')
        interface03()

        opcao3 = int(validarcampo('Digite uma opção: '))

        if opcao3 == 1:
            print('\n\033[1;34m__--__ Cadastrar Filme __--__\033[m')
            categoriadofilme = validarcampo('Digite a categoria que deseja adicionar o filme: ')
            categoria_encontrada = False

            for elemento in filmes:
                if elemento['categorias'] == categoriadofilme:
                    categoria_encontrada = True
                    adicionar_filme = validarcampo("\nDigite o nome do filme: ")
                    if adicionar_filme not in elemento.get('filme', []):
                        sinopse = validarcampo('\nDigite a sinopse do filme: ')
                        sala = int(validarcampo("\ndigite a sala do filme: "))

                        if 0 < sala <= 5:
                            horario = int(validarcampo("\ndigite o horario de exibição do filme: "))
                            if horario >= 0 and horario < 24:
                                valor = float(validarcampo("\ndigite o valor do ingresso: "))

                                if valor > 0:
                                    capacidade = int(validarcampo("\ndigite a capacidade da sala: "))

                                    if capacidade > 0:
                                        dicionario = {
                                            "filme": adicionar_filme, "sinopse": sinopse,
                                            "categorias": categoriadofilme,
                                            "sala": sala, "horário de exibição do filme": horario,
                                            "valor do ingresso": valor,
                                            "capacidade": capacidade, "contador": 0}

                                        print('\n\033[0;32mFilme adicionado com sucesso\033[m')
                                        print('_________________________')
                                        print(f': Filme: {adicionar_filme}')
                                        print(f': Categoria: {categoriadofilme}')
                                        print(f': Sinopse: {sinopse}')
                                        print(f': Sala: {sala}')
                                        print(f': Horário: {horario}H')
                                        print(f': Valor: {valor}')
                                        print(f': Capacidade: {capacidade}')
                                        print('_________________________')

                                        filmes.append(dicionario.copy())
                                        print('\n\033[0;32mFilme adicionado com sucesso\033[m\n')
                                    else:
                                        print('\033[0;31mCapacidade indisponível\033[m\n')
                                else:
                                    print('\033[0;31mValor inválido\033[m\n')
                            else:
                                print('\033[0;31mHorário indisponível\033[m\n')
                        else:
                            print('\033[0;31mSala indisponível, salas disponíveis = 5\033[m\n')
                        break
                    else:
                        print('\033[0;31mFilme já existe, digite outro título!\033[m\n')
                        break

            if not categoria_encontrada:
                print('\033[0;31mCategoria indisponível!\033[m\n')


        elif opcao3 == 2:
            print('\033[1;34m__--__ Buscar Filme __--__\033[m')
            buscar_filmes = validarcampo('\nDigite o filme que deseja buscar: ')

            achou = False
            for elemento in filmes:
                if elemento["filme"] == buscar_filmes:
                    achou = True
                    print("\033[0;32mfilme encontrado com sucesso\033[m")
                    print(f'O filme {buscar_filmes} está disponível em Cartaz!\n')
                    print('=================================================')
                    print(f'Filme: {elemento['filme']}')
                    print(f'Categoria: {elemento['categorias']}')
                    print(f'Sala: {elemento['sala']}')
                    print('=================================================')

            if not achou:
                print('\033[0;31mFilme indisponível!\033[m\n')

            if achou == False:
                print('\033[0;31mFilme não encontrado, por favor digite outro título!!\033[m\n')

        elif opcao3 == 3:
            print('\033[1;34m__--__ Atualizar Filme __--__\033[m')
            atualizar_filme = validarcampo('Digite o nome do filme que deseja atualizar: ')
            encontrou = False
            for elemento in filmes:
                if elemento['filme'] == atualizar_filme:
                    encontrou = True
                    atualizar = validarcampo('Digite o nome do novo filme: ')
                    elemento['filme'] = atualizar
                    print('\033[0;32mfilme Atualizado com sucesso\033[m\n')
                    atualizarsinopse = validarcampo("digite a nova sinopse: ")
                    elemento["sinopse"] = atualizarsinopse
                    print("\033[0;32mSinopse Atualizada com sucesso\033[m\n")

        elif opcao3 == 4:
            print('\033[1;34m__--__ Deletar Filme __--__\033[m')
            deletar_filme = input('\nDigite o nome do filme que deseja Deletar: ')

            achou2 = False
            for elemento in filmes:
                if elemento["filme"] == deletar_filme:
                    achou2 = True
                    filmes.remove(elemento)
                    print('\n\033[0;32mFilme removido com sucesso!\033[m\n')
            if achou2 == False:
                print('\n\033[0;31mO filme digitado não existe\033[m\n')

        elif opcao3 == 5:
            print('\033[1;34m__--__ Atualizar Credenciais __--__\033[m')
            alterar1 = validarcampo("\nDigite o nome do filme: \n")
            achou = False
            for elemento in filmes:
                if alterar1 == elemento["filme"]:
                    achou = True
                    interface04()

                    alterar = int(validarcampo("\nDigite uma opção: \n"))

                    if alterar == 1:
                        novopreco = float(validarcampo("digite o novo preço do ingresso: "))
                        if novopreco > 0:
                            elemento['valor do ingresso'] = novopreco
                            print('\n\033[0;32mPreço alterado com sucesso!\033[m\n')
                        else:
                            print('\n\033[0;31mValor inválido\033[m\n')

                    elif alterar == 2:
                        novohorario = int(validarcampo("digite o novo horário: "))
                        if novohorario <= 0 and novohorario <= 24:
                            elemento["horário de exibição do filme"] = novohorario
                            print("\n\033[0;32mHorário alterado com sucesso!\033[m\n")
                        else:
                            print('\n\033[0;31mHorário inválido\033[m\n')

                    elif alterar == 3:
                        print('ººººººººººººººººººººº°ººººº')
                        print('º                         º')
                        print('º  Salas Disponíveis = 5  º')
                        print('º                         º')
                        print('ººººººººººººººººººººººººººº\n')
                        novasala = int(validarcampo("digite o novo numero da sala: "))
                        if novasala > 0 and novasala <= 5:
                            elemento['sala'] = novasala
                            print("\n\033[0;32mSala alterada com sucesso!\033[m\n")
                        else:
                            print('\n\033[0;31mSala inválida\033[m\n')

                    elif alterar == 4:
                        novacapacidade = int(validarcampo("digite a nova capacidade da sala: "))
                        if novacapacidade > 0:
                            elemento["capacidade"] = novacapacidade
                            print("\n\033[0;32mCapacidade alterada com sucesso!\033[m\n")
                        else:
                            print('\n\033[0;31mCapacidade inválido\033[m\n')

                    else:
                        print("\n\033[0;31mOpção inválida!\033[m\n")

            if (achou == False):
                print("\n\033[0;31mO filme digitado não existe\033[m\n")

        elif opcao3 == 6:
            print('\033[1;34m__--__ Estatíticas dos Filmes __--__\033[m')
            interface05()
            opcao4 = int(validarcampo('Digite uma opção: '))

            if opcao4 == 1:
                for i in lista_ingressos:
                    print('------------------------------------------------------')
                    print('| Ingressos comprados por filme:')
                    print(f'| {i}                ')
                    print('----------------------------------------------------\n')

            elif opcao4 == 2:
                print('\n\033[1;34m__--__ Total de ingressos vendidos __--__\033[m')
                soma_total = sum(ingressos_comprados)
                print('°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°')
                print(f'-> Foram vendidos {soma_total} Ingressos ao todo')
                print('°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°')

            elif opcao4 == 3:
                procurar_filme = validarcampo('Digite o filme que deseja concultar Avaliações: ')
                filme_encontrada01 = False

                for elemento in filmes:
                    if elemento['filme'] == procurar_filme:
                        filme_encontrada01 = True
                        print('\n\033[1;34m__--__ Ultimas avaliações __--__\033[m')
                        print(
                            '°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°')
                        print(
                            f'-> A última classificação Para o filme {elemento['filme']}, foi {elemento["classificação"]} estrelas')
                        print(
                            '°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°\n')

                if not filme_encontrada01:
                    print("\n\033[0;31mFilme não encontrado!\033[m\n")
            elif opcao4 == 4:
                valor_total = sum(valor_arrecardado)
                print('\n\033[1;34m__--__ Valor total arrecardado __--__\033[m')
                print('°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°')
                print(f'-> O valor total arrecardado foi de {valor_total} R$')
                print('°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°\n')

        elif opcao3 == 0:
            break
        else:
            print("\n\033[0;31mOpção inválida!\033[m\n")





def pagina_de_usuarios(filmes, usuario2, ingressos_comprados, valor_arrecardado, lista_ingressos, arquivo01):
    import emoji
    while True:
        print('\033[1;34m__--__ Página Usuários __--__\033[m')
        interface06()
        opcao003 = int(validarcampo('Digite uma opção: '))

        if opcao003 == 1:
            interface07()
            opcao = int(validarcampo('\nSelecione uma categoria: '))
            if opcao == 1:
                print('\n\033[1;34m__--__ Ação __--__\033[m')
                print('Filmes disponíveis:\n')
                for elemento in filmes:
                    if elemento["categorias"] == "Ação":
                        print('______________________________________________________________')
                        print("| filme: ", elemento["filme"], )
                        print("| sinopse: ", elemento["sinopse"], )
                        print("| sala : ", elemento["sala"], )
                        print("| horário de exibição do filme :",
                              elemento["horário de exibição do filme"], )
                        print("| capacidade :", elemento["capacidade"], "pessoas")
                        print("| valor do ingresso :", elemento["valor do ingresso"], "R$")
                        print('______________________________________________________________')
                        print("deseja comprar o ingresso para assistir esse filme:")
                        ingresso = int(input("1: Sim\n2: Não(Exibir próximo filme disponível) "))

                        if (ingresso == 1):
                            total = int(
                                validarcampo("Digite o total de ingressos você deseja comprar: "))

                            if total + elemento["contador"] <= elemento["capacidade"] and total + \
                                    elemento["contador"] > 0:
                                ingressos_comprados.append(total)
                                elemento["total ingressos vendidos"] = total
                                elemento["capacidade"] -= total
                                print(f'A capacidade atual da sala é de: {elemento['capacidade']}')
                                elemento["contador"] += total
                                preco_total = total * elemento["valor do ingresso"]
                                valor_arrecardado.append(preco_total)
                                print("\033[0;32mingresso comprado com sucesso\033[m\n")

                                print(
                                    '-------------------------------------------  Cine Sertão  ------------------------------------')
                                print('\nsala : ', elemento["sala"],
                                      '                ========== Ticket de compra ========       cliente :', usuario2)
                                print('horário de exibição do filme : ', elemento["horário de exibição do filme"],
                                      '        Filme escolhido:', elemento["filme"])
                                print("quantidade de ingresso (s):", total,
                                      "                                  valor da compra:", preco_total, "R$")
                                print(
                                    '\n--------------------------------------Desejamos um ótimo filme!-------------------------------\n')

                                ingressos_vendidos_por_filme(elemento['filme'], total)
                                ingressos_clientes(usuario2, elemento['filme'], total, preco_total)

                                lista_ingresso = {"Filme": elemento['filme'], "Total ingresso": total}
                                lista_ingressos.append(lista_ingresso.copy())

                                classificacao = int(
                                    validarcampo('Classifique o filme de 1 a 5 estrelas:'))
                                if classificacao > 0 and classificacao <= 5:
                                    cla = emoji.emojize(':star:') * classificacao
                                    print(f'\033[0;32mFilme classificado com {cla} estrelas!\033[m\n')
                                    elemento['classificação'] = cla
                                else:
                                    print('\033[0;31mClassificação inválida!\033[m\n')

                            else:
                                print("\033[0;31mquantidade de ingressos indisponivel\033[m\n")
                                print('\nPróximo filme disponível:\n')

                        elif (ingresso == 2):
                            print('\033[0;31mCompra cancelada\033[m\n')
                        else:
                            print("\n\033[0;31mOpção inválida!\033[m\n")

            elif opcao == 2:
                print('\n\033[1;34m__--__ Comédia __--__\033[m')
                print('Filmes disponíveis:\n')
                for elemento in filmes:
                    if elemento["categorias"] == "Comedia":
                        print('______________________________________________________________')
                        print("| filme: ", elemento["filme"], )
                        print("| sinopse: ", elemento["sinopse"], )
                        print("| sala : ", elemento["sala"], )
                        print("| horário de exibição do filme :",
                              elemento["horário de exibição do filme"], )
                        print("| capacidade :", elemento["capacidade"], "pessoas")
                        print("| valor do ingresso :", elemento["valor do ingresso"], "R$")
                        print('______________________________________________________________')
                        print("deseja comprar o ingresso para assistir esse filme:")
                        ingresso = int(input("1: Sim\n2: Não(Exibir próximo filme disponível) "))

                        if (ingresso == 1):
                            total = int(input("Digite o total de ingressos você deseja comprar: "))
                            if total + elemento["contador"] <= elemento["capacidade"] and total + \
                                    elemento["contador"] > 0:
                                elemento["total ingressos vendidos"] = total
                                elemento["capacidade"] -= total
                                print(f'A capacidade atual da sala é de: {elemento['capacidade']}')
                                elemento["contador"] += total
                                preco_total = total * elemento["valor do ingresso"]
                                valor_arrecardado.append(preco_total)
                                ingressos_comprados.append(total)
                                print("\033[0;32mingresso comprado com sucesso\033[m")

                                lista_ingresso = {"Filme": elemento['filme'], "Total ingresso": total}
                                lista_ingressos.append(lista_ingresso.copy())

                                print(
                                    '-------------------------------------------  Cine Sertão  ------------------------------------')
                                print('\nsala : ', elemento["sala"],
                                      '                ========== Ticket de compra ========       cliente :', usuario2)
                                print('horário de exibição do filme : ', elemento["horário de exibição do filme"],
                                      '        Filme escolhido:', elemento["filme"])
                                print("quantidade de ingresso (s):", total,
                                      "                                  valor da compra:", preco_total, "R$")
                                print(
                                    '\n--------------------------------------Desejamos um ótimo filme!-------------------------------')
                                ingressos_vendidos_por_filme(elemento['filme'], total)
                                ingressos_clientes(usuario2, elemento['filme'], total, preco_total)

                                classificacao = int(
                                    validarcampo('Classifique o filme de 1 a 5 estrelas:'))
                                if classificacao > 0 and classificacao <= 5:
                                    cla = emoji.emojize(':star:') * classificacao
                                    print(f'\033[0;32mFilme classificado com {cla} estrelas!\033[m\n')
                                    elemento['classificação'] = cla
                                else:
                                    print('\033[0;31mClassificação inválida!\033[m\n')

                            else:
                                print("\033[0;31mquantidade de ingressos indisponivel\033[m\n")

                        elif (ingresso == 2):
                            print('\033[0;31mCompra cancelada\033[m\n')

                        else:
                            print("\n\033[0;31mOpção inválida!\033[m\n")

            elif opcao == 3:
                print('\n\033[1;34m__--__ Terror __--__\033[m')
                print('Filmes disponíveis:\n')
                for elemento in filmes:
                    if elemento["categorias"] == "Terror":
                        print('______________________________________________________________')
                        print("| filme: ", elemento["filme"], )
                        print("| sinopse: ", elemento["sinopse"], )
                        print("| sala : ", elemento["sala"], )
                        print("| horário de exibição do filme :",
                              elemento["horário de exibição do filme"], )
                        print("| capacidade :", elemento["capacidade"], "pessoas")
                        print("| valor do ingresso :", elemento["valor do ingresso"], "R$")
                        print('______________________________________________________________')
                        print("deseja comprar o ingresso para assistir esse filme:")
                        ingresso = int(input("1: Sim\n2: Não(Exibir próximo filme disponível) "))
                        if (ingresso == 1):
                            total = int(
                                validarcampo("Digite o total de ingressos você deseja comprar: "))
                            elemento["capacidade"] -= total
                            print(f'A capacidade atual da sala é de: {elemento['capacidade']}')
                            if total + elemento["contador"] <= elemento["capacidade"] and total + \
                                    elemento["contador"] > 0:
                                elemento["total ingressos vendidos"] = total
                                elemento["contador"] += total
                                preco_total = total * elemento["valor do ingresso"]
                                valor_arrecardado.append(preco_total)
                                ingressos_comprados.append(total)
                                print("\033[0;32mingresso comprado com sucesso\033[m\n")

                                lista_ingresso = {"Filme": elemento['filme'], "Total ingresso": total}
                                lista_ingressos.append(lista_ingresso.copy())

                                print(
                                    '-------------------------------------------  Cine Sertão  ------------------------------------')
                                print('\nsala : ', elemento["sala"],
                                      '                ========== Ticket de compra ========       cliente :', usuario2)
                                print('horário de exibição do filme : ', elemento["horário de exibição do filme"],
                                      '        Filme escolhido:', elemento["filme"])
                                print("quantidade de ingresso (s):", total,
                                      "                                  valor da compra:", preco_total, "R$")
                                print(
                                    '\n--------------------------------------Desejamos um ótimo filme!-------------------------------')
                                ingressos_vendidos_por_filme(elemento['filme'], total)
                                ingressos_clientes(usuario2, elemento['filme'], total, preco_total)

                                classificacao = int(
                                    validarcampo('Classifique o filme de 1 a 5 estrelas:'))
                                if classificacao > 0 and classificacao <= 5:
                                    cla = emoji.emojize(':star:') * classificacao
                                    print(f'\033[0;32mFilme classificado com {cla} estrelas!\033[m\n')
                                    elemento['classificação'] = cla
                                else:
                                    print('\033[0;31mClassificação inválida!\033[m\n')

                            else:
                                print("\033[0;31mquantidade de ingressos indisponivel\033[m\n")

                        elif (ingresso == 2):
                            print('\033[0;31mCompra cancelada\033[m\n')

                        else:
                            print("\n\033[0;31mOpção inválida!\033[m\n")

            elif opcao == 4:
                print('\n\033[1;34m__--__ Drama __--__\033[m')
                print('Filmes disponíveis:\n')
                for elemento in filmes:
                    if elemento["categorias"] == "Drama":
                        print('______________________________________________________________')
                        print("| filme: ", elemento["filme"], )
                        print("| sinopse: ", elemento["sinopse"], )
                        print("| sala : ", elemento["sala"], )
                        print("| horário de exibição do filme :",
                              elemento["horário de exibição do filme"], )
                        print("| capacidade :", elemento["capacidade"], "pessoas")
                        print("| valor do ingresso :", elemento["valor do ingresso"], "R$")
                        print('______________________________________________________________')
                        print("deseja comprar o ingresso para assistir esse filme:")
                        ingresso = int(validarcampo("1: Sim\n2: Não(Exibir próximo filme disponível) "))
                        if (ingresso == 1):
                            total = int(
                                validarcampo("Digite o total de ingressos você deseja comprar: "))
                            if total + elemento["contador"] <= elemento["capacidade"] and total + \
                                    elemento["contador"] > 0:
                                elemento["total ingressos vendidos"] = total
                                elemento["capacidade"] -= total
                                print(f'A capacidade atual da sala é de: {elemento['capacidade']}')
                                elemento["contador"] += total
                                preco_total = total * elemento["valor do ingresso"]
                                valor_arrecardado.append(preco_total)
                                ingressos_comprados.append(total)
                                print("\033[0;32mingresso comprado com sucesso\033[m\n")

                                lista_ingresso = {"Filme": elemento['filme'], "Total ingresso": total}
                                lista_ingressos.append(lista_ingresso.copy())

                                print(
                                    '-------------------------------------------  Cine Sertão  ------------------------------------')
                                print('\nsala : ', elemento["sala"],
                                      '                ========== Ticket de compra ========       cliente :', usuario2)
                                print('horário de exibição do filme : ', elemento["horário de exibição do filme"],
                                      '        Filme escolhido:', elemento["filme"])
                                print("quantidade de ingresso (s):", total,
                                      "                                  valor da compra:", preco_total, "R$")
                                print(
                                    '\n--------------------------------------Desejamos um ótimo filme!-------------------------------')
                                ingressos_vendidos_por_filme(elemento['filme'], total)
                                ingressos_clientes(usuario2, elemento['filme'], total, preco_total)

                                classificacao = int(
                                    validarcampo('Classifique o filme de 1 a 5 estrelas:'))
                                if classificacao > 0 and classificacao <= 5:
                                    cla = emoji.emojize(':star:') * classificacao
                                    print(f'\033[0;32mFilme classificado com {cla} estrelas!\033[m\n')
                                    elemento['classificação'] = cla
                                else:
                                    print('\033[0;31mClassificação inválida!\033[m\n')

                            else:
                                print("\033[0;31mquantidade de ingressos indisponivel\033[m\n")

                        elif (ingresso == 2):
                            print('\033[0;31mCompra cancelada\033[m\n')

                        else:
                            print("\n\033[0;31mOpção inválida!\033[m\n")

            elif opcao == 5:
                print('\n\033[1;34m__--__ Fantasia __--__\033[m')
                print('Filmes disponíveis:\n')
                for elemento in filmes:
                    if elemento["categorias"] == "Fantasia":
                        print('______________________________________________________________')
                        print("| filme: ", elemento["filme"], )
                        print("| sinopse: ", elemento["sinopse"], )
                        print("| sala : ", elemento["sala"], )
                        print("| horário de exibição do filme :",
                              elemento["horário de exibição do filme"], )
                        print("| capacidade :", elemento["capacidade"], "pessoas")
                        print("| valor do ingresso :", elemento["valor do ingresso"], "R$")
                        print('______________________________________________________________')
                        print("deseja comprar o ingresso para assistir esse filme:")
                        ingresso = int(validarcampo("1: Sim\n2: Não(Exibir próximo filme disponível) "))
                        if (ingresso == 1):
                            total = int(
                                validarcampo("Digite o total de ingressos você deseja comprar: "))
                            if total + elemento["contador"] <= elemento["capacidade"] and total + \
                                    elemento["contador"] > 0:
                                elemento["total ingressos vendidos"] = total
                                elemento["capacidade"] -= total
                                print(f'A capacidade atual da sala é de: {elemento['capacidade']}')
                                elemento["contador"] += total
                                preco_total = total * elemento["valor do ingresso"]
                                valor_arrecardado.append(preco_total)
                                ingressos_comprados.append(total)
                                print("\033[0;32mingresso comprado com sucesso\033[m\n")

                                lista_ingresso = {"Filme": elemento['filme'], "Total ingresso": total}
                                lista_ingressos.append(lista_ingresso.copy())

                                print(
                                    '-------------------------------------------  Cine Sertão  ------------------------------------')
                                print('\nsala : ', elemento["sala"],
                                      '                ========== Ticket de compra ========       cliente :', usuario2)
                                print('horário de exibição do filme : ', elemento["horário de exibição do filme"],
                                      '        Filme escolhido:', elemento["filme"])
                                print("quantidade de ingresso (s):", total,
                                      "                                  valor da compra:", preco_total, "R$")
                                print(
                                    '\n--------------------------------------Desejamos um ótimo filme!-------------------------------')
                                ingressos_vendidos_por_filme(elemento['filme'], total)
                                ingressos_clientes(usuario2, elemento['filme'], total, preco_total)

                                classificacao = int(
                                    validarcampo('Classifique o filme de 1 a 5 estrelas:'))
                                if classificacao > 0 and classificacao <= 5:
                                    cla = emoji.emojize(':star:') * classificacao
                                    print(f'\033[0;32mFilme classificado com {cla} estrelas!\033[m\n')
                                    elemento['classificação'] = cla
                                else:
                                    print('\033[0;31mClassificação inválida!\033[m\n')

                            else:
                                print("\033[0;31mquantidade de ingressos indisponivel\033[m\n")

                        elif (ingresso == 2):
                            print('\033[0;31mCompra cancelada\033[m\n')

                        else:
                            print("\n\033[0;31mOpção inválida!\033[m\n")

            elif opcao == 0:
                break

            else:
                print("\n\033[0;31mOpção inválida!\033[m\n")

        elif opcao003 == 2:
            print('\n\033[1;34m__--__ Lista de ingressos __--__\033[m')
            print('-> Sua lista de ingressos:\n')
            for i in arquivo01:
                print(i)

        elif opcao003 == 0:
            break

        else:
            print("\n\033[0;31mOpção inválida!\033[m\n")



def verificar_login_usuario(lista, usuario, senha, login):
    if usuario in lista:
        if lista[usuario] == senha:
            print('\n\033[0;32mLogin feito com sucesso!\033[m\n')

        else:
            print("\n\033[0;31mSenha incorreta!\033[m\n")
    else:
        print("\n\033[0;31mUsuário não existe!\033[m\n")

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



