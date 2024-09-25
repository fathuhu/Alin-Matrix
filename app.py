from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

# Route untuk landing page
@app.route('/')
def index():
    return render_template('index.html')

# Route untuk menangani pilihan operasi
@app.route('/choose_operation', methods=['POST'])
def choose_operation():
    operation = request.form.get('operation')  # gunakan .get() untuk mencegah error
    if not operation:
        return "Operation not selected", 400  # Berikan respons jika operation kosong
    return render_template('input.html', operation=operation)


# Route untuk memproses matriks dan menampilkan hasil
@app.route('/process_matrices', methods=['POST'])
def process_matrices():
    rows = int(request.form['rows'])
    cols = int(request.form['cols'])
    operation = request.form['operation']

    # Konversi input Matriks 1 dari grid menjadi numpy array
    matrix1 = np.zeros((rows, cols))
    for i in range(rows):
        for j in range(cols):
            matrix1[i, j] = float(request.form.get(f'matrix1-grid_cell_{i}_{j}', 0))

    matrix2 = None

    # Jika operasi membutuhkan dua matriks, ambil input Matriks 2
    if operation not in ['determinant', 'transpose']:
        matrix2 = np.zeros((rows, cols))
        for i in range(rows):
            for j in range(cols):
                matrix2[i, j] = float(request.form.get(f'matrix2-grid_cell_{i}_{j}', 0))

    # Pemrosesan operasi berdasarkan yang dipilih
    result = None
    if operation == 'addition' and matrix2 is not None:
        result = matrix1 + matrix2
    elif operation == 'subtraction' and matrix2 is not None:
        result = matrix1 - matrix2
    elif operation == 'multiplication' and matrix2 is not None:
        result = np.dot(matrix1, matrix2)  # Perkalian matriks
    elif operation == 'division' and matrix2 is not None:
        # Periksa agar tidak ada pembagian dengan 0
        try:
            result = matrix1 / matrix2  # Element-wise division
        except ZeroDivisionError:
            return "Error: Division by zero detected.", 400
    elif operation == 'determinant' and rows == cols:
        result = np.linalg.det(matrix1)
    elif operation == 'transpose':
        result = matrix1.T
    else:
        return "Invalid operation or matrix dimensions", 400

    # Mengirimkan hasil ke halaman result.html untuk ditampilkan
    return render_template('result.html', result=result, operation=operation)

if __name__ == '__main__':
    app.run(debug=True)
