# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
total = []
for n in range(0, len(student_heights)):
  total.append(student_heights[n])
  
sum = 0

for m in total:
  sum = sum + m
total_students = n + 1
average_height = round((sum/total_students))

print(f"total height = {sum}")
print(f"number of students = {total_students}")
print(f"average height = {average_height}")