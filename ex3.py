import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
text = "Excercise for stopword removal is run and verified."
words = word_tokenize(text.lower())
stop_words = set(stopwords.words('english'))
words = [w for w in words if w not in stop_words]
lemmatizer = WordNetLemmatizer()
lemmatized = [lemmatizer.lemmatize(w) for w in words]
print("Original Text:", text)
print("After Stopword Removal:", words)
print("After Lemmatization:", lemmatized)