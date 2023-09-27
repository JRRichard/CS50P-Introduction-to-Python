from twttr import shorten

def test_twttr_lowercase():
    assert shorten("lengthen") == "lngthn"

def test_twttr_uppercase():
    assert shorten("TWITTER") == "TWTTR"

def test_twttr_mixedcase():
    assert shorten("Cherie") == "Chr"

def test_twttr_allvowels():
    assert shorten("eauio") == ""

def test_twttr_nonumpunc():
     assert shorten("Juni0r7!") == "Jn0r7!"
