from time import sleep

a = []
nl, nc = int(input('Insira a quantidade de linhas: ')), int(input('Insira a quantidade de colunas: '))

def menuprincipal():
    escolha = input('\nSua matriz foi gerada. Como deseja lê-la?\nDigite 1 para padrão;\nDigite 2 para negar os elementos acima da diagonal principal;\nDigite 3 para negar os elementos abaixo da diagonal principal;\nDigite 4 para negar os elementos acima da diagonal segundária;\nDigite 5 para negar os elementos abaixo da diagonal segundária;\nDigite 6 para negar o triângulo superior;\nDigite 7 para negar o triângulo direito;\nDigite 8 para negar o triângulo inferior;\nDigite 9 para negar o triângulo esquerdo;\nDigite qualquer coisa para sair.\n')
    match escolha:
        case '1':
            lermatriz(nl, nc)
        case '2':
            if testar(nl, nc):
                principalsup(nl, nc)
            else: menuprincipal()
        case '3':
            if testar(nl, nc):
                principalinf(nl, nc)
            else: menuprincipal()
        case '4':
            if testar(nl, nc):
                segundariasup(nl, nc)
            else: menuprincipal()
        case '5':
            if testar(nl, nc):
                segundariainf(nl, nc)
            else: menuprincipal()
        case '6':
            triangulosup(nl, nc)
        case '7':
            triangulodir(nl, nc)
        case '8':
            trianguloinf(nl, nc)
        case '9':
            trianguloesq(nl, nc)
        case _:
            exit()

def gerarmatriz(nl, nc):
    for l in range(0, nl):
        linha = []
        for c in range(0, nc):
            linha.append(f'a{l}{c}')
        a.append(linha)
    menuprincipal()

def lermatriz(nl, nc):
    print('A matriz lida:\n')
    for l in range(0, nl):
        for c in range(0, nc):
            print(f'a{l}{c}', end=' ')
        print()
    sleep(5)
    menuprincipal()

def principalsup(nl, nc):
    for l in range(0, nl):
        for c in range(0, nc):
            if (c > l):
                print(f' 00', end=' ')
            else:
                print(f'a{l}{c}', end=' ')
        print()
    sleep(5)
    menuprincipal()

def principalinf(nl, nc):
    for l in range(0, nl):
        for c in range(0, nc):
            if (c < l):
                print(f' 00', end=' ')
            else:
                print(f'a{l}{c}', end=' ')
        print()
    sleep(5)
    menuprincipal()

def segundariasup(nl, nc):
    for l in range(0, nl):
        for c in range(0, nc):
            if (l + c < 9):
                print(f' 00', end=' ')
            else:
                print(f'a{l}{c}', end=' ')
        print()
    sleep(5)
    menuprincipal()

def segundariainf(nl, nc):
    for l in range(0, nl):
        for c in range(0, nc):
            if (l + c > 9):
                print(f' 00', end=' ')
            else:
                print(f'a{l}{c}', end=' ')
        print()
    sleep(5)
    menuprincipal()

def triangulosup(nl, nc):
    for l in range(0, nl):
        for c in range(0, nc):
            if (l + c < 9 and c > l):
                print(f'00', end=' ')
            else:
                print(f'{l}{c}', end=' ')
        print()
    sleep(5)
    menuprincipal()

def triangulodir(nl, nc):
    for l in range(0, nl):
        for c in range(0, nc):
            if (l + c > 9 and c > l):
                print(f'00', end=' ')
            else:
                print(f'{l}{c}', end=' ')
        print()
    sleep(5)
    menuprincipal()

def trianguloinf(nl, nc):
    for l in range(0, nl):
        for c in range(0, nc):
            if (l + c > 9 and c < l):
                print(f'00', end=' ')
            else:
                print(f'{l}{c}', end=' ')
        print()
    sleep(5)
    menuprincipal()

def trianguloesq(nl, nc):
    for l in range(0, nl):
        for c in range(0, nc):
            if (l + c < 9 and c < l):
                print(f'00', end=' ')
            else:
                print(f'{l}{c}', end=' ')
        print()
    sleep(5)
    menuprincipal()

def testar(nl, nc):
    if (nl != nc):
        print('Apenas matrizes quadradas têm diagonal!')
        return False
    else:
        return True


gerarmatriz(nl, nc)