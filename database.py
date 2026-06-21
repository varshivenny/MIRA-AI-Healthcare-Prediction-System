import sqlite3


def connection():

    return sqlite3.connect(
    "database/mira.db"
    )


def create():

    con=connection()

    con.execute(
    """
CREATE TABLE IF NOT EXISTS patients(

id INTEGER PRIMARY KEY,
name TEXT,
dob TEXT,
email TEXT,
glucose REAL,
haemoglobin REAL,
cholesterol REAL,
remarks TEXT

)
"""
)

    con.commit()



def insert(values):

    con=connection()

    con.execute(

"""
INSERT INTO patients VALUES
(NULL,?,?,?,?,?,?,?)
""",

values

)

    con.commit()



def show():

    con=connection()

    return con.execute(
    "SELECT * FROM patients"
    ).fetchall()



def update(id,remark):

    con=connection()

    con.execute(

"UPDATE patients SET remarks=? WHERE id=?",

(
remark,
id
)

)

    con.commit()



def delete(id):

    con=connection()

    con.execute(

"DELETE FROM patients WHERE id=?",

(id,)

)

    con.commit()