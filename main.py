from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

#templates

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/administrador')
def administrador():
    return render_template('administrador.html')

@app.route('/trabajador')
def trabajador():
    return render_template('trabajador.html')

@app.route('/perfil/<modo>/<nombre>')
#modo: administrador, trabajador, eliminar
def perfil(nombre, modo):
    return render_template('perfil.html', modo=modo)

@app.route('/mensaje/<modo>')
#modo: leer, escribir
def mensaje(modo):
    return render_template('mensaje.html', modo=modo)


# redireccionamientos
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and validateUser(request.form['nombre'], request.form['contrasena']):
        return redirect(url_for('home'))
    else:
        return redirect(url_for('index'))


@app.route('/home')
def home():
    rol = 'trabajador'
    if(rol != 'administrador'):
        return redirect(url_for('administrador'))
    else: 
        return redirect(url_for('trabajador'))

#editar perfil


#metodos
def validateUser(nombre, contrasena):
    return True

if __name__ == '__main__':
    app.run(debug=True)
