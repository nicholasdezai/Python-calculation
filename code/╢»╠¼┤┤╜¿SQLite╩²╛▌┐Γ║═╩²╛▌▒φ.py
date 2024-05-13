import sqlite3

databaseName = 'database.sqlite3'
tableName = 'articles'

def doSql(sql):
    '''执行SQL语句'''    
    with sqlite3.connect(databaseName) as conn:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()

def getData(sql):
    '''根据指定的SELECT语句获取并返回数据'''
    with sqlite3.connect(databaseName) as conn:
        cur = conn.cursor()
        cur.execute(sql)
        temp = cur.fetchall()
    return temp

def hasTable(tableName):
    sql = f'SELECT COUNT(*) FROM sqlite_master WHERE name="{tableName}"'
    return getData(sql)[0][0]!=0

if not hasTable(tableName):
    # 创建表时会自动创建系统表sqlite_sequence，存储每个用户表中RowId的最大值
    sql = (f'CREATE TABLE {tableName}' +
          '(id INTEGER PRIMARY KEY AUTOINCREMENT, author TEXT,'+
          ' content TEXT, publishTime DATETIME)')
    doSql(sql)

sql = (f'INSERT INTO {tableName}(author,content,publishTime)'+
       ' VALUES("dfg","test",datetime("now","localtime"))')
doSql(sql)
