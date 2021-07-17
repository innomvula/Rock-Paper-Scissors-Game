from random import randint

rps = ['rock', 'paper', 'scissors']
rounds = 5
user1score = 0
cp1score = 0
for i in range(rounds):
    j = randint(0,2)
    cp1 = rps[j]
 #   print(cp1)
    user1 = input("action: " )
    if user1 == cp1:
        print(str(user1score) + '-' + str(cp1score))
    else:
        if user1 == 'rock' and cp1 == 'paper':
            cp1score += 1
            print(str(user1score) + '-' + str(cp1score))
        elif user1 == 'rock' and cp1 == 'scissors':
            user1score += 1
            print(str(user1score) + '-' + str(cp1score))
        elif user1 == 'paper' and cp1 == 'rock':
            user1score += 1
            print(str(user1score) + '-' + str(cp1score))
        elif user1 == 'paper' and cp1 == 'scissors':
            cp1score += 1
            print(str(user1score) + '-' + str(cp1score))
        elif user1 == 'scissors' and cp1 == 'rock':
            cp1score += 1
            print(str(user1score) + '-' + str(cp1score))
        else:
            user1score +=1
            print(str(user1score) + '-' + str(cp1score))
if user1score > cp1score:
    print("User1 is the winner!!")
elif user1score < cp1score:
    print("CP1 is the winner!!")
else:
    print("Draw")
