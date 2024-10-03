from app.application import app


def init_app(application):
    from flask_migrate import Migrate

    from app.application.api import api, blueprint
    from app.application.models.base_model import authorize, db, login_manager
    from app.application.namespaces import self_improvement
    from app.application.routes import init_routes
    from app.config import Config

    migrate = Migrate()

    application.config.from_object(Config)

    application.register_blueprint(blueprint, url_prefix="/api")

    init_routes()
    api.add_namespace(self_improvement, path="/self-improvement")

    db.init_app(application)
    migrate.init_app(application, db)
    login_manager.init_app(application)
    authorize.init_app(application)


init_app(app)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
