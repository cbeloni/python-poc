from flask import Flask, render_template
from flasgger import Swagger
import logging
from werkzeug.exceptions import HTTPException, BadRequest
from app_flask_document import document_app

app = Flask(__name__)
app.register_blueprint(document_app)
swagger = Swagger(app)

def get_flashed_messages():    
    return ["oi","segunda mensagem", "teste"]

@app.route('/')
def index():
    
    """Hello world com swagger
    ---    
    responses:
      200:
        description: retorna pagina renderizada de oi
      400:
        description: Erro na requsição
    """

    logging.info("estou renderizando a mensagem")
    return render_template('index.html', message = "mensagem de teste")

@app.route('/<mensagem>')
def index_mensagem(mensagem):
    """
    Hello world com swaager e parametro    
    ---
     parameters:
      - name: mensagem
        in: path
        type: string
     responses:
      200:
        description: retorna hello world
      400:
        description: Erro na requisição   
    """
    if 1 == 1:
      raise BadRequest(description = "Deu algum erro")
    return ("hello world %s" % mensagem)
  
@app.errorhandler(BadRequest)
def handle_bad_request(e):
    return 'bad request: ' + e.description, 400  
 
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 