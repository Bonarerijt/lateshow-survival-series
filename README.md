# Lateshow Survival Series – Phase 4 Week 2 Code Challenge

#### Date: 11/1/2026

#### By *Judy Ogachi*

## Project Overview

The **Late Show API** is a Flask-based RESTful backend application that manages episodes, guests, and their appearances on a late-night talk show.  
It demonstrates a many-to-many relationship using a join table (`Appearance`) and supports full CRUD-style API interactions.

This project was built as part of the **Phase 4 Code Challenge** and follows best practices for Flask, SQLAlchemy, and API design.

---

## Data Models & Relationships

The application is built around three core models:

### Episode
- Has many Guests through Appearances

### Guest
- Has many Episodes through Appearances

### Appearance
- Belongs to one Episode
- Belongs to one Guest
- Includes a `rating` (1–5)

### Relationship Summary
- **Episode ↔ Guest** → many-to-many
- **Appearance** acts as the join table
- Cascade deletes are enabled to maintain data integrity

---

## Technologies Used

- Python 3
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- SQLite
- SQLAlchemy Serializer
- Postman (for API testing)

---

## Project Structure

lateshow-survival-series/
│
├── app.py
├── models.py
├── seed.py
├── seed.csv
├── README.md
│
├── instance/
│ └── lateshow.db
│
├── migrations/
│ └── versions/
│
└── .gitignore


---

## Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone git@github.com:Bonarerijt/lateshow-survival-series.git
cd lateshow-survival-series
```

### 2️⃣ Install Dependencies
```
flask db init
flask db migrate
flask db upgrade
```
### 4️⃣ Seed the Database
```
python seed.py
```
### 5️⃣ Run the Server
```
python app.py
```
The server will run on:
```
http://localhost:5555
```

## API Endpoints
GET /episodes

Returns a list of all episodes.

GET /episodes/:id

Returns a single episode with its appearances and guest details.

GET /episodes/:id

Returns a single episode with its appearances and guest details.

GET /episodes/:id

Returns a single episode with its appearances and guest details.

## Validations

Appearance.rating must be between 1 and 5 (inclusive).

Invalid data returns a 422 Unprocessable Entity response.

## Testing

All endpoints were tested using Postman, following the provided Postman collection.

## Author

Judy Ogachi

## License

MIT License

Copyright (c) 2026 Bonarerijt

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

