from flask import Flask, render_template

app = Flask(__name__)

def calcular_factorial(n):
    """Calcula el factorial de un número n."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * calcular_factorial(n - 1)

@app.route('/')
def index():
    """Página principal."""
    return render_template('index.html')

@app.route('/factorial/<int:numero>')
def factorial(numero):
    """Calcula y muestra el factorial del número proporcionado en la URL."""
    try:
        if numero < 0:
            return render_template('factorial.html', 
                numero=numero, 
                resultado="Error: No se puede calcular el factorial de un número negativo")
        resultado = calcular_factorial(numero)
        return render_template('factorial.html', 
            numero=numero, 
            resultado=resultado)
    except RecursionError:
        return render_template('factorial.html', 
            numero=numero, 
            resultado="Error: Número demasiado grande para calcular el factorial")

if __name__ == '__main__':
    app.run(debug=True)