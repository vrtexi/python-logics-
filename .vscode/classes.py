class car:
  def __init__(self,model,year,color,for_sale):
    self.model = model
    self.year = year
    self.color = color
    self.for_sale = for_sale
    
car1 = car("Mustang", 2004,"red",False)
car2 = car("covette", 2008,"black",True)

print(car1.model)