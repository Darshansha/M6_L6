import random

class FruitsQuiz:
    
    def __init__(self):
        self.fruits={'apple':'red',
                     'orange':'orange',
                     'watermelon':'green',
                     'banana':'yellow'}
    
    def quiz(self):
        while (True):

            fruit, color = random.choice(list(self.fruits.items()))

            print("What is the color of {}?".format(fruit))
            user_answer = input()
            if(user_answer.lower() == color):
                print("Correct answer!")
            else:
                print("Wrong answer!")
        
            option = int(input("Do  you wan to play again? (0 for yes/1 for no):"))
            if (option):
                break
print("Welcome to Fruit Quiz")
fq = FruitsQuiz() 
fq.quiz()          

