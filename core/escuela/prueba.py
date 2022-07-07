import mysql.connector 
mydb = mysql.connector.connect (
    host="localhost",
    username="root",
    password="rootroot",
    database="escuela"
)

mycursor = mydb.cursor()
sql='SELECT M.nombre, R.nota_1,R.nota_2,R.nota_3 FROM escuela_alumno AS Al, escuela_materia AS M, escuela_rinde AS R WHERE R.alumno_nro_registro_id = Al.num_reg AND R.materia_codigo_id = M.codigo AND Al.nombre = %s AND Al.apellido = %s ORDER BY M.nombre'
adr = ['German','Alvarez']       #NOMBRE Y APELL DEL ALUMNO LEIDO (TRAIDO)

mycursor.execute (sql, adr)
myresult = mycursor.fetchall()      #lista de python
    
#myresult=[('Informatica',9,9,8),('Matematica',10,9,8)]
lista=[]
for i in range(len(myresult)):
    diccAux={'materia':'','nota_1':'','nota_2':'','nota_3':''}
    for j in range(4):         #cantidad de campos = 4
        if j == 0:
            diccAux['materia'] = myresult[i][j]
        elif j == 1:
            diccAux['nota_1'] = myresult[i][j]
        elif j == 2:
            diccAux['nota_2'] = myresult[i][j]
        else:
            diccAux['nota_3'] = myresult[i][j]
    lista.append(diccAux)
dic={'f1':lista}
print(dic)
for x in dic['f1']:
    print(x['materia'])
    print(x['nota_1'])
    print(x['nota_2'])
    print(x['nota_3'])
