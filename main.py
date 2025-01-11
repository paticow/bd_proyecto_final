from flask import Flask, render_template, request, redirect, url_for, session
import pymysql

app = Flask(__name__)
app.secret_key = 'nailongsecret'
connection = pymysql.connect(host="127.0.0.1", user="user", password="12345", db="deliverys")

#templates

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/administrador')
def administrador():
    cursor = connection.cursor();
    sql = "SELECT * FROM trabajador"
    cursor.execute(sql)
    trabajadores = cursor.fetchall()
    return render_template('administrador.html', trabajadores=trabajadores, nombre=session['nombre'])

@app.route('/trabajador')
def trabajador():
    return render_template('trabajador.html', nombre=session['nombre'])

@app.route('/perfil/<modo>/<cedula>')
#modo: administrador, trabajador, eliminar, crear
def perfil(modo, cedula):
    user = getTrabajador(session['cedula']) if modo != "eliminar" else cedula
    return render_template('perfil.html', modo=modo, user=user)

@app.route('/mensaje/<modo>')
#modo: leer, escribir
def mensaje(modo):
    return render_template('mensaje.html', modo=modo)


# redireccionamientos
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and validateUser(request.form['nombre'], request.form['contrasena']):
        session['nombre'] = request.form['nombre']
        session['contrasena'] = request.form['contrasena']
        cursor = connection.cursor()
        sql = "SELECT * FROM trabajador WHERE nombre=%s AND contrasena=%s"
        cursor.execute(sql, [request.form['nombre'], request.form['contrasena']])
        usuario = cursor.fetchone()
        session['cedula'] = usuario[0]
        session['rol'] = usuario[4]
        return redirect(url_for('home'))
    else:
        return redirect(url_for('index'))

@app.route("/createUser", methods=['GET','POST'])
def createUser():
    if request.method == 'POST':
        cursor = connection.cursor()
        sql = "INSERT INTO trabajador (nombre, apellido, cedula, contrasena, datos_transferencia, rol, horas, sueldo, estado) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql, [request.form['nombre'], request.form['apellido'], request.form['cedula'], request.form['contrasena'], request.form['datos_transferencia'], request.form['rol'], request.form['horas'], request.form['sueldo'], 0])
        connection.commit()
        return redirect(url_for('home'))
    else:
        pass

@app.route("/modifyUser", methods=['GET','POST'])
def modifyUser():
    if request.method == 'POST':
        cursor = connection.cursor()
        print(trabajador)
        sql_administrador = "UPDATE trabajador SET nombre=%s, apellido=%s, cedula=%s, datos_transferencia=%s, rol=%s, horas=%s WHERE cedula=%s"
        sql_trabajador = "UPDATE trabajador SET nombre=%s, apellido=%s, cedula=%s, datos_transferencia=%s WHERE cedula=%s"
        if session['rol'] == 'administrador':
            cursor.execute(sql_administrador, [request.form['nombre'], request.form['apellido'], request.form['cedula'], request.form['datos_transferencia'], request.form['rol'], request.form['horas'], request.form['cedula']])
        else: 
            cursor.execute(sql_administrador, [request.form['nombre'], request.form['apellido'], request.form['cedula'], request.form['datos_transferencia'], request.form['cedula']])

        session['nombre'] = request.form['nombre']
        connection.commit()
        return redirect(url_for('home'))
    else:
        pass

@app.route('/logout')
def logout():
    session.pop('nombre', None)
    session.pop('contrasena', None)
    session.pop('rol', None)
    return redirect(url_for('index'))

@app.route('/home')
def home():
    if(session['rol'] == 'administrador'):
        return redirect(url_for('administrador'))
    else: 
        return redirect(url_for('trabajador'))

#editar perfil


#metodos
def validateUser(nombre, contrasena):
    return True

def getTrabajador(cedula):
    cursor = connection.cursor()
    sql = 'SElECT * FROM trabajador WHERE cedula = %s'
    cursor.execute(sql, [cedula])
    return cursor.fetchone()

if __name__ == '__main__':
    app.run(debug=True)
