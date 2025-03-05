# Lesson 29
def consonantsCounter(text, vowel = False):
    count = 0

    for character in text:
        character = character.lower()
        if character.isalpha() and character not in {'a', 'e', 'i', 'o', 'u'}:
            count += 1
    
    if not vowel:
        return count
    else:
        count = 0
        for character in text:
            character = character.lower()
            if character.isalpha() and character in {'a', 'e', 'i', 'o', 'u'}:
                count += 1
        return count


print(f"The amount of consonants in {consonantsCounter('hello, world!')}")
print(f"The amount of consonants in {consonantsCounter('hello, world!', True)}")