name1 = input()
name2 = input()

true_count = 0
love_count = 0

names = (name1 + name2).lower()

true_count = names.count('t') + names.count('r') + names.count('u') + names.count('e')
love_count = names.count('l') + names.count('o') + names.count('v') + names.count('e')

str_score = str(true_count) + str(love_count)
int_score = int(str_score)

if int_score < 10 or int_score > 90:
    print(f"Your score is {int_score}, you go together like coke and mentos.")
elif int_score >= 40 and int_score <= 50:
    print(f"Your score is {int_score}, you are alright together.")
else:
    print(f"Your score is {int_score}.")
