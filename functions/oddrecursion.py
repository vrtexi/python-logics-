def odd(lower,upper):
  if lower <=upper:
    if lower % 2 !=0:
      print(lower)
      odd(lower+1,upper)
    else:
      odd(lower+1,upper)
    

lower=int(input("1: "))
upper=int(input("2: "))
odd(lower,upper)