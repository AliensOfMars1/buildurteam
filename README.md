## BuildurTeam

**BuildurTeam** is a collaborative web platform that connects people with innovative ideas to those looking to join exciting projects.  
It’s a space where creators can **pitch projects**, **find teammates**, and **collaborate** 
insted of the traditional searching for funding, BUILDurTEAM focus on here human resource and community building   



## Project Overview

BuildurTeam is designed to help innovators and developers connect based on shared interests and project goals.  
Users can:
- Pitch an idea or project.
- Receive join requests from interested users.
- Approve or reject applicants.
- Collaborate and chat within project-specific teams.


## Core Concept

> Pitch. Connect. Build.
> Creators post projects → Interested people request to join → Project owners approve → A team is formed.

Once part of a project team, members can chat, coordinate tasks, and view each other’s profiles.


##  Tech Stack

 Layer - Technology

>Backend           =  Python (Flask) 
>Frontend          =  HTML, CSS, JavaScript 
>Database          =  SQL
>Templating        =  Jinja2 
>Version Control   =  Git + GitHub 
>Env Management    =  venv 



##  Project Structure
```
BuildurTeam/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── static/
│   ├── css/
│   │   ├── main.css
│   │   ├── components.css
│   │   └── index.css
│   ├── js/
│   │   └── script.js
│   ├── img/
│   └── uploads/
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── partials/
│   │   └── nav_dropdown.html
│   └── errors/
│       ├── 404.html
│       └── 500.html
│
├── extensions/
│   ├── __init__.py
│   └── db.py
│
├── models/
│   ├── __init__.py
│   ├── user.py
│   ├── project.py
│   ├── message.py
│   └── team.py
│
├── auth/
│   ├── __init__.py
│   ├── routes.py
│   ├── forms.py
│   ├── static/
│   │   └── css/auth.css
│   └── templates/
│       └── auth/
│           ├── login.html
│           ├── signup.html
│           └── forgot_password.html
│
├── user/
│   ├── __init__.py
│   ├── routes.py
│   ├── static/
│   │   └── css/user.css
│   └── templates/
│       └── user/
│           ├── dashboard.html
│           ├── profile.html
│           └── edit_profile.html
│
├── projects/
│   ├── __init__.py
│   ├── routes.py
│   ├── static/
│   │   └── css/projects.css
│   └── templates/
│       └── projects/
│           ├── create_project.html
│           ├── project_detail.html
│           ├── browse_projects.html
│           └── edit_project.html
│
└── messages/
    ├── __init__.py
    ├── routes.py
    ├── static/
    │   └── css/messages.css
    └── templates/
        └── messages/
            ├── inbox.html
            └── chat.html

```


##  Setup Instructions

 1. Clone the repository

```bash
git clone 
cd BuildurTeam

>2. create and activate virtual env

# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

>3. install dependancies 

pip install -r requirements.txt

 4. Run the app 
   python app.py 



> APP FEATURES 

> User authentication (signup, login, logout)

> Pitch a project / idea

> Join requests and approval system

> Project chat for team members

> Member profiles & dashboards

> Project showcase & browsing

> Error handling (404 / 500 pages)

