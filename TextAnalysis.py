"""
Program Name: TextAnalysis.py

Authors:
    Miles Butler
    William Ruben

Description:
    This program allows the user to select a text file (txt, rtf, MD, etc.) by entering its name before displaying the
    number of words, sentences, and syllables found within the file's text. In addition, this program also uses
    unique formulas to determine the academic grade and skill level of the text file's author.
    
Date Published: 2025-02-05

"""
import subprocess
import sys
download_pip = ''
download_syllapy = ''
download_setuptools = ''
try:
    import pip
except ImportError:
    
    download_pip = input("pip is needed to run this program, but wasn't found within your system.\nWould you like "
                         "to install it now? (y/n): ").upper()
if download_pip == 'Y':
    print('pip installing...')
    subprocess.run([sys.executable, "-m", "ensurepip", "--default-pip"])
    print('pip installed!')
    import pip
try:
    import setuptools
except ImportError:
    download_setuptools = input("A small package of pip installation tools are required to run this program, "
                                "but they weren't found within your directory\nWould you like to install them now?"
                                " (y/n): ").upper()
    if download_setuptools == 'Y':
        print('Installing setup tools...')
        subprocess.run([sys.executable, "-m", "pip", "install", "setuptools"], check=True)
        print("Installation Successful")
        import setuptools
    
 
   
try:
    import syllapy
except ImportError:
    download_syllapy = input("The syllapy package is needed to run this program, but wasn't found within your "
                             "system.\nWould you like to install it now? (y/n): ").upper()
    if download_syllapy == 'Y':
        print('Installing syllapy...')
        subprocess.run([sys.executable, "-m", "pip", "install", 'syllapy'], check=True)
        print("Installation Successful")
        import syllapy
        
if download_syllapy == 'Y' or download_pip == 'Y' or download_setuptools == 'Y':
    print('NOTICE:\nIn the case that this program crashes after installing all necessary recourses, '
          'please just run the program again.\nThis is normal, as your IDE may need to restart in order to '
          "use it's new installations.\n\n")
        


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
        x = int(syllapy.count(word))
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