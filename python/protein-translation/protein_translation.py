PROTEINS = {
    "AUG": "Methionine",
    "UUU": "Phenylalanine",
    "UUC": "Phenylalanine",
    "UUA": "Leucine",
    "UUG": "Leucine",
    "UCU": "Serine",
    "UCC": "Serine",
    "UCA": "Serine",
    "UCG": "Serine",
    "UAU": "Tyrosine",
    "UAC": "Tyrosine",
    "UGU": "Cysteine",
    "UGC": "Cysteine",
    "UGG": "Tryptophan",
    "UAA": "STOP",
    "UAG": "STOP",
    "UGA": "STOP"
}


def proteins(strand):

    codons = [strand[i:i+3] for i in range(0, len(strand), 3)]  # translate strand string to the list of codons

    prot = []  # list of proteins

    for codon in codons:  # find protein for each codon
        if codon in PROTEINS.keys() and PROTEINS[codon] == "STOP":
            break
        elif codon in PROTEINS.keys():
            prot.append(PROTEINS[codon])
        else:
            raise Exception("Codon", codon, "can not be translated to Protein")
    return prot
