import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('punkt_tab')

ps = PorterStemmer()
text = "Stemming reduces words to their root forms"
words = word_tokenize(text)
stemmed_words = [ps.stem(word) for word in words]

print("Original words:", words)
print("Stemmed words:", stemmed_words)