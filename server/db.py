import cryptograths as crpt
import psycopg2
from config import USER, PASSWORD, DATABASE


class DB:
    def __init__(self) -> None:
        try:
    # connect to exist database
            self.connection = psycopg2.connect(
                 host="localhost", user=USER, password=PASSWORD, database=DATABASE
            )
            self.connection.autocommit = True
        except Exception as _ex:
            print("[INFO] Error while working with PostgreSQL", _ex)


    def create_db(self):
        with self.connection.cursor() as cursor:
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS iktib (
                    id                  serial PRIMARY KEY,
                    name                varchar(32) NOT NULL,
                    password            varchar(64)  NOT NULL,
                    contraindications  varchar(512) NOT NULL
                );
                """)

            # connection.commit()
            print("[INFO] Table created successfully")
    def create_user(self, name, password, contraindications):
        f = self.__read_one("iktib", "id", f"name = '{name}'")
        if f:
            return 'User with this name already exist'
        passwordcr = crpt.hashing(password)
        return self.__write("iktib", "name, password, contraindications", f"'{name}', '{passwordcr}', '{contraindications}'")

    def get_contraindications(self, name, password):
        data = self.__read_one("iktib", "password,contraindications", f"name = '{name}'")
        if data and crpt.checking_hash(password, data[0]):
            return data[1]
        return False
    def edit_contraindications(self, name, password,contraindications):
        data = self.__read_one("iktib", "password,contraindications", f"name = '{name}'")
        if data and crpt.checking_hash(password, data[0]):
            return self.__update("iktib", f"contraindications = '{contraindications}' ", f"name = '{name}'")
        return False

    def __write(self, table, param, values):
        with self.connection.cursor() as cursor:
            cursor.execute(f"""INSERT INTO {table} ({param}) VALUES ({values});""")
            return True
        return False

    def __read(self, table, param):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(f"""SELECT {param} FROM {table}""")
                return cursor.fetchall()
        except:
            return False

    def __read_one(self, table, param, values):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(f"""SELECT {param} FROM {table} WHERE {values}""")
                return cursor.fetchone()
        except:
            return False

    def __update(self, table, seter, condition):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(f"UPDATE {table} SET {seter} WHERE {condition}")
            return True
        except:
            return False

    def __delete(self, table, column, values):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(f"DELETE FROM {table} WHERE {column} = '{values}'")
                return True
        except:
            return False

    def close(self):
        self.connection.close()
        print("[INFO] PostgreSQL connection closed")

if __name__ == '__main__':
    db = DB()
    db.close()