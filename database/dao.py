from database.DB_connect import DBConnect
from model.team import Team as t
class DAO:
    @staticmethod
    def get_anni():
        conn = DBConnect.get_connection()

        start = 1980

        cursor = conn.cursor()
        query = """SELECT MAX(year)
                    FROM team
                    WHERE year >= %s"""

        cursor.execute(query, (start,))

        (end,) = cursor.fetchone()

        cursor.close()
        conn.close()
        return start,end

    @staticmethod
    def get_squadre_anno(anno):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT t.id, t.year, t.team_code, t.name, COALESCE(SUM(s.salary), 0) AS tot_salary
                    FROM team t
                    LEFT JOIN salary s ON t.id = s.team_id
                    WHERE t.year = %s
                    GROUP BY t.id, t.year, t.team_code, t.name; """

        cursor.execute(query,(anno,))

        for row in cursor:
            result.append(t(**row))

        cursor.close()
        conn.close()
        return result