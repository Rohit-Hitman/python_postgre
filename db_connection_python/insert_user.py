from db_connection import get_db_connection


def insert_user(name, dob, city):
    """
    Insert user into users table
    """
    connection = get_db_connection()
    if not connection:
        return

    try:
        cursor = connection.cursor()
        query = """
        INSERT INTO users (name, dob, city)
        VALUES (%s, %s, %s);
        """
        cursor.execute(query, (name, dob, city))
        connection.commit()
        print("✅ User inserted successfully")

    except Exception as error:
        print("❌ Error inserting user:", error)
        connection.rollback()

    finally:
        cursor.close()
        connection.close()


if __name__ == "__main__":
    insert_user("Suresh Kumar", "1995-09-10", "Chennai")
