from textblob import TextBlob
import wikipedia

def search_wiki(name):
    print(f"Searching for name: {name}")
    return wikipedia.search(name)

def summarize_wiki(name):
    print(f"Finding summary for name {name}")
    return wikipedia.summary(name)

def get_text_blob(text):
    blob = TextBlob(text)
    return blob


def get_phrases(name):
    text = summarize_wiki(name)
    blob = get_text_blob(text)
    phrases =  blob.noun_phrases
    return phrases


