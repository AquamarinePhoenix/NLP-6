import nltk
from nltk.corpus import gutenberg
from nlplib.log import write_log

def list_nltk_books() -> None:
    try:
        nltk.data.find('corpora/gutenberg')
    except LookupError:
        nltk.download('gutenberg')

    return gutenberg.fileids()