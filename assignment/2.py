# Q4. Write a program to input lower limit and upper limit and check all
# numbers lies within such limit that if number is EVEN then check its
# prime or not.

# -------------------------------method 1--------------------------------
# lower= int(input("1: "))
# upper= int(input("2: "))

# for i in range(lower,upper+1):
#   if i % 2==0:
#     for n in range(2,i):
#       if i % n == 0:
#         print(f"the current {i} is not prime")
#         break
#       else:
#         print(f"{i} prime")
#     else:
#       print(f"{i}is prime")
      
#  ------------------------------method 2--------------------------------
lower = int(input("1: "))
upper = int(input("2: "))

for i in range(lower, upper + 1):

    if i % 2 == 0:

        found = False

        for n in range(2, i):

            if i % n == 0:
                found = True

        if found:
            print(f"{i} is not prime")
        else:
            print(f"{i} is prime")
  
