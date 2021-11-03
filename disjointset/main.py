# -*- coding: utf-8 -*-
"""
A Python implementation for the disjoint set data structure.

@author: Giliard Godoi
"""
from collections import defaultdict

class Subset():

    def __init__(self, vertice, rank=0):
        self.parent = vertice
        self.rank = rank

class DisjointSet():

    def __init__(self):
        self.subsets = defaultdict()

    def __contains__(self, item):
        return item in self.subsets

    def __len__(self):
        return len(self.subsets)

    def __bool__(self):
        return bool(self.subsets)

    def __link__(self, v, u):
        if self.subsets[u].rank > self.subsets[v].rank:
            self.subsets[v].parent = self.subsets[u].parent

        elif self.subsets[v].rank > self.subsets[u].rank:
            self.subsets[u].parent = self.subsets[v].parent

        else :
            self.subsets[v].parent = u
            self.subsets[u].rank += 1

    def make_set(self, item):
        if item in self.subsets:
            raise ValueError(f"Key <{item!r}> already exist")

        self.subsets[item] = Subset(item)
        return item

    def find(self, item):
        if item not in self.subsets:
            raise ValueError(f"There is no subset for {item}")

        if self.subsets[item].parent != item :
            self.subsets[item].parent = self.find(self.subsets[item].parent)

        return self.subsets[item].parent

    def union(self, v, u):
        self.__link__(self.find(v), self.find(u))

    def get_sets(self):

        disjointed = defaultdict(set)

        for key in self.subsets.keys():
            parent = self.find(key)
            disjointed[parent].add(key)

        return disjointed
