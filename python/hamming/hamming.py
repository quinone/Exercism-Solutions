def distance(strand_a, strand_b):
    count = 0
    for n, m in zip(strand_a, strand_b):
        count+=1
    return count
