import easygui as gui


def main_window():
    user_type = gui.buttonbox(msg="请选择您想进行的操作", title="未来Chat",  choices=["用户登录", "创建用户", "退出"])
    return user_type


def new_user_window():
    msg = "请输入您的帐号信息"
    title = "帐号申请"
    field_name = ["用户名", "密码", "密码确认"]
    # field_values = []
    field_values = gui.passwordbox(msg, title, field_name)
    return field_values


def old_user_window():
    msg = "请输入您的用户名"
    title = "用户登录"
    user = gui.multpasswordbox(msg,title,("用户名","密码"))
    print(user)
    print(type(user))
    return user


def admin_window():
    # choicebox()
    return 0


def pro_window():
    return 0


def error_msg(error_info="error"):
    if error_info == "creat_user_info_none":
        gui.msgbox("缺少必要的信息，请重新填写！", title=error_info)
    elif error_info == "passwords are different":
        gui.msgbox("两次输入的密码不一致，请重新输入！", title=error_info)
    elif error_info == "repeat of username":
        gui.msgbox("用户名重复，请重新输入！", title=error_info)
    elif error_info == "The username or password is incorrect":
        gui.msgbox("用户名或密码错误，请重新输入！", title=error_info)
    return error_info
    
# main_window()
