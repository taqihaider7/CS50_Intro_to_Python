from twttr import shorten

# testing for Upper, lower, mixed case words
def test_twttr():
    assert shorten("taqi")== "tq"
    assert shorten("TAlpha")== "Tlph"
    assert shorten("LIONS")=="LNS"


# testing for puncuations and numbers
    assert shorten("!,./?")=="!,./?"
    assert shorten("01234")=="01234"