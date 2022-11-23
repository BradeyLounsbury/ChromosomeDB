import sqlite3 as sql
from create_tables import create_tables
from display import display, display_att
from input import input_to, delete_from, input_to_dn, input_to_pgn, input_to_gene, input_to_motif
import pandas as pd

if __name__ == "__main__":
    conn = sql.connect('database.db')
    cursor = conn.cursor()
    
    # input_to_dn(cursor)
    # input_to_pgn(cursor)
    input_to_motif(cursor)
    # input_to_gene(conn)
    conn.commit()

    while True :
        query = input("""
        1. Create tables (don't do this one)
        2. Input into table
        3. Display a table
        4. Display an entity from some query
        5. Delete an entity from a table
        6. Exit
        
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
                display("interaction", cursor)
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
            conn.close()
            break
        else:
            print("sorry not an option")