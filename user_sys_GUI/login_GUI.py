import easygui as gui
import sys


def main_window():
    user_type = gui.buttonbox(msg="请选择你的用户类型",title="未来Chat",choices=("老用户","新用户","退出"))
    return user_type


def new_user_window():
    msg = "请输入您的帐号信息"
    title = "帐号申请"
    fieldName = ["用户名","密码","密码确认"]
    fieldValues = []
    fieldValues = gui.multenterbox(msg,title,fieldName)
    
    return fieldValues



def error_msg(error_info="error"):
    if error_info == "creat_user_info_none":
        gui.msgbox("缺少必要的信息，请重新填写！",title = "creat_user_info_none")
        return error_info
    if error_info == "passwords are different":
        gui.msgbox("两次输入的密码不一致，请重新输入！",title = "passwords are different")
        return error_info

    
# main_window()
