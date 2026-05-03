# Doctor Finder

This project features a basic web app for finding and managing doctor listings in New York City.

Features
- Browse doctors on the home page
- Search by name, specialty, or condition (with highlighted matches)
- View full doctor profiles including insurance, education, location, and contact info
- Add new doctors to the directory
- Edit existing doctor information

Tech Stack
- On the backend: Python, Flask
- On the frontend: HTML, CSS, JavaScript
- For templating: Jinja2

## How to Run

1. Clone the repo
2. Install Flask:

`pip install flask` 

3. Run the server:

`python server.py` 

4. Open your browser and go to http://localhost:5000
```
doctor-finder/
    server.py        # Flask server and all routes
    templates/       # HTML pages
    static/          # CSS and JavaScript files
```


## Additional Notes
- Doctor data is currently stored in memory, so additions and edits will reset when the server restarts.
- A database integration (SQLite or PostgreSQL) would be the next step for persistent storage.
