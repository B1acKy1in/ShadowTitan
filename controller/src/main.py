import requests
import psycopg2

# 定时调度功能

gate = 3

def main():
    conn = psycopg2.connect(
            host="172.18.0.3",
            database="postgres",
            user="postgres",
            password="postgres")
    cur = conn.cursor()

    codes = []

    sql = 'SELECT code FROM fund_info'
    cur = conn.cursor()
    cur.execute(sql)

    row = cur.fetchone()
    while row is not None:
        codes.append(row[0])
        row = cur.fetchone()

    cur.close()
    conn.close()

    count = 0
    codeCache = []
    for code in codes:
        if count != 0 and count % gate == 0:
            for c in codeCache:
                requests.get(url = "http://172.18.0.4:9999/api/update_fund_his/{code}".format(code = c))
            print(count)
            codeCache.clear()
        else:
            codeCache.append(code)
        count += 1

if __name__ == "__main__":
    main()
