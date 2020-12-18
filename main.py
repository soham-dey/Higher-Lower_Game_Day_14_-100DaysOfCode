from game_data import data
from art import logo, vs
from replit import clear
import random

def game():
  print(logo, "\n")
  game_end="No"
  point=0
  index=0
  random.shuffle(data)
  person=data[index]
  while game_end=="No":
      person=data[index]
      a_index=data.index(person)
      a_name=person["name"]
      a_des=person['description']
      a_loc=person['country']
      a_followers=person["follower_count"]
      b_person=data[a_index + 1]
      b_name=b_person["name"]
      b_des=b_person['description']
      b_loc=b_person['country']
      b_followers=b_person["follower_count"]
      name_dict={a_name: 'a', b_name: 'b'}
      compare_dict={a_followers:a_name , b_followers: b_name}
      follower_count_list=[]
      follower_count_list.append(a_followers)
      follower_count_list.append(b_followers)
      max_count=max(follower_count_list)
      max_name=compare_dict[max_count]
      max_option=name_dict[max_name]
      print(f"Option a: {a_name}, a {a_des} from {a_loc}.\n")
      print(vs)
      print(f"Option b: {b_name}, a {b_des} from {b_loc}.\n ")
      user_choice=input("Guess who has more followers on Instagram? Type 'a' or 'b': ")
      if user_choice==max_option:
        point+=1
        index+=1
        print("Let's move to the next guess...\n")
      else:
        game_end="Yes"
        print("You have lost!\n")
      print(f"Your Point is {point}\n")

  play_again='y'
  while play_again=='y':
    play_again=input("Do you want to restart game? Type 'y' for Yes or 'n' for No: ")
    if play_again=='y':
      clear()
      game()
    elif play_again=='n':
      clear()


game()





  
