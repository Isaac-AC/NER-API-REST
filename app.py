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

        # Itera sobre las oraciones en el documento
        for sentence in doc.sents:

            entities = {}

            # Itera sobre las entidades en la oración
            for ent in sentence.ents:

                # Agrega el texto de la entidad y la etiqueta al diccionario
                entities[ent.text] = ent.label_

            result = {
                "oración": sentence.text,
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

