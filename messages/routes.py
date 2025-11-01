
from flask import render_template, request, jsonify
from flask_login import login_required, current_user
from models import Message, User
from extensions import db
from . import messages_bp

@messages_bp.route('/inbox')
@login_required
def inbox():
    # Get user's received messages
    received_messages = Message.query.filter_by(receiver_id=current_user.id)\
                                   .order_by(Message.timestamp.desc())\
                                   .all()
    
    # Get unique senders for conversation list
    senders = db.session.query(User).join(Message, User.id == Message.sender_id)\
                                  .filter(Message.receiver_id == current_user.id)\
                                  .distinct().all()
    
    return render_template('messages/inbox.html', 
                         received_messages=received_messages,
                         senders=senders)

@messages_bp.route('/chat/<int:user_id>')
@login_required
def chat(user_id):
    other_user = User.query.get_or_404(user_id)
    
    # Get conversation between current user and other user
    messages = Message.query.filter(
        ((Message.sender_id == current_user.id) & (Message.receiver_id == user_id)) |
        ((Message.sender_id == user_id) & (Message.receiver_id == current_user.id))
    ).order_by(Message.timestamp.asc()).all()
    
    return render_template('messages/chat.html', 
                         other_user=other_user,
                         messages=messages)



