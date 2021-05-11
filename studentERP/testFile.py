"""
    实现一个学生信息管理系统
    主要功能是：增加、删除、编辑、查询、便利和退出输入
"""
info = []
'''展示系统主界面的功能菜单选项'''


def showMenu():
    print("-*-" * 10)
    print("欢迎登录学生信息管理系统")
    print("1. 添加学生信息")
    print("2. 删除学生信息")
    print("3. 修改学生信息")
    print("4. 查询学生信息")
    print("5. 列表显示学生信息")
    print("6. 退出学生信息管理系统")
    print("-*-" * 10)


def inputInfo():
    temp_id = input("请输入学生的ID信息：")
    temp_name = input("请输入学生的姓名：")
    temp_tel = input("请输入学生的手机号码：")

    global info
    for i in info:
        if temp_name == i['name']:
            print('您输入的学生信息已存在！')
            return
    temp_info = {'id': temp_id, 'name': temp_name, 'tel': temp_tel}
    info.append(temp_info)
    print(info)


def delInfo():
    del_name = input("请输入要删除的学生名称： ")
    for i in info:
        if del_name == i['name']:
            info.remove(i)
            print(info)
            return
    else:
        print("你输入的学生不存在！")

    print(info)


def modifyInfo():
    modify_name = input("请输入要修改的学生名称： ")
    global info  # × 此处漏声明了全局变量，修改会出现问题
    for i in info:
        if modify_name == i['name']:
            i['id'] = input("请输入学生的ID信息：")
            i['name'] = input("请输入学生的姓名：")
            i['tel'] = input("请输入学生的手机号码：")
    else:
        print("你输入的学生不存在！")

    print(info)


def queryInfo():
    query_name = input("请输入要查询的学生名称： ")
    global info  # × 查询可以不声明全局变量，但是也最好声明后再使用
    for i in info:
        if query_name == i['name']:
            print(f'您查询的学生ID是：{i["id"]}，姓名是：{i["name"]}, 电话号码是：{i["tel"]}')
            print(info)
            return
    else:
        print("你输入的学生不存在！")

    print(info)


def listInfo():
    print('ID\t姓名\t电话号码')
    global info  # × 查询可以不声明全局变量，但是也最好声明后再使用
    for i in info:
        print(f'{i["id"]}\t{i["name"]}\t{i["tel"]}')


'''调用显示来达到主入口功能'''

while True:
    showMenu()
    selection = int(input("请选择你要使用的功能: "))

    if selection == 1:
        inputInfo()
    elif selection == 2:
        delInfo()
    elif selection == 3:
        modifyInfo()
    elif selection == 4:
        queryInfo()
    elif selection == 5:
        listInfo()
    elif selection == 6:
        exF = input("确定退出学生信息管理系统吗？Y/N ")
        if exF == 'Y' or exF == 'y':
            break
    else:
        print("请输入合法的功能序号！")
