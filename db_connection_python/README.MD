
We are working with a PostgreSQL database. After establishing a connection, we perform various database operations, including inserting records, fetching data, and deleting entries. Additionally, the retrieved data can be exported to a CSV file and stored in a dedicated data/ directory for organized storage and further processing.

This design ensures modular, maintainable, and scalable code, allowing each functionality—database connection, CRUD operations, and data export—to be tested and executed independently.


project/
│
├── db_connection.py # Database connection module
├── insert_user.py # Insert user into 'users' table
├── fetch_users.py # Fetch users from 'users' table
├── export_users_csv.py # Export users to CSV file
├── main.py # Optional runner: insert → fetch → export
└── data/ # Folder where CSV files are stored


1.Test Database Connection
    python db_connection.py
2.Insert a User
    python insert_user.py
3.Fetch Users
    python fetch_users.py
4.Optional - Run All Operations Together
    python main.py
5.Exports users to CSV in data/ folder
    python export_users_csv.py
