import sqlite3


def create_table():
    conn = sqlite3.connect('phonebook.db')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS Entries (
                    Name TEXT NOT NULL,
                    Phone TEXT NOT NULL
                   )''')
    conn.commit()
    conn.close()


def add_entry(name, phone):
    conn = sqlite3.connect('phonebook.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO Entries (Name, Phone) VALUES (?, ?)', (name, phone))
    conn.commit()
    conn.close()


def look_up(name):
    conn = sqlite3.connect('phonebook.db')
    cur = conn.cursor()
    cur.execute('SELECT Phone FROM Entries WHERE Name=?', (name,))
    result = cur.fetchone()
    conn.close()
    return result[0] if result else None


def update_entry(name, new_phone):
    conn = sqlite3.connect('phonebook.db')
    cur = conn.cursor()
    cur.execute('UPDATE Entries SET Phone=? WHERE Name=?', (new_phone, name))
    conn.commit()
    conn.close()


def delete_entry(name):
    conn = sqlite3.connect('phonebook.db')
    cur = conn.cursor()
    cur.execute('DELETE FROM Entries WHERE Name=?', (name,))
    conn.commit()
    conn.close()


def display_entries():
    conn = sqlite3.connect('phonebook.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM Entries')
    results = cur.fetchall()
    conn.close()
    for row in results:
        print(f'Name: {row[0]}, Phone: {row[1]}')


def main():
    create_table()

    while True:
        print("\nPhone Book Application")
        print("1. Add Entry")
        print("2. Look Up Entry")
        print("3. Update Entry")
        print("4. Delete Entry")
        print("5. Display All Entries")
        print("6. Quit")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            add_entry(name, phone)
        elif choice == '2':
            name = input("Enter name: ")
            phone = look_up(name)
            print(f'Phone: {phone}' if phone else "No entry found.")
        elif choice == '3':
            name = input("Enter name: ")
            new_phone = input("Enter new phone number: ")
            update_entry(name, new_phone)
        elif choice == '4':
            name = input("Enter name: ")
            delete_entry(name)
        elif choice == '5':
            display_entries()
        elif choice == '6':
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == '__main__':
    main()
