"""
Reads in the the dna sequence
Provide as input the path to a phylip file
Must be a phylip file


Parameters
----------
arg1: DNA sequence
    A path to a phylip file containg a DNA sequence
    
Returns
-------
set
    A set of the DNA sequence
"""

import dendropy
import os

def sequence_reader(filepath):
    # check the file exist
    assert os.path.exists(filepath)
    # check if it is in the correct format
    sequence_set = dendropy.DnaCharacterMatrix.get(
    path = filepath, 
    schema="phylip"
)
    assert type(sequence_set) == dendropy.datamodel.charmatrixmodel.DnaCharacterMatrix
    return(sequence_set)