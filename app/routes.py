from flask import current_app as app, render_template, request, redirect, url_for, flash, session

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Aquí deberías añadir la lógica para verificar el usuario
        if username == 'papito' and password == 'password':  # Ejemplo simple
            flash('Inicio de sesión exitoso')
            session['username'] = username
            return redirect(url_for('home'))
        else:
            flash('Nombre de usuario o contraseña incorrectos')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Aquí deberías añadir la lógica para registrar el usuario
        flash('Registro exitoso')
        return redirect(url_for('login'))
    return render_template('register.html')
