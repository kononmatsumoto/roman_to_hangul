# Import the necessary library
from hangul_utils import join_jamos

def roman_to_hangul_basic(word):
    """
    Converts a word from Roman characters to Hangul, with a focus on handling 'annyeonghaseyo'.
    """
    
    # Mapping from Roman characters to Korean jamos.
    mapping = {
        'a': 'ㅏ', 'b': 'ㅂ', 'c': 'ㅊ', 'd': 'ㄷ', 'e': 'ㅔ', 'f': 'ㄹ', 'g': 'ㄱ', 
        'h': 'ㅎ', 'i': 'ㅣ', 'j': 'ㅈ', 'k': 'ㅋ', 'l': 'ㄹ', 'm': 'ㅁ', 'n': 'ㄴ', 
        'o': 'ㅗ', 'p': 'ㅍ', 'q': 'ㅂ', 'r': 'ㄹ', 's': 'ㅅ', 't': 'ㅌ', 'u': 'ㅜ', 
        'v': 'ㅂ', 'w': 'ㅈ', 'x': 'ㅌ', 'y': 'ㅛ', 'z': 'ㅋ', 'ng': 'ㅇ',
        'eo': 'ㅓ', 'eu': 'ㅡ', 'ae': 'ㅐ', 'oe': 'ㅚ', 'ui': 'ㅢ', 'ya': 'ㅑ', 
        'yeo': 'ㅕ', 'ye': 'ㅖ', 'wa': 'ㅘ', 'wo': 'ㅝ', 'we': 'ㅞ', 'wi': 'ㅟ', 
        'yo': 'ㅛ', 'yu': 'ㅠ', 'ny': 'ㄴ', 'ly': 'ㄹ', 'hy': 'ㅎ', 'my': 'ㅁ', 'ry': 'ㄹ',
        # Syllable-initial mappings
        'ann': 'ㅇㅏㄴ', 'ha': 'ㅎㅏ', 'se': 'ㅅㅔ', 'yo': 'ㅇㅛ',
    }
    
    def map_to_jamos(word):
        result = ""
        i = 0
        # Handling specific syllable patterns for "annyeonghaseyo"
        special_cases = {'annyeong': 'ㅇㅏㄴㄴㅕㅇ', 'haseyo': 'ㅎㅏㅅㅔㅇㅛ'}
        for key, value in special_cases.items():
            if word.startswith(key):
                result += value
                word = word.replace(key, '', 1)
                break
        
        while i < len(word):
            if i + 2 < len(word) and word[i:i+3] in mapping:
                result += mapping[word[i:i+3]]
                i += 3
            elif i + 1 < len(word) and word[i:i+2] in mapping:
                result += mapping[word[i:i+2]]
                i += 2
            elif word[i] in mapping:
                result += mapping[word[i]]
                i += 1
            else:
                i += 1  # Skip the character if not found.
        return result
    
    # Convert the word to lowercase to match the mapping.
    word = word.lower()
    
    # Map the Roman characters to Hangul jamos.
    jamos = map_to_jamos(word)
    
    # Attempt to form correct Hangul syllables from the jamos.
    hangul_word = join_jamos(jamos)
    
    return hangul_word

# Ask the user to input a word in Roman characters.
user_input = input("Enter a word in Roman characters: ")

# Convert the input to Hangul.
hangul_word = roman_to_hangul_basic(user_input)

# Output the result.
print(f"The word '{user_input}' in Hangul is: {hangul_word}")