"""
Auxiliary functions which are used in rosalind.sequence module.

Includes functions:
    read_multifasta:            Reads multi-line multi-sequence fasta file into a dictionary like so: {name:sequence}.
    is_valid:                   Checks if a given string is a valid nucleic acid sequence.
    gc:                         Calculates GC% of a DNA/RNA sequence.

"""


def read_multifasta(fasta_path):
    """
    A function to import multiline fasta into a dictionary.

    Returns a dictionary where key are sequence names (without >) and values are the sequences.

    :param fasta_path: Path to the fasta file.
    :return: Dictionary {name[str]:sequence[str]}
    """

    sequences = {}
    with open(fasta_path, 'r') as f:
        for line in f:
            if line.startswith('>'):
                name = line.strip()[1:]
                sequences[name] = ''
            else:
                try:
                    sequences[name] += line.strip()
                # catch a case where there is no name before the sequence
                except KeyError:
                    print('your fasta seems to be corrupt')

    return sequences


def is_valid(dna: str) -> bool:
    """
    Checks if a string is a valid nucleic acid sequence (only A,T,G,C,U in any case).
    Does not consider IUPAC code.

    :param dna: DNA or RNA string.
    :return: whether it consists only of A,T,G,C,U letters (lowercase allowed).
    """
    return set(dna.upper()) <= {'A', 'T', 'C', 'G', 'U'}


def gc(dna: str) -> float:
    """
    Calculate GC% of a nucleic acid string.

    :param dna: DNA sequence.
    :return: A float representing %GC.
    """
    if not is_valid(dna):
        print('Please provide only DNA/RNA (A,T,G,C,U allowed')

    dna = dna.upper()
    return (dna.count('G') + dna.count('C')) / len(dna)


def calculate_mw(protein: str) -> float:
    """
    This function calculates protein mass.

    :param protein: The sequence of the protein.
    :return: Molecular weight of the protein.
    """

    if not protein.isupper():
        protein = protein.upper()

    mw = {"A": 71.03711,
          "C": 103.00919,
          "D": 115.02694,
          "E": 129.04259,
          "F": 147.06841,
          "G": 57.02146,
          "H": 137.05891,
          "I": 113.08406,
          "K": 128.09496,
          "L": 113.08406,
          "M": 131.04049,
          "N": 114.04293,
          "P": 97.05276,
          "Q": 128.05858,
          "R": 156.10111,
          "S": 87.03203,
          "T": 101.04768,
          "V": 99.06841,
          "W": 186.07931,
          "Y": 163.06333}
    try:
        return sum(mw[aminoacid] for aminoacid in protein)
    except KeyError:
        print('Please provide a valid protein sequence.')

