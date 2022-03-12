from flask import Flask, render_template, flash, jsonify, request
from forms import FPLForm
from apis.fplAPI import FplAPI

app = Flask(__name__)
app.config['SECRET_KEY'] = '754ed566bad766b59bd7165c'


@app.route("/", methods=['GET'])
def index():
    fpl = FplAPI()
    choices = fpl.getTeams()
    playerChoices = fpl.getPlayersFromTeam('1')
    form = FPLForm()
    form.setChoices(choices)
    form.setPlayersChoices(playerChoices)
    if form.validate_on_submit():
        pass
    if form.errors != {}:
        for error in form.errors.values():
            flash(f'There was an error {error}')
    return render_template('form.html', form=form)


@app.route("/players/<teamID>")
def updateForm(teamID):
    fpl = FplAPI()
    names = fpl.getPlayersFromTeam(teamID)
    return jsonify({'players': names})


@app.route("/compare", methods=["POST"])
def displayResult():
    #render template, make requests and show results
    return f'{request.form.get("player1")} , {request.form.get("player2")}, {request.form.get("odds")}'
