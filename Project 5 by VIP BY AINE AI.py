#!/usr/bin/env python
# coding: utf-8

# # Essentials of Python Programming

# In[ ]:


#Write a Python program to develop a Rock, Papers and Scissors game to be played against a computer.


# In[1]:


import random

while True:
    human_action = input("enter the choice you want(rock,paper,scissors):")
    actions = ["rock","paper","scissors"]
    machine_actions = random.choice(actions)
    print("\nyou choose{human_actions},machine choose{machine_actions}.\n")
    
    if human_action == "machine_actors":
        print(f"both players selected same actions:it's tie")
    elif human_action == "rock":
        if machine_actions == "scissors":
            print("rock hits the scissors:you win")
        else:
            print("paper covers the rock:you lose")
            
    elif human_action =="paper":
        if machine_actions == "rock":
            print("paper covers the rock:you win")
        else:
            print("scissors cuts the paper:you lose")
    elif human_action =="scissors":
        if machine_actions == "papers":
            print("scissors cuts the paper:you win")
        else:
            print("rock hits the scissors:you lose")
            
    play_again = input("play again?(yes/no):")
    if play_again.lower() != "yes":
        break


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




