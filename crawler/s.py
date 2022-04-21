import sqlite3

def get_fund_info(ff:dict):
    fund = {}

    fund['code'] = ff.get("code").strip("\"")
    fund["full_name"] = ff.get("full_name").strip("\"")
    fund["sim_name"] = ff.get("sim_name").strip("\"")
    fund["sgzt"] = ff.get("sgzt").strip("\"")
    fund["shzt"] = ff.get("shzt").strip("\"")

    return fund

def save_fund_info(fund:list):
    conn = sqlite3.connect("db/fund.sqlite")
    conn.text_factory=str
    # https://docs.python.org/2/library/sqlite3.html#sqlite3.Connection.text_factory
    cursor = conn.cursor()

    sql = "DROP TABLE IF EXISTS fund_info"
    cursor.execute(sql)

    sql = "CREATE TABLE fund_info (\
        code varchar(8),\
        full_name varchar(255),\
        sim_name varchar(255),\
        sgzt varchar(255),\
        shzt varchar(255))"
    cursor.execute(sql)

    sql = "INSERT INTO fund_info (code, full_name, sim_name, sgzt, shzt) \
        VALUES ({code}, {full_name}, {sim_name}, {sgzt}, {shzt})"
    for fd in fund:
        s = sql.format(
            code = "\"" + fd.get('code') + "\"",
            full_name = "\"" + fd.get('full_name') + "\"",
            sim_name = "\"" + fd.get('sim_name') + "\"",
            sgzt = "\"" + fd.get('sgzt') + "\"",
            shzt = "\"" + fd.get('shzt') + "\"")
        cursor.execute(s)

    conn.commit()
    conn.close()

def get_fund_daily(ff:dict):
    fund = {}

    fund['code'] = ff.get("code").strip("\"")
    fund["dwjz"] = ff.get("dwjz")
    fund["ljjz"] = ff.get("ljjz")
    fund["dwzz"] = ff.get("dwzz")
    fund["ljzz"] = ff.get("ljzz")

    return fund

def save_fund_daily(fund:list):
    conn = sqlite3.connect("db/fund.sqlite")
    conn.text_factory=str
    # https://docs.python.org/2/library/sqlite3.html#sqlite3.Connection.text_factory
    cursor = conn.cursor()

    for fd in fund:
        code = str(fd.get('code'))

        sql = "DROP TABLE IF EXISTS fund_daily_{code}"
        s = sql.format(code = code)
        cursor.execute(s)

        sql = "CREATE TABLE fund_daily_{code} (\
            dwjz float,\
            ljjz float,\
            dwzz float,\
            ljzz float)"
        s = sql.format(code = code)
        cursor.execute(s)

        sql = "INSERT INTO fund_daily_{code} (dwjz, ljjz, dwzz, ljzz) \
        VALUES ({dwjz}, {ljjz}, {dwzz}, {ljzz})"
        s = sql.format(
            code = code,
            dwjz = fd.get('dwjz'),
            ljjz = fd.get('ljjz'),
            dwzz = fd.get('dwzz'),
            ljzz = fd.get('ljzz'))
        cursor.execute(s)

    conn.commit()
    conn.close()


def save_fund(funds:list):
    fis = list(map(get_fund_info,funds))
    save_fund_info(fis)
    print('save info done')


    fps = list(map(get_fund_daily, funds))
    save_fund_daily(fps)
    print('save daily done')

