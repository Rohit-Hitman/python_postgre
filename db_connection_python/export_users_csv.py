import csv
import os
from fetch_users import fetch_users

def export_users_to_csv(filename="users.csv"):
    users = fetch_users()

    if not users:
        print("❌ No data found to export")
        return

    data_dir = "data"

    # ✅ Check if directory exists, create if not
    if not os.path.exists(data_dir):
        print(f"🔹 Directory '{data_dir}' does not exist. Creating now...")
        os.makedirs(data_dir)
    else:
        print(f"🔹 Directory '{data_dir}' already exists. Using it.")

    file_path = os.path.join(data_dir, filename)

    headers = ["user_id", "name", "dob", "city"]

    try:
        with open(file_path, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            writer.writerows(users)

        print(f"✅ Data exported successfully to {file_path}")

    except Exception as error:
        print("❌ Error while writing CSV:", error)


if __name__ == "__main__":
    export_users_to_csv()
