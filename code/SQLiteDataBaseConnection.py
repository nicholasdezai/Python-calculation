import sqlite3

class DataBaseConnection:
    def __init__(self, dbName):
        '''dbName:要操作的数据库名'''
        # 构造方法，连接数据库
        self.__conn = sqlite3.connect(dbName)

    def __del__(self):
        # 析构方法，关闭数据库连接
        self.__conn.close()

    def __process(self, s):
        '''用来处理SQL语句中的字符串型字典值，在两侧加双引号'''
        if isinstance(s, str):
            return '"'+s+'"'
        return str(s)

    def insert(self, table, *values):
        '''插入数据
           table:要插入的表名,values:要插入的数据'''
        # 构造SQL语句
        sql = 'INSERT INTO ' + table + ' VALUES('
        if values:
            for item in values[:-1]:
                sql = sql + self.__process(item) + ','
            sql = sql + self.__process(values[-1]) + ')'
            # 执行SQL语句
            self.__conn.execute(sql)
            # 提交事务，确认插入
            self.__conn.commit()
        else:
            print('Nothing to insert.')

    def delete(self, table, **kwargs):
        '''删除数据
           table:要删除的数据所在的表名,kwargs:用来指定约束条件'''
        # 构造SQL语句
        sql = 'DELETE FROM ' + table
        if kwargs:
            sql = sql + ' WHERE '
            for key, value in kwargs.items():
                sql = sql + key + '=' + self.__process(value) + ' and '
            sql = sql[:-5]
        else:
            # 不加WHERE就删除，要确认一下
            flag = ''
            while flag not in ('y', 'n'):
                flag = input('你确定不加where吗？(y/n)：').lower()
            if flag == 'n':
                print('删除操作被取消.')
                return
        self.__conn.execute(sql)
        self.__conn.commit()

    def update(self, table, conditionKey=None, conditionValue=None, **kwargs):
        '''更新数据
           conditionKey:约束字段,conditionValue:约束字典的值,kwargs:要更新的字段和值'''
        if not kwargs:
            print('Nothing to update.')
            return
        # 构造SQL语句
        sql = 'UPDATE ' + table + ' SET '
        for key, value in kwargs.items():
            sql = sql + key + '=' + self.__process(value) + ' and '
        sql = sql[:-5]
        if conditionKey is None:
            # 不加WHERE就更新，要确认一下
            flag = ''
            while flag not in ('y', 'n'):
                flag = input('你确定不加where吗？(y/n)').lower()
            if flag == 'n':
                print('更新操作被取消')
                return
        else:
            sql = sql + ' WHERE ' + conditionKey + '='
            if isinstance(conditionValue, str):
                sql = sql + self.__process(conditionValue)
        self.__conn.execute(sql)
        self.__conn.commit()

    def select(self, table, **kwargs):
        '''查询数据
           table:表名,kwargs:约束条件'''
        sql = 'SELECT * FROM ' + table
        if kwargs:
            sql = sql + ' WHERE '
            for key, value in kwargs.items():
                sql = sql + key + '=' + self.__process(value) + ' and '
            sql = sql[:-5]
        return list(self.__conn.execute(sql))
