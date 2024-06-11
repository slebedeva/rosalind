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
