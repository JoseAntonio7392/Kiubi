from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulación de datos de vuelos (puedes conectar esto a una base de datos o API externa después)
vuelos_db = [
    {"id": 1, "airline": "Aeroméxico", "origin": "CDMX", "destination": "Cancún", "price": "$300", "duration": "3h 45m", "date": "2025-04-15"},
    {"id": 2, "airline": "Volaris", "origin": "CDMX", "destination": "Cancún", "price": "$250", "duration": "4h 10m", "date": "2025-04-15"},
    {"id": 3, "airline": "Interjet", "origin": "Guadalajara", "destination": "Monterrey", "price": "$200", "duration": "2h 30m", "date": "2025-04-16"}
]

@app.route('/api/vuelos', methods=['GET'])
def buscar_vuelos():
    # Obtener parámetros de búsqueda desde la solicitud (origen, destino, fecha)
    origin = request.args.get('origin', '').upper()
    destination = request.args.get('destination', '').upper()
    date = request.args.get('date', '')

    # Filtrar vuelos según los parámetros
    resultados = [
        vuelo for vuelo in vuelos_db
        if (not origin or vuelo['origin'] == origin) and
           (not destination or vuelo['destination'] == destination) and
           (not date or vuelo['date'] == date)
    ]

    # Respuesta sin cookies (Flask no usa cookies por defecto a menos que las configures)
    return jsonify(resultados)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)