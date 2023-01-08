def write_db(login,Password):
    import json
    strdata = {login:Password}
    db_open = open("db.json", "w")
    json.dump(strdata,db_open)