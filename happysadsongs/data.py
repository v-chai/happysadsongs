import re
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


# Consider reducing this list further
stop_words = set(stopwords.words('english')) - {
    'into', 'against', 'myself', 'doing', 'own', 'above', 'our', 'now', 'up',
    'down', 'been', 'not', 'no', 'would', 'should', 'again', 'won', 'if',
    'only', 'yours', 'your', 'you', 'ours', 'here', 'there', 'below', 'before'
}


def get_training_data():
    # ADD CODE
    pass

def get_lyrics_data():
    # ADD CODE
    pass

def clean(text):
    # lowercase
    new_text = text.lower()

    # remove twitter handles
    new_text = re.sub(r"@\w+", '', new_text)

    # remove urls
    new_text = re.sub(r'http:\S+', '', new_text)
    new_text = re.sub(r'https:\S+', '', new_text)

    # remove punctuation
    for punctuation in string.punctuation:
        new_text = new_text.replace(punctuation, '')

    # remove numbers
    new_text = ''.join(word for word in new_text if not word.isdigit())

    return new_text


def remove_stopwords(text):
    word_list = [
        word for word in word_tokenize(text) if not word in stop_words
    ]
    return ' '.join(word_list)


def lemma_text(text):
    lemmatizer = WordNetLemmatizer()
    lemmatized = [lemmatizer.lemmatize(word) for word in word_tokenize(text)]
    return ' '.join(lemmatized)


# Possibly remove single letter words
def clean_length(text):
    return [word for word in text if len(word) > 2]
