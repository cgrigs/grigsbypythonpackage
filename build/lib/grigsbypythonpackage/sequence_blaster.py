"""
Recieves a FASTA file format. Writes the results for a BLAST search to a specified file.

Provies the fuction with a FASTA file containg the sequence of a specific taxon, the file in which to write the BLAST file too.

The file must be in FASTA format

Parameters
-------------
arg1: fasta_path
    A path to the file containg the molecular data
arg2: results_path
    A path to the file in whcih you wish to write the results of the BLAST search file to

Returns
------------
Does not return anything
"""

from Bio.Blast import NCBIWWW
from Bio import SeqIO
import os

def sequence_blaster(fasta_path, results_path):
    
    record = SeqIO.read(fasta_path, format = "fasta")
    results = NCBIWWW.qblast("blastn", "nt", record.format("fasta"))
    
    save_file = open(results_path, "w")
    save_file.write(results.read())
    save_file.close()
    
    assert os.stat(results_path).st_size != 0