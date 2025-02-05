import syllapy
textNumList = []
words = 'The quick brown fox jumps over the lazy dog. This sentence is an example of a simple and straightforward ' \
        'sentence. It contains short words and has a clear structure. On the other hand, the intricacies of the ' \
        'English language can lead to more complex and challenging texts. Reading comprehension and text analysis ' \
        'are important skills for individuals of all ages and backgrounds.'
words = words.split()
for word in words:
    x = int(syllapy._syllables(word))
    textNumList.append(x)
syllables = sum(textNumList)
print(syllables)
