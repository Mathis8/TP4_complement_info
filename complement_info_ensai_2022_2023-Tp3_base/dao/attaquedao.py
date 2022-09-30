from dao.db_connection import DBConnection

class AttaqueDao :
    def find_all_attack(self, limit, offset) :
        connection = DBConnection().connection
        with connection.cursor() as cursor :
            cursor.execute(
                "SELECT * FROM attack LIMIT %(limit)s OFFSET %(offset)s",
                {"limit": limit, "offset": offset}
            )
            res = cursor.fetchall()
        return res