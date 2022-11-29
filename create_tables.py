import sqlite3 as sql

def create_tables(cursor):
    # DN motif intersect
    # dn_motif_table = """CREATE TABLE dn_motif_intersect (
    #     Chromosome STRING,
    #     Locus_start INT,
    #     Locus_end INT,
    #     Motif_start INT,
    #     Motif_end INT,
    #     Model STRING,
    #     Threshold REAL,
    #     Direction CHAR);"""
    # cursor.execute(dn_motif_table)

    # # PGN motif intersect
    # pgn_motif_table = """CREATE TABLE pgn_motif_intersect (
    #     Chromosome STRING,
    #     Locus_start INT,
    #     Locus_end INT,
    #     Motif_start INT,
    #     Motif_end INT,
    #     Model STRING,
    #     Threshold REAL,
    #     Direction CHAR);"""
    # cursor.execute(pgn_motif_table)

    # Specific Interaction
    # dn_specific_table = """CREATE TABLE dn_specific (
    # Chromosome STRING,
    # Locus_1_start INT,
    # Locus_1_end INT,
    # Locus_2_start INT,
    # Locus_2_end INT
    # );"""
    # cursor.execute(dn_specific_table)

    # # Specific Interaction
    # pgn_specific_table = """CREATE TABLE pgn_specific (
    # Chromosome STRING,
    # Locus_1_start INT,
    # Locus_1_end INT,
    # Locus_2_start INT,
    # Locus_2_end INT
    # );"""
    # cursor.execute(pgn_specific_table)

    # # # Interaction
    # dn_interaction_table = """CREATE TABLE dn_interactions (
    # InteractionID STRING,
    # Chromosome STRING,
    # Locus_1_start INT,
    # Locus_1_end INT,
    # Locus_2_start INT,
    # Locus_2_end INT
    # );"""
    # cursor.execute(dn_interaction_table)

    # # # Interaction
    # pgn_interaction_table = """CREATE TABLE pgn_interactions (
    # InteractionID STRING,
    # Chromosome STRING,
    # Locus_1_start INT,
    # Locus_1_end INT,
    # Locus_2_start INT,
    # Locus_2_end INT
    # );"""
    # cursor.execute(pgn_interaction_table)

    # # Locus
    # locus_table = """CREATE TABLE locus (
    # Chromosome STRING,
    # Start INT,
    # End INT,
    # ID INT,
    # PRIMARY KEY(ID));"""
    # # cursor.execute(locus_table)

    # # Motif
    # motif_table = """CREATE TABLE motif (
    # Name STRING,
    # Family_name STRING,
    # Quality STRING,
    # Entrez INT,
    # Length INT,
    # Uni_proc_ID STRING,
    # PRIMARY KEY(Name));"""
    # cursor.execute(motif_table)

    # Gene
    # gene_table = """CREATE TABLE gene (
    # Name STRING,
    # Chromosome STRING,
    # Start INT,
    # End INT,
    # DN_expression REAL,
    # Length INT,
    # PGN_expression REAL,
    # Expression_diff REAL,
    # PRIMARY KEY(Name));"""
    # cursor.execute(gene_table)
    cursor.execute()