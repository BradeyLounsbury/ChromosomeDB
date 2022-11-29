def query_1(cell, cursor):
    if cell == "1":
        cursor.execute("SELECT EXISTS (SELECT 1 FROM dn_specific) AS result")
        result = cursor.fetchone()
        if result[0] == 0:    # dn_specific is empty
            cursor.execute("SELECT * FROM dn_interactions EXCEPT SELECT * FROM pgn_interactions")
            for row in cursor.fetchall():
                values = []
                for item in row:
                    values.append(item)
                cursor.execute("INSERT INTO dn_specific (Chromosome, Locus_1_start, Locus_1_end, Locus_2_start, Locus_2_end) VALUES(\"{}\", {}, {}, {}, {})".format(values[0], values[1], values[2], values[3], values[4]))
                print(row)
        else: 
            cursor.execute("SELECT * FROM dn_interactions EXCEPT SELECT * FROM pgn_interactions")
            for row in cursor.fetchall():
                print(row)
    elif cell == "2":
        cursor.execute("SELECT EXISTS (SELECT 1 FROM pgn_specific) AS result")
        result = cursor.fetchone()
        if result[0] == 0:    # pgn_specific is empty
            cursor.execute("SELECT * FROM pgn_interactions EXCEPT SELECT * FROM dn_interactions")
            for row in cursor.fetchall():
                values = []
                for item in row:
                    values.append(item)
                cursor.execute("INSERT INTO pgn_specific (Chromosome, Locus_1_start, Locus_1_end, Locus_2_start, Locus_2_end) VALUES(\"{}\", {}, {}, {}, {})".format(values[0], values[1], values[2], values[3], values[4]))
                print(row)
        else: 
            cursor.execute("SELECT * FROM pgn_interactions EXCEPT SELECT * FROM dn_interactions")
            for row in cursor.fetchall():
                print(row)

def query_2(step, conn):
    if step == "1":
        c_1 = conn.cursor()

        c_1.execute("""CREATE TABLE dnmi1 AS SELECT interaction.InteractionID, motif.Model, motif.Chromosome, motif.Locus_start, motif.Locus_end
        FROM dn_motif_intersect AS motif
        INNER JOIN dn_interactions AS interaction
        WHERE motif.Chromosome = interaction.Chromosome 
        AND motif.Locus_start = interaction.Locus_1_start 
        AND motif.Locus_end = interaction.Locus_1_end""")
        c_1.execute("""CREATE TABLE dnmi2 AS SELECT interaction.InteractionID, motif.Model, motif.Chromosome, motif.Locus_start, motif.Locus_end
        FROM dn_motif_intersect AS motif
        INNER JOIN dn_interactions AS interaction
        WHERE motif.Chromosome = interaction.Chromosome 
        AND motif.Locus_start = interaction.Locus_2_start 
        AND motif.Locus_end = interaction.Locus_2_end""")

        c_1.execute("""CREATE TABLE dn_pairs (
        Model1 STRING,
        Model2 STRING,
        InteractionID)""")

        c_1.execute("""INSERT INTO dn_pairs
        SELECT dnmi1.Model, dnmi2.Model, dnmi1.InteractionID
        FROM dnmi1
        INNER JOIN dnmi2
        WHERE dnmi1.InteractionID = dnmi2.InteractionID""")
    elif step == "2":
        c_1 = conn.cursor()

        c_1.execute("""CREATE TABLE pgnmi1 AS SELECT interaction.InteractionID, motif.Model, motif.Chromosome, motif.Locus_start, motif.Locus_end
        FROM pgn_motif_intersect AS motif
        INNER JOIN pgn_interactions AS interaction
        WHERE motif.Chromosome = interaction.Chromosome 
        AND motif.Locus_start = interaction.Locus_1_start 
        AND motif.Locus_end = interaction.Locus_1_end""")
        c_1.execute("""CREATE TABLE pgnmi2 AS SELECT interaction.InteractionID, motif.Model, motif.Chromosome, motif.Locus_start, motif.Locus_end
        FROM pgn_motif_intersect AS motif
        INNER JOIN pgn_interactions AS interaction
        WHERE motif.Chromosome = interaction.Chromosome 
        AND motif.Locus_start = interaction.Locus_2_start 
        AND motif.Locus_end = interaction.Locus_2_end""")

        c_1.execute("""CREATE TABLE pgn_pairs (
        Model1 STRING,
        Model2 STRING,
        InteractionID)""")

        c_1.execute("""INSERT INTO pgn_pairs
        SELECT pgnmi1.Model, pgnmi2.Model, pgnmi1.InteractionID
        FROM pgnmi1
        INNER JOIN pgnmi2
        WHERE pgnmi1.InteractionID = pgnmi2.InteractionID""")
    elif step == "3":
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE udn_pairs AS SELECT * FROM dn_pairs EXCEPT SELECT * FROM pgn_pairs""")
    elif step == "4":
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE upgn_pairs AS SELECT * FROM pgn_pairs EXCEPT SELECT * FROM dn_pairs""")

def query_3(cursor):
    cursor.execute("""CREATE TABLE dn_interest
    AS SELECT * FROM dn_interactions
    WHERE dn_interactions.InteractionID 
    IN (SELECT InteractionID FROM udn_pairs)""")
    cursor.execute("""CREATE TABLE pgn_interest 
    AS SELECT * FROM pgn_interactions
    WHERE pgn_interactions.InteractionID 
    IN (SELECT InteractionID FROM upgn_pairs)""")

def query_4(step, cursor):
    if step == "1":
        cursor.execute("""SELECT * FROM gene
        WHERE gene.DN_expression = 0 OR gene.PGN_expression = 0""")
        for row in cursor.fetchall():
            print(row)
    elif step == "2":
        cursor.execute("""SELECT * FROM gene
        WHERE gene.Expression_diff > 0
        ORDER BY gene.Expression_diff DESC
        LIMIT 10""")
        for row in cursor.fetchall():
            print(row)
        cursor.execute("""SELECT * FROM gene
        WHERE gene.Expression_diff < 0
        ORDER BY gene.Expression_diff ASC
        LIMIT 10""")
        for row in cursor.fetchall():
            print(row)

def query_5(cursor):
    cursor.execute()