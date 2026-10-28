import pytest
from functions import (
    calculate_discount,
    count_vowels,
    fibonacci,
    flatten_list,
    is_palindrome,
    is_prime,
    word_frequencies,
)

def test_is_palindrome_simple():
    assert is_palindrome("kajak") is True


def test_is_palindrome_sentence_with_spaces_and_caps():
    assert is_palindrome("Kobyła ma mały bok") is True


def test_is_palindrome_not_palindrome():
    assert is_palindrome("python") is False


def test_is_palindrome_empty_string():
    assert is_palindrome("") is True


def test_is_palindrome_single_char():
    assert is_palindrome("A") is True


# 2. fibonacci
def test_fibonacci_zero():
    assert fibonacci(0) == 0


def test_fibonacci_one():
    assert fibonacci(1) == 1


def test_fibonacci_five():
    assert fibonacci(5) == 5


def test_fibonacci_ten():
    assert fibonacci(10) == 55


def test_fibonacci_negative_raises_error():
    with pytest.raises(ValueError):
        fibonacci(-1)


# 3. count_vowels
def test_count_vowels_basic():
    assert count_vowels("Python") == 2


def test_count_vowels_uppercase():
    assert count_vowels("AEIOUY") == 6


def test_count_vowels_consonants_only():
    assert count_vowels("bcd") == 0


def test_count_vowels_empty():
    assert count_vowels("") == 0


def test_count_vowels_polish_chars():
    assert count_vowels("Próba żółwia") in (4, 5)


def test_calculate_discount_standard():
    assert calculate_discount(100, 0.2) == 80.0


def test_calculate_discount_zero():
    assert calculate_discount(50, 0) == 50.0


def test_calculate_discount_full():
    assert calculate_discount(200, 1) == 0.0


def test_calculate_discount_negative_raises_error():
    with pytest.raises(ValueError):
        calculate_discount(100, -0.1)


def test_calculate_discount_greater_than_one_raises_error():
    with pytest.raises(ValueError):
        calculate_discount(100, 1.5)


# 5. flatten_list
def test_flatten_list_already_flat():
    assert flatten_list([1, 2, 3]) == [1, 2, 3]


def test_flatten_list_multi_level():
    assert flatten_list([1, [2, 3], [4, [5]]]) == [1, 2, 3, 4, 5]


def test_flatten_list_empty():
    assert flatten_list([]) == []


def test_flatten_list_single_element_deep():
    assert flatten_list([[[1]]]) == [1]


def test_flatten_list_chained():
    assert flatten_list([1, [2, [3, [4]]]]) == [1, 2, 3, 4]


def test_word_frequencies_standard():
    assert word_frequencies("To be or not to be") == {"to": 2, "be": 2, "or": 1, "not": 1}


def test_word_frequencies_punctuation():
    assert word_frequencies("Hello, hello!") == {"hello": 2}


def test_word_frequencies_empty():
    assert word_frequencies("") == {}


def test_word_frequencies_repeated():
    assert word_frequencies("Python Python python") == {"python": 3}


def test_word_frequencies_polish_sentence():
    expected = {"ala": 2, "ma": 2, "kota": 1, "a": 1, "kot": 1, "ale": 1}
    assert word_frequencies("Ala ma kota, a kot ma Ale.") == expected


def test_is_prime_values():
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(4) is False
    assert is_prime(0) is False
    assert is_prime(1) is False
    assert is_prime(5) is True
    assert is_prime(97) is True