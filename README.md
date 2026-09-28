# Credit Card Payment System

## Tech Stack

- Django
- Django REST Framework
- JWT Authentication
- SQLite

## Features

### User Authentication
- User Registration
- User Login
- JWT Authentication
- Protected Routes

### Card Management
- Add Card
- View Cards
- Delete Card
- Card Masking

### Payment Processing
- Simulated Payments
- SUCCESS / FAILED Status

### Transaction Management
- Transaction History
- CSV Export

### Admin Panel
- Manage Users
- Manage Cards
- Manage Transactions

## Installation

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Apply Migrations

```bash
python manage.py migrate
```

### Run Server

```bash
python manage.py runserver
```

## API Endpoints

### Authentication

- /api/register/
- /api/login/

### Cards

- /api/cards/add-card/
- /api/cards/view-cards/
- /api/cards/delete-card/<id>/

### Transactions

- /api/transactions/make-payment/
- /api/transactions/history/

## Security Features

- Password Hashing
- JWT Authentication
- Protected APIs
- Card Number Masking
- No CVV Storage

## Admin Credentials

Username: Gaddam

Password: Available upon request