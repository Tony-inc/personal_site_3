from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, TextAreaField
from wtforms.validators import DataRequired, Email


class SendLetter(FlaskForm):
    name = StringField('', validators=[DataRequired()], render_kw={"placeholder": "Your name"})
    email = EmailField('', validators=[DataRequired(), Email()], render_kw={"placeholder": "Your email"})
    message = TextAreaField('', validators=[DataRequired()], render_kw={"placeholder": "Your message"})
    submit_button = SubmitField('Send the message')
