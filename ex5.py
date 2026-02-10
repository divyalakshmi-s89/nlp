from nltk.util import ngrams

sentence = "Hello This is 5th excercise succesfully Run"
n = 2  
words = sentence.split()
word_ngrams = ngrams(words, n)
print("Word N-grams:")
for gram in word_ngrams:
    print(gram)

n = 5
char_ngrams = ngrams(sentence, n)
print("\nCharacter N-grams:")
for gram in char_ngrams:
    print(''.join(gram))