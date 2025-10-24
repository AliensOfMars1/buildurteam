from flask import render_template
from . import messages_bp

@messages_bp.route('/inbox')
def inbox():
    return render_template('messages/inbox.html')

@messages_bp.route('/chat')
def chat():
    return render_template('messages/chat.html')
