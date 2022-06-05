from multiprocessing.connection import answer_challenge
# Quiz Program done my yogi
print( "Welcome to my computer quiz" )

playing = input( "Do you want to play ?" )
print(playing)
if playing != "yes":
    quit()

print( "Okay! Lets play the game :) ")

answer = input( "What does CPU stands for?")
if answer == "central processing unit":
    print('Correct!')
else:
    print(" Wrong Answer! ")

answer2 = input("Prime Minister of India :")
if answer2 == "Narendra Modi":
    print('Correct Good Job')
else:
    print("Wrong Answer :( ")

answer3 = input("National Bird of India :")
if answer3 == "peacock":
    print('Correct Answer')
else:
    print("Wrong Answer :( ")
