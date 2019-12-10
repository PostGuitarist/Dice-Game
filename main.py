import random
from dice import *

def main():
  
  #Sets the min and max to 1 and 6
  min = 1
  max = 6
 
  roll_again = 'yes' or 'y' or 'Yes' or 'Y' or 'no' or 'n' or 'No' or 'N'
 
  #Asks for guess and requires it to be an integer 
  user_guess = raw_input("What is your guess: ")
  
  
  #Requires number to be between 1 and 6
  if user_guess <= 0:
    print ('Sorry, but numbers must be between 1 and 6.')
    main()
  elif user_guess >= 7:
    print ('Sorry, but numbers must be between 1 and 6.')
    main()    

  #Starts loop
  while roll_again == 'yes' or roll_again == 'y' or roll_again == 'Yes' or roll_again == 'Y':
    print ('Rolling the dice...')
    print ('The result is....')
    result = random.randint(min, max)
    print result
 
    #Calls on dice drawing depending on result
    if result == 1:
      dice1()
    elif result == 2:
      dice2()
    elif result == 3:
      dice3()
    elif result == 4:
      dice4()
    elif result == 5:
      dice5()
    elif result == 6:
      dice6()
    
    #Tells user if guess was right or wrong
    if user_guess == result:
      print('---------------------------------------')
      print('|                                     |')
      print('|  Congrats! Your guess was correct.  |')
      print('|                                     |')
      print('---------------------------------------')
      break
    elif user_guess != result:
      print('----------------------------------------')
      print('|                                      |')
      print('|   Sorry! Your guess was incorrect.   |')
      print('|                                      |')
      print('----------------------------------------')
      break
  
  #Asks for redo
  roll_again = raw_input('Do you want to roll the dice again? Type Yes or No to choose: ')
 
  if roll_again == 'no' or roll_again == 'n' or roll_again == 'No' or roll_again == 'N':
    print ('Ok, see you next time!')
  elif roll_again != 'y' or roll_again != 'Y' or roll_again != 'Yes' or roll_again != 'yes' or roll_again != 'no' or roll_again != 'No' or roll_again != 'N' or roll_again != 'n':
    print ('Not a valid input. Restarting.')
    main()
  else:
    main()
  
  if user_guess != '1' or user_guess != '2' or user_guess != '3' or user_guess != '4' or user_guess != '5' or user_guess != '6':
    print ('Not a valid guess. Restarting.')
    main()
    
#Starts program    
main() 
