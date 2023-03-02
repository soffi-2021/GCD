import pytest

def test_gcd():
    assert gcd(48, 60) == 12
    assert gcd(10, 25) == 5
    assert gcd(17, 23) == 1

def gcd(n, m):
    """Compute the GCD of two integers by Euclid's algorithm."""
    n, m = abs(n), abs(m)
    n, m = min(n, m), max(n, m)  # Sort their absolute values.
    if not n:
        return m
    while m % n:         # While `n` doesn't divide into `m`:
        n, m = m % n, n  # update the values of `n` and `m`.
    return n
