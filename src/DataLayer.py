import DataFunctions as df


def check_usr(scanned_rfid):
    return df.check_user_permission(scanned_rfid)


def check_lvl(scanned_rfid):
    return df.check_user_level(scanned_rfid)


def get_usr(scanned_rfid):
    return df.get_user(scanned_rfid)


def add_usr(scanned_rfid):
    return df.add_user(scanned_rfid)


def edit_usr(user_info, user_role):
    return df.edit_user(user_info, user_role)


def get_usr_by_id(id_no):
    return df.get_user_by_id(id_no)


def get_mach(mach_id):
    mach_id = mach_id.trim()
    return df.get_machine(mach_id)


def add_mach(mach):
    return df.add_machine(mach)


def get_all_mach():
    return df.get_all_machines()


def use_mach(mach_id, id_no=None):
    return df.using_machine(mach_id, id_no)


def mach_used(id_no):
    return df.machine_in_use(id_no)
