from flask import Flask, render_template, request, send_file
import pdfkit

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form
    generate_pdf(data)
    return send_file('output.pdf')

def generate_pdf(data):
    # Use data to fill the PDF
    options = {
        'page-size': 'A4',
        'encoding': 'UTF-8',
    }
    html = render_template('template.html', data=data)
    pdfkit.from_string(html, 'output.pdf', options=options)

if __name__ == '__main__':
    app.run(debug=True)
