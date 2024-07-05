from flask import Flask, render_template, request, send_file
from fpdf import FPDF
import io

app = Flask(__name__)

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Dados para Registro da Central Geradora', 0, 1, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(10)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

    def add_section(self, title, data):
        self.chapter_title(title)
        self.chapter_body(data)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    form_data = request.form
    buffer = io.BytesIO()
    pdf = PDF()
    pdf.add_page()
    
    pdf.add_section('1 - Identificação da Unidade Consumidora - UC', f"Titular da UC: {form_data['titular']}\n"
                                                                   f"Rua/Av.: {form_data['rua']} No.: {form_data['numero']} CEP: {form_data['cep']}\n"
                                                                   f"Bairro: {form_data['bairro']} Cidade: {form_data['cidade']}\n"
                                                                   f"E-mail: {form_data['email']} Telefone: {form_data['telefone']} Celular: {form_data['celular']}\n"
                                                                   f"CNPJ/CPF: {form_data['cnpj_cpf']}")
    # Add other sections similarly

    pdf_output = pdf.output(dest='S').encode('latin1')
    buffer.write(pdf_output)
    buffer.seek(0)
    
    return send_file(buffer, as_attachment=True, download_name='form.pdf', mimetype='application/pdf')

if __name__ == '__main__':
    app.run(debug=True)
