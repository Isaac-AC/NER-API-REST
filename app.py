from flask import Flask, request, jsonify
import spacy

# Carga el modelo de lenguaje español de SpaCy
nlp = spacy.load('es_core_news_sm')

app = Flask(__name__)

@app.route('/process', methods=["POST"])
def process():
    if request.method == 'POST':
        # Obtiene la opción de tarea y el texto sin formato del formulario de solicitud
        choice = request.form['taskoption']
        rawtext = request.form['rawtext']

        # Crea un documento SpaCy
        doc = nlp(rawtext)

        results = []

        # Divide el texto en oraciones utilizando los puntos como separadores
        sentences = [sent.text for sent in doc.sents]

        # Itera sobre las oraciones en el documento
        for sentence in sentences:

            entities = {}

            # Crea un documento SpaCy para cada oración
            sentence_doc = nlp(sentence)

            # Itera sobre las entidades en la oración
            for ent in sentence_doc.ents:

                # Agrega el texto de la entidad y la etiqueta al diccionario
                entities[ent.text] = ent.label_

            result = {
                "oracion": sentence,
                "entidades": entities
            }

            # Agrega el objeto de resultado a la lista de resultados
            results.append(result)

        response = {
            "resultado": results
        }

        return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
