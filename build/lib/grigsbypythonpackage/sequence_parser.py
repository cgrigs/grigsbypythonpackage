""""""""""""""""""""""""""""""""""""""""""""""
This function parsers the information from 
the BLAST search done by the function 
sequence_blaster. Sorry for the lack of 
creativity.
"""""""""""""""""""""""""""""""""""""""""""""""

from Bio.Blast import NCBIXML

def sequence_parser(results_path):
    assert os.path.exists(filepath)

    parsed = NCBIXML.read(open(results_path))

    alignment = parsed.alignments
    for every_alignment in alignment:
        print(every_alignment)