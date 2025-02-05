import syllapy

sen1 = "The quick brown fox jumps over the lazy dog."
print(syllapy._syllables(sen1))
sen2 = "This sentence is an example of a simple and straightforward sentence"
print(syllapy._syllables(sen2))
sen3 = "It contains short words and has-a-clear-structure.-On-the other-hand, the intricacies of the\n"\
        " English language can lead to more complex and challenging texts. "
print(syllapy._syllables(sen3))
sen4 = "Reading comprehension and text analysis are important skills for individuals of all ages and backgrounds."
print(syllapy._syllables(sen4))

print(f"\nSUM TOTAL:  "
      f"{(syllapy._syllables(sen1) + syllapy._syllables(sen2) + syllapy._syllables(sen3) + syllapy._syllables(sen4))}")
while True:
    x = input('')
    print(syllapy._syllables(x))

