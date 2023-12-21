import psycopg2

# retrieving and storing data in the db
def save_user_data(username, password, email):
    try:
        # Connect to the PostgreSQL database
        connection = psycopg2.connect(
            user="postgres",
            password="postgres",
            host="localhost",
            port="5433",
            database="Antisemitism",
        )

        cursor = connection.cursor()

        # Insert user data into the database
        cursor.execute(
            "INSERT INTO users (username, password, email) VALUES (%s, %s, %s)",
            (username, password, email),
        )

        # Commit changes and close the connection
        connection.commit()

    except psycopg2.Error as e:
        print("Error: Unable to execute SQL statement.")
        print(e)

    finally:
        # Close the connection in the 'finally' block to ensure it happens regardless of success or failure
        if connection:
            connection.close()

# example Usage
save_user_data("testuser", "testpassword", "test@example.com")


