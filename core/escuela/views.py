from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.views.generic import FormView, RedirectView
import prj_escuela.settings as setting
from .forms import UserRegisterForm,TipoUsuarioForm,PreceptorForm,AulaForm,AlumnoForm,MateriaForm,CursoForm,TurnoForm,TieneForm,RindeForm,ProfesorForm,DictaForm
from .models import Preceptor,Aula,Alumno,Materia,Curso,Turno,Tiene,Rinde,Profesor,Dicta
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from core.user.models import TipoUsuario,User
from datetime import datetime
from dateutil.relativedelta import relativedelta # calcula la edad

import mysql.connector 
mydb = mysql.connector.connect (
    host="localhost",
    username="root",
    password="rootroot",
    database="escuela"
)

mycursor = mydb.cursor()

def index(request,template_name='escuela/index.html'):
    return render(request,template_name)

def index_admin(request,template_name='escuela/index_admin.html'):
    return render(request,template_name)

def register(request,username=None,template_name='escuela/register.html'):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)           #aca es donde te digo de pegar todo el trozo de codigo q hice
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			user = User.objects.get(username=username)
			messages.success(request, f'Usuario {username} creado.')
			return redirect('index') #
	else:
		form = UserRegisterForm()

	context = { 'form' : form }
	return render(request, template_name, context)

@login_required
def nuevo_tipo_usuario(request,template_name='escuela/tipo_usuario_form.html'):
    if request.method=='POST':
        form = TipoUsuarioForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('tipos_usuario') # invoca al nombre del name='...' en urls.py
        else:
            print(form.errors)
    else:
        form = TipoUsuarioForm()
    dato={'form':form}
    return render(request,template_name,dato)

'''def nuevo_genero(request,template_name='escuela/genero_form.html'):
    if request.method=='POST':
        form = GeneroForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('index') # invoca al nombre del name='...' en urls.py
        else:
            print(form.errors)
    else:
        form = GeneroForm()
    dato={'form':form}
    return render(request,template_name,dato)

def nueva_persona(request,template_name='escuela/persona_form.html'):
    if request.method=='POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('index')
        else:
            print(form.errors)
    else:
        form = PersonaForm()
    dato={'form':form}
    return render(request,template_name,dato)'''


@login_required
def nuevo_preceptor(request,template_name='escuela/preceptor_form.html'):
    if request.method=='POST':
        form = PreceptorForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('preceptores') # invoca al nombre del name='...' en urls.py
        else:
            print(form.errors)
    else:
        form = PreceptorForm()
    dato={'form':form}
    return render(request,template_name,dato)


@login_required
def nueva_aula(request,template_name='escuela/aula_form.html'):
    if request.method=='POST':
        form = AulaForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('aulas') # invoca al nombre del name='...' en urls.py
        else:
            print(form.errors)
    else:
        form = AulaForm()
    dato={'form':form}
    return render(request,template_name,dato)

@login_required
def nuevo_alumno(request,template_name='escuela/alumno_form.html'):
    if request.method=='POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('alumnos') # invoca al nombre del name='...' en urls.py
        else:
            print(form.errors)
    else:
        form = AlumnoForm()
    dato={'form':form}
    return render(request,template_name,dato)

@login_required
def nueva_materia(request,template_name='escuela/materia_form.html'):
    if request.method=='POST':
        form = MateriaForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('materias') # invoca al nombre del name='...' en urls.py
        else:
            print(form.errors)
    else:
        form = MateriaForm()
    dato={'form':form}
    return render(request,template_name,dato)

@login_required
def nuevo_curso(request,template_name='escuela/curso_form.html'):
    if request.method=='POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('cursos') # invoca al nombre del name='...' en urls.py
        else:
            print(form.errors)
    else:
        form = CursoForm()
    dato={'form':form}
    return render(request,template_name,dato)

@login_required
def nuevo_turno(request,template_name='escuela/turno_form.html'):
    if request.method=='POST':
        form = TurnoForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('turnos') # invoca al nombre del name='...' en urls.py
        else:
            print(form.errors)
    else:
        form = TurnoForm()
    dato={'form':form}
    return render(request,template_name,dato)

@login_required
def nuevo_tiene(request,template_name='escuela/tiene_form.html'):
    if request.method=='POST':
        form = TieneForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('tienen') # invoca al nombre del name='...' en urls.py
        else:
            print(form.errors)
    else:
        form = TieneForm()
    dato={'form':form}
    return render(request,template_name,dato)

@login_required
def nuevo_rinde(request,template_name='escuela/rinde_form.html'):
    if request.method=='POST':
        form = RindeForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('rinden') # invoca al nombre del name='...' en urls.py
        else:
            print(form.errors)
    else:
        form = RindeForm()
    dato={'form':form}
    return render(request,template_name,dato)

@login_required
def nuevo_profesor(request,template_name='escuela/profesor_form.html'):
    if request.method=='POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('profesores') # invoca al nombre del name='...' en urls.py
        else:
            print(form.errors)
    else:
        form = ProfesorForm()
    dato={'form':form}
    return render(request,template_name,dato)

@login_required
def nuevo_dicta(request,template_name='escuela/dicta_form.html'):
    if request.method=='POST':
        form = DictaForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('dictan') # invoca al nombre del name='...' en urls.py
        else:
            print(form.errors)
    else:
        form = DictaForm()
    dato={'form':form}
    return render(request,template_name,dato)


@login_required
def listar_tipos_usuario(request, template_name='escuela/tipos_usuario.html'):
    tipos_usuario = TipoUsuario.objects.all()       #
    dato = {'tipos_usuario': tipos_usuario}
    return render(request,template_name,dato)

@login_required
def listar_usuarios(request, template_name='escuela/usuarios.html'):
    usuarios = User.objects.all()
    dato = {'usuarios': usuarios}
    return render(request,template_name,dato)

@login_required
def listar_preceptores(request, template_name='escuela/preceptores.html'):
    preceptores = Preceptor.objects.all()
    for preceptor in preceptores:
        preceptor.edad = relativedelta(datetime.now(), preceptor.fecha_nac).years
    dato = {'preceptores': preceptores}
    return render(request,template_name,dato)

@login_required
def listar_aulas(request, template_name='escuela/aulas.html'):
    aulas = Aula.objects.all()
    dato = {'aulas': aulas}
    return render(request,template_name,dato)

@login_required
def listar_alumnos(request, template_name='escuela/alumnos.html'):
    alumnos = Alumno.objects.all()
    for alumno in alumnos:
        alumno.edad = relativedelta(datetime.now(), alumno.fecha_nac).years
    dato = {'alumnos': alumnos}
    print(dato)
    return render(request,template_name,dato)

@login_required
def listar_materias(request, template_name='escuela/materias.html'):
    materias = Materia.objects.all()
    dato = {'materias': materias}
    return render(request,template_name,dato)

@login_required
def listar_cursos(request, template_name='escuela/cursos.html'):
    cursos = Curso.objects.all()
    dato = {'cursos': cursos}
    return render(request,template_name,dato)

@login_required
def listar_turnos(request, template_name='escuela/turnos.html'):
    turnos = Turno.objects.all()
    dato = {'turnos': turnos}
    return render(request,template_name,dato)

@login_required
def listar_tienen(request, template_name='escuela/tienen.html'):
    tienen = Tiene.objects.all()
    dato = {'tienen': tienen}
    return render(request,template_name,dato)

@login_required
def listar_rinden(request, template_name='escuela/rinden.html'):
    rinden = Rinde.objects.all()
    dato = {'rinden': rinden}
    return render(request,template_name,dato)

@login_required
def listar_profesores(request, template_name='escuela/profesores.html'):
    profesores = Profesor.objects.all()
    for profesor in profesores:
        profesor.edad = relativedelta(datetime.now(), profesor.fecha_nac).years
    dato = {'profesores': profesores}
    return render(request,template_name,dato)

@login_required
def listar_dictan(request, template_name='escuela/dictan.html'):
    dictan = Dicta.objects.all()
    dato = {'dictan': dictan}
    return render(request,template_name,dato)

@login_required
def funcionalidades_alumno (request, template_name='escuela/funcionalidades_alumno.html'):
    if request.method == 'POST':
        form = request.POST
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        ingreso = True


        sql = "SELECT M.nombre, R.nota_1,R.nota_2,R.nota_3 FROM escuela_alumno AS Al, escuela_materia AS M, escuela_rinde AS R WHERE R.alumno_nro_registro_id = Al.num_reg AND R.materia_codigo_id = M.codigo AND Al.nombre = %s AND Al.apellido = %s ORDER BY M.nombre;"
        adr = [nombre, apellido]       #NOMBRE Y APELL DEL ALUMNO LEIDO (TRAIDO)

        mycursor.execute (sql, adr)

        myresult = mycursor.fetchall()      #lista de python

        if len(myresult) == 0: 
            denegado = True
            dato = {'ingreso':ingreso, 'denegado': denegado}
            return render(request,template_name,dato)
            
        else:

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


            #FUNCIONALIDAD 2
            sql = "SELECT M.nombre, R.cant_inasist FROM escuela_alumno AS Al, escuela_materia AS M, escuela_rinde AS R WHERE R.alumno_nro_registro_id = Al.num_reg AND R.materia_codigo_id = M.codigo AND Al.nombre = %s AND Al.apellido = %s ORDER BY M.nombre;"

            mycursor.execute (sql, adr)

            myresult = mycursor.fetchall()    

            acumInasit = 0

            lista2=[]
            for i in range(len(myresult)):
                diccAux={'materia':'','cant_inasist':''}
                for j in range(2):         #cantidad de campos = 2
                    if j == 0:
                        diccAux['materia'] = myresult[i][j]
                    elif j == 1:
                        diccAux['cant_inasist'] = myresult[i][j]
                        acumInasit += int(myresult[i][j])
                lista2.append(diccAux)

            dato = {'f1':lista, 'f2': lista2, 'acumInasist': acumInasit, 'nomyapp': str(adr[0]+' '+adr[1]), 'form':form, 'ingreso': ingreso}
            return render(request,template_name,dato)

    ingreso = False
    form = None
    dato = {'form':form, 'ingreso':ingreso}
    return render(request,template_name,dato)


@login_required
def funcionalidad_preceptor (request, template_name='escuela/funcionalidad_preceptor.html'):
    if request.method == 'POST':
        form = request.POST
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        ingreso = True

        #Funcionalidad 1----------------------------------------------------------
        sql = "SELECT A.año,A.division,T.nombre AS NombreTurno,Ti.hora_ingreso,Ti.hora_egreso FROM escuela_aula AS A,escuela_turno AS T, escuela_tiene AS Ti,escuela_preceptor AS P WHERE P.idPreceptor = A.preceptor_id AND Ti.aula_idAula_id = A.idAula AND Ti.turno_idturno_id = T.idTurno AND P.nombre = %s AND P.apellido = %s ORDER BY A.idAula;"
        adr = [nombre,apellido]         #de prueba hicimos con pablo perez

        mycursor.execute(sql,adr)
    
        myresult = mycursor.fetchall()

        if len(myresult) == 0: 
            denegado = True
            dato = {'ingreso':ingreso, 'denegado': denegado}
            return render(request,template_name,dato)
            
        else:

            lista=[]
            for i in range(len(myresult)):
                diccAux={'año':'','division':'','turno':'','ingreso':'','egreso':''}
                for j in range(5):         #cantidad de campos = 4
                    if j == 0:
                        diccAux['año'] = myresult[i][j]
                    elif j == 1:
                        diccAux['division'] = myresult[i][j]
                    elif j == 2:
                        diccAux['turno'] = myresult[i][j]
                    elif j == 3:
                        diccAux['ingreso'] = myresult[i][j]
                    else:
                        diccAux['egreso'] = myresult[i][j]
                lista.append(diccAux)
                
            #FUNCIONALIDAD 2 --------------------------------------------------
            sql = "SELECT  A.idAula,A.año,A.division,M.nombre AS NomMateria,Al.num_reg AS NroRegAl,Al.nombre,Al.apellido, R.cant_inasist FROM escuela_aula AS A, escuela_preceptor AS P,escuela_curso AS C,escuela_materia AS M,escuela_rinde AS R, escuela_alumno AS Al WHERE P.idPreceptor = A.preceptor_id AND C.aula_idAula_id = A.idAula AND C.materia_codigo_id = M.codigo AND R.materia_codigo_id = M.codigo AND R.alumno_nro_registro_id = Al.num_reg AND P.nombre = %s AND P.apellido = %s ORDER BY A.idAula;"
            mycursor.execute (sql,adr)
            myresult = mycursor.fetchall()      #lista de python
            lista2=[]
            for i in range(len(myresult)):
                diccAux={'año':'','division':'','materia':'','registro':'','nombre':'','apellido':'','inasistencias':''}
                for j in range(7):         #cantidad de campos = 4
                    if j == 0:
                        diccAux['año'] = myresult[i][j]
                    elif j == 1:
                        diccAux['division'] = myresult[i][j]
                    elif j == 2:
                        diccAux['materia'] = myresult[i][j]
                    elif j == 3:
                        diccAux['registro'] = myresult[i][j]
                    elif j==4:
                        diccAux['nombre'] = myresult[i][j]
                    elif j==5:
                        diccAux['apellido']=myresult[i][j]
                    else:
                        diccAux['inasistencias']=myresult[i][j]
                lista2.append(diccAux)
            
            preceptor={'nombre':nombre,'apellido':apellido}
                
            dato = {'form':form,'f1':lista,'f2':lista2,'ingreso':ingreso,'preceptor':preceptor}
            return render(request,template_name,dato)
            
    form=None
    ingreso=False
    dato={'form':form,'ingreso':ingreso}
    return render(request,template_name,dato)


@login_required
def funcionalidades_profesor (request, template_name='escuela/funcionalidades_profesor.html'):
    #FUNCIONALIDAD 1
    if request.method == 'POST':
        form = request.POST
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        ingreso = True


        sql = "SELECT A.idAula,A.año,A.division,Tur.nombre AS NombreTurno,Ti.hora_ingreso,Ti.hora_egreso FROM escuela_aula AS A,escuela_turno AS Tur, escuela_tiene AS Ti,escuela_profesor AS Pr,escuela_dicta AS DI,escuela_materia AS M,escuela_curso AS C WHERE Pr.idProfesor = DI.profesor_id_profesor_id AND DI.materia_codigo_id = M.codigo AND M.codigo = C.materia_codigo_id AND C.aula_idAula_id = A.idAula AND A.idAula = Ti.aula_idAula_id AND Ti.turno_idturno_id = Tur.idTurno AND Pr.nombre = %s AND Pr.apellido = %s ORDER BY A.idAula;"
        adr = [nombre, apellido]       #NOMBRE Y APELL DEL PROF LEIDO (TRAIDO)

        mycursor.execute (sql, adr)

        myresult = mycursor.fetchall()      

        if len(myresult) == 0: 
            denegado = True
            dato = {'ingreso':ingreso, 'denegado': denegado}
            return render(request,template_name,dato)
            
        else:

            lista=[]
            for i in range(len(myresult)):
                diccAux={'idAula':'','año':'','division':'','nomTurno':'','horaIng':'','horaEgr':''}
                for j in range(6):         #cantidad de campos = 6
                    if j == 0:
                        diccAux['idAula'] = myresult[i][j]
                    elif j == 1:
                        diccAux['año'] = myresult[i][j]
                    elif j == 2:
                        diccAux['division'] = myresult[i][j]
                    elif j == 3:
                        diccAux['nomTurno'] = myresult[i][j]
                    elif j == 4:
                        diccAux['horaIng'] = myresult[i][j]
                    else:
                        diccAux['horaEgr'] = myresult[i][j]

                lista.append(diccAux)

            #FUNCIONALIDAD 2
            sql = "SELECT M.nombre AS NombreMateria, D.cargo,R.alumno_nro_registro_id AS NroRegAlum, R.nota_1,R.nota_2,R.nota_3 FROM escuela_profesor AS Pr, escuela_materia AS M, escuela_dicta AS D,escuela_rinde AS R WHERE Pr.idProfesor = D.profesor_id_profesor_id AND D.materia_codigo_id = M.codigo AND M.codigo = R.materia_codigo_id AND Pr.nombre = %s AND Pr.apellido = %s ORDER BY M.nombre;"

            mycursor.execute (sql, adr)

            myresult = mycursor.fetchall()      

            lista2=[]
            for i in range(len(myresult)):
                diccAux={'nomMateria':'','cargo':'','nroReg':'','nota1':'','nota2':'','nota3':''}
                for j in range(6):         #cantidad de campos = 6
                    if j == 0:
                        diccAux['nomMateria'] = myresult[i][j]
                    elif j == 1:
                        diccAux['cargo'] = myresult[i][j]
                    elif j == 2:
                        diccAux['nroReg'] = myresult[i][j]
                    elif j == 3:
                        diccAux['nota1'] = myresult[i][j]
                    elif j == 4:
                        diccAux['nota2'] = myresult[i][j]
                    else:
                        diccAux['nota3'] = myresult[i][j]

                lista2.append(diccAux)

            dato = {'f1':lista, 'f2': lista2,'nomyapp': str(adr[0]+' '+adr[1]),'form':form, 'ingreso': ingreso}
            return render(request,template_name,dato)

    ingreso = False
    form = None
    dato = {'form':form, 'ingreso':ingreso}
    return render(request,template_name,dato)


@login_required
#EN ESTAS FUNCIONALIDADES NO DEBO TRABAJAR CON FORMULARIO! RESPETO LOS DATOS YA DADOS EN EL INFORME!
def funcionalidades_admin (request, template_name='escuela/funcionalidades_admin.html'):
    #FUNCIONALIDAD 1
    sql = "SELECT DISTINCT Pr.idProfesor,Pr.nombre,Pr.apellido,Al.num_reg,Al.nombre, Al.apellido, R.nota_1,R.nota_2,R.nota_3 FROM escuela_aula AS C, escuela_profesor AS Pr, escuela_alumno AS Al, escuela_materia AS M, escuela_rinde AS R, escuela_dicta AS E, escuela_curso AS MA WHERE M.codigo = E.materia_codigo_id AND E.profesor_id_profesor_id = Pr.idProfesor AND M.codigo = R.materia_codigo_id AND R.alumno_nro_registro_id = Al.num_reg AND M.codigo = MA.materia_codigo_id AND MA.aula_idAula_id = Al.aula_id AND R.materia_codigo_id = MA.materia_codigo_id AND M.nombre = %s ORDER BY Pr.idProfesor;"
    adr = ['Informatica']       #NOMBRE DEL CURSO A MOSTRAR

    mycursor.execute (sql, adr)

    myresult = mycursor.fetchall()      #lista de tuplas python
    print("idProf NomProf ApellProf Nro_Reg NomAl ApellAl Nota1 Nota2 Nota3\n")
    lista=[]
    for i in range(len(myresult)):
        diccAux={'idProf':'','nomProf':'','apellProf':'','nroReg':'','nomAl':'','apellAl':'','nota_1':'','nota_2':'','nota_3':''}
        for j in range(9):         #cantidad de campos = 9
            if j == 0:
                diccAux['idProf'] = myresult[i][j]
            elif j == 1:
                diccAux['nomProf'] = myresult[i][j]
            elif j == 2:
                diccAux['apellProf'] = myresult[i][j]
            elif j == 3:
                diccAux['nroReg'] = myresult[i][j]
            elif j == 4:
                diccAux['nomAl'] = myresult[i][j]
            elif j == 5:
                diccAux['apellAl'] = myresult[i][j]
            elif j == 6:
                diccAux['nota_1'] = myresult[i][j]
            elif j == 7:
                diccAux['nota_2'] = myresult[i][j]
            else:
                diccAux['nota_3'] = myresult[i][j]
        lista.append(diccAux)

    #FUNCIONALIDAD 2
    sql = "SELECT Pr.idProfesor, Pr.nombre,Pr.apellido,M.nombre,C.año, C.division, A.turno_idturno_id, MA.dia_clase, A.hora_ingreso, A.hora_egreso FROM escuela_aula AS C,escuela_profesor AS Pr, escuela_materia AS M, escuela_dicta AS E, escuela_curso AS MA, escuela_tiene AS A WHERE Pr.idProfesor = E.profesor_id_profesor_id AND E.materia_codigo_id = M.codigo AND M.codigo = MA.materia_codigo_id AND MA.aula_idAula_id = A.aula_idAula_id AND C.idAula=MA.aula_idAula_id ORDER BY Pr.idProfesor;"

    mycursor.execute(sql)

    myresult = mycursor.fetchall()   
    lista2=[]
    for i in range(len(myresult)):
        diccAux={'idProf':'','nomProf':'','apellProf':'','nomMat':'','añoAula':'','div':'','idTurno':'','diaClase':'','horaIng':'','horaEgr':''}
        for j in range(10):         #cantidad de campos = 10
            if j == 0:
                diccAux['idProf'] = myresult[i][j]
            elif j == 1:
                diccAux['nomProf'] = myresult[i][j]
            elif j == 2:
                diccAux['apellProf'] = myresult[i][j]
            elif j == 3:
                diccAux['nomMat'] = myresult[i][j]
            elif j == 4:
                diccAux['añoAula'] = myresult[i][j]
            elif j == 5:
                diccAux['div'] = myresult[i][j]
            elif j == 6:
                diccAux['idTurno'] = myresult[i][j]
            elif j == 7:
                diccAux['diaClase'] = myresult[i][j]
            elif j == 8:
                diccAux['horaIng'] = myresult[i][j]
            else:
                diccAux['horaEgr'] = myresult[i][j]
        lista2.append(diccAux)


    #FUNCIONALIDAD 3
    sql = "SELECT C.idAula,C.año,C.division,Pr.idPreceptor,Pr.nombre,Pr.apellido,A.num_reg,A.nombre,A.apellido,T.nombre, AHT.hora_ingreso, AHT.hora_egreso FROM escuela_aula AS C,escuela_preceptor AS Pr,escuela_alumno AS A, escuela_tiene AS AHT, escuela_turno as T WHERE Pr.idPreceptor = C.preceptor_id AND A.aula_id=C.idAula AND C.idAula = AHT.aula_idAula_id AND AHT.turno_idturno_id = T.idTurno AND C.idAula=%s  ORDER BY C.año;"
    adr3 = ['1']             #ACA TRAEMOS LEIDO EL NRO DE UN AULA

    mycursor.execute (sql, adr3)

    myresult = mycursor.fetchall()     
    lista3=[]
    for i in range(len(myresult)):
        diccAux={'idAula':'','añoAula':'','div':'','idPrec':'','nomPrec':'','apellPrec':'','nroReg':'','nomAl':'','apellAl':'','nomTurno':'','horaIng':'','horaEgr':''}
        for j in range(12):         #cantidad de campos = 10
            if j == 0:
                diccAux['idAula'] = myresult[i][j]
            elif j == 1:
                diccAux['añoAula'] = myresult[i][j]
            elif j == 2:
                diccAux['div'] = myresult[i][j]
            elif j == 3:
                diccAux['idPrec'] = myresult[i][j]
            elif j == 4:
                diccAux['nomPrec'] = myresult[i][j]
            elif j == 5:
                diccAux['apellPrec'] = myresult[i][j]
            elif j == 6:
                diccAux['nroReg'] = myresult[i][j]
            elif j == 7:
                diccAux['nomAl'] = myresult[i][j]
            elif j == 8:
                diccAux['apellAl'] = myresult[i][j]
            elif j == 9:
                diccAux['nomTurno'] = myresult[i][j]
            elif j == 10:
                diccAux['horaIng'] = myresult[i][j]
            else:
                diccAux['horaEgr'] = myresult[i][j]


        lista3.append(diccAux)

    #FUNCIONALIDAD 4
    sql = "SELECT C.año, C.division, M.nombre, Al.num_reg, Al.nombre,Al.apellido, MA.cant_inasist FROM escuela_aula AS C, escuela_alumno AS Al,escuela_rinde AS MA, escuela_materia AS M WHERE Al.aula_id = C.idAula AND Al.num_reg = MA.alumno_nro_registro_id AND MA.alumno_nro_registro_id = Al.num_reg AND MA.materia_codigo_id = M.codigo AND MA.cant_inasist > 2 AND C.año=%s  ORDER BY C.año;"
    
    adr4 = ['5']                 #ACA TRAEMOS LEIDO UN AÑO POR EJ

    mycursor.execute (sql, adr4)

    myresult = mycursor.fetchall()    
    lista4=[]
    for i in range(len(myresult)):
        diccAux={'aulaAño':'','div':'','nomMat':'','nroReg':'','nomAl':'','apellAl':'','cantInasist':''}
        for j in range(7):         #cantidad de campos = 7
            if j == 0:
                diccAux['aulaAño'] = myresult[i][j]
            elif j == 1:
                diccAux['div'] = myresult[i][j]
            elif j == 2:
                diccAux['nomMat'] = myresult[i][j]
            elif j == 3:
                diccAux['nroReg'] = myresult[i][j]
            elif j == 4:
                diccAux['nomAl'] = myresult[i][j]
            elif j == 5:
                diccAux['apellAl'] = myresult[i][j]
            else:
                diccAux['cantInasist'] = myresult[i][j]
        lista4.append(diccAux)


    #FUNCIONALIDAD 5
    sql = "SELECT C.idAula,C.año,C.division,M.nombre,Pr.idProfesor,Pr.nombre,Pr.apellido, PE.idPreceptor,PE.nombre,PE.apellido, Al.num_reg,Al.nombre,Al.apellido, alt.hora_ingreso, alt.hora_egreso FROM escuela_aula AS C, escuela_materia AS M, escuela_profesor AS Pr, escuela_alumno as Al,escuela_turno AS T,escuela_tiene AS alt,escuela_curso AS MA,escuela_dicta AS PM, escuela_preceptor AS PE WHERE T.idTurno=alt.turno_idturno_id AND alt.aula_idAula_id=C.idAula AND MA.aula_idAula_id=C.idAula AND C.preceptor_id = PE.idPreceptor AND MA.materia_codigo_id =M.codigo AND PM.materia_codigo_id =M.codigo AND PM.profesor_id_profesor_id=Pr.idProfesor AND Al.aula_id=C.idAula AND T.nombre=%s ORDER BY C.idAula;"
    adr5 = ['Tarde']                 #ACA TRAEMOS LEIDO UN NOMBRE DE TURNO POR EJ

    mycursor.execute (sql, adr5)

    myresult = mycursor.fetchall()      
    print("idAula Año Division NomMat idProf Nombre Apell Nro_Reg  NombAl ApellAl HoraIng  HoraEgr\n")
    lista5=[]
    for i in range(len(myresult)):
        diccAux={'idAula':'','año':'','div':'','nomMat':'','idProf':'','nomProf':'','apellProf':'','nroReg':'','nomAl':'','apellAl':'','horaIng':'','horaEgr':''}
        for j in range(15):         #cantidad de campos = 15
            if j == 0:
                diccAux['idAula'] = myresult[i][j]
            elif j == 1:
                diccAux['año'] = myresult[i][j]
            elif j == 2:
                diccAux['div'] = myresult[i][j]
            elif j == 3:
                diccAux['nomMat'] = myresult[i][j]
            elif j == 4:
                diccAux['idProf'] = myresult[i][j]
            elif j == 5:
                diccAux['nomProf'] = myresult[i][j]
            elif j == 6:
                diccAux['apellProf'] = myresult[i][j]
            elif j == 7:
                diccAux['idPrec'] = myresult[i][j]
            elif j == 8:
                diccAux['nomPrec'] = myresult[i][j]
            elif j == 9:
                diccAux['apellPrec'] = myresult[i][j]
            elif j == 10:
                diccAux['nroReg'] = myresult[i][j]
            elif j == 11:
                diccAux['nomAl'] = myresult[i][j]
            elif j == 12:
                diccAux['apellAl'] = myresult[i][j]
            elif j == 13:
                diccAux['horaIng'] = myresult[i][j]
            else:
                diccAux['horaEgr'] = myresult[i][j]
        lista5.append(diccAux)


    dicc = {'f1':lista,'curso': adr[0],'f2':lista2,'f3':lista3, 'aula': adr3[0],'f4':lista4,'curso': adr4[0],'f5':lista5,'turno': adr5[0]}
    return render(request,template_name,dicc)


@login_required
def modificar_tipo_usuario(request,pk,template_name='escuela/tipo_usuario_form.html'):
    tipo_usuario = TipoUsuario.objects.get(nombre=pk)
    form = TipoUsuarioForm(request.POST or None, instance=tipo_usuario)
    if form.is_valid():
        form.save(commit=True)
        return redirect('tipos_usuario')
    else:
        print(form.errors)
    dato = {'form':form}
    return render(request,template_name,dato)

'''def modificar_usuario(request,pk,template_name='escuela/usuario_form.html'):
    usuario = usuario.objects.get(num_cuit=pk)
    form = UserForm(request.POST or None, instance=usuario)
    if form.is_valid():
        form.save(commit=True)
        return redirect('usuarios')
    else:
        print(form.errors)
    dato = {'form':form}
    return render(request,template_name,dato)'''
    
'''def modificar_genero(request,pk,template_name='escuela/genero_form.html'):
    genero = Genero.objects.get(nombre=pk)
    form = GeneroForm(request.POST or None, instance=genero)
    if form.is_valid():
        form.save(commit=True)
        return redirect('generos')
    else:
        print(form.errors)
    dato = {'form':form}
    return render(request,template_name,dato)

def modificar_persona(request,pk,template_name='escuela/persona_form.html'):
    persona = Persona.objects.get(num_cuit=pk)
    form = PersonaForm(request.POST or None, instance=persona)
    if form.is_valid():
        form.save(commit=True)
        return redirect('personas')
    else:
        print(form.errors)
    dato = {'form':form}
    return render(request,template_name,dato)'''

@login_required
def modificar_preceptor(request,pk,template_name='escuela/preceptor_form.html'):
    preceptor = Preceptor.objects.get(idPreceptor=pk)
    form = PreceptorForm(request.POST or None, instance=preceptor)
    if form.is_valid():
        form.save(commit=True)
        return redirect('preceptores')
    else:
        print(form.errors)
    dato = {'form':form}
    return render(request,template_name,dato)

@login_required
def modificar_aula(request,pk,template_name='escuela/aula_form.html'):
    aula = Aula.objects.get(idAula=pk)
    form = AulaForm(request.POST or None, instance=aula)
    if form.is_valid():
        form.save(commit=True)
        return redirect('aulas')
    else:
        print(form.errors)
    dato = {'form':form}
    return render(request,template_name,dato)

@login_required
def modificar_alumno(request,pk,template_name='escuela/alumno_form.html'):
    alumno = Alumno.objects.get(num_reg=pk)
    form = AlumnoForm(request.POST or None, instance=alumno)
    if form.is_valid():
        form.save(commit=True)
        return redirect('alumnos')
    else:
        print(form.errors)
    dato = {'form':form}
    return render(request,template_name,dato)

@login_required
def modificar_materia(request,pk,template_name='escuela/materia_form.html'):
    materia = Materia.objects.get(codigo=pk)
    form = MateriaForm(request.POST or None, instance=materia)
    if form.is_valid():
        form.save(commit=True)
        return redirect('materias')
    else:
        print(form.errors)
    dato = {'form':form}
    return render(request,template_name,dato)

@login_required
def modificar_curso(request,pk,template_name='escuela/curso_form.html'):
    curso = Curso.objects.get(id=pk)
    form = CursoForm(request.POST or None, instance=curso)
    if form.is_valid():
        form.save(commit=True)
        return redirect('cursos')
    else:
        print(form.errors)
    dato = {'form':form}
    return render(request,template_name,dato)

@login_required
def modificar_turno(request,pk,template_name='escuela/turno_form.html'):
    turno = Turno.objects.get(idTurno=pk)
    form = TurnoForm(request.POST or None, instance=turno)
    if form.is_valid():
        form.save(commit=True)
        return redirect('turnos')
    else:
        print(form.errors)
    dato = {'form':form}
    return render(request,template_name,dato)

@login_required
def modificar_tiene(request,pk,template_name='escuela/tiene_form.html'):
    tiene = Tiene.objects.get(id=pk)
    form = TieneForm(request.POST or None, instance=tiene)
    if form.is_valid():
        form.save(commit=True)
        return redirect('tienen')
    else:
        print(form.errors)
    dato = {'form':form}
    return render(request,template_name,dato)

@login_required
def modificar_rinde(request,pk,template_name='escuela/rinde_form.html'):
    rinde = Rinde.objects.get(id=pk)
    form = RindeForm(request.POST or None, instance=rinde)
    if form.is_valid():
        form.save(commit=True)
        return redirect('rinden')
    else:
        print(form.errors)
    dato = {'form':form}
    return render(request,template_name,dato)

@login_required
def modificar_profesor(request,pk,template_name='escuela/profesor_form.html'):
    profesor = Profesor.objects.get(idProfesor=pk)
    form = ProfesorForm(request.POST or None, instance=profesor)
    if form.is_valid():
        form.save(commit=True)
        return redirect('profesores')
    else:
        print(form.errors)
    dato = {'form':form}
    return render(request,template_name,dato)

@login_required
def modificar_dicta(request,pk,template_name='escuela/dicta_form.html'):
    dicta = Dicta.objects.get(id=pk)
    form = DictaForm(request.POST or None, instance=dicta)
    if form.is_valid():
        form.save(commit=True)
        return redirect('dictan')
    else:
        print(form.errors)
    dato = {'form':form}
    return render(request,template_name,dato)

@login_required
def eliminar_tipo_usuario(request,pk,template_name='escuela/tipo_usuario_confirmar_eliminacion.html'):
    tipo_usuario=TipoUsuario.objects.get(nombre=pk)
    if request.method=='POST':
        tipo_usuario.delete()
        return redirect('tipos_usuario')
    else:
        dato={'form':tipo_usuario}
        return render(request,template_name,dato)

'''def eliminar_usuario(request,pk,template_name='escuela/usuario_confirmar_eliminacion.html'):
    usuario=User.objects.get(num_cuit=pk)
    if request.method=='POST':
        usuario.delete()
        return redirect('usuarios')
    else:
        dato={'form':usuario}
        return render(request,template_name,dato)'''

'''def eliminar_genero(request,pk,template_name='escuela/genero_confirmar_eliminacion.html'):
    genero=Genero.objects.get(nombre=pk)
    if request.method=='POST':
        genero.delete()
        return redirect('generos')
    else:
        dato={'form':genero}
        return render(request,template_name,dato)

def eliminar_persona(request,pk,template_name='escuela/persona_confirmar_eliminacion.html'):
    persona=Persona.objects.get(num_cuit=pk)
    if request.method=='POST':
        persona.delete()
        return redirect('personas')
    else:
        dato={'form':persona}
        return render(request,template_name,dato)'''

@login_required
def eliminar_preceptor(request,pk,template_name='escuela/preceptor_confirmar_eliminacion.html'):
    preceptor=Preceptor.objects.get(idPreceptor=pk)
    if request.method=='POST':
        preceptor.delete()
        return redirect('preceptores')
    else:
        dato={'form':preceptor}
        return render(request,template_name,dato)

@login_required
def eliminar_aula(request,pk,template_name='escuela/aula_confirmar_eliminacion.html'):
    aula=Aula.objects.get(idAula=pk)
    if request.method=='POST':
        aula.delete()
        return redirect('aulas')
    else:
        dato={'form':aula}
        return render(request,template_name,dato)

@login_required
def eliminar_alumno(request,pk,template_name='escuela/alumno_confirmar_eliminacion.html'):
    alumno=Alumno.objects.get(num_reg=pk)
    if request.method=='POST':
        alumno.delete()
        return redirect('alumnos')
    else:
        dato={'form':alumno}
        return render(request,template_name,dato)

@login_required
def eliminar_materia(request,pk,template_name='escuela/materia_confirmar_eliminacion.html'):
    materia=Materia.objects.get(codigo=pk)
    if request.method=='POST':
        materia.delete()
        return redirect('materias')
    else:
        dato={'form':materia}
        return render(request,template_name,dato)

@login_required
def eliminar_curso(request,pk,template_name='escuela/curso_confirmar_eliminacion.html'):
    curso=Curso.objects.get(id=pk)
    if request.method=='POST':
        curso.delete()
        return redirect('cursos')
    else:
        dato={'form':curso}
        return render(request,template_name,dato)

@login_required
def eliminar_turno(request,pk,template_name='escuela/turno_confirmar_eliminacion.html'):
    turno=Turno.objects.get(idTurno=pk)
    if request.method=='POST':
        turno.delete()
        return redirect('turnos')
    else:
        dato={'form':turno}
        return render(request,template_name,dato)

@login_required
def eliminar_tiene(request,pk,template_name='escuela/tiene_confirmar_eliminacion.html'):
    tiene=Tiene.objects.get(id=pk)
    if request.method=='POST':
        tiene.delete()
        return redirect('tienen')
    else:
        dato={'form':tiene}
        return render(request,template_name,dato)

@login_required
def eliminar_rinde(request,pk,template_name='escuela/rinde_confirmar_eliminacion.html'):
    rinde=Rinde.objects.get(id=pk)
    if request.method=='POST':
        rinde.delete()
        return redirect('rinden')
    else:
        dato={'form':rinde}
        return render(request,template_name,dato)

@login_required
def eliminar_profesor(request,pk,template_name='escuela/profesor_confirmar_eliminacion.html'):
    profesor=Profesor.objects.get(idProfesor=pk)
    if request.method=='POST':
        profesor.delete()
        return redirect('profesores')
    else:
        dato={'form':profesor}
        return render(request,template_name,dato)

@login_required
def eliminar_dicta(request,pk,template_name='escuela/dicta_confirmar_eliminacion.html'):
    dicta=Dicta.objects.get(id=pk)
    if request.method=='POST':
        dicta.delete()
        return redirect('dictan')
    else:
        dato={'form':dicta}
        return render(request,template_name,dato)