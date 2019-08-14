def distance(strand_a, strand_b):

    if len(strand_a) != len(strand_b):
        raise ValueError("Strands should have equal length")

    return len([d1 for d1, d2 in zip(strand_a, strand_b) if d1 != d2])

