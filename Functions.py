import cx_Oracle
import os

### Set Path to instant Oracle client ###
os.environ['PATH']='C:\\...\\instantclient'
### End ###

### Function: SetUp query,variables and lists ###
def SetUp():
    con = cx_Oracle.connect("username", "password", "localhost/orcl")
    cur = con.cursor()
    query_select="select * From inputdata"
    execution=cur.execute(query_select)
    TC1=[]
    TC2=[]
    n=1
    return con, cur, execution, TC1, TC2, n
### End ###

### Function: Results ###
def Results(status,list,cur,con):
    for i in list:
        cur.execute("update inputdata set result='{}' where id='{}'".format(status,i))
    con.commit()
### End ###

