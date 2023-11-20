import stanza

# Download the English model and initialize the pipeline
stanza.download('en')
nlp = stanza.Pipeline('en')

# Process a piece of text
doc = nlp("Marlon climate here, assistant professor, most of our research these days looking at by online community, and as far as like networks, that part of the suite of skills.")

# Access the parsed output
for sentence in doc.sentences:
    for word in sentence.words:
        print(word.text, word.lemma, word.pos, word.deprel)
