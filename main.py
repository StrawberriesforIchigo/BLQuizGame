#making a simple BL test for the fujoshis, fudanshis, fujins....
playerName = input("Hi there! Nice of you to drop in. My name's 1chigo. What's yours? ")

playerIntro = "Well hi {}! I hope you're ready to play a game today. Make sure you've got all your BL series out because we're gonna be testing just how much you know~~~"

print(playerIntro.format(playerName))

#define the means to check if answers are correct
def checkAnswer(question, answer, attempts, score):
  if quiz[question]["answer"].lower() == answer.lower():
    print("Wow so you do know your stuff~ \nYour score is ", (score + 1))
    return True
  else:
    print("You got it wrong tho, sis :( ... \nYou got only ", (attempts - 1), " attempts left...")
    return False
  

#get our questions from the other file!
from blquestions import quiz

score = 0

for question in quiz:
  
  attempts = 3
  
    #for as long as the player still has attempts they can answer questions
  while attempts > 0:
    
    #the first question is our variable in the for loop
    print(quiz[question]["question"])
    
    yourAnswer = input("You think you know bl? Try your luck and enter you answer ... ")
    check = checkAnswer(question, yourAnswer, attempts, score)
    if check:
      score += 1
      break
      attempts -= 1
      continue
      
  else: 
    print("Sorry about that ... I guess you don't really know your BL like that. Go to fujo class! \nYour score is ", score)
      
#now lets have some commentary after you finish
if score >= 8:
  print(("Wow!!!! are you so cool! We should watch some BL sometime. {}, you are top class!").format(playerName))

elif score > 4 and score < 8:
  print(("You did great! You still have much to discover int the world of BL young padawan, but that's okay. Do you {}!").format(playerName))

else: 
  print(("It could have been worse...? Please {} never get this kind of score again...").format(playerName))