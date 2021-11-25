import sys
from better_profanity import profanity

with open(sys.argv[1], 'r') as f:
    contents = f.read()

    Racial_word = ["white", "black", "racial","caste", "shit", "racism", "bully"]
    profanity.load_censor_words(Racial_word)
    print(profanity.censor(contents))


def profanity_check():   
    count = 0
    
   
    for i in Racial_word:
        if i in contents:
            count += 1
    return count


# profanity_read()
print("Total profanity words found in file are :", profanity_check())


if profanity_check() == 0:
    print("Profanity Degree: Appropriate no profanity present")
elif profanity_check() < 5:
    print("Profanity Degree: Offensive Content")
else:
    print("Profanity Degree: Highly Offensive")
