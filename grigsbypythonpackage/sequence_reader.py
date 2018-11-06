import dendropy

def sequence_reader(filepath):
    # check the file exist
    assert os.path.exists(filepath)
    # check if it is in the correct format
    sequence_set = dendropy.DnaCharacterMatrix.get(
    path = filepath,     
    schema="phylip"
)
      assert type(sequence_set) == dendropy.datamodel.charmatrixmodel.DnaCharacterMatrix 
    return (sequence_set)    