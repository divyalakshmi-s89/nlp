import nltk
from nltk.tokenize import word_tokenize

# Download required resources (run once)
nltk.download('punkt')
nltk.download('punkt_tab')

text = "Natural Language Processing is interesting."
tokens = word_tokenize(text)

print("TOKENS:", tokens)
