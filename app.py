from flask import Flask
from configuración.config import Config
from rutas.ventas import ventas_bp

def crear_app():
  app = Flask(__name__)
  app.config.from_object(Config)

  app.register_blueprint(ventas_bp)


  return app


app = crear_app()

if __name__ == "__main__":
      app.run(debug=True)