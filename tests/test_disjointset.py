from disjointset import DisjointSet

import random
import pytest
from pytest import fixture, mark
from string import ascii_uppercase as symbols
from itertools import combinations, product


@fixture
def dset():
    return DisjointSet()

def test_contains_dunder_method(dset):

    assert  not ('A' in dset)

    dset.make_set('A')

    assert  'A' in dset
    assert not (1 in dset)

def test_len_dunder_method(dset):
    assert len(dset) == 0

    for i in range(100): dset.make_set(i)

    assert len(dset) == 100

    i = 0
    for j in range(i+1, 100):
        dset.union(i, j)
        i = j

    assert len(dset) == 100

def test_bool_method(dset):

    assert not bool(dset)

    for i in range(1, 101): # arbitrary values
        j = dset.make_set(i)
        assert i == j

    assert bool(dset)

@mark.parametrize(
    'number_elements',
    [100, 10_000, 100_000]
)
def test_make_set_method(number_elements):
    dset = DisjointSet()

    for i in range(number_elements):
        dset.make_set(i)

    assert len(dset) == number_elements


def test_insert_an_element_again(dset):

    elements = list()
    for i in range(10_000):
        elements.append(i)
        dset.make_set(i)

    random_elemnt = random.choice(elements)

    with pytest.raises(ValueError) :
        dset.make_set(random_elemnt)


@mark.parametrize(
    'number_elements',
    [100, 10_000, 100_000]
)
def test_union_method_with_numeric_values(number_elements):
    dset = DisjointSet()

    max_range = number_elements + 1

    for i in range(1, max_range): # arbitrary values
        j = dset.make_set(i)
        assert i == j

    i = 2
    for j in range((i+2), max_range,2):
        dset.union(i, j) # even numbers
        i = j

    i = 1
    for j in range((i+2), max_range, 2):
        dset.union(i, j) # even numbers
        i = j

    assert len(dset) == number_elements

    random_element = 4

    assert random_element in dset, f"{random_element=} should be in the disjoint set"
    assert not (max_range in dset), "this value shouldn't belong to disjoint set"

    flatted_sets = dset.get_sets()

    assert len(flatted_sets) == 2

    assert dset.find(24) % 2 == 0
    assert dset.find(25) % 2 == 1

def test_union_with_string_values(dset):

    elements = list()
    for letters in combinations(symbols, 3):
        key = ''.join(letters)
        dset.make_set(key)
        elements.append(key)

    assert len(dset) == len(elements)

    random.shuffle(elements)

    counter = 0
    for a, b in product(elements, repeat=2):
        counter += 1
        if a[0] == b[0]:
            dset.union(a, b)

    assert len(dset.get_sets()) == (len(symbols) - 2)


def test_union_with_tuple_values(dset):

    elements = list()
    for key in combinations(symbols, 3):
        dset.make_set(key)
        elements.append(key)

    assert len(dset) == len(elements)

    random.shuffle(elements)

    counter = 0
    for a, b in product(elements, repeat=2):
        counter += 1
        if a[0] == b[0]:
            dset.union(a, b)

    assert len(dset.get_sets()) == (len(symbols) - 2)