import mysql.connector
import dbconfig as cfg



class moviesDAO:
    connection=""
    cursor =''
    host=       ''
    user=       ''
    password=   ''
    database=   ''
    
    
    
class moviesDAO:
    db=""
    def __init__(self): 
        self.db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root123",
        database="movies"
        )
        
    def createDbTable(self):
        cursor = self.getcursor()
        sql = "CREATE TABLE movies (id int NOT NULL AUTO_INCREMENT, Movie VARCHAR(250), Rating VARCHAR(20), year int, PRIMARY KEY (id))"
        cursor.execute(sql)
        self.closeAll()
    
            
    def create(self, values):
        cursor = self.db.cursor()
        sql="insert into movies (movie, rating, year) values (%s,%s, %s)"
        cursor.execute(sql, values)

        self.db.commit()
        return cursor.lastrowid

    def getAll(self):
        cursor = self.db.cursor()
        sql="select * from movies"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        print(results)
        for result in results:
            print(result)
            returnArray.append(self.convertToDictionary(result))

        return returnArray

    def findByID(self, id):
        cursor = self.db.cursor()
        sql="select * from movies where id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDictionary(result)

    def update(self, values):
        cursor = self.db.cursor()
        sql="update movies set movie= %s, rating=%s, year=%s, where id = %s"
        cursor.execute(sql, values)
        self.db.commit()
    def delete(self, id):
        cursor = self.db.cursor()
        sql="delete from movies where id = %s"
        values = (id,)

        cursor.execute(sql, values)

        self.db.commit()
        print("delete done")

    def convertToDictionary(self, result):
        colnames=['id','movie','rating', 'year']
        item = {}
        
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        
        return item
    


moviesDAO = moviesDAO()