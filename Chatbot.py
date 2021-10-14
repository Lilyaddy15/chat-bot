print ("Hi! I am Chat Botterson! What is your name?")
name = input()
print ("What a great name! It is so nice to meet you,",name)
print ("So,",name,", what brings you her to talk to me?")
reason = input()
print ("Ahh I see. Well, I don't care so much how you got here, I am just glad you are here!")
print ("Moving on, how old are you,",name,"?")
age = input()
print ("Oh yes. I remember when I was ",age,". The best year of my life!")
print ("So are you or have you been in school? Please say yes or no.")
school = input()

if school == "yes":
    print ("Great! School leads you to become a billionare! Got to get those dollar bills!")
    print ("So, what do you hope to do as an adult to bring in the money?")
    job = input()
    print ("Wow, I always wanted to do that!")

elif school == "no":
    print ("Aww that is a shame. Have you ever thought about looking into it? Answer with yes or no.")
    start_school = input()

    if start_school == "yes":
        print ("That's great! You know what they say better late than never!")

    if start_school == "no":
            print ("Oh well. They say that school just isn't for some people.")

    else:
        print ("Well that was rude of you to not answer my question like I wanted! But I will forget about it if you answer the rest of my questions correctly.")

else:
    print ("Well that was rude of you to not answer my question like I wanted! But I will forget about it if you answer the rest of my questions correctly.")


print ("Anyways, lets move on. Is there any sports you like?")
sports = input()
print ("I love",sports,"too!")
print ("So,",name,"have you ever thought about pursuing",sports,"as a career? Please respond with a yes or no.")
sport_career = input()


if sport_career == "yes":
    print ("I knew it!",sports,"is great to do as a career!")

elif sport_career == "no":
    print ("That makes sense. Doing",sports,"as a career is a very hard sport to be succesful with.")

else:
    print ("Well that was rude of you to not answer my question like I wanted! But I will forget about it if you answer the rest of my questions correctly.")


print ("Anyways,",name,"I have had a great time getting to know you! I have learned alot like you are",age,"years old, your favorite sport is",sports,"and you came to me because",reason,"and so much more! I hope to see you again soon",name,"!")
    
