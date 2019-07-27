import sqlite3


class DbDao():
    # Database creation and checking of tables existance
    def __init__(self):
        self.conn = sqlite3.connect('mydatabase.sql')
        self.cursor = self.conn.cursor()

    def db_tab_creation(self):
        # Getting table names from database
        tabnames = {x[0] for x in self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")}

        # Cheching tables existance and its creation
        if "Groups" in tabnames:
            print('TABLE Groups EXISTS')
        else:
            self.cursor.execute("""CREATE TABLE Groups
               (Group_id int NOT NULL,
                Group_member int, 
                Refresh_date DATE NOT NULL, 
                PRIMARY KEY(Group_id, Refresh_date))""")
            print('TABLE Groups HAS BEEN CREATED')
        if "Groupnames" in tabnames:
            print('TABLE Groupnames EXISTS')
        else:
            self.cursor.execute("""CREATE TABLE Groupnames
               (Group_id int NOT NULL,
                Groupname VARCHAR,
                PRIMARY KEY(Group_id))""")
            print('TABLE Groupnames HAS BEEN CREATED')

    # Data saving
    def save(self, data):
        for x in data:
            self.cursor.execute("""INSERT INTO Groups(Group_id, Group_member, Refresh_date)
                                VALUES(%d, %d, DATETIME('NOW', 'localtime'))""" % (x[0], x[2]))
            self.cursor.execute("INSERT OR REPLACE INTO Groupnames(Group_id, Groupname) VALUES(%d, '%s')" % (x[0], x[1]))
        self.conn.commit()

    # ----------------- ADDITIONAL METHODS ---------------------------------
    # Print the database
    def data_select(self):
        print(list(self.cursor.execute("SELECT * FROM Groups")))
        print(list(self.cursor.execute("SELECT * FROM Groupnames")))

    # Database cleaner
    def cleaner(self):
        self.cursor.execute("DROP TABLE Groups")
        self.cursor.execute("DROP TABLE Groupnames")

    # Cheat method to use DB. Don't use it))
    def cheat_method(self, sql_msg):
        self.cursor.execute(sql_msg)
        self.conn.commit()