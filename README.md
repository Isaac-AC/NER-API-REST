# API de Análisis de Entidades con SpaCy

Esta API utiliza el modelo de lenguaje spaCy para analizar texto y extraer entidades con nombres específicos.

## Requisitos

- Python 3.x

Bibliotecas requeridas:

- pip install flask 

- pip install -U pip setuptools wheel

- pip install -U spacy

- python -m spacy download en_core_web_sm


## Ejecución


1. Clona este repositorio:


~~~ 
git clone https://github.com/Isaac-AC/NER-API-REST.git

cd NER-API-REST
~~~

2. Abre la terminal y ejecuta la aplicacion 

~~~
python app.py
~~~

La API estará disponible en http://localhost:5000.



### Uso

    Envía una solicitud POST a http://localhost:5000/process con el formulario que contiene los parámetros taskoption (opción de tarea) y rawtext (texto a analizar).
    La API devolverá un JSON con una lista de oraciones en el texto, junto con las entidades identificadas en cada oración y sus tipos correspondientes.


## Ejemplo 

1. Abre otra terminal.

2. Ejecuta el siguiente comando:

~~~
curl -X POST -F "taskoption=organization" -F "rawtext=Apple esta buscando comprar una startup del Reino Unido por mil millones de dólares. San Francisco considera prohibir los robots de entrega en la acera." http://localhost:5000/process

~~~

3. Deberías recibir una respuesta JSON con las entidades identificadas en el texto, similar al siguiente ejemplo:

~~~
{
  "resultado": [
    {
      "entidades": {
        "Apple": "ORG",
        "Reino Unido": "LOC"
      },
      "oracion": "Apple esta buscando comprar una startup del Reino Unido por mil millones de d\u00f3lares."
    },
    {
      "entidades": {
        "San Francisco": "LOC"
      },
      "oracion": "San Francisco considera prohibir los robots de entrega en la acera."
    }
  ]
}
~~~

