"""
Utility functions to process nucleic acid sequences.

The functions are tailored to solving Rosalind problems but can be used independently.

Included functions:
    is_valid:           Checks if a given string is a valid nucleic acid sequence.
    reverse_complement: Returns reverse complement of a DNA or RNA sequence.
    hamming_distance:   Calculates Hamming distance (substitution only) between two sequences of equal length.
    find_motif:         Returns 1-based starts of all locations of a motif within given sequence (exact match).
"""

# import utility functions (like reading fasta)
from .utils import read_multifasta


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

    if 'U' in dna.upper() and 'T' not in dna.upper():
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

    The output is not case-sensitive.

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
        ans.append(i + 1)  # use 1-based indexing
    while i < len(s):
        # jump to the mext motif
        i = s.find(t, i + 1)
        if i > 0:
            ans.append(i + 1)
        # if none is found, finish
        else:
            break

    return ans


###############################################################################################
# Functions to find common substrings
###############################################################################################


def all_common_substrings(seq1, seq2):
    """
    An auxiliary function that will find all common substrings of all lengths between the two strings/sequences.

    :param seq1: First sequence.
    :param seq2: Second sequence.
    :return: A set of all common substrings between the two strings.
    :return type: set[str]
    """

    # initiate answer as set to store all substrings
    ans = set()

    # go over all indices of the first string
    for i in range(len(seq1) - 1):
        start1 = i
        end1 = i

        # find the first match in the second string
        start2 = seq2.find(seq1[start1])
        end2 = start2

        # check every match in second string and prolong until there is no match or end of sequence is reached
        while 0 < end2 < len(seq2) and end1 < len(seq1):
            # move the pointers if there is a match:
            if seq1[end1] == seq2[end2]:
                curr_subseq = seq1[start1:end1 + 1]
                # add the match to the answer
                ans.add(curr_subseq)
                end1 += 1
                end2 += 1

            # otherwise jump to the next match:
            else:
                # move the start pointer to include all shorter substrings of the current match
                for k in range(start2, end2):
                    ans.add(seq2[k:end2 + 1])
                # reset end of the match in the first string
                end1 = start1
                # jump to next match in string2 and reset end of the match in second string
                start2 = seq2.find(seq1[i], start2 + 1)
                end2 = start2
    return ans


def longest_common_substring(fasta_path: str) -> str:
    """
    Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.

    Return: One longest common substring of the collection. (If multiple solutions exist, it returns only one of them.)

    Note: this function uses brute-force approach and will be too slow on larger inputs.

    :param fasta_path: Path to the fasta file with sequences.
    :return: A string which is one longest common substring for all sequences.
    """

    # read input fasta into a list of sequences
    sequences = list(read_multifasta(fasta_path).values())

    # find all the common substrings of any length between the first two sequences
    seq1 = sequences.pop()
    seq2 = sequences.pop()
    substrings = list(all_common_substrings(seq1, seq2))

    # read more sequences until EOF and eliminate substrings which are not included in each sequence
    for seq in sequences:
        # only take substrings which are in sequence
        substrings = [subs for subs in substrings if subs in seq]

    # sort remaining substrings by length
    substrings.sort(key=lambda x: len(x))
    # return the longest
    return substrings[-1]
