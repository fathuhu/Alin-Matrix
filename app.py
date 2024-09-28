from flask import Flask, render_template, request, jsonify
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_matrices', methods=['POST'])
def process_matrices():
    rows = int(request.form['rows'])
    cols = int(request.form['cols'])
    operation = request.form['operation']

    # Konversi input Matriks 1 dari grid menjadi numpy array
    matrix1 = np.zeros((rows, cols))
    for i in range(rows):
        for j in range(cols):
            cell_value = request.form.get(f'matrix1-grid_cell_{i}_{j}')
            matrix1[i, j] = float(cell_value) if cell_value else 0

    # Mengambil nilai matriks 2 jika diperlukan
    matrix2 = None
    if operation not in ['determinant', 'transpose', 'scalar_multiplication', 'power', 'inverse', 'row_echelon', 'solve_linear_system']:
        matrix2 = np.zeros((rows, cols))
        for i in range(rows):
            for j in range(cols):
                cell_value = request.form.get(f'matrix2-grid_cell_{i}_{j}')
                matrix2[i, j] = float(cell_value) if cell_value else 0

    # Proses operasi sesuai pilihan
    if operation == 'addition':
        result = np.add(matrix1, matrix2)
    elif operation == 'subtraction':
        result = np.subtract(matrix1, matrix2)
    elif operation == 'multiplication':
        result = np.matmul(matrix1, matrix2)
    elif operation == 'determinant':
        result = np.linalg.det(matrix1)
    elif operation == 'transpose':
        result = matrix1.T
    elif operation == 'scalar_multiplication':
        scalar = float(request.form['scalar'])
        result = matrix1 * scalar
    elif operation == 'power':
        result = np.linalg.matrix_power(matrix1, 2)  # Ganti sesuai kebutuhan
    elif operation == 'inverse':
        result = np.linalg.inv(matrix1)
    elif operation == 'row_echelon':
        result = row_echelon(matrix1)
    elif operation == 'solve_linear_system':
        result = solve_linear_system(matrix1)

    return str(result)

if __name__ == '__main__':
    app.run(debug=True)


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
