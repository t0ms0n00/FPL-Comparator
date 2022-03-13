from flask_wtf import FlaskForm
from wtforms import BooleanField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired, NumberRange
from apis.fplAPI import FplAPIGWHandler


class FPLForm(FlaskForm):
    gw = FplAPIGWHandler().getFinishedGW()
    team1 = SelectField("Team_1", validators=[DataRequired()])
    team2 = SelectField("Team_2", validators=[DataRequired()])
    player1 = SelectField("Player_1", validators=[DataRequired()])
    player2 = SelectField("Player_2", validators=[DataRequired()])
    from_gw = IntegerField("From_GW", validators=[DataRequired(), NumberRange(min=1, max=gw)])
    extras = BooleanField("Show extras")
    submit = SubmitField(label='Submit')

    def setChoices(self, choices):
        self.team1.choices = choices
        self.team2.choices = choices

    def setPlayersChoices(self, choices):
        self.player1.choices = choices
        self.player2.choices = choices
