def soundex(name):
    # Soundex mappings
    soundex_mapping = {
        'b': '1', 'f': '1', 'p': '1', 'v': '1',
        'c': '2', 'g': '2', 'j': '2', 'k': '2', 'q': '2', 's': '2', 'x': '2', 'z': '2',
        'd': '3', 't': '3',
        'l': '4',
        'm': '5', 'n': '5',
        'r': '6'
    }
    
    name = name.lower()
    first_letter = name[0].upper()
    encoded_name = first_letter
    
    previous_digit = ''
    for char in name[1:]:
        if char in 'aeiouyhw':
            continue
        digit = soundex_mapping.get(char, '0')
        if digit != previous_digit:
            encoded_name += digit
        previous_digit = digit
    
    encoded_name = encoded_name.replace('0', '')
    return (encoded_name + '000')[:4]

# Testing Soundex Implementation
print(soundex("User"))    # Expected: U260
print(soundex("Clam"))    # Expected: C450
print(soundex("India"))   # Expected: I530
print(soundex("Kumta"))   #Expected: K530

