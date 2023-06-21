from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


vocab_file = "imdb.vocab"
vocab_list = []

with open(vocab_file, "r", encoding="utf-8") as file:
    for line in file:
        word = line.strip()  # Supprimer les espaces en début et fin de ligne
        vocab_list.append(word)

analyzer = SentimentIntensityAnalyzer()
for vocab in vocab_list[:100]:
    vs = analyzer.polarity_scores(vocab)
    print("{:-<65} {}".format(vocab, str(vs)))