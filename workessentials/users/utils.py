import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from workessentials import mail

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename) # Grab both file name and file extension that the user upload use '_' to throw away 
    picture_fn = random_hex + f_ext # gets random hex + uploaded file extension
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn) # app.root_path = full path up to our package directory 
    # os.path.join make sure that all gets joined in one correct path

    # Image resizing before uploading with Pillow (Check out Video for more in depth guide to Pillow)
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn



# use jinja2 to help with complicated messages check out viceo
def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
                  sender='noreply@workessentials.info',
                  recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{url_for('users.reset_token', token=token, _external=True)}
If you did not make this request then simply ignore this email and no changes will be made.
'''
    mail.send(msg)
