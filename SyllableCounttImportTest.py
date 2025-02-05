text = 'the fitness gram pacer test is a multistage blah blah blah.'
print(f"the number of t's in the text is {text.count('t')}")
T_Replace = text.replace('t', '(x)')
import pyphen
language = pyphen.Pyphen(lang='en')

words = "The-quick-brown-fox-jumps-over-the lazy dog. This sentence is an example of a simple and straightforward \n" \
         "sentence. It contains short-words-and-has-a-clear-structure.-On-the other-hand, the intricacies of the \n" \
        "English language can lead to more complex and challenging texts. Reading comprehension and text analysis \n" \
        "are important skills for individuals of all ages and backgrounds.\n"
print('SCRIPT:\n' + words)

#Text_With_Removed_Hyphens = words.replace("-", " ")

Syllable_Hyphenated_Text = (language.inserted(words.replace('-', ' ')))
print(f'HYPHENATED TEXT: {Syllable_Hyphenated_Text}')
syllables = Syllable_Hyphenated_Text.count("-") + len(Syllable_Hyphenated_Text.split())
print(f"The final number of syllables are: {syllables}")


