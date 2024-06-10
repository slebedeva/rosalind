"""
Utility functions to modify nucleic acid sequences.

The functions are somewhat tailored to solving Rosalind problems but can be used independently.

Includes functions:
    is_valid:           Checks if a given string is a valid nucleic acid sequence.
    reverse_complement: Returns reverse complement of a DNA or RNA sequence.
    hamming_distance:   Calculates Hamming distance (substitution only) between two sequences of equal length.
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
