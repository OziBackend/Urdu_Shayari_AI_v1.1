import urduhack

# Downloading models
urduhack.download()

nlp = urduhack.Pipeline()
text = "بہادر شاہ ظفر کی شاعری"
doc = nlp(text)

for sentence in doc.sentences:
    print(sentence.text)
    for word in sentence.words:
        print(f"{word.text}\t{word.pos}")

    for token in sentence.tokens:
        print(f"{token.text}\t{token.ner}")
