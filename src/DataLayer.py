import DataFunctions as df

def check_usr(scanned_rfid):
    return df.check_user_permission(scanned_rfid)

def check_lvl(scanned_rfid):
    return df.check_user_level(scanned_rfid)

def get_usr(scanned_rfid):
    return df.get_user(scanned_rfid)
