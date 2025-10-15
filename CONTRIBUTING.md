> REMINDER 

Navigation (Navbar) 


🧭 Navigation (Temporary Reminder)

The navigation bar in base.html includes only Home for now.
Other links (like Dashboard, Browse Projects, Messages, etc.) will be added after their respective blueprints and routes are registered.

When a new module is ready:

1. Register its Blueprint in app.py

2. then add its nav link inside templates/base.html


📌 Future Navbar Structure (when all blueprints are ready)
<ul class="nav-menu">
    {% if session.get('user_id') %}
        <li><a href="{{ url_for('index') }}" class="nav-link">Home</a></li>
        <li><a href="{{ url_for('user.dashboard') }}" class="nav-link">Dashboard</a></li>
        <li><a href="{{ url_for('projects.browse_projects') }}" class="nav-link">Browse Projects</a></li>
        <li><a href="{{ url_for('projects.create_project') }}" class="nav-link">Pitch Idea</a></li>
        <li><a href="{{ url_for('messages.inbox') }}" class="nav-link">Messages</a></li>
        <li><a href="{{ url_for('user.profile', user_id=session['user_id']) }}" class="nav-link">
            {{ session.get('username', 'Profile') }}
        </a></li>
        <li><a href="{{ url_for('auth.logout') }}" class="nav-link btn-signin">Logout</a></li>
    {% else %}
        <li><a href="{{ url_for('index') }}" class="nav-link">Home</a></li>
        <li><a href="{{ url_for('projects.browse_projects') }}" class="nav-link">Browse Projects</a></li>
        <li><a href="{{ url_for('main.about') }}" class="nav-link">About</a></li>
        <li><a href="{{ url_for('auth.login') }}" class="nav-link btn-signin">Login</a></li>
        <li><a href="{{ url_for('auth.register') }}" class="nav-link btn-join">Join Now</a></li>
    {% endif %}
</ul>