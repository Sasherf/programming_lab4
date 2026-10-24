letter = input(str())
small_letter = letter.lower()

if small_letter == 'a' or small_letter == 'e' or small_letter == 'i' or small_letter == 'o' or small_letter == 'u':
    print(f"{letter} is a vowel")
else:
    print(f"{letter} is a consonant")