from flask_wtf import FlaskForm
from wtforms import BooleanField, SelectField, SubmitField
from wtforms.validators import DataRequired


class FPLForm(FlaskForm):
    team1 = SelectField("Team_1", validators=[DataRequired()])
    team2 = SelectField("Team_2", validators=[DataRequired()])
    player1 = SelectField("Player_1", validators=[DataRequired()])
    player2 = SelectField("Player_2", validators=[DataRequired()])
    odds = BooleanField("Show odds")
    submit = SubmitField(label='Submit')

    def setChoices(self, choices):
        self.team1.choices = choices
        self.team2.choices = choices

    def setPlayersChoices(self, choices):
        self.player1.choices = choices
        self.player2.choices = choices
