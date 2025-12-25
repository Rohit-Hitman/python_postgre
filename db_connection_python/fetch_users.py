from db_connection import get_db_connection


def fetch_users():
    """
    Fetch all records from users table
    """
    connection = get_db_connection()
    if not connection:
        return []

    try:
        cursor = connection.cursor()
        query = """
        SELECT user_id, name, dob, city
        FROM users
        ORDER BY user_id;
        """
        cursor.execute(query)
        users = cursor.fetchall()
        return users

    except Exception as error:
        print("❌ Error fetching users:", error)
        return []

    finally:
        cursor.close()
        connection.close()


if __name__ == "__main__":
    users = fetch_users()
    print("\n====== USERS DATA ======\n")
    for user in users:
        print(f"User ID : {user[0]}")
        print(f"Name    : {user[1]}")
        print(f"DOB     : {user[2]}")
        print(f"City    : {user[3]}")
        print("-" * 30)
