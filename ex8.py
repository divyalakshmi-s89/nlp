
import nltk

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')

sentence = "The smart student solved a difficult problem quickly"

tokens = nltk.word_tokenize(sentence)
print("Tokens:", tokens)

pos_tags = nltk.pos_tag(tokens)
print("POS Tags:", pos_tags)

grammar = "NP: {<DT>?<JJ>*<NN>}"

chunk_parser = nltk.RegexpParser(grammar)

chunked_tree = chunk_parser.parse(pos_tags)

print("\nChunked Tree:")
print(chunked_tree)

print("\nNoun Phrases:")
for subtree in chunked_tree.subtrees():
    if subtree.label() == 'NP':
        print(" ".join(word for word, tag in subtree.leaves()))

try:
    chunked_tree.draw()
except:
    print("\nTree visualization not supported on this system.")