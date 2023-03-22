import pandas as pd
from Bio import SeqIO

def get_parent_seq(handle: str) -> str:
    for record in SeqIO.parse(handle, 'fasta'):
        if "parent" in record.id:
            #print(record)
            return record.seq

def get_mutations(handle: str, parent: str):

    mut_dict: dict = {}
    counter_lim: int = len(parent)

    for record in SeqIO.parse(handle, 'fasta'):
        seq = record.seq
        id = record.id
        for i in range(counter_lim):
            parent_nucleotide: str = parent[i]
            sequence_nucleotide: str = seq[i]
            if sequence_nucleotide != parent_nucleotide:
                if id not in mut_dict.keys():
                    mut_dict[id] = [(i+1, f"{parent_nucleotide} --> {sequence_nucleotide}")]

                else:
                    mut_dict[id].append((i+1, f"{parent_nucleotide} --> {sequence_nucleotide}"))

    return mut_dict

def get_dataframe(mut_dict: dict):

    max_columns: int = 0

    for x in mut_dict.values():
        no_of_columns = len(x)
        if max_columns < no_of_columns:
            max_columns = no_of_columns

    #print(max_columns)

    df = pd.DataFrame.from_dict(mut_dict, orient='index', columns=[y for y in range(1, max_columns+1)])
    #print(df)
    df.to_csv("2023-03-22_teln_mutants_101_to_195.csv")

    pass


def main():
    #handle: str = 'test_file.txt'
    handle: str = 'R1_AA.txt'
    wt_seq: str = get_parent_seq(handle)
    mut_dict: dict = get_mutations(handle, wt_seq)
    #print(mut_dict)
    get_dataframe(mut_dict)

if __name__ == '__main__':
    main()
