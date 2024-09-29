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
    rows1 = int(request.form['rows1'])
    cols1 = int(request.form['cols1'])
    operation = request.form['operation']
    steps = []  # Inisialisasi steps sebagai list kosong
    method = request.form.get('method', 'gauss')  # Tambahkan nilai default 'gauss' jika tidak ada input method

    if operation not in ['determinant', 'transpose', 'scalar_multiplication', 'power', 'inverse', 'row_echelon', 'solve_linear_system']:
        rows2 = int(request.form['rows2'])
        cols2 = int(request.form['cols2'])

    # Konversi input Matriks 1 dari grid menjadi numpy array
    matrix1 = np.zeros((rows1, cols1))
    for i in range(rows1):
        for j in range(cols1):
            cell_value = request.form.get(f'matrix1-grid_cell_{i}_{j}')
            matrix1[i, j] = float(cell_value) if cell_value else 0

    # Mengambil nilai matriks 2 jika diperlukan
    matrix2 = None
    if operation not in ['determinant', 'transpose', 'scalar_multiplication', 'power', 'inverse', 'row_echelon', 'solve_linear_system']:
        matrix2 = np.zeros((rows2, cols2))
        for i in range(rows2):
            for j in range(cols2):
                cell_value = request.form.get(f'matrix2-grid_cell_{i}_{j}')
                matrix2[i, j] = float(cell_value) if cell_value else 0

    # Mengambil nilai skalar jika diperlukan
    scalar = float(request.form.get('scalar', 1))
    power = int(request.form.get('power', 1))

    # Pemrosesan operasi berdasarkan yang dipilih
    result = None
    try:
        if operation == 'addition' and matrix2 is not None and matrix1.shape == matrix2.shape:
            result = matrix1 + matrix2
        elif operation == 'subtraction' and matrix2 is not None and matrix1.shape == matrix2.shape:
            result = matrix1 - matrix2
        elif operation == 'multiplication' and matrix2 is not None:
            result = np.dot(matrix1, matrix2)
        elif operation == 'determinant' and rows1 == cols1:
            result = np.linalg.det(matrix1)
        elif operation == 'transpose':
            result = matrix1.T
        elif operation == 'scalar_multiplication':
            result = scalar * matrix1
        elif operation == 'power' and rows1 == cols1:
            result = np.linalg.matrix_power(matrix1, int(power))
        elif operation == 'inverse' and rows1 == cols1:
            try:
                result = np.linalg.inv(matrix1)
            except np.linalg.LinAlgError:
                result = "Error: Matriks tidak dapat dibalik (singular)."
        elif operation == 'row_echelon':
            result, steps = row_echelon_with_steps(matrix1)
        elif operation == 'solve_linear_system' :
            result, steps = solve_linear_system(matrix1, method)
        else:
            return "Error: Operasi tidak valid atau dimensi matriks tidak cocok.", 400
    except ValueError as ve:
        result = f"Error: Nilai input tidak valid. {str(ve)}"
    except TypeError as te:
        result = f"Error: Jenis input tidak valid. {str(te)}"
    except Exception as e:
        result = f"Error tidak terduga: {str(e)}"

    # Render template dengan menambahkan variabel `steps`
    return render_template('result.html', result=result, operation=operation, steps=steps)

def row_echelon_with_steps(matrix):
    # Salin matriks asli untuk diproses dan pastikan dalam bentuk float
    m = matrix.copy().astype(float)
    rows, cols = m.shape
    steps = []  # List untuk menyimpan setiap langkah
    
    for i in range(min(rows, cols)):
        max_row = np.argmax(np.abs(m[i:, i])) + i
        if m[max_row, i] != 0:  # Jika elemen terbesar tidak nol, tukar baris
            if max_row != i:
                m[[i, max_row]] = m[[max_row, i]]  # Tukar baris
                steps.append(f"Tukar baris {i+1} dengan baris {max_row+1}:\n{m}\n")
        
        # Normalisasi baris dengan pivot (buat elemen utama menjadi 1)
        if m[i, i] != 0:
            pivot = m[i, i]
            m[i] = m[i] / pivot
            steps.append(f"Normalisasi baris {i+1} dengan pivot {pivot}:\n{m}\n")
        
        # Eliminasi elemen di bawah elemen pivot
        for j in range(i + 1, rows):
            if m[j, i] != 0:
                factor = m[j, i]
                m[j] = m[j] - factor * m[i]
                steps.append(f"Eliminasi elemen pada baris {j+1} menggunakan baris {i+1}:\n{m}\n")
    
    return m, steps

def solve_linear_system(matrix, method):
    try:
        A = matrix[:, :-1]
        B = matrix[:, -1]
        det_A = np.linalg.det(A)
        if det_A == 0:
            return "Sistem tidak memiliki solusi unik (determinannya nol).", []

        if method == 'gauss':
            solution, steps = gauss_elimination(matrix)
        elif method == 'gauss-jordan':
            solution, steps = gauss_jordan_elimination(matrix)
        else:
            return f"Metode '{method}' tidak dikenali. Gunakan 'gauss' atau 'gauss-jordan'.", []

        result = "Solusi variabel yang dicari:\n"
        for i, sol in enumerate(solution):
            result += f"x{i+1} = {sol:.2f}\n"

        return result, steps
    except np.linalg.LinAlgError:
        return "Sistem tidak memiliki solusi atau memiliki solusi tak hingga.", []
    except Exception as e:
        return f"Terjadi kesalahan: {str(e)}", []
    
def gauss_elimination(matrix):
    m = matrix.copy().astype(float)
    rows, cols = m.shape
    steps = []  # List untuk menyimpan langkah-langkah eliminasi

    for i in range(min(rows, cols - 1)):
        # Partial pivoting: Cari elemen terbesar di kolom sebagai pivot
        max_row = np.argmax(np.abs(m[i:, i])) + i
        if m[max_row, i] != 0:
            if max_row != i:
                m[[i, max_row]] = m[[max_row, i]]  # Tukar baris
                steps.append(f"Tukar baris {i+1} dengan baris {max_row+1}:\n{m}\n")

            # Normalisasi baris dengan pivot
            pivot = m[i, i]
            m[i] = m[i] / pivot
            steps.append(f"Normalisasi baris {i+1} dengan pivot {pivot}:\n{m}\n")

            # Eliminasi elemen di bawah pivot
            for j in range(i + 1, rows):
                factor = m[j, i]
                m[j] = m[j] - factor * m[i]
                steps.append(f"Eliminasi elemen pada baris {j+1} menggunakan baris {i+1}:\n{m}\n")

    # Back substitution untuk menemukan solusi
    solution = np.zeros(rows)
    for i in range(rows - 1, -1, -1):
        solution[i] = (m[i, -1] - np.dot(m[i, i+1:cols-1], solution[i+1:])) / m[i, i]
        steps.append(f"Substitusi balik untuk x{i+1} = {solution[i]}:\n{m}\n")

    return solution, steps

def gauss_jordan_elimination(matrix):
    m = matrix.copy().astype(float)
    rows, cols = m.shape
    steps = []  # List untuk menyimpan langkah-langkah eliminasi

    for i in range(min(rows, cols - 1)):
        # Partial pivoting: Cari elemen terbesar di kolom sebagai pivot
        max_row = np.argmax(np.abs(m[i:, i])) + i
        if m[max_row, i] != 0:
            if max_row != i:
                m[[i, max_row]] = m[[max_row, i]]  # Tukar baris
                steps.append(f"Tukar baris {i+1} dengan baris {max_row+1}:\n{m}\n")

            # Normalisasi baris dengan pivot
            pivot = m[i, i]
            m[i] = m[i] / pivot
            steps.append(f"Normalisasi baris {i+1} dengan pivot {pivot}:\n{m}\n")

            # Eliminasi elemen di atas dan di bawah pivot
            for j in range(rows):
                if j != i:
                    factor = m[j, i]
                    m[j] = m[j] - factor * m[i]
                    steps.append(f"Eliminasi elemen pada baris {j+1} menggunakan baris {i+1}:\n{m}\n")

    # Solusi dari matriks Gauss-Jordan
    solution = m[:, -1]
    return solution, steps

if __name__ == '__main__':
    app.run(debug=True)
