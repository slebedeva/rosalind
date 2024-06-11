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
