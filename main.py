from game_data import data
from art import logo, vs
from replit import clear
import random

def game():
  """Calls the Higher Lower Game. """
  
  #Initialization of variables
  game_end="No"
  point=0
  index=0

  #The data list is randomy shuffled each time a new game starts.
  random.shuffle(data)

  #Looping through the options until the game gets ended.
  person=data[index]
  while game_end=="No":
      person=data[index]
      a_index=data.index(person)
      a_name=person["name"]
      a_followers=person["follower_count"]
      b_person=data[a_index + 1]
      b_name=b_person["name"]
      b_followers=b_person["follower_count"]
      name_dict={a_name: 'a', b_name: 'b'}
      compare_dict={a_followers:a_name , b_followers: b_name}
      follower_count_list=[]
      follower_count_list.append(a_followers)
      follower_count_list.append(b_followers)
      max_count=max(follower_count_list)
      max_name=compare_dict[max_count]
      max_option=name_dict[max_name]
      print(logo, "\n")
      print(f"Your Point is {point}\n")
      print(f"Option a: {a_name}, a {person['description']} from {person['country']}.\n")
      print(vs, "\n")
      print(f"Option b: {b_name}, a {b_person['description']} from {b_person['country']}.\n ")
      user_choice=input("Guess who has more followers on Instagram? Type 'a' or 'b': ")

      #Checking if game is continuing or ended.
      if user_choice==max_option:
        point+=1
        index+=1
        clear()
        print("Let's move to the next guess...\n\n")
      else:
        game_end="Yes"
        print("You have lost!\n\n")
        print(f"Your Point is {point}\n")
      
  #Ask the user if he wants to play another game.
  play_again='y'
  while play_again=='y':
    play_again=input("Do you want to restart game? Type 'y' for Yes or 'n' for No: ")
    if play_again=='y':
      clear()
      game()
    elif play_again=='n':
      clear()

#Starting the game by calling the game() function.
game()





  
