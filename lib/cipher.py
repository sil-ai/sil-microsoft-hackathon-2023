# Encypt a string by substiuting each character with another character from our table below
# the table is made of all vowels and then all constants
substitution_table = {
    'a': 'e',
    'e': 'i',
    'i': 'o',
    'o': 'u',
    'u': 'a',
    'b': 'f',
    'c': 'k',
    'd': 'w',
    'f': 's',
    'g': 'g',
    'h': 'x',
    'j': 'y',
    'k': 'c',
    'l': 'p',
    'm': 'n',
    'n': 'r',
    'p': 'q',
    'q': 't',
    'r': 'v',
    's': 'z',
    't': 'l',
    'v': 'm',
    'w': 'h',
    'x': 'b',
    'y': 'j',
    'z': 'd'
}

# invert substitution table
decoder_table = {v: k for k, v in substitution_table.items()}

def substitution_cipher(text, encode=True):
    result = ""
    if encode:
        codes = substitution_table
    else:
        codes = decoder_table

    for character in text:
        was_capitilized = character.isupper()
        character = character.lower()
        if character.isalpha() and character in codes:
            if was_capitilized:
                result += codes[character].upper()
            else:
                result += codes[character]
        else:
            result += character
    return result