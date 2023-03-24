from flask import Flask

from .controllers.fise import test_fise, controlador2_bp

app = Flask(__name__)

print("sssssssssssssssssss")

app.register_blueprint(test_fise)
app.register_blueprint(controlador2_bp)



app.run(host='0.0.0.0', port=5000)
