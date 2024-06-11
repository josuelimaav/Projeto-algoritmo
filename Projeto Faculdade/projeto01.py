
from funcionalidades import validarcampo
from funcionalidades import interface01
from funcionalidades import interface02
from funcionalidades import cadastro_de_adm
from funcionalidades import cadastro_de_usuario
from funcionalidades import pagina_de_usuarios
from funcionalidades import pagina_de_administrador

administradores = {'josue': '123'}
usuarios = {'kevin': '123'}

filmes = [{"categorias": "Ação","filme":"o exterminador do futuro","sinopse":"Disfarçado de humano, o assassino conhecido como o Exterminador viaja de 2029 a 1984 para matar Sarah Connor. Enviado para proteger Sarah está Kyle Reese, que divulga a chegada do Skynet, um sistema de inteligência artificial que detonará um holocausto nuclear. Sarah é o alvo porque a Skynet sabe que seu futuro filho comandará a luta contra eles. Com o implacável Exterminador os perseguindo, Sarah e Kyle tentam sobreviver.","sala": 1,"horário de exibição do filme":"20:00 Hrs","capacidade":25,"valor do ingresso":12,"contador":0, "total ingressos vendidos": 12, 'classificação': 0},
          {"categorias":"Comedia","filme":"aprovados","sinopse":"Após ser recusado por todas as faculdades em que se inscreveu, Bartleby Gaines inventa uma forma de enganar a todos para pensarem que ele vai estudar: abre sua própria universidade. O jovem e seus amigos em situação semelhante tomam um prédio abandonado, criam um site falso, contratam o tio de um amigo para posar como o reitor e, pronto, nasce uma escola.","sala": 2,"horário de exibição do filme":"15:00 Hrs","capacidade":20 ,"valor do ingresso": 10 ,"contador":0, "total ingressos vendidos": 0, 'classificação': 0},
          {"categorias":"Terror","filme":"jogos mortais - O Final","sinopse":"Sobreviventes se reúnem devido aos traumas adquiridos. Entre eles, o psicólogo que controla o encontro e não é uma vítima como as outras, mas tem segredos que podem reiniciar os ataques do psicopata.","sala":"3","horário de exibição do filme":"21:00 Hrs","capacidade":30 ,"valor do ingresso":16,"contador":0, "total ingressos vendidos": 0, 'classificaçao': 0},
          {"categorias":"Drama","filme":"milagre na cela 7","sinopse":"Memo, um pastor de ovelhas com deficiência mental, vive com sua filha e avó em uma vila na costa turca do mar Egeu. Um dia, sua vida é virada de cabeça para baixo quando a filha do comandante morre e Memo é acusado do assassinato e condenado à morte.","sala": 4,"horário de exibição do filme":"16:00 Hrs","capacidade":25 ,"valor do ingresso":12 ,"contador":0, "total ingressos vendidos": 0, 'classificação': 0},
          {"categorias":"Fantasia","filme":"Eu sou a lenda","sinopse":"Robert Neville é um brilhante cientista e o único sobrevivente de uma epidemia que transformou os humanos em mutantes sedentos por sangue. Andando pela cidade de Nova York, ele procura por outros possíveis sobreviventes e tenta achar a cura da praga usando seu próprio sangue, que é imune.","sala": 5,"horário de exibição do filme":"22:00 Hrs","capacidade": 30,"valor do ingresso": 20 ,"contador":0, "total ingressos vendidos": 0, 'classificação': 0}]
usuario = ""
ingressos_comprados = []
valor_arrecardado = []
classificacoes = {}
ingressos_por_filme = []
arquivo01 =[]
lista_ingressos = []



while True:
    print('\n\033[7m=-=-=-=-=-=-= CINE Sertão =-=-=-=-=-=-=\033[m\n')
    print('\033[1;34m__--__ Menu inicial __--__\033[m')
    interface01()

    opcao = int(validarcampo('Selecione uma opção: '))


    if opcao == 1:
        cadastro_de_adm(administradores)


    elif opcao == 2:
        cadastro_de_usuario(usuarios)



    elif opcao == 3:
        print('\n\033[1;34m__--__ Login __--__\033[m')
        interface02()

        opcao02 = int(validarcampo('Selecione uma opção: '))


        if opcao02 == 1:
            print('\nFaça login para prosseguir para página de Administrador...')
            admin2 = validarcampo('Admin: ')
            senha_admin = validarcampo('Senha: ')

            if admin2 in administradores:
                if administradores[admin2] == senha_admin:
                    print('\n\033[0;32mLogin feito com sucesso!\033[m\n')
                    pagina_de_administrador(filmes, ingressos_comprados, lista_ingressos, valor_arrecardado)



                else:
                    print("\n\033[0;31mSenha incorreta!\033[m\n")
            else:
                print("\n\033[0;31mAdministrador não existe!\033[m\n")

        elif opcao02 == 2:
            print('\nFaça login para prosseguir para página de Usuário...')
            usuario2 = validarcampo('Usuário: ')
            senha_usuario = validarcampo('Senha: ')

            if usuario2 in usuarios:
                if usuarios[usuario2] == senha_usuario:
                    print('\n\033[0;32mLogin feito com sucesso!\033[m\n')
                    pagina_de_usuarios(filmes, usuario2, ingressos_comprados, valor_arrecardado, lista_ingressos,arquivo01)

                else:
                    print("\n\033[0;31mSenha incorreta!\033[m\n")
            else:
                print("\n\033[0;31mUsuário não existe!\033[m\n")


