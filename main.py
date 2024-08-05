#lista de nomes
nomes = []

#inicio do loop
while True:
    #menu
    print('1 - Inserir novo nome.')
    print('2 - Exibir lista de nome.')
    print('3 - Exibir em ordem alfabetica')
    print('4 - Sair do programa.')

    #opcao do usuario
    opcao = input('Opção do usuário: ')

    #verifica opcao escolhida
    match opcao:
        case '1':
            novo_nome = input('Insira um novo nome: ').capitalize()
            nomes.append(novo_nome)  
            print(f'{novo_nome} inserido com sucesso.')
            continue
        case '2':
            print('\nLista de Nomes:')
            for nome in nomes:
                print(nome)
            continue     
        case '3':
            nomes.sort()
            for nome in nomes: 
                print(nome)
            print('Lista ordenada com sucesso.')
            continue
        case '4':
            print('Programa encerrado.')
            break