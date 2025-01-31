def lonelyinteger(array):
    occurrence_count = {}  
    
   
    for number in array:
        occurrence_count[number] = occurrence_count.get(number, 0) + 1
    
    
    for number, count in occurrence_count.items():
        if count == 1:
            return number
        
# crazy efficient solution recommended by claude using bits/xor something I hadn't heard of

def lonelyinteger(a):
    result = 0  
    for num in a:
        result = result ^ num
    return result