import sqlite3 as sql

def create_tables(cursor):
    # Chromosome
    chromosome_table = """CREATE TABLE chromosome (
    Number text,
    Cell_type text,
    PRIMARY KEY(Number));"""
    cursor.execute(chromosome_table)

    # Interaction
    interaction_table = """CREATE TABLE interaction (
    Locus1 text,
    Locus2 text,
    ID INT,
    PRIMARY KEY(ID));"""
    cursor.execute(interaction_table)

    # Locus
    locus_table = """CREATE TABLE locus (
    Chromosome text,
    Start text,
    End text,
    ID INT,
    PRIMARY KEY(ID));"""
    cursor.execute(locus_table)

    # Motif
    motif_table = """CREATE TABLE motif (
    ID text,
    Chromosome text,
    Start text,
    End text,
    Name text,
    Family_name text,
    Quality text,
    Entrex text,
    Length text,
    Unit_proc_ID text,
    Threshold text,
    PRIMARY KEY(ID));"""
    cursor.execute(motif_table)

    # Gene
    gene_table = """CREATE TABLE gene (
    Name text,
    Chromosome text,
    Start text,
    End text,
    DN_expression text,
    Length text,
    PGN_expression text,
    PRIMARY KEY(Name));"""
    cursor.execute(gene_table)