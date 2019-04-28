import pymysql


class FindData(object):
    def __init__(self, connect_info):
        self.connect_info = connect_info

    def test_db(self):
        connect = self.connect_info
        db = pymysql.connect(connect[0],connect[1],connect[2],connect[3],connect[4])
        cursor = db.cursor(cursor=pymysql.cursors.DictCursor)

        sql = "SELECT * from news;"

        try:
            # Execute the SQL command
            cursor.execute(sql)
            results = cursor.fetchall()


        except:
            # Rollback in case there is any error
            db.rollback()

        # disconnect from server
        db.commit()
        cursor.close()
        db.close()
        return results
        pass

