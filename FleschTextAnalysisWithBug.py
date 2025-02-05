"""
Program Name: textanalysis.py

Authors:
    Miles Butler
    William Ruben

Description:
    This program allows the user to select a text file (txt, rtf, MD, etc) by entering its name before displaying the
    number of words, sentences, and syllables found within the file's text. In adition, this program also 
    
Date Published: 2025-02-05


   
"""

import syllapy

def Vowel_Count(fullText):
    """
    Count the number of vowels in any string
    
    :param fullText: The text in which vowels will be counted
    :type fullText: str
    :return: The number of vowels found in the "fullText" string.
    :rtype: int
    """
    global syllables
    textNumList = []
    fullText = fullText.split()
    for word in fullText:
        x = int(syllapy._syllables(word))
        textNumList.append(x)
    return sum(textNumList)
while True:
    # Take the inputs
    fileName = input("Enter the file name: ")
    try:
        inputFile = open(fileName, 'r')
    except FileNotFoundError:
        print('File Not Found\nPlease make sure this file is in the same folder as this program.\n')
        continue
    text = inputFile.read()
    
    # Count the sentences
    sentences = text.count('.') + text.count('?') + \
                text.count(':') + text.count(';') + \
                text.count('!')
    
    # Count the words
    words = len(text.split())
    
    suffixes = ['es', 'ed', 'e']
    
    # Count the syllables
    syllables = Vowel_Count(text)
    
    
    
    # Compute the Flesch Index and Grade Level
    index = 206.835 - 1.015 * (words / sentences) - \
            84.6 * (syllables / words)
    level = int(round(0.39 * (words / sentences) + 11.8 * \
                      (syllables / words) - 15.59))
    
    # Output the results
    print("The Flesch Index is", index)
    print("The Grade Level Equivalent is", level)
    print(sentences, "sentences")
    print(words, "words")
    print(syllables, "syllables")