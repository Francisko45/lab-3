n = int(input("Введіть кількість чисел N: "))  
zero_count = 0  
count = 0  

while count < n: 
    number = int(input())  
    if number == 0:
        zero_count += 1  
    count += 1  

print("Кількість нулів:", zero_count)  