# format specifier = {value:flags} format a value based on wat flags are inserted

# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces 
# :03 = allocate and zero pad that many spaces 
# :< = left justify 
# :> = right justify
# :^ = center align 
# :+ = use a plsu sign to indecate a postive value
# :, = comma seperator

price1 = 3.1415
price2 = -9.786
price3 = 1200000.34

print(f"price 1 is {price1:10.2f}")
print(f"price 2 is {price2:<10}")
print(f"price 3 is {price3:10,.2f}")