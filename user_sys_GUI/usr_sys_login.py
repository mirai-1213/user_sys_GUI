import usr_info_op


# ui界面
def ui(retype='success'):
    if retype == 'success':
        print("Welcome to our STUDENT_SYSTEM")
    print("_____________________________")
    print("please sellect your user type")
    print("    1.Old user  0.New user   ")
    print("_____________________________")
    user_type = input("Your type: ")
    return user_type


# 管理员ui界面
def admin_ui():
    print("***************************************")
    print(" 1.All_user  2.Del_User      ")
    print("     　0.EXIT         ")
    print("***************************************")
    do_type = input("You want to do:")
    return do_type

#用户ui
def user_ui():
    print("***************************************")
    print(" 1.Change Password           ")
    print(" 0.EXIT          ")
    print("***************************************")
    do_type = input("You want to do:")
    return do_type


# 创建新用户
def new_user(retype='success'):
    global user
    username = str()
    print("＿＿＿＿Create Page＿＿＿＿")
    if retype == 'success':
        print("please input your username:")
        username = input()
        # 检查是否存在重复的用户名，即在字典中进行key的遍历，重复返回0
        if username_repeat(username) == 0:
            print("用户名重复，请输入新的用户名：")
            new_user()
            return 1
        # 如果不需要递归，必须在之后return结束递归调用
    print("please input your password")
    pwd_1 = input()
    print("please input your password again")
    pwd_2 = input()
    if pwd_1 == pwd_2:
        # 两次密码输入一致，创建用户
        new_user_info = {"%s" % username: "%s" % pwd_1}
        user.update(new_user_info)
        # print("新用户信息录入内存后的user字典:",user)
        return 1
    else:
        # 两次密码输入不一致，重新执行此函数
        print("两次密码输入不一致，请重新输入：")
        new_user('error')
        return 0


# 检查是否存在重复的用户名，即在字典中进行key的遍历，重复返回0
def username_repeat(usr):
    global user
    if user.get(usr) is not None:
        return 0
    return 1


# 登录
def old_user():
    # 返回值是1登录成功 0登录失败
    # Login
    global NOW_USER
    print("＿＿＿＿Login Page＿＿＿＿")
    print("please input your username:")
    usr = input()   
    print("please input your password")
    pwd = input()
    check_value = check(usr, pwd)
    # 用户名，密码信息比对
    if check_value == 1:
        print("Login success")
        # 当前登录的用户名存入全局变量NOW_USER
        NOW_USER = usr
        return 1
    elif check_value == 9:
        print("Enter in the Administrator Mode!")
        operation = usr_operation()
        while operation != 1:
            operation = usr_operation()
    else:
        print("The username or password is incorrect. Please try again.")
        old_user()
    return 0


# 管理员用户信息验证
def usr_admin(retype='success'):
    # 管理员账户密码预设，usr=admin，pwd=admin
    global user
    if retype == 'success':
        pwd = input("Please enter the administrator password:\n")
    else:
        pwd = input("Please try again:\n")
    if check('admin', pwd) == 9:
        print("Enter in the Administrator Mode!")
        operation = usr_operation()
        while operation != 1:
            operation = usr_operation()
    else:
        print("Failed!")
        usr_admin("error")
    return 0


# 管理员用户操作
def usr_operation():
    do_type = admin_ui()
    # admin_ui会返回三个值，1显示全部，2删除指定，0退出
    if do_type == '0':
        return 1
    elif do_type == '1':
        # 预留管理员功能，可以查看全部用户数据
        all_user()
        return 0
    elif do_type == '2':
        # 预留管理员功能，可以删除指定用户数据
        all_user()
        user_del = input("请输入想要删除的用户的用户名：")
        if user_del == "admin":
            print("\nuser_admin is administrator,cannot delete!\n")
        else:
            for key in user.keys():
                if key == user_del:
                    user.pop(user_del)
                    usr_info_op.write_in_file(user)
                    print("剩下的用户列表：")
                    all_user()
                    return 0
            print("指定的用户不存在！")
        return 0


# 显示全部用户信息
def all_user():
    for userItem in user.items():
        print(userItem)
    print()


# 用户名密码验证
def check(usr, pwd):
    # 正确返回1，不正确返回0，管理员返回9，异常返回-1
    global user
    # 用户名不存在
    if user.get(usr) is None:
        # print("用户名不存在")
        return 0
    # 密码不正确
    elif user.get(usr) != pwd:
        # print("密码不正确")
        return 0
    else:
        if usr == "admin":
            return 9
        else:
            return 1


#修改密码
def user_ch_pwd():
    global user
    # global NOW_USER
    new_pwd_1 = input("please enter your new password:\n")
    new_pwd_2 = input("please enter your new password again:\n")
    if new_pwd_1 == new_pwd_2:
        print("change password successed!")
        user[NOW_USER] = new_pwd_1
        usr_info_op.write_in_file(user)
    return 0


# 主进程
def main():
    # 手动退出返回1，其他情况退出返回0
    global user
    user_type = ui('success')
    # 返回用户类型，新用户是1，老用户是0
    while user_type != '1' and user_type != '0':
        # 当既不是新用户又不是老用户时，执行循环，直到输入正确的数字
        # 预留管理员账户功能  user_type='admin'
        if user_type == 'admin':
            usr_admin()
            return 1
        else:
            print("error! please input \"1\"or\"0\" ")
            user_type = ui('error')
        # 传入“error”，实际上传入任意非“success”值都可以
    if user_type == '0':
        # 如果选择0，创建用户
        new_user('success')
        usr_info_op.write_in_file(user)
    # 新用户创建完成后，或者选择老用户时，进入登陆步骤
    if old_user() == 1:
        # 预留主模块接口

        # 退出登录 目前无论输入什么都退出登录
        while(1):
            user_op = user_ui()
            if user_op == '1':
                # Change Password
                user_ch_pwd()
            elif user_op == '0':
                # EXIT
                return 1
            else:
                print("error! please input \"1\"or\"0\" ")


# begin-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

NOW_USER = ""
user = usr_info_op.load_from_file()
# 从use_info文件中读取用户信息
while 1:
    main()
    # 输入“exit”退出程序，输入其他任意值从头再次执行程序
    if input('''If you want to quit the program, please input \"exit\"
    Enter any letters to return to the login page\n''') == "exit":
        break
    else:
        continue
