n = int(input("Введіть кількість чисел N: ")) 
zero_count = 0 

for _ in range(n):  
    number = int(input()) 
    if number == 0:
        zero_count += 1  

print("Кількість нулів:", zero_count) 
