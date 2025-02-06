def countingValleys(steps, path):
    level = 0    
    valleys = 0
    
    for step in path:
        previous_level = level
        
        
        if step == 'U':
            level += 1
        else:  # D
            level -= 1
            
       
        if previous_level < 0 and level == 0:
            valleys += 1
            
    return valleys