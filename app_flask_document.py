import time
from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
import random

document_app = Blueprint('document_app', __name__,
                        template_folder='templates')

@document_app.route('/document', methods=["GET"])
def document_get():
    """Hello world com swagger
    ---    
    responses:
      200:
        description: retorna pagina renderizada de oi
      400:
        description: Erro na requsição
    """
    time.sleep(5)
    return "Exemplo get"