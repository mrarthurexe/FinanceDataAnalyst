__package__ = "Finance.SQL"
import psycopg2
from Scrappers.DollarGoogleScraperBS import getValue, getDate

try:
        conn = None
        cur = None
        conn = psycopg2.connect(
            host='localhost',
            port=5432,
            user='postgres',
            password='adminsql',
            database='Finance'
        )
        cur = conn.cursor()
        print('Connected to database.')

except Exception as e:
    print('Error connecting to database:' + e)

def insertDollar():
    dollar = getValue()
    date = getDate()
    query = f"INSERT INTO public.\"dollar\" (\"dollar_value\", \"dollar_date\") VALUES ('{dollar}', '{date}')"
    try:
        cur.execute(query)
        conn.commit()
        print('Table updated with new dollar value.')

    except Exception as e:
        print('Error inserting to database:' + e)

def getDollarValues():
    query = f"SELECT dollar_value FROM public.\"dollar\""
    values_list = []
    try:
        cur.execute(query)
        conn.commit()

        for row in cur.fetchall():
            values_list.append(row[0])
        return values_list    

    except Exception as e:
        print('Error getting dollar value:' + e)
