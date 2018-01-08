def dna_replication(dna):
    pairs = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    chromosone = [pairs[base] for base in dna.split(' ')]

    def codon_map(codon):

        codon_table = {
            'Ala': ['GCT', 'GCC', 'GCA', 'GCG'],
            'Arg': ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
            'Asn': ['AAT', 'AAC'],
            'Asp': ['GAT', 'GAC'],
            'Cys': ['TGT', 'TGC'],
            'Gln': ['CAA', 'CAG'],
            'Glu': ['GAA', 'GAG'],
            'Gly': ['GGT', 'GGC', 'GGA', 'GGG'],
            'His': ['CAT', 'CAC'],
            'Ile': ['ATT', 'ATC', 'ATA'],
            'Leu': ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'],
            'Lys': ['AAA', 'AAG'],
            'Met': ['ATG'],
            'Phe': ['TTT', 'TTC'],
            'Pro': ['CCT', 'CCC', 'CCA', 'CCG'],
            'Ser': ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'],
            'Thr': ['ACT', 'ACC', 'ACA', 'ACG'],
            'Trp': ['TGG'],
            'Tyr': ['TAT', 'TAC'],
            'Val': ['GTT', 'GTC', 'GTA', 'GTG'],
            'STOP': ['TAA', 'TGA', 'TAG']
        }

        lookup = [k for k, v in codon_table.items() if codon in v]
        return lookup[0]

    dna_split = dna.split(' ')
    codon_parts = [''.join(dna_split[i:i+3]) for i in range(0, len(dna_split), 3)]


    print(dna)
    print(list(map(codon_map, codon_parts)))
    print(' '.join(chromosone))

if __name__ == "__main__":
    input_1 = 'A A T G C C T A T G G C'
    input_2 = 'A T G T T T C G A G G C T A A'
    dna_replication(input_1)
    dna_replication(input_2)