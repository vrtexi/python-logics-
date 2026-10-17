# WAP to input an age and marks of a paerson and gender and check its eligibility for participatiung in ICPC 2026. 
# Condition are as follows 
# For Male Candidate 
# age>=14 < = 30
# Marks
#   if marls <= 33, Not Eligibile 
#   if marks > 33 < = 70, eligible for prelims round
#   if marks> 70 Direct eligible for the Main round
# For Female Candidate
# age>=15 <=35
# Marks
#   if marks<30, Not eligible
#   if marks> 30 <=60 Eligible for prelims
#   if marks >60 direct eligible for main round
  
gender = input("Enter your gender: ")
marks = int(input("Enter your marks: "))
age = int(input("Enter your age: "))

if gender.capitalize() == 'Male':
  if age>=14 and age<=30:
    if marks> 100:
      print("Number is out of range")
    elif marks <=33:
      print("not eligible")
    elif marks>33 and marks<=70:
      print("Eligible for the prelims round")
    else:
      print("Direct eligible for main rounds")
  else: 
    print("not a valid age")
elif gender.capitalize() == "Female":
  if age>=15 and age<=35:
      if marks> 100:
        print("Number is out of range")
      elif marks <=33:
        print("not eligible")
      elif marks>33 and marks<=60:
        print("Eligible for the prelims round")
      else:
        print("Direct eligible for main rounds")
  else: 
    print("not a valid age")
else:
  print("invalid gender")