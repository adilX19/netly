from flask import Flask, request, jsonify, render_template, flash, redirect
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    CORS(app)

    migrate = Migrate(app, db)

    db.init_app(app)

    with app.app_context():
        from . import account_routes  # Import routes
        db.create_all()  # Create database tables for our data models

        return app