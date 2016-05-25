import re


def processing_text(text):
    text = text.lower()

    text_split = text.split(" ")

    for j in xrange(len(text_split)):
        text_split[j] = re.sub(r'\W+', '', text_split[j])

    text = ' '.join(text_split)

    text = text.replace("  ", " ")

    return text
