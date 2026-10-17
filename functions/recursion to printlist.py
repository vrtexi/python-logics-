# WRITE A RECURSIVE FUNCTION TO PRINT ALL ELEMENTS IN A LIST 

L = [ " A", "B ", "C ", "D ", "E ", "F " ]

def print_list(L,i=0):
  if i == len(L):
    return 
  print(L[i])
  print_list(L,i+1)  
  
print_list(L)  