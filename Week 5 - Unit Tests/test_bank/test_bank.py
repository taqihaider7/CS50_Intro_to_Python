from bank import value

# testing lower case greetings
def test_bank_lower_case():
    assert value("hello") == 0
    assert value("hello ") == 0
    assert value(" hello ") == 0
# testing upper case greetings
def test_bank_upper_case():
    assert value("HELLO") == 0
    assert value(" HELLO ") == 0
    assert value(" HELLO") == 0

# testing mixed case and numbers with words greetings
def test_bank_mixed_case():
    assert value("HElLo") == 0
    assert value("ha") == 20
    assert value(" HE") == 20
    assert value("Whats's up ") == 100
    assert value("Yo Man ") == 100