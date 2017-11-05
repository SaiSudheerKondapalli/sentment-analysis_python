from nltk.tokenize import sent_tokenize, word_tokenize

#tokenizing -- words tokenizers ----  sentenece tokenziers

#lexicons and corporas

#corporas -- body of text

#lexicons -- words and thier meanings

#investor speaks  regelar english speaks diff

# in investor point of view Bull means a positive about stock market but in english it refers to a animal

EXAMPLE_TEXT = "hello Mr. Sudheer, how are you. Sent 2. sent 3."

print(sent_tokenize(EXAMPLE_TEXT))


print(word_tokenize(EXAMPLE_TEXT))


# for good formate split it into line

for i in word_tokenize(EXAMPLE_TEXT):
  print(i)
