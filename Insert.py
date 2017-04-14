import ibm_db_dbi
conn = ibm_db_dbi.connect("DATABASE=AEDB1;HOSTNAME=172.16.151.78;PORT=50000;PROTOCOL=TCPIP;UID=db2admin;PWD=Pass1234;", "", "")
if conn:
    conn.set_autocommit(True)
    cursor = conn.cursor()
    sql = "insert into AEDB1.TEST1(id, name, jobrole)  values(100,'ravi','admin')"
    result = cursor.execute(sql)
    print(result)
