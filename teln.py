import pandas as pd
from Bio import SeqIO

def get_parent_seq(handle: str) -> str:
    for record in SeqIO.parse(handle, 'fasta'):
        if "parent" in record.id:
            #print(record)
            return record.seq

def get_mutations(handle: str, parent: str):

    mut_dict = {}
    counter_lim = len(parent)

    for record in SeqIO.parse(handle, 'fasta'):
        seq = record.seq
        id = record.id
        for i in range(counter_lim):
            if seq[i] != parent[i]:
                if id not in mut_dict.keys():
                    mut_dict[id] = [(i+1, seq[i])]

                else:
                    mut_dict[id].append((i+1, seq[i]))

    return mut_dict

def get_dataframe(mut_dict: dict):

    df = pd.DataFrame.from_dict(mut_dict, orient='index')
    #print(df)
    df.to_csv("teln_mutants.csv")

    pass


def main():
    #handle: str = 'test_file.txt'
    handle: str = 'teln_mutants_fasta.txt'
    wt_seq: str = get_parent_seq(handle)
    mut_dict: dict = get_mutations(handle, wt_seq)
    #print(mut_dict)
    get_dataframe(mut_dict)

if __name__ == '__main__':
    main()
