def decimal_to_binary(decimal):
    binary = ""
    
    if decimal == 0:
        return "0"
    
    while decimal > 0:
        temp = decimal
        binary_temp = ""
        
        while temp > 0:
            binary_temp = str(temp % 2) + binary_temp
            temp //= 2  
        
        binary = binary_temp
        break  
    
    return binary

number = int(input("Please enter a decimal number: "))
binary_result = decimal_to_binary(number)

print("Binary:", binary_result)