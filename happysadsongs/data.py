import re
import string
import os
import pandas as pd

def get_training_data():
    root_path = os.path.dirname(os.path.dirname(__file__))
    data_path = os.path.join(root_path,'raw_data')
    df = pd.read_csv(os.path.join(data_path, 'balanced_hsa_dataset.csv'))
    return df[['text','word_label']]

def get_lyrics_data():
    root_path = os.path.dirname(os.path.dirname(__file__))
    data_path = os.path.join(root_path, 'raw_data')
    df = pd.read_csv(os.path.join(data_path,'labeled_lyrics_cleaned.csv'))
    return df[['title', 'artist', 'label', 'lyrics']]

def get_test_lyrics():
    root_path = os.path.dirname(os.path.dirname(__file__))
    data_path = os.path.join(root_path,'raw_data')
    df = pd.read_csv(os.path.join(data_path, "hsa_labeled_lyrics.csv"))
    return df


def clean(text, rem_punc=False):
    """Preprocess input text"""
    # lowercase
    new_text = text.lower()

    # remove twitter handles
    new_text = re.sub(r"@\w+", '', new_text)

    # remove urls
    new_text = re.sub(r'http:\S+', '', new_text)
    new_text = re.sub(r'https:\S+', '', new_text)

    # lyrics - specific
    new_text = new_text.replace('\n\n', '. ').replace('\n', ', ')
    new_text = re.sub(r"\[[^]]*\]", ' ', new_text)

    # remove punctuation OPTIONAL
    if rem_punc:
        for punctuation in string.punctuation:
            new_text = new_text.replace(punctuation, '')

    # remove numbers
    new_text = ''.join(word for word in new_text if not word.isdigit())

    return new_text
