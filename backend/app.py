# app.py
from flask import Flask, request, render_template
from summarize import summarize_document, get_summary_history

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', original_text='', summary='', history=get_summary_history())

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.form['document']
    summary = summarize_document(data)
    return render_template('index.html', original_text=data, summary=summary, history=get_summary_history())

if __name__ == '__main__':
    app.run(debug=True)
