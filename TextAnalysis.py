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
try:
    import pip
except ImportError:
    
    download_pip = input("pip is needed to run this program, but wasn't found within your system.\nWould you like "
                         "to install it now? (y/n): ").upper()
    
if download_pip == 'Y':
    print('pip installing...')
    subprocess.run([sys.executable, "-m", "ensurepip", "--default-pip"])
    import pip
    print('pip installed!')
    

try:
    import syllapy
except ImportError:
    download_syllapy = input("The syllapy package is needed to run this program, but wasn't found within your "
                             "system.\nWould you like to install it now? (y/n): ").upper()
    if download_syllapy == 'Y':
        print('installing syllapy:')
        subprocess.run([sys.executable, "-m", "pip", "install", 'syllapy'], check=True)
        print("Installation Successful")
    try:
        import syllapy
    except ImportError:
        print("One or more packages still missing. Please see the README.MD file, or try installing pip and syllapy "
          "through the bash console. ")
        exit()


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