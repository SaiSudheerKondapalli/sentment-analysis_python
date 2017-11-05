from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sent = "stop words examples. this is the example that says about stop words"

stop_words = set(stopwords.words('english'))

# code to print example sent with and with out stop words.

word_tokens = word_tokenize(example_sent)

filtered_sentence = [w for w in word_tokens if not w in stop_words]

filtered_sentence = []

for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)

print(word_tokens)
print(filtered_sentence)
