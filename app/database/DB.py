from mysql.connector import errors

class DB:    
    def __init__(self, mysql):
        self.mysql = mysql

    def _start_conn(self):
        try:
            # print(self.mysql.pool_size)
            self.conn = self.mysql.get_connection()
            self.cur = self.conn.cursor(dictionary=True, buffered=True)
        except errors.PoolError as e:

            print(e)
            print('Closing  connection ')


    def _close_conn(self):
        try:
            self.conn.commit()
            self.cur.close()
        except:
            print("Exception Here")
        # finally:
        #     self.conn.close()