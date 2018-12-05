"""
Recieves a specific DNA sequence set. Reformats to FASTA file format. Writes the FASTA file to a specified file.

Provies the fuction with the DNA sequence, the file which to write the FASTA file to, the specific taxon in which you would like to subset, and the beginning and end indices of the gene in whhich you will be preforming the BLAST search on.

The the gene indicies will be provied in seperate arguements(0, 1). Rather than, [0:1]

Parameters
-------------
arg1: sequence_set
    A set of molecular data
arg2: out_file
    A path to the file in whcih you wish to write the FASTA file to
arg3: taxon
    Specify the specific taxon in which you wish to subset. Puth the name of the taxon quotations marks.
arg4: gene_start
    The first number of the specific gene you will be searching
arg5: gene_end
    The first number of the specific gene you will be searching

Returns
------------
Does not return anything
"""
import dendropy
import os

def sequence_cleanup(sequence_set, out_file, taxon, gene_start, gene_end):
    assert sequence_set[taxon]
    
    my_taxon_sequence = sequence_set[taxon].symbols_as_string()
    my_taxon_sequence = my_taxon_sequence[gene_start: gene_end]
    ofile = open(out_file, "w")
    ofile.write(">" + taxon + "\n" + my_taxon_sequence + "\n")
    ofile.close()
    
    assert os.stat(out_file).st_size != 0