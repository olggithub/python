# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# (расшифровка этого выражения 
# not (x[0] or x[1] or x[2] = not x[0] and not x[1] and not x[2]) 
# для всех значений предикат.

x=[False,False,False]
print(x[2],x[1],x[0])
print((not(x[0] or x[1] or x[2])) ==(not(x[0]) and not(x[1]) and not(x[2]))) 

for i in range (1,8):
#   print(i)
    x[0]=not(x[0])
    if (i==2) | (i==4) | (i==6):
        x[1] = not(x[1])
    if i==4:
        x[2]=not(x[2])
    print(x[2],x[1],x[0])
    print((not(x[0] or x[1] or x[2])) ==(not(x[0]) and not(x[1]) and not(x[2])))