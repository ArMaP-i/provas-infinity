number = 7
guesses = 0
while guesses < 3:
    guess = int(input('adivinhe o numero!'))
    if guess != number and guesses < 2:
        guesses += 1
        print('tente novamente')
        continue
    elif guess != number and guesses == 2:
        print('tudo bem!! tente de novo :]')
        break
    else: 
        print('parabens!')
        break
