import syllapy
text = "The quick brown fox jumps over the lazy dog. This sentence is an example of a simple and straightforward " \
       "sentence. It contains short words and has a clear structure. On the other hand, the intricacies of the " \
       "English language can lead to more complex and challenging texts. Reading comprehension and text analysis are " \
       "important skills for individuals of all ages and backgrounds."

def Vowel_Count(fullText):
    global syllables
    textNumList = []
    fullText = fullText.split()
    for word in fullText:
        x = int(syllapy._syllables(word))
        textNumList.append(x)
    return sum(textNumList)
    
print(Vowel_Count(text))
