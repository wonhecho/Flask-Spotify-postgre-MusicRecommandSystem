from    flask       import jsonify
import json
import psycopg2

class BaseDao:

    def __init__(self, database):
        self.db = database

    def getConnection(self):
        try:
            conn   = psycopg2.connect(
                    host='localhost',
                    dbname='test',
                    user = 'postgres',
                    password='root',
                    port='5432')
        except psycopg2.OperationalError as e:
            print("Database Connect Error")
        return conn

    def createTable(self):
        conn        = self.getConnection()
        cursor      = conn.cursor()

        result      = {}


        try:
            cursor.execute("CREATE TABLE User_table (title text, year text, date timestamp with time zone);")
            conn.commit()
            
        except Exception as e:
            result["result"]=0
            result["msg"] = str(e)

        finally:
            result["result"] = 0
            result["msg"] = "변환"

            cursor.close()
            conn.close()	

        return result
    
    def InsertTable(self,data):

        conn        = self.getConnection()
        cursor      = conn.cursor()
        Dummy_data  = data
        result      = {}
        result["result"] = 0
        print(Dummy_data[0])
        print("INSERT INTO user_table (title, year, date) VALUES ('"+Dummy_data[0]['name']+"','"+str(Dummy_data[0]['year'])+"',now());")
        
        try:
            cursor.execute("INSERT INTO user_table (title, year, date) VALUES ('"+Dummy_data[0]['name']+"','"+str(Dummy_data[0]['year'])+"',now());")
            conn.commit()

        except Exception as e:
            result["result"]=0
            result["msg"] = str(e)

        finally:
            result["result"] = 0
            result["msg"] = "데이터 삽입"
            cursor.close()
            conn.close()
        return result
    
    def CheckTable(self):
        conn        = self.getConnection()
        cursor      = conn.cursor()
        result      = {}
        try:
            cursor.execute("SELECT column_name FROM information_schema.columns WHERE table_name = 'recommand_table';")
            conn.commit()

        except psycopg2.OperationalError  as e:
            result["result"]=0
            result["msg"] = str(e)

        finally:
            if (bool(cursor.rowcount)) is False:
                result["result"] = 0
                result["msg"] = "테이블이 없습니다"
            else:
                result["result"] = 1
                result["msg"] = "테이블 존재 확인"
            cursor.close()
            conn.close()
        return result
    def CreateRecommendTable(self):
        conn        = self.getConnection()
        cursor      = conn.cursor()

        result      = {}

        try:
            cursor.execute("CREATE TABLE Recommend_Table (title text, year text);")
            conn.commit()
            
        except Exception as e:
            result["result"]=0
            result["msg"] = str(e)

        finally:
            result["result"] = 1
            result["msg"] = "생성"

            cursor.close()
            conn.close()
        return result	
    def SelectPlaylist(self):

        conn        = self.getConnection()
        cursor      = conn.cursor()

        result      = {}

        try:
            cursor.execute("SELECT title,year FROM user_table ORDER BY date DESC;")
            data = cursor.fetchall()   
            conn.commit()
            
        except Exception as e:
            result["result"]=0
            result["msg"] = str(e)

        finally:
            result["result"] = 1
            result["msg"] = "생성"
            result["data"] = data
            cursor.close()
            conn.close()
        return result
    def InsertReommendTable(self,data):

        conn        = self.getConnection()
        cursor      = conn.cursor()
        recommend   = data
        result      = {}
        result["result"] = 0
        print(recommend[0])
        print("INSERT INTO recommend_table (title, year) VALUES ('"+recommend[0]['name']+"','"+str(recommend[0]['year'])+"')")
        
        try:
            cursor.execute("INSERT INTO recommend_table (title, year) VALUES ('"+recommend[1]['name']+"','"+str(recommend[1]['year'])+"')")
            conn.commit()

        except Exception as e:
            result["result"]=0
            result["msg"] = str(e)

        finally:
            result["result"] = 0
            result["msg"] = "추천 데이터 삽입"
            cursor.close()
            conn.close()
        return result
    	



