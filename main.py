from flask import Flask, render_template, url_for, send_from_directory
from werkzeug.utils import redirect

from forms import SendLetter
from flask_bootstrap import Bootstrap
from contact import Contact

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sadgfsg'
Bootstrap(app)


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/generic')
def generic_page():
    return render_template('generic.html')


@app.route('/elements')
def elements_page():
    return render_template('elements.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact_page():
    message_form = SendLetter()
    if message_form.validate_on_submit():

        email_data = {
            'name' : message_form.name.data,
            'email' : message_form.email.data,
            'message' : message_form.message.data}

        Contact.send_message(email_data)
        return redirect(url_for('contact_page'))

    return render_template('contact.html', form=message_form, message='Feel free to leave a note for me')


@app.route('/download_cv')
def download_cv():
    return send_from_directory('static', path='files/Resume.pdf')


if __name__ == '__main__':
    app.run(debug=True)


