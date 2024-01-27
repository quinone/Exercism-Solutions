def to_rna(dna_strand):
    rna = ''
    for nucleo in dna_strand:
        if nucleo == 'A':
            rna+='U'
        elif nucleo == 'T':
            rna+='A'
        elif nucleo == 'G':
            rna+='C'
        elif nucleo == 'C':
            rna+='G'
    return rna
