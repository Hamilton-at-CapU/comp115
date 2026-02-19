'''
  Data definition for the Standard Genetic Code
  source: https://en.wikipedia.org/wiki/Genetic_code#Standard_codon_tables
'''
# A Dictionary that maps each Amino Acid name to the set of Codons that encodes it
GENETIC_CODE = {
  'Alanine'       : ('GCT', 'GCC', 'GCA', 'GCG'),
  'Arginine'      : ('CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'),
  'Asparagine'    : ('AAT', 'AAC'),
  'Aspartic acid' : ('GAT', 'GAC'),
  'Cysteine'      : ('TGT', 'TGC'),
  'Glutamine'     : ('CAA', 'CAG'),
  'Glutamic acid' : ('GAA', 'GAG'),
  'Glycine'       : ('GGT', 'GGC', 'GGA', 'GGG'),
  'Histidine'     : ('CAT', 'CAC'),
  'Isoleucine'    : ('ATT', 'ATC', 'ATA'),
  'Leucine'       : ('TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'),
  'Lysine'        : ('AAA', 'AAG'),
  'Methionine'    : ('ATG', ), 
  'Phenylalanine' : ('TTT', 'TTC'),
  'Proline'       : ('CCT', 'CCC', 'CCA', 'CCG'),
  'Serine'        : ('TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'),
  'Threonine'     : ('ACT', 'ACC', 'ACA', 'ACG'),
  'Tryptophan'    : ('TGG', ),
  'Tyrosine'      : ('TAT', 'TAC'),
  'Valine'        : ('GTT', 'GTC', 'GTA', 'GTG'), 
  'START'         : ('ATG', ),
  'STOP'          : ('TAA', 'TGA', 'TAG'),
}

print('lookup.py has been imported, GENETIC_CODE dictionary is available.')
