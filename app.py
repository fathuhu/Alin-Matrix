from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/choose_operation', methods=['POST'])
def choose_operation():
    operation = request.form['operation']
    return render_template('input.html', operation=operation)

@app.route('/process_matrices', methods=['POST'])
def process_matrices():
    rows = int(request.form['rows'])
    cols = int(request.form['cols'])
    operation = request.form['operation']

    # Konversi input Matriks 1 dari grid menjadi numpy array
    matrix1 = np.zeros((rows, cols))
    for i in range(rows):
        for j in range(cols):
<<<<<<< HEAD
            matrix1[i, j] = float(request.form.get(f'matrix1-grid_cell_{i}_{j}', 0))
=======
            cell_value = request.form.get(f'matrix1-grid_cell_{i}_{j}')
            matrix1[i, j] = float(cell_value) if cell_value else 0
>>>>>>> f1afa3652627189447a61027b04f0d82f7e0d3e7

    # Mengambil nilai matriks 2 jika diperlukan
    matrix2 = None
    if operation not in ['determinant', 'transpose', 'scalar_multiplication', 'power', 'inverse', 'row_echelon', 'solve_linear_system']:
        matrix2 = np.zeros((rows, cols))
        for i in range(rows):
            for j in range(cols):
<<<<<<< HEAD
                matrix2[i, j] = float(request.form.get(f'matrix2-grid_cell_{i}_{j}', 0))
=======
                cell_value = request.form.get(f'matrix2-grid_cell_{i}_{j}')
                matrix2[i, j] = float(cell_value) if cell_value else 0

    # Mengambil nilai skalar jika diperlukan
    scalar = float(request.form.get('scalar', 1))
>>>>>>> f1afa3652627189447a61027b04f0d82f7e0d3e7

    # Pemrosesan operasi berdasarkan yang dipilih
    result = None
    if operation == 'addition' and matrix2 is not None:
        result = matrix1 + matrix2
    elif operation == 'subtraction' and matrix2 is not None:
        result = matrix1 - matrix2
    elif operation == 'multiplication' and matrix2 is not None:
        result = np.dot(matrix1, matrix2)
    elif operation == 'division' and matrix2 is not None:
        result = matrix1 / matrix2
    elif operation == 'determinant' and rows == cols:
        result = np.linalg.det(matrix1)
    elif operation == 'transpose':
        result = matrix1.T
    elif operation == 'scalar_multiplication':
        result = scalar * matrix1
    elif operation == 'power' and rows == cols:
        result = np.linalg.matrix_power(matrix1, int(scalar))
    elif operation == 'inverse' and rows == cols:
        try:
            result = np.linalg.inv(matrix1)
        except np.linalg.LinAlgError:
            result = "Matriks tidak dapat dibalik (singular)."
    elif operation == 'row_echelon':
        result = row_echelon(matrix1)
    elif operation == 'solve_linear_system':
        result = solve_linear_system(matrix1)
    else:
        return "Invalid operation or matrix dimensions", 400

    return render_template('result.html', result=result, operation=operation)

def row_echelon(matrix):
    # Implementasi sederhana OBE (Row Echelon Form)
    m = matrix.copy()
    rows, cols = m.shape
    for i in range(min(rows, cols)):
        # Jika elemen utama nol, cari baris lain untuk diganti
        if m[i, i] == 0:
            for j in range(i + 1, rows):
                if m[j, i] != 0:
                    m[[i, j]] = m[[j, i]]  # Tukar baris
                    break
        if m[i, i] != 0:
            m[i] = m[i] / m[i, i]  # Normalisasi baris
            for j in range(i + 1, rows):
                m[j] = m[j] - m[j, i] * m[i]  # Hilangkan elemen di bawah elemen utama
    return m

def solve_linear_system(matrix):
    # Implementasi sederhana SPL menggunakan numpy (metode linalg.solve)
    try:
        A = matrix[:, :-1]
        B = matrix[:, -1]
        solution = np.linalg.solve(A, B)
        return solution
    except np.linalg.LinAlgError:
        return "Sistem tidak memiliki solusi atau memiliki solusi tak hingga."

if __name__ == '__main__':
    app.run(debug=True)
