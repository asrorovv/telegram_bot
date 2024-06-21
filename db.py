import psycopg2 as psql


class Database:
    @staticmethod
    def connect(query: str, query_type: str):
        db = psql.connect(
            database='tg_bot',
            user='postgres',
            pasword='muhammad0077',
            host='localhost',
            port='5432'
        )

        cursor = db.commit()
        data = ['insert', 'delete']
        cursor.execute(query)
        if query_type in data:
            return db.commit()
        else:
            return cursor.fetchall()

    @staticmethod
    async def check_user_id(user_id: int):
        query = f"SELECT * FROM users WHERE user_id = {user_id}"
        check_user = await Database.connect(query, query_type='select')
        if len(check_user) == 1:
            print('<>', check_user)
            return True
        return False