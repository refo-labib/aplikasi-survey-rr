from flask import Flask, render_template, request, redirect, url_for

# Inisialisasi aplikasi Flask
app = Flask(__name__)

# Ini adalah "database" sementara kita, hanya sebuah list di memori.
# Data akan hilang jika aplikasi di-restart.
responses = []

# Halaman utama untuk mengisi survei
@app.route('/')
def survey_form():
    return render_template('survey.html')

# Rute untuk menerima data dari form survei
@app.route('/submit', methods=['POST'])
def submit():
    # Ambil data dari form yang dikirim
    response_data = {
        'jenis_kelamin': request.form.get('jenis_kelamin'),
        'umur': request.form.get('umur'),
        'pekerjaan': request.form.get('pekerjaan'),
        'kepuasan': request.form.get('kepuasan'),
        'saran': request.form.get('saran')
    }
    # Tambahkan data ke list 'responses'
    responses.append(response_data)
    # Arahkan pengguna ke halaman dashboard setelah submit
    return redirect(url_for('admin_dashboard'))

# Halaman dashboard admin untuk melihat rekap
@app.route('/admin')
def admin_dashboard():
    total_responses = len(responses)
    
    # Kalkulasi sederhana untuk rekap
    kepuasan_summary = {
        '1': 0, '2': 0, '3': 0, '4': 0
    }
    for resp in responses:
        if resp['kepuasan'] in kepuasan_summary:
            kepuasan_summary[resp['kepuasan']] += 1

    return render_template(
        'dashboard.html', 
        responses=responses, 
        total_responses=total_responses,
        kepuasan_summary=kepuasan_summary
    )

if __name__ == '__main__':
    app.run(debug=True)