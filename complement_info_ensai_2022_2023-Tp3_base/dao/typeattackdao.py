from dao.db_connection import DBConnection

class TypeAttackDao :
    def find_id_by_label (self, type_attack) :
        connection = DBConnection().connection
        with connection.cursor() as cursor :
            cursor.execute(
                "SELECT id_attack_type FROM attack_type WHERE attack_type_name =%(type_attack)s",
                {"type_attack": type_attack}
                )
            res = cursor.fetchone()
        print(res["id_attack_type"])
        return res["id_attack_type"]

    def find_all (self) :
        connection = DBConnection().connection
        with connection.cursor() as cursor :
            cursor.execute(
                "SELECT * FROM attack_type"
            )
            res = cursor.fetchall()
        res_tab = []
        for element in res :
            res_tab.append([element["id_attack_type"], element["attack_type_name"]])
        print(res_tab)
        return res_tab
