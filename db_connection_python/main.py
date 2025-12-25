from insert_user import insert_user
from fetch_users import fetch_users


insert_user("Neha Singh", "1999-02-25", "Pune")

users = fetch_users()

print("\n====== USERS ======\n")
print(f"{'ID':<5} {'NAME':<20} {'DOB':<12} {'CITY':<15}")
print("-" * 55)

for user in users:
    # print(user)
    print(f"{user[0]:<5} {user[1]:<20} {str(user[2]):<12} {user[3]:<15}")
