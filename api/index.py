from flask import Flask, render_template, request, redirect, url_for

# PENTING: Nama variabel harus 'app'
app = Flask(__name__)

# "Database" sementara kita, sama seperti sebelumnya.
responses = []

@app.route('/')
def survey_form():
    # Flask akan otomatis mencari folder 'templates' di root proyek
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

# Catatan: Blok 'if __name__ == "__main__"' tidak diperlukan di Vercel.
# Vercel akan menangani cara menjalankan 'app' ini.