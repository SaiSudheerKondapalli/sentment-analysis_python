
# A stem is the root or roots of a word, together with any derivational affixes, to which inflectional affixes are added.

# ex: disadvantage,disagreement,disappointment....

from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

ps = PorterStemmer()

# let us consider 2 sent
# sent 1: I was taking a ride in the car.
# sent 2: I was riding in the car.

# they both mean the same but it was different in writting...

example_words = ["riding", "ride"]

for w in example_words:
    print(ps.stem(w))

# consider a new line

new_text = "It is important to by very pythonly while you are pythoning with python. All pythoners have pythoned poorly at least once."

words = word_tokenize(new_text)

for w in words:
    print(ps.stem(w))
