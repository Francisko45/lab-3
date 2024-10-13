import time

start_time = time.perf_counter()  

sum_with_for_while = 0  
for number in range(1, 1000): 
    if number % 3 == 0 or number % 5 == 0:
        sum_with_for_while += number  

end_time = time.perf_counter() 
print("Сума (for):", sum_with_for_while)
print("Час виконання (for):", end_time - start_time, "секунд")


start_time = time.perf_counter()  

sum_with_for_while_2 = 0  
number = 1  

while number < 1000:  
    if number % 3 == 0 or number % 5 == 0:
        sum_with_for_while_2 += number 
    number += 1  

end_time = time.perf_counter()  
print("Сума (while в поєднанні):", sum_with_for_while_2)
print("Час виконання (while в поєднанні):", end_time - start_time, "секунд")
