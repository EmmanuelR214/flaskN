from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

notes = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add_note():
    note = request.form.get('note')
    print("Nota recibida desde el formulario:", note) 
    if note:
        notes.append(note)
        print("Nota agregada correctamente:", note)  
        return f"Nota agregada: {note}"
    else:
        print("Error: No se recibió ninguna nota.")  
        return "Por favor, envía una nota."

@app.route('/notes', methods=['GET'])
def list_notes():
    print("Lista de notas:", notes)  
    return jsonify(notes)

if __name__ == '__main__':
    app.run(debug=True)