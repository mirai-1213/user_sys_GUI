# import user_sys_GUI.login_GUI as gui
import login_GUI as gui
import usr_info_op as info



# 调用用户登录窗口
# 取得创建用户窗口返回值，判断
# 返回成功创建后的用户名和密码，以list形式
def new_user():
    field_values = gui.new_user_window()
    if field_values is None:
        return CANCEL
    for count in range(len(field_values)):
        if field_values[count] == "":
            gui.error_msg("creat_user_info_none")
            return 0
    if field_values[1] != field_values[2]:
        gui.error_msg("passwords are different")
        return 0
    # 检查是否存在重复的用户名，即在字典中进行key的遍历，重复返回0
    if username_repeat(field_values[0]) == 0:
        gui.error_msg("repeat of username")
        return 0
    # 成功创建时返回field_values    
    return field_values

    
# 登录
def old_user():
    enter_user_info = gui.old_user_window()
    check_value = user_check(list_to_dict(enter_user_info))
    # 用户名，密码信息比对
    if check_value == 1 or check_value == ADMIN:
        print("Login success")
        # 当前登录的用户名存入全局变量NOW_USER
        print(enter_user_info)
        print(type(enter_user_info))
        # NOW_USER = enter_user_info["user_name"]
        NOW_USER = enter_user_info[0]
    else:
        gui.error_msg("The username or password is incorrect")
    return check_value


def pro_window():
    gui.pro_window
    return 0

def admin_window():
    gui.admin_window()
    return 0

# 退出程序
def exit_pro():
    return 0


# 文件操作区域***************************************


# 文件操作区域****************结束*******************


# 数据操作区域***************************************
# 列表转化为字典
def list_to_dict(field_values):
    target_dict = {}
    if len(field_values) == 3 or len(field_values) == 2:
        # ‘==3’的情况下是创建用户，收到用户名，密码，确认密码三个值的list
        target_dict = dict(zip(["user_name","user_password"],field_values))
        # target_dict = {field_values[0]:field_values[1]}
        print(target_dict)
    return target_dict


# 检查是否存在重复的用户名，即在字典中进行key的遍历，重复返回0
def username_repeat(user_dict):
    if user.get(user_dict) is not None:
        return 0
    return 1


# 用户名密码验证
def user_check(enter_user):
    # 字典拆分
    user_name = enter_user["user_name"]
    user_password = enter_user["user_password"]
    #    print("enter_user:",enter_user)
    #    print("enter_user_type:",type(enter_user))
    # 正确返回1，不正确返回0，管理员返回ADMIN，异常返回-1
    # 用户名不存在
    if user.get(user_name) is None:
        # print("用户名不存在")
        return 0
    # 密码不正确
    elif user.get(user_name) != user_password:
        # print("密码不正确")
        return 0
    else:
        if user_name == "admin":
            return ADMIN
        else:
            return 1

# 数据操作区域****************结束*******************

# 用户注册窗逻辑
def new_user_window():
    void_new_user = new_user()
    if type(void_new_user) is list:
        # 成功取得窗口返回数据，并转化为字典
        user_dict = list_to_dict(void_new_user)
        user.update(user_dict)
        # 将用户信息写入文件
        if info.write_in_file(user) == 1:
            print("write in file successed!")
            return 1
        else:
            print("write in file failed!")
            return 0    
    elif void_new_user == CANCEL:
        # 退出帐号申请界面，返回到主界面
        # main_window()
        return CANCEL
    elif void_new_user == 0:
        # 如果提示错误信息，返回创建用户界面
        re_write=new_user_window()
        return re_write


# 用户登录窗逻辑
def old_user_window():
    login_type = old_user()
    if login_type == 0:
        old_user_window()
        return 0
    elif login_type == 1:
        return 1
    elif login_type == ADMIN:
        return ADMIN
    
        
# 主窗逻辑
def main_window():
    user_type = gui.main_window()
    # user_type return is 'str'
    if user_type == "用户登录":
        login_type = old_user_window()
        if login_type == 1:
            pro_window()
            print("pro_window")
        elif login_type == ADMIN:
            admin_window()
            print("admin_window")
    elif user_type == "创建用户":
        # 进入创建用户窗体
        create_return = new_user_window()
        main_window()
        return 0
    elif user_type == "退出":
        exit_pro()
        return 0
    return 0
    
# 取消宏值CANCEL
CANCEL = -1
ADMIN = 9
NOW_USER = ""
user = info.load_from_file()
main_window()
