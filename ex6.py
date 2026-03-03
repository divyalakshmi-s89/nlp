from collections import defaultdict

def calculate_ngram_probabilities(corpus):
    ngrams = defaultdict(int)
    context = defaultdict(int)

    for sentence in corpus:
        words = sentence.lower().split()

        for i in range(len(words) - 2):
            trigram = (words[i], words[i+1], words[i+2])
            ctx = (words[i], words[i+1])

            ngrams[trigram] += 1
            context[ctx] += 1

    probabilities = {}
    vocab_size = len(ngrams)

    for trigram, count in ngrams.items():
        ctx = (trigram[0], trigram[1])
        context_count = context[ctx]

        prob = (count + 1) / (context_count + vocab_size)
        probabilities[trigram] = prob

    return probabilities


corpus = [
    "Students study machine learning",
    "Students study data science",
    "Teachers teach machine learning"
]

trigram_probabilities = calculate_ngram_probabilities(corpus)

for trigram, probability in trigram_probabilities.items():
    print(f"Trigram: {trigram}, Probability: {probability:.4f}")