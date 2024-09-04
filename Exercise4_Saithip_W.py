import os

def clearscreen():
   
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")
      
foundation_english_score          = float(input("Enter Foundation English Score: "))
general_business_score            = float(input("Enter General Business Score: "))
intro_to_computer_systems_score   = float(input("Enter Introduction to Computer Systems Score: "))
computer_programming_score        = float(input("Enter Computer Programming Score: "))

clearscreen()
print("--- Your Score ---")
print(f"Foundation English: {foundation_english_score}")
print(f"General Business: {general_business_score}")
print(f"Introduction to Computer Systems: {intro_to_computer_systems_score}")
print(f"Computer Programming: {computer_programming_score}")
