"""
Utility functions to process nucleic acid sequences.

The functions are tailored to solving Rosalind problems but can be used independently.

Included functions:
    is_valid:           Checks if a given string is a valid nucleic acid sequence.
    reverse_complement: Returns reverse complement of a DNA or RNA sequence.
    hamming_distance:   Calculates Hamming distance (substitution only) between two sequences of equal length.
    find_motif:         Returns 1-based starts of all locations of a motif within given sequence (exact match).
"""


def is_valid(dna: str) -> bool:
    """
    Checks if a string is a valid nucleic acid sequence (only A,T,G,C,U in any case).
    Does not consider IUPAC code.

    :param dna: DNA or RNA string.
    :return: whether it consists only of A,T,G,C,U letters (lowercase allowed).
    """
    return set(dna.upper()) <= {'A', 'T', 'C', 'G', 'U'}


def reverse_complement(dna: str) -> str:
    """
    Accepts DNA as a string of capital A,C,T,G letters in Rosalind format.
    Returns reverse complement sequence.

    If a sequence has both U and T it assumes DNA and translates A to T by default.

    :param dna: Input DNA or RNA sequence (allowed letters A,a,T,t,G,g,C,c,U,u)
    :type dna: str
    """

    # check if is valid nucleic acid sequence
    if not is_valid(dna):
        return 'Please enter a valid DNA/RNA sequence (no IUPAC allowed)'

    # determine if RNA or DNA
    # TODO add IUPAC letters

    if 'U' in dna.upper() and not 'T' in dna.upper():
        table = str.maketrans({'G': 'C', 'C': 'G', 'A': 'U', 'U': 'A', 'g': 'c', 'c': 'g', 'a': 'u', 'u': 'a'})
    else:
        table = str.maketrans(
            {'G': 'C', 'C': 'G', 'A': 'T', 'T': 'A', 'U': 'A', 'g': 'c', 'c': 'g', 'a': 't', 't': 'a', 'u': 'a'})
    # reverse and complement
    return dna[::-1].translate(table)


def hamming_distance(dna1: str, dna2: str) -> int:
    """
    Returns Hamming distance (the number of substitutions) between two DNA sequences of equal length.

    DNA are strings of A,C,G and T. This function will in principle work on other strings as well.

    The output is not case sensitive.

    :param dna1:
    :param dna2:
    :return ham_dist:
    """

    # exception if the length is not the same
    if len(dna1) != len(dna2):
        raise ValueError('Length of the two sequences must be the same!')

    ham_dist = 0

    for i in range(len(dna1)):
        if dna1[i].upper() != dna2[i].upper():
            ham_dist += 1

    return ham_dist


def find_motif(s: str, t: str) -> list[int]:
    """
    Given two DNA strings s and t (each of length at most 1 kbp), return all locations of t as a substring of s.

    :param s: Longer sequence in which to search.
    :param t: The motif to be found.
    :return: List of 1-based integer starts of all found motif locations.
    """

    # initiate answer
    ans = []

    # go through the string finding next motif and moving the pointer
    # start with the first motif
    i = s.find(t)
    if i > 0:
        ans.append(i + 1) #use 1-based indexing
    while i < len(s):
        # jump to the mext motif
        i = s.find(t, i + 1)
        if i > 0:
            ans.append(i + 1)
        # if none is found, finish
        else:
            break

    return ans
