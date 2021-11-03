from disjointset import DisjointSet

def test_with_numeric_values():
    dset = DisjointSet()

    for i in range(1, 101): # arbitrary values
        j = dset.make_set(i)
        assert i == j

    i = 2
    for j in range((i+2), 101,2):
        dset.union(i, j) # even numbers
        i = j

    i = 1
    for j in range((i+2), 101, 2):
        dset.union(i, j) # even numbers
        i = j

    assert len(dset) == 100

    assert 4 in dset, "this value should be in the disjoint set"
    assert not (101 in dset), "this value shouldn't belong to disjoint set"

    flatted_sets = dset.get_sets()

    assert len(flatted_sets) == 2

    assert dset.find(24) % 2 == 0
    assert dset.find(25) % 2 == 1


def test_bool_method():
    dset = DisjointSet()

    assert not bool(dset)

    for i in range(1, 101): # arbitrary values
        j = dset.make_set(i)
        assert i == j

    assert bool(dset)