from flask import Blueprint, render_template, redirect, url_for

from src.models.headlines.headlines import Headlines
headlines_blueprint = Blueprint('headlines', __name__)
import src.models.headlines.constant as HeadlinesConstants


@headlines_blueprint.route("/")
def index():
    headlines = Headlines.get_all()
    try:
        # try is added to avoid the TypeError when the DB is empty
        rev = Headlines.get_highest_revision()
    except TypeError:
        rev = None
    headlines_clean = []
    # keeping a copy of healines list to remove the keyword filtered ones

    for headline in headlines:
        elements = HeadlinesConstants.rm_list
        rem = False

        for elem in elements:
            if elem in str(headline.name):
                try:
                    rem = True
                    break

                except ValueError as e:
                    continue
        if not rem:
            headlines_clean.append(headline)

    return render_template('headlines/headlines_index.html', headlines=headlines_clean, rev=rev)


@headlines_blueprint.route('/deactivate/<string:headline_id>')
def deactivate_headline(headline_id):
    Headlines.find_by_id(headline_id).deactivate()
    return redirect(url_for(".index"))


@headlines_blueprint.route('/remove_all/<int:rev>')
def deactivate_all_read(rev):
    Headlines.deactivate_all_by_rev(rev)
    return redirect(url_for(".index"))

