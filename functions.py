import math
import re
import string


def is_palindrome(text: str) -> bool:
    cleaned = [ch.lower() for ch in text if not ch.isspace()]
    return cleaned == cleaned[::-1]


def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("Liczba musi być nieujemna.")
    if n == 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def count_vowels(text: str) -> int:
    vowels = set("aeiouyąęó")
    return sum(1 for ch in text.lower() if ch in vowels)


def calculate_discount(price: float, discount: float) -> float:
    if not (0.0 <= discount <= 1.0):
        raise ValueError("Zniżka musi mieścić się w przedziale od 0 do 1.")
    return float(price * (1.0 - discount))


def flatten_list(nested_list: list) -> list:
    flat = []
    for item in nested_list:
        if isinstance(item, list):
            flat.extend(flatten_list(item))
        else:
            flat.append(item)
    return flat


def word_frequencies(text: str) -> dict:
    cleaned = re.sub(rf"[{re.escape(string.punctuation)}]", " ", text.lower())
    words = cleaned.split()
    frequencies = {}
    for word in words:
        frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    limit = math.isqrt(n)
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False
    return True