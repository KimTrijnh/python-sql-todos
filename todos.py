# db_utils.py
import os  
import sqlite3
import fire


# create a default path to connect to and create (if necessary) a database
# called 'database.sqlite3' in the same directory as this script
DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'database.sqlite3')

def db_connect(db_path=DEFAULT_PATH):  
    con = sqlite3.connect(db_path)
    print("connected to", db_path)
    return con


def create_db():
    con = db_connect()
    sql="""
        CREATE TABLE IF NOT EXISTS todos (
        id INTEGER PRIMARY KEY,
        text TEXT NOT NULL
    )
    """
    cur = con.cursor()
    cur.execute(sql)
    con.close()


def add_todo(text, due_date, project_id):
    con = db_connect()
    sql="""
    INSERT INTO todos (text, due_date, project_id)
    VALUES (?, ?, ?)
    """
    cur = con.cursor()
    cur.execute(sql, (text, due_date, project_id))
    con.commit()

    my_sql="""
    SELECT * FROM todos
    """ 
    cur.execute(my_sql)
    print('new todo is added')
    result = cur.fetchall()
    for row in result:
        print(row)
    con.close()


def remove_all_row(table_name):
    con = db_connect()
    sql="""
    DELETE FROM {}
    """.format(table_name)
    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    con.close()
    print('all row deleted', table_name)    


def add_column(table_name, column):
    con= db_connect()
    sql="""
    ALTER TABLE {}
    ADD {}
    """.format(table_name, column)
    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    con.close()
    print('new collum', column, 'is added to', table_name)

def update_row(table_name, update_set, id):
    con = db_connect()
    sql="""
    UPDATE {}
    SET {}
    WHERE id={}
    """.format(table_name, update_set, id,)
    cur = con.cursor()
    cur.execute(sql)
    print('row', id, 'is updated')
    print(sql)
    con.commit()
    con.close()

def mark_completed(table_name, id):
    con= db_connect()
    sql="""
    UPDATE {}
    SET status=1
    WHERE id=?
    """.format(table_name,)
    cur = con.cursor()
    cur.execute(sql, (id,))
    con.commit()
    con.close()
    print(id, 'completed')

def list(status, project_id, order):
    con = db_connect()
    if status == 'all':
        sql="""
        SELECT * FROM todos
        """
    else: 
        sql="""
        SELECT * FROM todos 
        WHERE status={}
        ORDER BY due_date ASC
        """.format(status,)
    
    cur = con.cursor()
    cur.execute(sql)
    con.commit
    result = cur.fetchall()
    for i in result:
        print(i)
    con.close()

def test():
    a="hi"
    sql="""abc""" + a+  """ztz"""
    print(sql)

if __name__ == '__main__':
  fire.Fire()

