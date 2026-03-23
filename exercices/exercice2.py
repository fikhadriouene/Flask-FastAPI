# ## Exercice 2: Convertisseur de Température

# **Énoncé**:
# Créez une route `/convert/temp` qui accepte deux paramètres query:
# - `value`: la température (nombre)
# - `unit`: "c2f" (Celsius to Fahrenheit) ou "f2c" (Fahrenheit to Celsius)

# Exemple:
# ```bash
# curl "http://localhost:5000/convert/temp?value=25&unit=c2f"
# # {"celsius": 25, "fahrenheit": 77.0}

# curl "http://localhost:5000/convert/temp?value=77&unit=f2c"
# # {"fahrenheit": 77, "celsius": 25.0}
# ```

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/convert/temp', methods=['GET'])
def convert_temp():

    value = request.args.get('value')
    unit = request.args.get('unit')

    # Vérification des paramètres
    if value is None:
        return jsonify({
            "success": False,
            "error": "Missing value"
        }), 400
    
    if unit is None:
        return jsonify({
            "success": False,
            "error": "Missing unit"
        }), 400
    
    try:
        value = float(value)
    except ValueError:
        return jsonify({
            "success": False,
            "error": "Value not numeric"
        }), 400

    # Conversion
    if unit == "c2f":
        fahrenheit = (value * 9/5) + 32
        return jsonify({
            "celsius": value,
            "fahrenheit": round(fahrenheit, 2)
        })

    elif unit == "f2c":
        celsius = (value - 32) * 5/9
        return jsonify({
            "fahrenheit": value,
            "celsius": round(celsius, 2)
        })

    else:
        return jsonify({
            "success": False,
            "error": "unit not in [c2f,f2c]"
        }), 400


if __name__ == '__main__':
    app.run(debug=True)