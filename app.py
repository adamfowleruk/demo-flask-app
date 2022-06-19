import time
import os
import sys
import psycopg2
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/time')
def get_current_time():
    return {'time': time.time()}


@app.route('/dbtime')
def get_database_time():
    conn = get_db_connection()
    if conn is None:
        return {'dbtime': 0}
    cur = conn.cursor()
    cur.execute('select extract(epoch from now());')
    dbtime = cur.fetchone()
    cur.close()
    conn.close()
    return {'dbtime': dbtime[0]}


def get_db_connection():
    if "PGHOST" in os.environ and "PGDATABASE" in os.environ and "PGUSER" in os.environ and "PGPASSWORD" in os.environ:
        try:
            conn = psycopg2.connect(host=os.environ['PGHOST'],
                                    database=os.environ['PGDATABASE'],
                                    user=os.environ['PGUSER'],
                                    password=os.environ['PGPASSWORD'])
            return conn
        except psycopg2.OperationalError as err:
            # get details about the exception
            err_type, err_obj, traceback = sys.exc_info()

            # get the line number when exception occured
            line_num = traceback.tb_lineno
            # print the connect() error
            print("\npsycopg2 ERROR:", err, "on line number:", line_num)
            print("psycopg2 traceback:", traceback, "-- type:", err_type)

            # psycopg2 extensions.Diagnostics object attribute
            print("\nextensions.Diagnostics:", err.diag)

            # print the pgcode and pgerror exceptions
            print("pgerror:", err.pgerror)
            print("pgcode:", err.pgcode, "\n")
            return None
    else:
        print("\nmissing environment ERROR: check PGHOST, PGDATABASE, PGUSER, PGPASSWORD are set")
        return None

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.environ.get('PORT', 5000))
