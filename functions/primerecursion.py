def prime(n,i=2):
  if i <n:
    if n%i ==0:
      print("not prime")
    else:  
      prime(n,i+1)
  else:
    print("prime")
    
prime(2)