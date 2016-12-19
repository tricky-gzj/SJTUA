#coding=utf-8
import sqlite3

conn = sqlite3.connect('test.db')

print "Opened database successfully";
"""
conn.execute('''CREATE TABLE member
    (pid int primary key NOT NULL,
    name text NOT NULL,
    phone char(11), email text,
    school text, dept text, stunum char(20),
    field text, skill text,
    trend text, locate text,
    GM text, TM text, MM text, HR text, PM text, OT text);''')


print "Table created successfully";
CREATE TABLE message
    (mid int primary key NOT NULL,
    sender int, receiver int,
    content text,pointer text);
conn.execute("INSERT INTO member (id,pid,name,stunum,phone,email) \
      VALUES (1, 10000, 'sjtu_cc', -1, '18709884365', 'faymek@sjtu.edu.cn')");
conn.commit()
print "Records created successfully";
ALTER TABLE table_name ADD column_name datatype
DROP TABLE member;
INSERT INTO member (pid,name,phone,email) VALUES (10003, '王五','12309877890','example@126.com')
UPDATE member set  email = 'example@163.com' where pid=10000
print(cursor.fetchall())"""

conn.execute("");
conn.commit()
cursor = conn.execute("SELECT * FROM member ")
for m in cursor:
    print m

print "Total number of rows updated :", conn.total_changes
print "Operation done successfully";

conn.close()