def marsExploration(s):
    changes = 0
    for i in range(len(s)):
        position = i % 3
        expected = ''
        
        # Determine what letter we expect
        if position == 0 or position == 2:  # First and third positions expect 'S'
            expected = 'S'
        else:  # Middle position expects 'O'
            expected = 'O'
        
        
        if s[i] != expected:
            changes += 1  # If they don't match, increment our counter
        
    return changes