def to_rna(dna_strand):
    return dna_strand.translate(dna_strand.maketrans("CGTA", "GCAU"))

