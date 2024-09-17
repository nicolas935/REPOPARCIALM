from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Conexión a la base de datos MySQL
db = mysql.connector.connect(
    host="localhost",
    user="tu_usuario_mysql",  # Reemplaza con el nombre de usuario MySQL
    password="tu_contraseña_mysql",  # Reemplaza con la contraseña MySQL
    database="user_registration"
)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        password = request.form['password']
        fecha_nacimiento = request.form['fecha_nacimiento']

        cursor = db.cursor()
        query = "INSERT INTO usuarios (nombre, apellido, password, fecha_nacimiento) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (nombre, apellido, password, fecha_nacimiento))
        db.commit()

        return "Usuario registrado con éxito"
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
