import random

print('H A N G M A N')
run_flg = input('Type "play" to play the game, "exit" to quit: ')
while run_flg == 'play':
    answers = ['java', 'python', 'kotlin', 'javascript']
    word = list(random.choice(answers))
    guesses = ''
    turns = 8
    hint = ['-'] * len(word)
    while turns > 0:
        if hint == word:
            print('You guessed the word {}!\nYou survived!'.format(''.join(word)))
            run_flg = input('\nType "play" to play the game, "exit" to quit: ')
            break
        print('\n' + ''.join(hint))
        guess = input('Input a letter: ')
        for i in range(len(word)):
            if word[i] == guess:
                hint[i] = guess

        if len(guess) != 1:
            print('You should input a single letter')
            continue
        if guess.isupper() or not guess.isalpha():
            print('It is not an ASCII lowercase letter')
            continue
        if guess in guesses:
            print("You already typed this letter")
            continue
        if guess not in word:
            print("No such letter in the word")
            guesses += guess
            turns -= 1
        else:
            guesses += guess
    else:
        print('You are hanged!')
        run_flg = input('\nType "play" to play the game, "exit" to quit: ')
