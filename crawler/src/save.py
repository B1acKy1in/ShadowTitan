import psycopg2
from parse_his import FundHis

class DB_Utile():
    def __init__(self):
        self.conn = psycopg2.connect(
            host="172.18.0.3",
            database="postgres",
            user="postgres",
            password="postgres")

    def save_fund_info(self, fund:list):
        cur = self.conn.cursor()

        sql = "DROP TABLE IF EXISTS fund_info"
        cur.execute(sql)

        sql = "CREATE TABLE fund_info (\
            code varchar(8),\
            full_name varchar(255),\
            sim_name varchar(255),\
            sgzt varchar(255),\
            shzt varchar(255))"
        cur.execute(sql)

        sql = "INSERT INTO fund_info (code, full_name, sim_name, sgzt, shzt) \
            VALUES ({code}, {full_name}, {sim_name}, {sgzt}, {shzt})"
        for fd in fund:
            s = sql.format(
                code = "\'" + fd.get('code').strip("\"") + "\'",
                full_name = "\'" + fd.get('full_name').strip("\"") + "\'",
                sim_name =  "\'" + fd.get('sim_name').strip("\"") +  "\'",
                sgzt =  "\'" + fd.get('sgzt').strip("\"") +  "\'",
                shzt =  "\'" + fd.get('shzt').strip("\"") +  "\'")
            try:
                cur.execute(s)
            except:
                print(s)
        self.conn.commit()
        cur.close()

    def save_fund_daily(self,fund:list):
        cursor = self.conn.cursor()

        count = int(0)

        for fd in fund:
            count += 1

            code = fd.get('code').strip("\"")

            sql = "DROP TABLE IF EXISTS fund_price_{code}"
            s = sql.format(code = code)
            cursor.execute(s)

            sql = "CREATE TABLE fund_price_{code} (\
                dwjz float,\
                ljjz float,\
                dwzz float,\
                ljzz float)"
            s = sql.format(code = code)
            cursor.execute(s)

            sql = "INSERT INTO fund_price_{code} (dwjz, ljjz, dwzz, ljzz) \
            VALUES ({dwjz}, {ljjz}, {dwzz}, {ljzz})"
            s = sql.format(
                code = code,
                dwjz = fd.get('dwjz'),
                ljjz = fd.get('ljjz'),
                dwzz = fd.get('dwzz'),
                ljzz = fd.get('ljzz'))
            cursor.execute(s)

            if count == 1000:
                self.conn.commit() # solve the out of the memory
                count = 0

        self.conn.commit() # solve the out of the memory
        cursor.close()

    def save_fund_his(self, fund:FundHis):
        print('save')
        code = fund.code
        cursor = self.conn.cursor()

        sql = """
            DROP TABLE IF EXISTS fund_dwjz_{code}
        """
        cursor.execute(sql.format(code = code))
        sql = """
            CREATE TABLE fund_dwjz_{code}(\
                date varchar(13),\
                dwjz float,\
                equityReturn float,\
                unitMoney varchar
                )
        """
        cursor.execute(sql.format(code = code))

        sql = """
            DROP TABLE IF EXISTS fund_ljjz_{code}
        """
        cursor.execute(sql.format(code = code))
        sql = """
            CREATE TABLE fund_ljjz_{code}(\
                date varchar(13),\
                dwjz float,\
                equityReturn float,\
                unitMoney varchar
                )
        """
        cursor.execute(sql.format(code = code))

        self.conn.commit()
        cursor.close()


def get_fund_list():
    conn = psycopg2.connect(
            host="172.18.0.3",
            database="postgres",
            user="postgres",
            password="postgres")

    codes = []

    sql = 'SELECT code FROM fund_info'
    cur = conn.cursor()
    cur.execute(sql)

    row = cur.fetchone()
    while row is not None:
        codes.append(row[0])
        row = cur.fetchone()

    cur.close()

    return codes

def get_fund_daily(ff:dict):
    fund = {}

    fund['code'] = ff.get("code").strip( "\'")
    fund["dwjz"] = ff.get("dwjz")
    fund["ljjz"] = ff.get("ljjz")
    fund["dwzz"] = ff.get("dwzz")
    fund["ljzz"] = ff.get("ljzz")

    return fund

def get_fund_info(ff:dict):
    fund = {}

    fund['code'] = ff.get("code").strip( "\'")
    fund["full_name"] = ff.get("full_name").strip( "\'")
    fund["sim_name"] = ff.get("sim_name").strip( "\'")
    fund["sgzt"] = ff.get("sgzt").strip( "\'")
    fund["shzt"] = ff.get("shzt").strip( "\'")

    return fund

sql = DB_Utile()

def save_fund_info(funds:list):
    fis = list(map(get_fund_info,funds))
    sql.save_fund_info(fis)
    print('save info done')

def save_fund_daily(funds:list):
    fps = list(map(get_fund_daily, funds))
    sql.save_fund_daily(fps)
    print('save daily done')

def save_fund_his(fund:FundHis):
    sql.save_fund_his(fund)
    print('save his done')
