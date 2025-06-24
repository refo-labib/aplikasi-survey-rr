# Tambahkan 'os' untuk membantu kita menentukan path
import os
from flask import Flask, render_template, request, redirect, url_for

# ----- INI BAGIAN YANG DIPERBAIKI -----
# Tentukan path absolut ke folder templates
# 1. os.path.dirname(__file__) -> mendapatkan direktori saat ini ('/api')
# 2. os.path.join(..., '..') -> naik satu level ke direktori root
# 3. os.path.join(..., 'templates') -> masuk ke folder templates
template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))

# Beri tahu Flask lokasi folder template saat inisialisasi
app = Flask(__name__, template_folder=template_dir)
# ------------------------------------


# "Database" sementara kita, sama seperti sebelumnya.
responses = []

@app.route('/')
def survey_form():
    return render_template('survey.html')

@app.route('/submit', methods=['POST'])
def submit():
    response_data = {
        'jenis_kelamin': request.form.get('jenis_kelamin'),
        'umur': request.form.get('umur'),
        'pekerjaan': request.form.get('pekerjaan'),
        'kepuasan': request.form.get('kepuasan'),
        'saran': request.form.get('saran')
    }
    responses.append(response_data)
    return redirect(url_for('admin_dashboard'))

@app.route('/admin')
def admin_dashboard():
    total_responses = len(responses)
    kepuasan_summary = {'1': 0, '2': 0, '3': 0, '4': 0}
    for resp in responses:
        if resp['kepuasan'] in kepuasan_summary:
            kepuasan_summary[resp['kepuasan']] += 1

    return render_template(
        'dashboard.html',
        responses=responses,
        total_responses=total_responses,
        kepuasan_summary=kepuasan_summary
    )
