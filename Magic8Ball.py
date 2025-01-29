#Magic8Ball.py
#Name: Eduardo Esau Hernandez Abreo
#Date: 1/29/2025
#Assignment: lab 2

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.
  print("Magic 8 Ball")
  #Prompt the user for their question.
  answers = ["Yes you do", "No", "ask me again", "tomorrow no", "tomorrow mabey", "just doit",
              "No No", "Out of servies", "funy but no", "Funy but yes", "Just decide", "You have doit by yuor self",
              "is fine doit", "Come back tomorrow", "Don't ask me", "Fine", "Go and doit", "Come back in and week",
             "nah i dont have time", "I going to tell your mom", "Get help"] 
  #Answer question randomly with one of the options from your earlier list.
  for i in range(10):
    num = random.random()
    num = num * 1000
    num = int(num)
    num = num % 20
    question = input("Ask me a question: ")
    print(answers[num])

  
  #print(answers[0])


if __name__ == '__main__':
  main()
