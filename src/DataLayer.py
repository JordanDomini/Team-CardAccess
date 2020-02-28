import DataFunctions as df


def check_usr(scanned_rfid):
    return df.check_user_permission(scanned_rfid)


def check_lvl(scanned_rfid):
    return df.check_user_level(scanned_rfid)


def get_usr(scanned_rfid):
    return df.get_user(scanned_rfid)


def add_usr(scanned_rfid):
    return df.addUser(scanned_rfid)


def edit_usr(user_info, user_role):
    return df.edit_user(user_info, user_role)


def get_usr_by_id(id_no):
    return df.get_user_by_id(id_no)
