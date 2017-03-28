from flask import Blueprint, render_template, redirect, url_for

from src.models.headlines.headlines import Headlines
headlines_blueprint = Blueprint('headlines', __name__)


@headlines_blueprint.route("/")
def index():
    headlines = Headlines.get_all()
    return render_template('headlines/headlines_index.html', headlines=headlines)


@headlines_blueprint.route('/deactivate/<string:headline_id>')
def deactivate_headline(headline_id):
    print(headline_id)
    Headlines.find_by_id(headline_id).deactivate()
    print('deleting the link')
    return redirect(url_for(".index"))

