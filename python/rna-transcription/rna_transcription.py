dna_to_rna = str.maketrans("ATGC", "UACG")

def to_rna(dna_strand):
    return dna_strand.translate(dna_to_rna)
