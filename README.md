# Blood Donor Management System

A Python-based Blood Donor Management System with a graphical interface and SQL integration.

## Description

This application provides a user-friendly interface for managing blood donor information. It supports adding, updating, deleting, and searching donor records stored in a PostgreSQL database.

## Features

- Intuitive graphical interface built with Tkinter.
- Full CRUD operations (Create, Read, Update, Delete) for donor records.
- Advanced search functionality by:
  - Blood group
  - Last donation date
  - Address
  - Phone number
- Secure database connection using environment variables.

## Technologies Used

- **Python 3**
- **Tkinter** for GUI
- **PostgreSQL** for database
- **psycopg2** for database connection
- **python-dotenv** for environment variable management

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-repo/Blood-Bank-Management-System.git
   cd Blood-Bank-Management-System
   ```

2. **Install required packages:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up PostgreSQL:**

   - Create a database named `bdms`.
   - Create a table named `donors`

4. **Configure environment variables:**
   - Create a `.env` file in the project root with the following content:
     ```
     DB_PASSWORD=your_database_password
     ```

## Usage

Run the application:

```bash
python main.py
```

## Database Schema

The `donors` table contains the following fields:

| Field           | Type        | Description            |
| --------------- | ----------- | ---------------------- |
| `id`            | Primary Key | Unique identifier      |
| `name`          | Text        | Donor's name           |
| `gender`        | Text        | Donor's gender         |
| `blood_group`   | Text        | Blood group (e.g., A+) |
| `number`        | Text        | Phone number           |
| `email`         | Text        | Email address          |
| `dob`           | Text        | Date of birth          |
| `ailment`       | Text        | Medical conditions     |
| `last_donation` | Text        | Last donation date     |
| `address`       | Text        | Residential address    |

## Screenshots

_Add screenshots of the application here._

## License

_Specify your license here (e.g., MIT, Apache 2.0)._
