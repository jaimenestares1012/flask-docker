from flask import Blueprint
from ..utils.db import insertarMongo, buscarMongo, deletearMongo
test_fise = Blueprint('controlador1', __name__)
controlador2_bp = Blueprint('controlador2', __name__)


@test_fise.route('/')
def index_test():
    return {"codRes":"00", "detalles":"ok"}



@controlador2_bp.route('/test', methods=['POST'])
def controlador():
    data = {"codRes":"00", "documento":"70066431"}
    documento = "70066431"
    result_busqueda= buscarMongo( "fise", "documento" ,documento)
    print("result_busqueda---> ", result_busqueda)
    inster = insertarMongo("fise", data)
    print("inster---------->", inster)
    result_busqueda= buscarMongo( "fise", "documento" ,documento)
    print("result_busqueda---> ", result_busqueda)
    # deletearMongo( "fise", "documento", documento)
    return  {"codRes":"00", "detalles":"ok"}
