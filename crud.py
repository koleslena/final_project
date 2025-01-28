from database import get_connection

def add(table_name, args, values):
    conn = get_connection()
    cursor = conn.cursor()
    vls = ','.join(['?' for i in range(0, len(values))])
    cursor.execute(f"""
        INSERT INTO {table_name} ({','.join(args)})
        VALUES ({vls})
    """, values)
    conn.commit()
    conn.close()

def get_list(table_name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    lst = cursor.fetchall()
    conn.close()
    return lst

def update(table_name, id, args, values):
    conn = get_connection()
    cursor = conn.cursor()
    chs = [f'{args[i]}={values[i]}' for i in range(0, len(values))]
    query = f"UPDATE {table_name} SET {', '.join(chs)} WHERE id = {id}"
    cursor.execute(query)
    conn.commit()
    conn.close()

def delete(table_name, id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM {table_name} WHERE id = ?", (id,))
    conn.commit()
    conn.close()