---
marp: true
---

# PYTHON

### ortografia
### interpunkcja
### zwroty grzecznościowe
### kaligrafia

---

## PEP 8<br>*Style Guide for Python Code*

> PEP - Python Enhancement Proposal

---

## PEP 8: tabulacja

**4 spacje zamiast znaku tabulacji!**
- czytelność
- wcięcia wyglądają tak samo, niezależnie od konfiguracji edytora
- można jednoznacznie wyznaczyć linię 120 (lub 79) znaków

---

## PEP 8: wcięcia

```python
import math

def eratostenes(n):
    sieve = [
    True for _ in range(n + 1)]
    for i in range(2, math.ceil(math.sqrt(n))):
                if sieve[i]:
                    for j in range(2 * i, n, i):
                        sieve[j] = False
    primes = []
    for i in range(2, n + 1):
            if sieve[i]:
                primes.append(i)
    return primes

def main():
            n = 137
            primes = eratostenes(n)
            print('liczby pierwsze od 2 do {}:'.format(n))
            print(', '.join(map(str, primes)))

if __name__ == '__main__':
        main()

```

---

## PEP 8: długość linii

*Limit all lines to a maximum of **79** characters.*

*For flowing long blocks of text with fewer structural restrictions (docstrings or comments), the line length should be limited to **72** characters.*

...

> PEP 8 powstała 5 stycznia 2001

---

## PEP 8: załamanie linii, a operatory arytmetyczne?

```python
income = (gross_wages +
          taxable_interest +
          (dividends - qualified_dividends) -
          ira_deduction -
          student_loan_interest)
```

---

## PEP 8: załamanie linii przed operatorami arytmetycznymi

```python
income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)
```

---

## PEP 8: kodwanie

Python 2: domyślnie ASCII

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

pass
```

Python 3: domyślnie UTF-8

---

## PEP 8: importowanie bibliotek

```python
# brzydko
import sys, requsts, os, math, json

# ładnie
import sys
import requests
import os
import math
import json
```


---

## PEP 8: importowanie bibliotek

```python
# bardzo ładnie
import json
import math
import os
import requests
import sys
```

---

## PEP 8: importowanie bibliotek

dla struktury plików

```
program.py
biblioteka
--- __init__.py
--- funkcje.py
--- stale.py
```

program.py:
```python
from biblioteka import stale

# lub
from biblioteka.stale import STALA_1, STALA_2

# tak lepiej nie
from biblioteka.stale import *
```

---

## PEP 8: importowanie bibliotek

funkcje.py uruchamiane "standalone":
```python
from stale import STALA_1, STALA_2
```

funkcje.py wywoływane z program.py:
```python
from . import stale

x = stale.STALA_1 + stale.STALA_2

# lub
from .stale import STALA_1, STALA_2
```

---

## PEP 8: cudzysłowy

```python
x, y = 1, 2
print('x="{}", y="{}"'.format(x, y))
print("x='{}', y='{}'".format(x, y))
print("x=\"{}\", y=\"{}\"".format(x, y))
# tak jest źle (SyntaxError):
print(r"x="{}", y="{}"".format(x, y))
```

---

## PEP 8: białe znaki

```python
# brzydko
def funkcja (a,b,c): pass

funkcja ( a = 1, b = 2, c = { 2 : 2 , 3 : 3})

# ładnie
def funkcja(a, b, c): pass

funkcja(a=1, b=2, c={2: 2, 3: 3})

# w javascripcie coś takiego jest ok:
slownik = { 'a': 1, 'b': 2 }
# w pythonie powinno być tak:
slownik = {'a': 1, 'b': 2}
```

---

## Zagnieżdżenia

```python
lista = [{1: 1, 2: 2}, {'a': 1, 'b': 2}, {'a1': 1, 'b2': 2}]
```

---

## Zagnieżdżenia

```python
lista = [
    {1: 1, 2: 2},
    {'a': 1, 'b': 2},
    {'a1': 1, 'b2': 2}
]
```

---

## Zagnieżdżenia

```python
lista = [
    {
        1: 1,
        2: 2,
    }, {
        'a': 1,
        'b': 2,
    }, {
        'a1': 1,
        'b2': 2,
    },
]
```

---

## Zagnieżdżenia

```python
lista = [{
    1: 1,
    2: 2,
}, {
    'a': 1,
    'b': 2,
}, {
    'a1': 1,
    'b2': 2,
}]
```

---

## Atrybuty chronione i prywatne

```python
class Klasa:

    def _protected(self):
        return 'protected'
    
    def __private(self):
        return 'private'
```

---

## Atrybuty chronione i prywatne

```python
k = Klasa()

print(k._protected())
# zwróci nam "protected"

print(k.__private())
# zwróci nam... AttributeError
```

---

## Atrybuty chronione i prywatne

```python
dir(k)
# [..., '_Klasa__private', ..., '_protected', ...]

print(k._Klasa__private())
# wzróci nam "private"
```

---

1. Słowniki, krotki, listy, generatory, list comprehension
2. Linter (użycie i konfiguracja)
