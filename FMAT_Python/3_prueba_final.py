x = 1
x = x == x
print(x)

i = 0
while i <= 3 :
    i += 2
    print("*")

print("Nuevo ejercicio")

i = 0
while i <= 5 :
    i += 1
    if i % 2 == 0:
      break
    print("*")

vals = [0, 1, 2]
vals.insert(0, 1)
del vals[1]
total = 0

for number in vals:
    total += number
    
print(total)
