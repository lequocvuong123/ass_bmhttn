import cx_Oracle 

cur = cx_Oracle.connect('system','duong123')
conn = cx_Oracle.connect('system','duong123')
cur = conn.cursor()
cur.execute("""INSERT INTO customers (customer_id, customer_name, city) VALUES ('004', 'Nguyen Van A', 'TP.HCM') """)
conn.commit()