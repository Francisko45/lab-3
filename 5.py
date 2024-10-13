max_value = None  

while True:
    number = int(input())  
    
    if number == 0:
        break  
    
    if max_value is None or number > max_value:
        max_value = number  

if max_value is not None:
    print(max_value) 
else:
    print("Послідовність пуста.")
