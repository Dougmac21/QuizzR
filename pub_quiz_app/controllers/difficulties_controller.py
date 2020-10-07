from flask import Blueprint, Flask, redirect, render_template, request

from models.difficulty import Difficulty
import repositories.difficulty_repository as difficulty_repository

difficulties_blueprint = Blueprint("difficulties", __name__)


# difficulties are not to be manipulated by the user at this time.
# they are set as reference data for questions.