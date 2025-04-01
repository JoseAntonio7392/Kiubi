from flask import Flask, jsonify, request
import psycopg2
from psycopg2.extras import RealDictCursor
import os

app = Flask(__name__)

def get_db_connection():
    db_url = os.environ.get('DATABASE_URL', 'dbname=kiubi_db user=postgres password=1234 host=localhost port=5432')
    conn = psycopg2.connect(db_url)
    return conn

@app.route('/api/vuelos', methods=['GET'])
def buscar_vuelos():
    origin = request.args.get('origin', '').upper()
    destination = request.args.get('destination', '').upper()
    date = request.args.get('date')

    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    query = """
        SELECT 
            v.id, 
            v.aerolinea, 
            a_origen.codigo_iata AS origin, 
            a_destino.codigo_iata AS destination, 
            v.hora_salida, 
            v.precio, 
            v.moneda, 
            v.duracion::text AS duracion,  -- Convertimos INTERVAL a texto
            v.asientos_disponibles, 
            v.estado
        FROM vuelos v
        JOIN aeropuertos a_origen ON v.aeropuerto_salida_id = a_origen.id
        JOIN aeropuertos a_destino ON v.aeropuerto_llegada_id = a_destino.id
        WHERE (a_origen.codigo_iata = %s OR %s = '')
        AND (a_destino.codigo_iata = %s OR %s = '')
        AND (%s IS NULL OR DATE(v.hora_salida) = %s)
    """
    cur.execute(query, (origin, origin, destination, destination, date or None, date))
    resultados = cur.fetchall()
    cur.close()
    conn.close()

    return jsonify(resultados)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)