num = int(input("Enter a number: "))

#multiplication table
print(f"Multiplication Table of {num}:")
for i in range(1,11): #loop frm 1 to 10 
  print(f"{num} x {i} = {num * i}")
