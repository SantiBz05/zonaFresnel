from flask import Flask, request, render_template
import math

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    error = None

    if request.method == 'POST':
        distancia_str = request.form.get('distancia', '').strip()
        frecuencia_str = request.form.get('frecuencia', '').strip()

        # Validar campos vacíos
        if not distancia_str or not frecuencia_str:
            error = "Por favor completá ambos campos."
            return render_template('index.html', resultado=resultado, error=error)

        # Validar coma en frecuencia
        if ',' in frecuencia_str:
            error = "Por favor usá punto (.) como separador decimal en la frecuencia."
            return render_template('index.html', resultado=resultado, error=error)

        # Intentar convertir a float directamente
        try:
            distancia = float(distancia_str)
            frecuencia = float(frecuencia_str)
        except ValueError:
            error = "Por favor ingresá números válidos."
            return render_template('index.html', resultado=resultado, error=error)

        # Validar que sean positivos
        if distancia <= 0 or frecuencia <= 0:
            error = "La distancia y la frecuencia deben ser mayores a cero."
            return render_template('index.html', resultado=resultado, error=error)

        # Calcular zona Fresnel
        try:
            fresnel = 8.656 * math.sqrt(distancia / frecuencia)
            resultado = f"La Zona de Fresnel es igual a {fresnel:.2f} metros"
        except Exception as e:
            error = f"Error al calcular la zona de Fresnel: {e}"

    return render_template('index.html', resultado=resultado, error=error)

if __name__ == '__main__':
    app.run(debug=True)
