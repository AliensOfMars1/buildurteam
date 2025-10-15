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

BuildurTeam/
│
├── app.py ← App entry point / Factory pattern
├── config.py ← Configuration (dev, test, prod)
├── requirements.txt ← Python dependencies
├── README.md ← You are here
├── .gitignore ← Ignored files & folders
│
├── static/
│ ├── css/
│ │ ├── main.css
│ │ └── components.css
│ ├── js/
│ │ └── script.js
│ ├── img/
│ │ └── logo.png
│ └── uploads/ ← Uploaded project media
│
├── templates/
│ ├── base.html ← Global layout template
│ ├── landingpage.html ← Public landing page
│ └── errors/
│ ├── 404.html
│ └── 500.html
│
├── extensions/ ← Reusable Flask extensions (DB, login, etc.)
│ └── db.py
│
├── models/ ← Database models
│ ├── user.py
│ ├── project.py
│ ├── message.py
│ └── team.py
│
├── auth/ ← Handles user authentication
│ ├── routes.py
│ ├── forms.py
│ └── templates/auth/
│ ├── login.html
│ ├── signup.html
│ └── forgot_password.html
│
├── user/ ← Handles user dashboards and profiles
│ ├── routes.py
│ └── templates/user/
│ ├── dashboard.html
│ ├── profile.html
│ └── edit_profile.html
│
├── projects/ ← Manages project creation and browsing
│ ├── routes.py
│ └── templates/projects/
│ ├── create_project.html
│ ├── project_detail.html
│ ├── browse_projects.html
│ └── edit_project.html
│
├── teams/ ← Manages team membership and approvals
│ ├── routes.py
│ └── templates/teams/
│ ├── team_detail.html
│ └── manage_members.html
│
└── messages/ ← Team chat and communication
├── routes.py
└── templates/messages/
├── inbox.html
└── chat.html




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

