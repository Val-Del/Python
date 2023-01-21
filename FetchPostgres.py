import psycopg2
import json

hostname = 'localhost'
database = 'pokemons'
username = 'postgres'
pw = 'postroot'
port_id = 5432 
conn = None
cur = None

def get_pokemon():
    try :
        conn = psycopg2.connect(
            host = hostname,
            dbname= database,
            user = username,
            password = pw,
            port = port_id)

        cur = conn.cursor()
        cur.execute('SELECT * FROM public.poke ORDER BY idpokemon ASC')
        getPok = cur.fetchall()
        return json.dumps(getPok)
    except Exception as error:
        return json.dumps({"error": str(error)})
    finally:
        if cur is not None: 
            cur.close()
        if conn is not None:
            conn.close()