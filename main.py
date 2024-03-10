import database as db

cursor = db.conec.cursor()
cursor.execute("SELECT * FROM tb_user_estudante")
user = cursor.fetchall()

for users in user:
    print(users)