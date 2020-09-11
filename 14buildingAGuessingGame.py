# xxx

secret_number = 9
guess_limit = 3
guess_count = 0

print('guess the number, only three attempts: 11')

while guess_count < guess_limit :
  guess = int(input('Guess: '))
  guess_count = guess_count + 1
  if guess == secret_number:
    print("you won")
    break
else :
  print('sorry you reached 3 attemps, and failed')

