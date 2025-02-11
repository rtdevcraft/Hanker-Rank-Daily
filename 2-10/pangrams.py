def pangrams(s):
    # Handle invalid input
    if s is None:
        raise ValueError("Input string cannot be None")
        
    # Early return if string is too short
    if len(s.replace(" ", "")) < 26:
        return "not pangram"
    
    # Convert to lowercase
    s = s.lower()
    
    # Create set for unique letters
    letters = set()
    
    # Check each character
    for char in s:
        if char.isalpha():
            letters.add(char)
            # Early return if we found all letters
            if len(letters) == 26:
                return "pangram"
    
    return "not pangram"