import spacy

# Load the English tokenizer, tagger, parser, NER, and word vectors
nlp = spacy.load("en_core_web_sm")

# Process the text
text = ("I was involved with the development but it was one of the very first "
        "network programs that was developed. It was developed primarily by "
        "there was a computer science undergraduate at adopted in the early 70s. "
        "A project where we brought in gathered data, the Office of Civil Defense "
        "and if we had 162 respondents and we flipped them. We graph paper, "
        "and we stuck them together. When we put them up on the board. "
        "We read the information off of each, each")
with open('./output/output1.txt', 'r', encoding='utf-8') as file:
    text = file.read()

doc = nlp(text)

# Analyze sentence structures and output the grammatical roles for each sentence
for sent in doc.sents:
    print(len(sent))
    if len(sent) < 8:
        continue
    roles = {
        'SUBJECT': [],
        'VERB': [],
        'OBJECT': [],
        'INDIRECT OBJECT': [],
        'PREPOSITIONAL PHRASE': [],
        'CLAUSE': []
        # Add more roles as needed
    }
    
    # Output the sentence
    print(f"Sentence: {sent.text}\n")

    for token in sent:
        # Identify the grammatical role of each token in the sentence
        if token.dep_ == 'nsubj' or token.dep_ == 'nsubjpass':
            roles['SUBJECT'].append(token.text)
        elif token.dep_ == 'ROOT':
            roles['VERB'].append(token.text)
        elif token.dep_ == 'dobj':
            roles['OBJECT'].append(token.text)
        elif token.dep_ == 'dative':
            roles['INDIRECT OBJECT'].append(token.text)
        elif token.dep_.startswith('prep') or token.dep_ == 'pobj':
            roles['PREPOSITIONAL PHRASE'].append(token.text)
        elif token.dep_ == 'acl' or token.dep_ == 'relcl':
            roles['CLAUSE'].append(token.text)
        # Add more roles and conditions as needed

    # Output the roles and examples
    for role, examples in roles.items():
        if examples:  # Only print the role if there are examples
            print(f"{role}: {' '.join(examples)}")
    print("\n")  # Add a new line for readability between sentences
