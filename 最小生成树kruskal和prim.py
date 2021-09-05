import win32api, win32gui, win32con
import win32clipboard as wt
import time
import random
import re


def Get_hwnd(name="QQ"):
    """
    根据窗口名查找句柄号
    :param name: 窗口名
    :return: 句柄号
    """
    hwnd_title = dict()

    def get_all_hwnd(hwnd, mouse):
        if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
            hwnd_title.update({win32gui.GetWindowText(hwnd): hwnd})

    win32gui.EnumWindows(get_all_hwnd, 0)
    print(hwnd_title)
    return hwnd_title.get(name)


def Get_hwnd_blurry(name="QQ"):
    """
    根据窗口名模糊查找包含的群名，主要用于针对在一个窗口中同时打开了多个群存在多个会话的情况
    :param name:
    :return:
    """
    hwnd_title = dict()
    global tmp
    tmp = ''

    def get_all_hwnd(hwnd, mouse):
        global tmp
        if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
            hwnd_title.update({win32gui.GetWindowText(hwnd): hwnd})
            if name in win32gui.GetWindowText(hwnd):
                tmp = win32gui.GetWindowText(hwnd)

    win32gui.EnumWindows(get_all_hwnd, 0)
    if tmp == '':
        return 0
    else:
        return hwnd_title.get(tmp)


def GetText():
    """
    获取剪切板文本
    :return:
    """
    wt.OpenClipboard()
    d = wt.GetClipboardData(win32con.CF_UNICODETEXT)
    wt.CloseClipboard()
    return d


def SetText(aString):
    """
    设置剪贴板文本
    :param aString:
    :return:
    """
    wt.OpenClipboard()
    wt.EmptyClipboard()
    wt.SetClipboardData(win32con.CF_UNICODETEXT, aString)
    wt.CloseClipboard()


def mouse_click(x, y, type=1):
    """
    鼠标移动到目标位置并点击
    :param x: x
    :param y: y
    :param type:点击次数
    :return:
    """
    if type == 2:
        win32api.SetCursorPos([x, y])
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    else:
        win32api.SetCursorPos([x, y])
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


def Open_win(phwnd):
    """
    将当前句柄窗口置顶显示
    :param phwnd:
    :return:
    """
    win32gui.ShowWindow(phwnd, win32con.SW_SHOWNORMAL)
    win32gui.SetForegroundWindow(phwnd)


def Close_win(phwnd):
    """
    关闭当前句柄窗口
    :param phwnd:
    :return:
    """
    win32gui.PostMessage(phwnd, win32con.WM_CLOSE, 0, 0)


def Get_win_size(phwnd):
    """
    获取窗口大小
    :param phwnd:
    :return: (0,0,0,0)返回的是窗口左上角坐标和窗口右下角坐标
    """
    # winRect = win32gui.GetWindowRect(phwnd)
    return win32gui.GetWindowRect(phwnd)


def Random_Sleep():
    """
    随机休息一定时间
    import random
    print( random.randint(1,10) )        # 产生 1 到 10 的一个整数型随机数
    print( random.random() )             # 产生 0 到 1 之间的随机浮点数
    print( random.uniform(1.1,5.4) )     # 产生  1.1 到 5.4 之间的随机浮点数，区间可以不是整数
    print( random.choice('tomorrow') )   # 从序列中随机选取一个元素
    print( random.randrange(1,100,2) )   # 生成从1到100的间隔为2的随机整数
    :return:
    """
    time.sleep(random.uniform(0.05, 0.1))


def Ctrl_A():
    """
    全选
    :return:
    """
    win32api.keybd_event(17, 0, 0, 0)  # Ctrl
    win32api.keybd_event(65, 0, 0, 0)  # A
    win32api.keybd_event(65, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
    win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(random.uniform(0.1, 0.2))


def Ctrl_C():
    """
    粘贴
    :return:
    """
    win32api.keybd_event(17, 0, 0, 0)  # Ctrl
    win32api.keybd_event(67, 0, 0, 0)  # A
    win32api.keybd_event(67, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
    win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(random.uniform(0.1, 0.2))


def Ctrl_Home():
    """
    向上翻页
    :return:
    """
    win32api.keybd_event(17, 0, 0, 0)  # Ctrl
    win32api.keybd_event(36, 0, 0, 0)  # Home
    win32api.keybd_event(36, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
    win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(random.uniform(0.1, 0.2))


def Ctrl_End():
    """
    向下翻页
    :return:
    """
    win32api.keybd_event(17, 0, 0, 0)  # Ctrl
    win32api.keybd_event(35, 0, 0, 0)  # End
    win32api.keybd_event(35, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
    win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(random.uniform(0.1, 0.2))


def Match_time(string):
    """
    匹配字符串中的时间，如果只有时分秒则以当前的年月日补充
    :param string: 待匹配字符串
    :return: 返回时间
    """
    pattern_ymdhms = re.compile("(\d{4}/\d{1,2}/\d{1,2} \d{1,2}:\d{1,2}:\d{1,2})")
    chat_time = re.findall(pattern_ymdhms, string)
    if chat_time == []:
        pattern_hms = re.compile("(\d{1,2}:\d{1,2}:\d{1,2})")
        chat_time = re.findall(pattern_hms, string)
        if chat_time == []:
            return "None"
        else:
            chat_time = time.strftime("%Y/%m/%d") + " " + chat_time[0]
            return chat_time
    else:
        return chat_time[0]


def Match_qq(string):
    """
    匹配字符串中括号里面的QQ号
    :param string:
    :return:
    """
    pattern_qq = re.compile("\((\d+)\)")
    chat_qq = re.findall(pattern_qq, string)
    if chat_qq == []:
        return "None"
    else:
        return chat_qq[0]


def Get_Match_data(listdata, type="\n"):
    """
    通过正则表达式对QQ聊天信息进行匹配提取用户信息，时间，聊天内容
    :param listdata:测试语句：'【管理员】隆昌 21  尤小鱼(152440688)  2020/08/10 16:42:03\n八月还有31\n七月还有100天'
    :return:
    """
    data = []
    result = listdata.split(type)
    if len(result) >= 2:
        data.append(Match_qq(result[0]))
        data.append(Match_time(result[0]))
        data.append(result[1:])
        if data[0] != "None":
            return data
        else:
            data = []
            data.append(Match_qq(result[1]))
            data.append(Match_time(result[1]))
            data.append(result[2:])
            return data
    else:
        return []


def Get_Last_list(file):
    try:
        f = open("./tmpdata/%s.txt" % file, "r", encoding="utf-8")
        tmpt = f.read()
        result = tmpt.split("\n\n\n\n")
        data = []
        for i in result:
            out = Get_Match_data(i, type="\n\n")
            data.append(out)
        return data
    except:
        return []


def Save_Processed_data(file, data):
    f = open(file, "a", encoding="utf-8")
    for i in range(len(data)):
        if data[i] != []:
            for j in data[i]:
                f.write(str(j) + "\t")
            f.write("\n")


start = time.time()
while True:
    grouptext = ["测试"]
    phwnd = Get_hwnd()  # 获取窗口句柄
    # phwnd=66334
    if phwnd != None:
        Open_win(phwnd)
        winRect = Get_win_size(phwnd)
        """依次查询获取的群名，获取群消息记录"""
        for i in grouptext:
            time.sleep(1)
            SetText(i)  # 设置剪切板文字
            mouse_click(winRect[0] + 120, winRect[1] + 125)  # 移动到QQ搜索窗口并点击
            Random_Sleep()
            win32gui.SendMessage(phwnd, 258, 22, 2080193)
            win32gui.SendMessage(phwnd, 770, 0, 0)
            time.sleep(1)  # 信息输入完毕休息等待窗口反应
            mouse_click(winRect[0] + 120, winRect[1] + 200, type=2)
            time.sleep(1)  # 鼠标点击后等待界面弹出
            num = 5  # 最多尝试10次
            try:
                while True:
                    if num > 0:
                        nowphwnd = Get_hwnd_blurry(i)
                        if nowphwnd == None:
                            num -= 1
                        else:
                            print("%s：窗口打开成功！" % i)
                            Open_win(nowphwnd)
                            nowwinRect = Get_win_size(nowphwnd)
                            mouse_click(nowwinRect[0] + 300, nowwinRect[1] + 380)
                            Ctrl_Home()
                            mouse_click(nowwinRect[0] + 270, nowwinRect[1] + 110)  # 刷新窗口
                            time.sleep(1)  # 刷新等待1秒
                            Ctrl_Home()
                            mouse_click(nowwinRect[0] + 270, nowwinRect[1] + 110)  # 刷新窗口
                            time.sleep(1)  # 刷新等待1秒
                            Ctrl_A()
                            Ctrl_C()
                            list_last = Get_Last_list(i)  # 得到已经获取了的数据
                            """保存当前的临时数据"""
                            getdata = GetText().split("\r\n\r\n")
                            list_now = []
                            # print(getdata)
                            for n in getdata:
                                list_now.append(Get_Match_data(n))
                            list_out = [y for y in list_now if y not in list_last]
                            """处理后的数据存储"""
                            Save_Processed_data("./Data/%s.txt" % i, list_out)
                            print("新增数据！", time.strftime("%Y-%m-%d-%H-%M-%S"), list_out)
                            f = open("./tmpdata/%s.txt" % i, "w", encoding="utf-8")
                            f.write(GetText())
                            f.close()
                            Close_win(nowphwnd)
                            time.sleep(1)
                            break
                        time.sleep(1)
                    else:
                        break
            except:
                print("Wrong!")
            time.sleep(2)
        time.sleep(100)
    end = time.time()
    print(end - start)
