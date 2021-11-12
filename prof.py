from better_profanity import profanity


def profanity_read():
    file = open("C:/Users/MEGHANA/Documents/My documents/sample.txt")
    content = file.read()
    Racial_word = ["white", "black", "racial","caste", "shit", "racism", "bully"]
    profanity.load_censor_words(Racial_word)
    print(profanity.censor(content))
    
    
    

def profanity_check():
    file = open("enter your file path")
    content = file.read()
    Racial_word = ["white", "black", "racial","caste", "shit", "racism", "bully"]
    
    
    count = 0
    
   
    for i in Racial_word:
        if i in content:
            count += 1
    return count


profanity_read()
print("Total profanity words found in file are :", profanity_check())


if profanity_check() == 0:
    print("Profanity Degree: Appropriate no profanity present")
elif profanity_check() < 5:
    print("Profanity Degree: Offensive Content")
else:
    print("Profanity Degree: Highly Offensive")
