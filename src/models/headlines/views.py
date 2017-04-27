from flask import Blueprint, render_template, redirect, url_for

from src.models.headlines.headlines import Headlines
headlines_blueprint = Blueprint('headlines', __name__)


@headlines_blueprint.route("/")
def index():
    headlines = Headlines.get_all()
    # get the headlines revision number
    try:
        # try is added to avoid the TypeError when the DB is empty
        rev = Headlines.get_highest_revision()
    except TypeError:
        rev = None
    # print(rev)
    return render_template('headlines/headlines_index.html', headlines=headlines, rev=rev)


@headlines_blueprint.route('/deactivate/<string:headline_id>')
def deactivate_headline(headline_id):
    Headlines.find_by_id(headline_id).deactivate()
    return redirect(url_for(".index"))


@headlines_blueprint.route('/remove_all/<int:rev>')
def deactivate_all_read(rev):
    # print('the revision is {}'.format(rev))
    Headlines.deactivate_all_by_rev(rev)
    return redirect(url_for(".index"))

