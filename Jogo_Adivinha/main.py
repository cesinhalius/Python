from random import randint

seuNome = input('Olá qual eh o seu nome? ')
print(
    f'Okay! {seuNome}, eu estou escolhendo um numero. voce consegue adivinhar?'
)

numero_adivinhado = randint(1,20)
numeros_tentativas = 10


for tentativas in range(1,numeros_tentativas + 1):
    numeroEscolhido = int(input('Escolha um numero:'))
    if numeroEscolhido == numero_adivinhado:
        print(
            f'Voce acertou em {tentativas} tentativas. O numero eh {numero_adivinhado}'
        )
        break
    elif numeroEscolhido > numero_adivinhado:
        print('Escolha numero menor')
    else:
        print('Escolha numero maior')

print(f'O numero era {numero_adivinhado}. Obrigado por jogar')