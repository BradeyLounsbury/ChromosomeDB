import sqlite3 as sql
from create_tables import create_tables
from display import display, display_att
from input import input_to, delete_from, input_to_dn, input_to_pgn, input_to_gene, input_to_motif, input_to_dn_motif, input_to_pgn_motif
from queries import query_1, query_2, query_3, query_4, query_5
import pandas as pd

if __name__ == "__main__":
    conn = sql.connect('database.db')
    cursor = conn.cursor()
    
    # input_to_dn(cursor)
    # input_to_pgn(cursor)
    # input_to_motif(cursor)
    # input_to_gene(cursor)
    # input_to_dn_motif(cursor)
    # input_to_pgn_motif(cursor)
    # conn.commit()

    while True :
        query = input("""
        1. Create tables (don't do this one)
        2. Input into table
        3. Display a table
        4. Display an entity from some query
        5. Delete an entity from a table
        6. Queries
        7. Exit
        
        """)

        if query == "1":
            create_tables(cursor)


        elif query == "2":
            table = input("""Which table:
            1. Interaction
            2. Locus
            3. Motif
            4. Gene
            """)
            if table == "1":
                display("interaction", cursor)
            elif table == "2":
                display("locus", cursor)
            elif table == "3":
                display("motif", cursor)
            elif table == "4":
                name = input("Name: ")
                chr = input("Chromosome (as chr_): ")
                start = input("Start: ")
                end = input("End: ")
                dn = input("DN_expression: ")
                length = input("Length: ")
                pgn = input("PGN_expression: ")
                values = "\"{}\", \"{}\", {}, {}, {}, {}, {}".format(name, chr, start, end, dn, length, pgn)
                input_to("gene", values, cursor)
                conn.commit()
            else:
                print("sorry try again")


        elif query == "3":
            table = input("""Which table:
            1. Interaction
            2. Locus
            3. Motif
            4. Gene 
            """)
            if table == "1":
                display("dn_interaction", cursor)
            elif table == "2":
                display("locus", cursor)
            elif table == "3":
                display("motif", cursor)
            elif table == "4":
                display("gene", cursor)
            else:
                print("sorry try again")


        elif query == "4":
            table = input("""Which table:
            1. Interaction
            2. Locus
            3. Motif
            4. Gene 
            """)

            att = input ("What attribute: ")
            boolean = input("What expression: ")
            result = input("What result: ")

            if table == "1":
                display_att("interaction", cursor)
            elif table == "2":
                display_att("locus", cursor)
            elif table == "3":
                display_att("motif", cursor)
            elif table == "4":
                display_att("gene", att, boolean, result, cursor)
            else:
                print("sorry try again")

        elif query == "5":
            table = input("""Which table:
            1. Interaction
            2. Locus
            3. Motif
            4. Gene 
            """)

            att = input ("What attribute: ")
            boolean = input("What expression: ")
            result = input("What result: ")
            
            if table == "1":
                display_att("interaction", cursor)
            elif table == "2":
                display_att("locus", cursor)
            elif table == "3":
                display_att("motif", cursor)
            elif table == "4":
                delete_from("gene", att, boolean, result, cursor)
                conn.commit()
            else:
                print("sorry try again")
        elif query == "6":
            q = input("""Which query:
            1. Interactions specific to a cell type
            2. Signature motif pairs
            3. Interesting interactions
            4. Genes expressed differently between cell types
            5. Expressed genes in the interesting interactions
            """)
            if q == "1":
                cell = input ("Which cell type:\n1. DN\n2. PGN ")
                query_1(cell, cursor)
                conn.commit()
            elif q == "2":                
                cell = input ("Which cell type:\n1. DN\n2. PGN ")
                query_2(cell, conn)
                conn.commit()
            elif q == "3":
                query_3(cursor)
                conn.commit()
            elif q == "4":
                step = input ("Which step:")
                query_4(step, cursor)
            elif q == "5":
                query_5(cursor)
            else:
                print("sorry not an option")
        elif query == "7":
            conn.close()
            break
        else:
            print("sorry not an option")