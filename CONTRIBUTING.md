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


sign up template 

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sign Up - CodeCamp</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
</head>
<body>
    <div class="auth-container">
        <div class="auth-form">
            <div style="text-align: center; margin-bottom: 2rem;">
                <i class="fas fa-graduation-cap" style="font-size: 3rem; color: #667eea;"></i>
                <h1>Join CodeCamp</h1>
                <p style="color: #666; margin-top: 0.5rem;">Create your account and start learning today</p>
            </div>
            
            {% with messages = get_flashed_messages(with_categories=true) %}
                {% if messages %}
                    <div class="flash-messages">
                        {% for category, message in messages %}
                            <div class="flash-message {{ category }}">{{ message }}</div>
                        {% endfor %}
                    </div>
                {% endif %}
            {% endwith %}
            
            <form method="POST">
                <div class="form-group">
                    <label for="username">
                        <i class="fas fa-user"></i> Username
                    </label>
                    <input type="text" id="username" name="username" required 
                           placeholder="Choose a unique username">
                </div>
                
                <div class="form-group">
                    <label for="email">
                        <i class="fas fa-envelope"></i> Email Address
                    </label>
                    <input type="email" id="email" name="email" required 
                           placeholder="your.email@example.com">
                </div>
                
                <div class="form-group">
                    <label for="password">
                        <i class="fas fa-lock"></i> Password
                    </label>
                    <input type="password" id="password" name="password" required 
                           placeholder="Choose a strong password">
                </div>
                
                <div class="form-group">
                    <label for="confirm_password">
                        <i class="fas fa-lock"></i> Confirm Password
                    </label>
                    <input type="password" id="confirm_password" name="confirm_password" required 
                           placeholder="Confirm your password">
                </div>
                
                <button type="submit" class="auth-btn">
                    <i class="fas fa-user-plus"></i> Create Account
                </button>
            </form>
            
            <div class="auth-links">
                <p>Already have an account? <a href="{{ url_for('signin') }}">Sign in here</a></p>
                <p><a href="{{ url_for('home') }}">← Back to Home</a></p>
            </div>
        </div>
    </div>
    
    <script>
        // Auto-hide flash messages
        setTimeout(() => {
            const flashMessages = document.querySelector('.flash-messages');
            if (flashMessages) {
                flashMessages.style.opacity = '0';
                setTimeout(() => flashMessages.remove(), 300);
            }
        }, 3000);
        
        // Password confirmation validation
        const password = document.getElementById('password');
        const confirmPassword = document.getElementById('confirm_password');
        
        confirmPassword.addEventListener('input', function() {
            if (password.value !== confirmPassword.value) {
                confirmPassword.setCustomValidity('Passwords do not match');
            } else {
                confirmPassword.setCustomValidity('');
            }
        });
    </script>
</body>
</html>


