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
        WHERE status={} AND project_id={}
        ORDER BY due_date {}
        """.format(status, project_id, order,)
    cur = con.cursor()
    cur.execute(sql)
    con.commit
    result = cur.fetchall()
    for i in result:
        print(i)
    con.close()

#TABLE projects
def create_tb_project():
    con = db_connect()
    sql="""
    CREATE TABLE IF NOT EXISTS projects (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        due_date DATE
    )
    """
    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    con.close()

def create_tb_users():
    con = db_connect()
    sql="""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        name text NOT NULL,
        email text
    )
    """
    cur= con.cursor()
    cur.execute(sql)
    con.commit()
    con.close()
    print('table_users is created')   

def add_user(name, email):
    con =db_connect()
    sql="""
    INSERT INTO users (name, email)
    VALUES (?, ?)
    """
    cur=con.cursor()
    cur.execute(sql,(name, email))
    con.commit()
    select_sql="""
    SELECT * FROM users
    """
    result= cur.execute(select_sql)
    for row in result:
        print(row)
    con.close()
    print('user', name, 'created')

def add_project(name, due_date):
    con=db_connect()
    sql="""
    INSERT INTO projects (name, due_date)
    VALUES (?, ?)
    """
    cur = con.cursor()
    cur.execute(sql,(name, due_date))
    con.commit()

    select_sql="""
    SELECT * FROM projects
    """
    con = cur.execute(select_sql)
    result=cur.fetchall()
    print(result)
    for row in result:
        print(row)
    con.close()


def add_user_id_column():
    con = db_connect()
    sql="""
    ALTER TABLE todos
    ADD user_id int
    """
    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    con.close()
    print('user_id addted to todos')


def assign_user(user_id, id):
    con=db_connect()
    sql="""
    UPDATE TABLE todos
    SET user_id={}
    WHERE id={}
    """.format(user_id, id)
    cur=con.cursor()
    cur.execute(sql, )
    con.commit()
    con.close()
    print('user_id', user_id)

#def add_user_id()
# def add_foreign_key():
#     con = db_connect()
#     sql="""
#     ALTER TABLE todos
#     ADD FOREIGN KEY (user_id) REFERENCES user(id)
#     """
#     cur = con.cursor()
#     cur.execute(sql)
#     con.commit()
#     con.close()

def alter_colum():
    con=db_connect()
    sql="""
    ALTER TABLE users
    ADD CONSTRAINT userId PRIMARY KEY (id);
    """
    cur =con.cursor()
    cur.execute(sql)
    con.commit()
    con.close()


def staff():
    con= db_connect()
    sql="""
    SELECT project_id, user_id FROM 
    todos JOIN users
    WHERE todos.user_id = users.id
    ORDER BY project_id ASC
    """
    cur=con.cursor()
    result = cur.execute(sql)
    for row in result:
        print(row)
    con.close()
    
def who_to_fire():
    con=db_connect()
    sql="""
    SELECT users.id, users.name FROM
    users LEFT JOIN todos
    ON users.id=todos.user_id
    WHERE project_id IS NULL
    """
    cur = con.cursor()
    result= cur.execute(sql)
    print(result)
    for row in result:
        print(row)
    con.close()

if __name__ == '__main__':
  fire.Fire()

