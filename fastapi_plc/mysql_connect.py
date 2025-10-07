import mysql.connector

cnx = mysql.connector.connect(
    user = 'root',
    password = 'root_password',
    host ='localhost',
    port = '3306'
)

cursor = cnx.cursor()
cursor.execute('SELECT * FROM udemy_practice.sec2_items')

for id,name,price,description,stock,category_id,created_at in cursor:
    print(f'{id}:{name}:{price}:{description}:{stock}:{category_id}:{created_at}')