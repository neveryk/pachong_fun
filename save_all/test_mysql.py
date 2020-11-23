import pymysql
# 连接数据库
db=pymysql.connect(host='localhost',port=3306,user='root',password='123456',db='test')
# 声明mysql对象db
# cursor=db.cursor()
# # 获得mysql游标
# cursor.execute('SELECT VERSION()')
# #利用游标执行MySQL语句
# data=cursor.fetchone()
# # 获得一条数据
# print('Database version:',data)
# cursor.execute('CREATE DATABASE testlogin DEFAULT CHARACTER SET utf8')
# db.close()

# 创建表
# cursor=db.cursor()
# cursor.execute('CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, age INT NOT NULL, PRIMARY KEY (id ))')
# db.close()
# insert
data={
    'id':1,
    "name":"zippo",
    "age":10
}
table="students"
keys=','.join(data.keys())
values=','.join(['%s'] * len(data))
print(values)
# sql = 'INSERT INTO students(id, name, age) values(%s, %s, %s) '
# cursor=db.cursor()
# try :
#     cursor. execute ( sql, (id, name, age))
#     db . commit()
# except:
#     db. rollback ()
# db.close()