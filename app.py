from flask import Flask, render_template, flash, jsonify, request
from forms import FPLForm
from apis.fplAPI import FplAPIPlayersHandler, FplAPIGWHandler
from dataParser import Parser

app = Flask(__name__)
app.config['SECRET_KEY'] = '754ed566bad766b59bd7165c'


@app.route("/", methods=['GET'])
def index():
    fpl = FplAPIPlayersHandler()
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
    fpl = FplAPIPlayersHandler()
    names = fpl.getPlayersFromTeam(teamID)
    return jsonify({'players': names})


@app.route("/compare", methods=["POST"])
def displayResult():
    formData = {
        'team1': request.form.get("team1"),
        'team2': request.form.get("team2"),
        'player1': request.form.get("player1"),
        'player2': request.form.get("player2"),
        'from_gw': request.form.get("from_gw"),
        'to_gw': FplAPIGWHandler().getFinishedGW(),
        'odds': request.form.get("odds"),
    }
    player1Data, player2Data = Parser(formData).parse()
    return render_template('compare.html', player1Data=player1Data, player2Data=player2Data)
