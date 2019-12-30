#！/usr/bin/python

# -*- coding: UTF-8 -*-

import MySQLdb  

#包的导入

db = MySQLdb.connect("jdbc:mysql://127.0.0.1:3306/demo?characterEncoding=utf8&useSSL=true","root","root","demo")

#打开数据库的连接 

cursor = db.cursor()

#使用cursor()方法获得操作游标

try:
   # 执行sql语句
   cursor.execute("SELECT VERSION()")
   data = cursor.fetchone()

   print ("Database version : %s " % data)

   # 提交到数据库执行
   db.commit()
except:
   # 发生错误时回滚    回滚到获取游标的位置开始重新执行  看代码上面的文字有说明
   db.rollback()

db.close()

#关闭数据库的连接