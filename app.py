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
    operation = request.form['operation']
    return render_template('input.html', operation=operation)

# Route untuk memproses matriks dan menampilkan hasil
@app.route('/process_matrices', methods=['POST'])
def process_matrices():
    matrices = request.form.getlist('matrices')
    operation = request.form['operation']
    
    # Konversi input ke numpy array
    matrix1 = np.array(eval(request.form['matrix1']))
    if 'matrix2' in request.form:
        matrix2 = np.array(eval(request.form['matrix2']))
    
    result = None
    if operation == 'addition':
        result = matrix1 + matrix2
    elif operation == 'subtraction':
        result = matrix1 - matrix2
    elif operation == 'multiplication':
        result = matrix1 @ matrix2
    elif operation == 'division':
        result = matrix1 / matrix2
    elif operation == 'determinant':
        result = np.linalg.det(matrix1)
    elif operation == 'transpose':
        result = matrix1.T

    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
