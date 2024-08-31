from nlplogic.corenlp import summarize_wiki, get_phrases,get_text_blob,search_wiki

def test_get_phrase():
    assert 'golden state' in get_phrases("Golden State Warriors")
