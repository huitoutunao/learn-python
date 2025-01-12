from pymysql import Connection

# 构建到 MySQL 数据库链接
conn = Connection(
    host='localhost',
    port=3306,
    user='root',
    password='123456',
    autocommit=True # 自动提交事务
)

print(conn.get_server_info())

# 执行非查询性质sql
cursor = conn.cursor()
# 选择数据库
conn.select_db('world')
# 执行sql
# cursor.execute('create table test_pymysql(id int, name varchar(20));')
cursor.execute('select * from world.student')
result = cursor.fetchall()
print(result) # 获取所有查询结果(元组类型)
for row in result:
    print(row)

# 插入数据
cursor.execute('insert into world.student values(%s, %s, %s, %s)', (9, '张三哈', 24, '女'))
# 通过commit确认插入操作
# conn.commit()

# 关闭链接
conn.close()
