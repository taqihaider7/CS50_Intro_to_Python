from plates import is_valid

def test_letters_after_numbers():
    assert is_valid('dg65a8') == False

# testing letters in first
def test_first_letters():
    assert is_valid('0ab232') == False
    assert is_valid('A02356') == False
    assert is_valid('AB2345') == True
    assert is_valid('12345') == False

# testing single letter
def test_under():
    assert is_valid('a') == False

# testing after letters and exceding limits
def test_over():
    assert is_valid('asd2356')==False

# testing with placing zero first
def test_zero_placement():
    assert is_valid('ALP032') == False

# testing letters with sepcial characters
def test_alphanumeric():
    assert is_valid('ab@?#')== False