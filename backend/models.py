from database import get_connection

def save_itinerary(destination, duration, interests, itinerary):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO itinerariess
    (destination, duration, interests, itinerary)
    VALUES (%s, %s, %s, %s)
    """

    cursor.execute(query, (destination, duration, interests, itinerary))
    conn.commit()
    cursor.close()
    conn.close()


def get_all_itineraries():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM itinerariess")
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data
