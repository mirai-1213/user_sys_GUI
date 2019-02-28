import user_sys_GUI.login_GUI as gui


# 创建新用户
def new_user():
    field_values = gui.new_user_window()
    for count in range(len(field_values)):
        if field_values[count] == "":
            gui.error_msg("creat_user_info_none")
            return 0
    if field_values[1] != field_values[2]:
        gui.error_msg("passwords are different")
        
    return 1

    
# 登录
def old_user():
    return 0


# 退出程序
def exit_pro():
    return 0


def main():
    user_type = gui.main_window()
    # user_type return is 'str'
    if user_type == "老用户":
        old_user()
    elif user_type == "新用户":
        while 1:
            if new_user() == 1:
                break
    elif user_type == "退出":
        exit_pro()
        return 0


main()
