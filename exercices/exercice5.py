# ## Exercice 5: Calculatrice API

# **Énoncé**:
# Créez une route `/calculate` qui accepte:
# - `operation`: "add", "subtract", "multiply", "divide"
# - `a`: premier nombre
# - `b`: deuxième nombre

# Exemple:
# ```bash
# curl "http://localhost:5000/calculate?operation=add&a=10&b=5"
# # {"operation": "add", "a": 10, "b": 5, "result": 15}

# curl "http://localhost:5000/calculate?operation=divide&a=10&b=0"
# # {"error": "Cannot divide by zero"}
# ```


from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculate', methods=['GET'])
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