"""
Recieves the file path to the results of the BLAST search preformed in sequence_blaster.py 
The information is alignmed printed  


Parameters
-------------
arg1: results_path
    A path to the results from the BLAST search preformed in sequence_blaster.py

Returns
------------
Does not return anything
"""

from Bio.Blast import NCBIXML

def sequence_parser(results_path):
    assert os.path.exists(filepath)

    parsed = NCBIXML.read(open(results_path))

    alignment = parsed.alignments
    for every_alignment in alignment:
        print(every_alignment)