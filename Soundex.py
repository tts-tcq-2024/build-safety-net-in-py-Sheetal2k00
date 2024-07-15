def first_letter(name):
    """
    Return the first letter of the name in uppercase.
    """
    return name[0].upper()

def get_replacement(char):
    """
    Map a character to its corresponding Soundex digit.
    """
    replacements = {
        'b': '1', 'f': '1', 'p': '1', 'v': '1',
        'c': '2', 'g': '2', 'j': '2', 'k': '2', 'q': '2', 's': '2', 'x': '2', 'z': '2',
        'd': '3', 't': '3',
        'l': '4',
        'm': '5', 'n': '5',
        'r': '6'
    }
    return replacements.get(char, None)

def is_redundant_digit(last_digit, current_digit):
    """
    Determine if the current digit is redundant.
    """
    return last_digit == current_digit

def append_digit(result, digit, last_digit):
    """
    Append a digit to the result if it's not redundant.
    """
    if digit and not is_redundant_digit(last_digit, digit):
        result.append(digit)
    return digit

def process_character(char, last_digit, result):
    """
    Process a single character from the name, handling Soundex encoding.
    """
    # Ignore vowels and specific characters unless they separate consonants
    if char in 'aeiouyhw':
        return last_digit  # Do not change the last_digit

    digit = get_replacement(char)
    return append_digit(result, digit, last_digit)

def encode_name(name):
    """
    Encode the name into Soundex digits, omitting redundant digits.
    """
    if not name:
        return ''

    result = [first_letter(name)]
    last_digit = None

    for char in name[1:]:
        last_digit = process_character(char, last_digit, result)

    return ''.join(result)

def format_code(code):
    """
    Format the encoded name to ensure it has exactly 4 characters.
    """
    return (code + '000').ljust(4, '0')[:4]

def soundex(name):
    """
    Convert a name to its Soundex code.
    """
    if not name:
        return "0000"

    encoded_name = encode_name(name.lower())
    return format_code(encoded_name)
