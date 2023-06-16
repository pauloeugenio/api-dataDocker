from flask import Flask, jsonify
import csv
import mysql.connector

app = Flask(__name__)

@app.route('/consulta', methods=['GET'])
def consultar_dados():
    try:
        # Conecta ao banco de dados MySQL
        conn = mysql.connector.connect(
            host='172.18.1.9',
            port=3306,
            user='MEU_USER',
            password='MINHA_SENHA',
            database='MINHA_BASE'
        )
        cursor = conn.cursor()

        # Executa a consulta dos últimos 20 dados da tabela
        cursor.execute('SELECT * FROM SM_002_Sensor ORDER BY recvTime DESC LIMIT 20')
        data = cursor.fetchall()

        # Gera um arquivo CSV com os dados
        with open('consulta.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)

        cursor.close()
        conn.close()

        return jsonify({'message': 'Consulta realizada com sucesso!'})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0')
