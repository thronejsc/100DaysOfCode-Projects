# sentence = input()
# # 🚨 Don't change code above 👆
# # Write your code below 👇
# word_list = [word for word in sentence.split(" ")]
#
# result = {word: len(word) for word in word_list}
#
#
#
#
# print(result)


weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
# 🚨 Don't change code above 👆
weather_f = {day: (temp*1.8 + 32) for (day,temp) in weather_c.items()}
# Write your code 👇 below:



print(weather_f)