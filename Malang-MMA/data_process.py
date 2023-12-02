from flask import Flask
import subprocess
import time

app = Flask(__name__)

@app.route('/')
def run_python():
    while True:  # Menggunakan loop tak terbatas
        result = subprocess.run(['python', 'data_to_graph.py'], capture_output=True, text=True)
        result2 = subprocess.run(['python', 'data_to_graph_flip.py'], capture_output=True, text=True)
        response = f"Result 1: {result.stdout}<br>Result 2: {result2.stdout}"

        # Tunggu selama 5 detik sebelum eksekusi berikutnya
        time.sleep(5)

    return response

if __name__ == '__main__':
    app.run(debug=True)
