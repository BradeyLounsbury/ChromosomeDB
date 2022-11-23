import pandas as pd

def input_to(table, values, cursor):
    cursor.execute("INSERT INTO {} VALUES({})".format(table, values))

def delete_from(table, att, boolean, result, cursor):
    cursor.execute("DELETE FROM {} WHERE {} {} {}".format(table, att, boolean, result))

def input_to_dn(cursor):
    # interactions = pd.read_csv('DN_interactions.txt')
    with open('DN_interactions.txt', 'r') as f:
        next(f)
        for line in f:
            chromosome, rest = line.split(':', 1)
            locus_1_start, rest = rest.split('-', 1)
            locus_1_end, rest = rest.split('\t', 1)
            _, rest = rest.split(':', 1)
            locus_2_start, locus_2_end = rest.split('-', 1)
            cursor.execute("INSERT INTO dn_interactions (Chromosome, Locus_1_start, Locus_1_end, Locus_2_start, Locus_2_end) VALUES(\"{}\", {}, {}, {}, {})".format(chromosome, locus_1_start, locus_1_end, locus_2_start, locus_2_end))

def input_to_pgn(cursor):
    with open('PGN_interactions.txt', 'r') as f:
        next(f)
        for line in f:
            chromosome, rest = line.split(':', 1)
            locus_1_start, rest = rest.split('-', 1)
            locus_1_end, rest = rest.split('\t', 1)
            _, rest = rest.split(':', 1)
            locus_2_start, locus_2_end = rest.split('-', 1)
            cursor.execute("INSERT INTO pgn_interactions (Chromosome, Locus_1_start, Locus_1_end, Locus_2_start, Locus_2_end) VALUES(\"{}\", {}, {}, {}, {})".format(chromosome, locus_1_start, locus_1_end, locus_2_start, locus_2_end))

def input_to_motif(cursor):
    with open('50_TF.tsv', 'r') as f:
        next(f)
        for line in f:
            name, _, _, length, quality, f_name, entrez, uniprot = line.split('\t')
            # print("{} {} {} {} {} {}".format(name, length, quality, f_name, entrez, uniprot))
            if entrez != '':
                cursor.execute("INSERT INTO motif VALUES(\"{}\", \"{}\", \"{}\", {}, {}, \"{}\")".format(name, f_name, quality, entrez, length, uniprot))
            else: cursor.execute("INSERT INTO motif VALUES(\"{}\", \"{}\", \"{}\", {}, {}, \"{}\")".format(name, f_name, quality, 0, length, uniprot))

def input_to_gene(conn):
    genes = pd.read_csv('Expression_PGN_DN_filter_repeat_gene.csv')
    genes.to_sql('gene', conn, if_exists='append', index=False)
