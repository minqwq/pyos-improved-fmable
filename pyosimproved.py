# DONT CHANGE ANY IMPORTED MODULES NAME, IM SERIOUS
#
# PY OS Improved -- Open-source FAKE Operating System(OS) written using Python 3
# Make sure you have Python 3.8.10 or higher, lower version is not tested
# Project creator:minqwq / LR Studio 2024
# 
# For our developer:
# After you write code finished, please add comment(s) in your code nearby, you maybe know why.

# How to add a quick jump for vim?:
# add comment with some special word(like uw1 uw2 ..)
# Press esc and type /uw1 to quick jump.

# (Chinese)
# 为什么我不想像那样重构:我懒。
# 所以我想出了一个办法，它基于编辑器的搜索功能
# 只需在某个地方加上注释，然后输入一些字(不要和已有的注释同名即可)
# 之后你只需使用搜索功能搜索这个注释你就可以快速定位了
# --minqwq | 2024-10-05
#
# 在需要显示反斜杠到屏幕的情况下，请输入两个反斜杠，这是一个兼容性问题
# --minqwq | 2024-10-07
from coreutil.module.actions import *
from coreutil.module.style import *
from python_goto import goto # Goto a line
import json # Read json file(config file need this)
conf = open("./config/conf.json", "r", encoding="utf-8")
jsonRead = json.load(conf)
import time as tm # Time
import getpass # Password?
import calendar # Calendar
import os # Communicate to your system
import sys # idk
import datetime
import colorama
import time # Time
# import socket
# import struct
# import select
import random # Random tools
import uuid # Generate uuid
from os import path # Path control
# import rich.spinner # idk
# sys.path.append("./")
import platform
# import rich
import requests # Get file from server
# import pretty_errors # Crash screen replace
import base64 # Encode and decode
# import tqdm # Progress bar
import traceback
import logging # Log.
import profile # Maybe useless?
import re
import autoexec
# import coreutil.module.history as history
print("\033[?25l")
print(colorama.Fore.LIGHTGREEN_EX + "All modules-1 loaded!" + "\033[0m")
# Preload classes
#
# New color library imported, but legacy will never remove
# How to use these color:
# green for example
# use this trick:
# (color.green + "text here" + color.reset)
# if you want use other color, change "green" to any below name on class color
# color.<color>
class color: # Text colors
    red = "\033[31m"
    green = "\033[32m"
    blue = "\033[34m"
    yellow = "\033[33m"
    purple = "\033[35m"
    cyan = "\033[36m"
    grey = "\033[37m"
    reset = "\033[0m"
print("Added class 'color'")
class text: # TIcons
    error = color.red + "[!] " + color.reset
    success = color.green + "[O] " + color.reset
    loading = color.yellow + "[...] " + color.reset
    doubt = color.grey + "[?] " + color.reset
    no = color.red + "[X]" + color.reset
print("Added class 'text'")
class textmoji: # Textmojis
    ciallo = "(∠・ω< )⌒☆"
    omg0 = "₍•Д•)"
    hahaha = "ꉂ(ˊᗜˋ*)"
    owo_neko = " ฅ( ̳• ◡ • ̳)ฅ"
    owo = "(´･ω･`)"
    uhmm = "(*/ω＼*)"
    nya0 = "(ฅ>ω<*ฅ)"
    nya1 = "ヽ(=ˆ･ω･ˆ=)丿"
    nah0 = "╮(‵▽′)╭"
print("Added class 'textmoji'")
class style_cur:
    hide = "\033[?25l"
    show = "\033[?25h"
class override:
    errorexpection = "teto:ErrorExpection"
    tongue = "teto:a-------"
def echo(string):
    print(string)
# pretty_errors.configure(
#    postfix               = '!!! FALLBACK CRASH SCREEN !!!\nPY OS Improved has been crashed.\nRestart command:python pyosimproved.py\nReport this error!:https://github.com/minqwq/pyos-improved/issues',
#    separator_character   = '#',
#    line_color            = colorama.Fore.LIGHTBLUE_EX + 'Here > ' + color.reset,
# print("config updated for pretty-errors")
try:
    os.remove("output.log")
except FileNotFoundError:
    pass
cmdhist_lines = 0
cmdhist_time = "nul"
LOG_FORMAT = '[%(levelname)s] %(asctime)s | %(message)s'
logging.basicConfig(filename='.output.log', datefmt='%b %a %d %H:%M:%S %Y', level=logging.INFO, format=LOG_FORMAT)
logger = logging.getLogger(__name__)
logger.info("Logger started successfully.")
pyosimprovedtips = ["Official forum:https://minqwq.proboards.com/board/10/py-os-improved", "awa", "Also try original PY OS! link available after login.", "No stay back gordon!", "sjsjsjnwnwjsosjq????"]
print("Tips loaded success")
os.system("alias cls=clear")

# CONFIG START

system_version = jsonRead["system_version"] # 版本号
system_codename = jsonRead["system_codename"]
system_build = jsonRead["system_build"] # 每做一个修改或增减内容，就加一个 Build
system_is_beta = True # 是否为 Beta 版
isWindows = jsonRead["isWindows"] # 是否为 Windows
cmd_theme = jsonRead["cmd_theme"] # 终端 Shell 主题
isDev = False # 是否为 Dev 模式
enable_instant_show_time = jsonRead["enable_instant_show_time"]
isUnregistered = jsonRead["isUnregistered"]

# CONFIG END
# coreutil/plaintext loads START
co_manualHelp = "coreutil/plaintext/manualhelp.txt"
co_welcome = "coreutil/plaintext/welcome.txt"
# coreutil/plaintext loads END
def cmdhistory_write():
    tmp_f = open("./cache/history.txt", "a", encoding="utf-8")
    # cmdhist_lines += 1
    cmdhist_timed = datetime.datetime.now().strftime("%b %a %d %H:%M:%S %Y")
    tmp_f.write(str(cmdhist_time) + " " + user + ":" + lsh_hostname + " | " + cmd + "\n")

# BIOS Animation
# with open("./config/conf.json", "w", encoding="utf-8") as temp_writeConfig:
if jsonRead["isWindows"] == "":
    # print("Unknown OS type, please set one.\nfalse:Linux\ntrue:Windows")
    # conf_isWindows_write = input(">")
    # if conf_isWindows_write == "false":
        # pass
        # 这不会写，帮我写一下，就是把配置文件里的"isWindows"值改成"false"("isWindows": "false")
    # elif conf_isWindows_write == "true":
        # pass
        # 这里和上面一样，不过false改成true
    print("Please configure the 'isWindows' to false or true on config/conf.json\nIt's looks like this:\"isWindows\": \"\", Change it to:\n\"isWindows\": \"false\" If you are linux\n\"isWindows\": \"true\" If you are windows")
    print("Exiting...")
    sys.exit()

def clearScreen():
    if isWindows == "true":
        os.system("cls")
    elif isWindows == "false":
        os.system("clear")

def beep():
    print("\a", end="\r")

if sys.platform.startswith("linux") or sys.platform.startswith("posix"):
    print("If you dont have 'python' command, please set alias 'python=python3'")
temp_clock1 = time.time()
print("Press d to fastboot.\nElse, press enter" + style_cur.show)

if temp_clock1 < 2:
    goto(line=181)
debugMode = input("\n")
if debugMode == "d":
    now = datetime.datetime.now()
    startingtime_t = "???"
    end_startingtime = "???"
    startingtime = "???"
    print("You are now in debug mode.")
    print("If crash, dont report ANY error.")
    goto(line=271)
print(style_cur.hide)
import psutil
print("module import: psutil")
print(colorama.Back.LIGHTRED_EX + colorama.Fore.LIGHTYELLOW_EX + "E:NO SINGAL" + color.reset)
time.sleep(2)
clearScreen()
print("_")
time.sleep(0.5)
clearScreen()
print(" ")
time.sleep(0.5)
clearScreen()
print("_")
time.sleep(0.5)
clearScreen()
slowprint(colorama.Fore.LIGHTRED_EX + "minsoft 2011--2025 No lefts unserved")
slowprint("EveryBooter Redistributeable")
slowprint("Testing memory...")
time.sleep(0.15)
memtest = 0
for memtest in range(129):
    print(str(memtest) + "MB", end="\r")
    time.sleep(0.02)
    memtest = memtest + 1
beep()
print("128MB OK")
time.sleep(0.5)
profile.run("re.compile")
time.sleep(1.5)
clearScreen()
print(color.reset)
time.sleep(0.1)
# Boot manager
bootManagerLoopRun = True
logger.info("Start logging.")
logger.info("Starting PY OS Improved Boot manager.")
print(colorama.Fore.LIGHTCYAN_EX + "PY OS Improved Boot manager" + color.reset + style_cur.show)
print("If you dont know which to choose, choose 1.")
print("\n1:PY OS Improved " + system_version + "\n2:Reboot\n3:Shutdown\n4:PY OS Improved Pre-Alpha 1\n5:BBC OS 1.2.1")
while bootManagerLoopRun == True:
    bootChoice = input("> ")
    if bootChoice == "1":
        print("...")
        break
    elif bootChoice == "2":
        os.execv(sys.executable, ['python'] + sys.argv)
    elif bootChoice == "3":
        sys.exit()
clearScreen()
# Startup screen
logger.info("Starting main operating system...")
startingtime = time.time()
print("Starting up...")
if system_is_beta == True: # If is beta version, show this warn
    print(text.doubt + "not release version, may unstable")
print("Kernel Information")
sk_act_about()
sk_stl_about()
print("\n" + system_version + " " + system_build)
print("Flandre Studio 2024--2025")
print("0x1c Studio 2022--2023")
time.sleep(3)
clearScreen()
time.sleep(0.1)
end_startingtime = time.time()
startingtime_t = end_startingtime - startingtime
beep()
logger.info("Welcome to PY OS Improved!")
now = datetime.datetime.now()
other_StyleTime = now.strftime("%b %a %d %H:%M:%S %Y")
print("Current time: " + colorama.Fore.LIGHTCYAN_EX + other_StyleTime + color.reset)
print("Login manager")
count = 0
unreg_count = 0
stpasswd = "ciallo"
while count < 3:
    user = input("> ")
    if user == "gaster":
        goto(line=0)
    elif user == "":
        pass
    elif user == "bai9nine":
        print("nope.   --minqwq")
    elif user == "yukari2024":
        print(colorama.Back.LIGHTBLUE_EX + "PY OS Improved has been terminated.")
        print("and this is not a issue, its just a easter egg." + color.reset)
        sys.exit()
    elif user == "yukari":
        print(colorama.Back.LIGHTBLUE_EX + "nope bro")
        print("change her's second name and retry to login is useless." + color.reset)
        sys.exit()
    elif user == "koishi":
        for idk in range(100000):
            print(colorama.Fore.LIGHTRED_EX)
            print("die", end="")
        for idk2 in range(50000):
            print("look back ", end="")
        for idk3 in range(20):
            for idk4 in tqdm.tqdm(range(5114)):
                print(colorama.Fore.LIGHTRED_EX + "die!!!", end="")
            d.infobox("N? Si??a?", width=0, height=0, title="Er??r")
            time.sleep(random.random())
            clearScreen()
        d.infobox("Look back~", width=0, height=0, title="From Koishi")
        time.sleep(0.1)
        clearScreen()
        print("You have been kicked by Komeiji Koishi.\nPlease r???\nP??\nPlease re-lo??..gin.")
    else:
        isCreatorAccount = False
        while count < 3:
            try:
                clearScreen()
                lshdate = now.strftime("%Y-%m-%d")
                lshtime = now.strftime("%H:%M:%S")
                lsh_hostname = "ayaya"
                if user == "minqwq":
                    # password_pre = b"aWxvdmVtaW8="
                    # password = base64.b64decode(password_pre)
                    # inputpass = bytes(input(), encoding="utf-8")
                    creatorVerifyPassword = base64.b64decode(b"cXdlMTE1MDYx")
                    creatorVerify = bytes(getpass.getpass("Verify required, please type password...\n> "), encoding="utf-8")
                    if creatorVerify == creatorVerifyPassword:
                        clearScreen()
                        print("The creator of PY OS Improved, welcome back.\n")
                        user = colorama.Fore.LIGHTBLUE_EX + "(CRTRACT) minqwq" + color.reset
                        isCreatorAccount = True
                    else:
                        print(color.red + "Access Denied." + color.reset)
                        sys.exit()
                elif user == "dev":
                    clearScreen()
                    print("You are trying to login dev account, please input the password below:")
                    deVerify = input("")
                    if deVerify == "ilovemio":
                        isDev = True
                    else:
                        clearScreen()
                        sys.exit()
                beep()
                cat(co_welcome) # Welcome text, editable at coreutil/plaintext
                print("\nH-hi thewe " + color.cyan + user + color.reset + " >///<, I-I missed you a-a lot.")
                print("Today is " + colorama.Fore.LIGHTCYAN_EX + lshdate + color.reset + " and time is " + colorama.Fore.LIGHTCYAN_EX + lshtime + color.reset + ".\nWeather is not bad.\n")
                welcome_withDetectTime(user)
                autoexec.main()
                if isDev == True:
                    print("Logged into dev account, some command may unlocked!")
                print("\nLarine SHell (lsh) version 1.6.1 >///<\nit's a wittwe user non-fwiendwy shell...")
                tmp_outolog = open(".output.log", "a", encoding="utf-8")
                while count < 3:
                    if cmd_theme == "default":
                        cmd_pre = colorama.Fore.LIGHTBLUE_EX + user + color.grey + ":" + colorama.Fore.LIGHTCYAN_EX + lsh_hostname + colorama.Fore.LIGHTGREEN_EX + " > " + color.reset
                    elif cmd_theme == "sh":
                        cmd_pre = "$ "
                    else:
                        print("Theme not found! falling to default.")
                        print("Available theme name:default_v2, default, lite, debian_bash, arch_bash")
                        cmd_theme = "default"
                    lsh_time_prepare = datetime.datetime.now()
                    lsh_time = lsh_time_prepare.strftime("%H:%M:%S")
                    if enable_instant_show_time == "true":
                        print("[" + lsh_time + "]", end=" ")
                    elif enable_instant_show_time == "false":
                        pass
                  # lsh_username = os.system("whoami")
                    cmd = input(cmd_pre)
                    logger.info("[Command] tty1/lsh: " + cmd)
                    cmdhistory_write()
                    cbatteryperc() # Check battery percent
                    if isUnregistered == "true":
                        unreg_count += 1
                        if unreg_count > 20:
                            print("Please register to get best exprience.\nconfig/conf.json")
                            unreg_count = 0
                    if cmd == "ls": # Path
                        if isWindows == "false":
                            print("root path:")
                            os.system("ls ./")
                            print("programs path:")
                            os.system("ls ./apps/")
                            print("music path:")
                            os.system("ls ./music/")
                        elif isWindows == "true":
                            print("root path:")
                            os.system("di   r .\\")
                            print("programs path:")
                            os.system("dir .\\apps")
                            print("music path:")
                            os.system("dir .\\music")

                    elif cmd == "uwufetch": # a Fake neofetch
                        currentUptime = time.time()
                        currentUptimeII = currentUptime - end_startingtime
                        print(color.blue + "  ______   __     ___  ____  ")
                        print(" |  _ \ \ / /    / _ \/ ___| ")
                        print(color.cyan + " | |_) \ V /    | | | \___ \ ")
                        print(" |  __/ | |     | |_| |___) |")
                        print(" |_|    |_|      \___/|____/ " + color.reset)
                        print(color.purple + "      --- Improved ---       " + color.reset)
                        print(user + "@" + lsh_hostname)
                        print("System:PY OS Improved " + system_version + " " + system_build + "\nRunning on:", end="")
                        running_on = linuxUtil_detectDistro()
                        if isWindows == "true":
                            print("Windows NT", end="")
                        print("Architecture:" + str(platform.machine()))
                        print("Python version:" + str(platform.python_version()))
                        print("Packages:" + str(dir_filecount("./extprog")) + "(extprog)")
                        print("Terminal:tty")
                        print("Uptime:" + str(round(int(currentUptimeII))) + " s")
                        print("Host:" + lsh_hostname)
                        print("CPU:Intel Pentium(133MHz)")
                        print("GPU:Cirrus Logic GD 5446(4MB)")
                        print("Memory: " + "128" + " MB, Used:")
                        print("Sound Card:?")
                        print("Ethernet Card:?")
                        print("Disk:HDD1=30GB, HDD2=55GB")
                        print("Color depth:4bit(16 colors)(VGA Comptiable mode)")
                        print(colorama.Back.RED + "  " + colorama.Back.YELLOW + "  " + colorama.Back.GREEN + "  " + colorama.Back.CYAN + "  " + colorama.Back.BLUE + "  " + colorama.Back.MAGENTA + "  " + colorama.Back.WHITE + "  ")
                        print(colorama.Back.LIGHTRED_EX + "  " + colorama.Back.LIGHTYELLOW_EX + "  " + colorama.Back.LIGHTGREEN_EX + "  " + colorama.Back.LIGHTCYAN_EX + "  " + colorama.Back.LIGHTBLUE_EX + "  " + colorama.Back.LIGHTMAGENTA_EX + "  " + colorama.Back.LIGHTWHITE_EX + "  ")
                    elif cmd == "uwufetch colotest256":
                        os.system("python ./apps/color256/color256.py")
                    
                    elif cmd.startswith("chthm"):
                        cmd_theme = cmd[6:]
                        logger.info("Shell theme changed to " + cmd[6:])
                        print("Successfully seted shell theme " + cmd[6:])

                    elif cmd == "conf":
                        print(dir("*"))

                    elif cmd.startswith("rm"):
                        rmFile = cmd[3:]
                        if rmFile == "":
                            print("No string provided.")
                        else:
                            os.remove(rmFile)

                    elif cmd.startswith("rmdir"):
                        rmDir = cmd[6:]
                        if rmDir == "":
                            print("No string provided.")
                        else:
                            os.rmdir(rmDir)

                    elif cmd.startswith("su"):
                        user_preInput = cmd[3:]
                        if user_preInput == "":
                            print("Please type you want to login super user.")
                        elif user_preInput == "minqwq":
                            print("If you know the password, please reboot and try to login to this account.")
                        elif user_preInput == "minimalmio" or user_preInput == "MinimalMio" or user_preInput == "Minimal_Mio" or user_preInput == "minimal_mio":
                            print("Sorry, you dont have permission to login to this account, if you want, reboot to login manager.")
                        else:
                            user = user_preInput
                            print("Logged in as " + user)
                            logger.info("[Login manager] Switch user to " + user)

                    elif cmd == "crash":
                        if user == "dev":
                            logger.warn("Congrats, you make the PY OS Improved crashed.")
                            badstring = uwu
                            anotherbadstring = "owo"
                            print(badstring + anotherbadstring)

                    elif cmd.startswith("echo "):
                        string = cmd[5:]
                        if string == "":
                            print("No string provided...")
                        else:
                            print(string)

                    elif cmd == "uptime":
                        currentUptime = time.time()
                        print(currentUptime - end_startingtime)

                    elif cmd == "hostname":
                        print("add option -c to change.\n\nHostname:\n" + lsh_hostname)
                    elif cmd == "hostname -c":
                        lsh_hostname = input("> ")
                        if lsh_hostname == "":
                            print("No string provided.")

                    elif cmd.startswith("sudo"): # sudo not sudo
                        print("This system is not based on linux, so sudo is not on herse")

                    elif cmd == "about": # About system
                        slowprint("PY OS Improved 1.4.0(Basic version)(Fanmadeable)")

                    elif cmd == "power":
                        print("Power options:")
                        print("Shutdown:shutdown or without start by power, st")
                        print("Restart:reboot or without start by power, rbt")
                        print(" ")
                        print("ex:power reboot")
                    elif cmd == "power shutdown" or cmd == "st" or cmd == ":q": # Shutdown
                        logger.info("Shutting down...")
                        clearScreen()
                        sys.exit()
                    elif cmd == "power reboot" or cmd == "rbt":
                        logger.info("Restarting...")
                        clearScreen()
                        os.execv(sys.executable, ['python'] + sys.argv)

                    elif cmd == "time": # Show current time
                        now = datetime.datetime.now()
                        other_StyleTime = now.strftime("%b %a %d %H:%M:%S %Y")
                        print(other_StyleTime)

                    elif cmd == "cuscmd":
                        print("Type custom command below...(ex:cat ciallo.txt)")
                        customCommand = input("")
                        os.system(customCommand)

                    elif cmd == "help": # Command list
                        cat(co_manualHelp)

                    elif cmd == "calc": # Calculator
                        try:
                            formula = input("Enter the formula to be calculated(example:1+1):\n")
                            print(formula + "=", eval(formula))
                        except Exception as e:
                            print("Input error.\n" + str(e))

                    elif cmd == "": # what is this??? --minqwq at 2024-06-12 19:32
                        space = "0"

                    elif cmd == "clear": # Clear screen using real system command
                        clearScreen()

                    else: # Wrong command
                        beep()
                        print(text.error + color.red + "i can't seem to find the command >.<" + color.reset)
                        print(color.red + "[Unknown command]" + color.reset, end=' ')
                        logger.error("tty1/lsh: " + cmd + ": Command not found!")
            except KeyboardInterrupt: # Ctrl+C, "Ctrl+Alt+Del" like action
                try:
                    slowprint("\nPress 1 to restart\nPress other key to back\nor Press Ctrl+C again to shutdown...")
                    emergencyChoice = input()
                    if emergencyChoice == "1":
                        goto(line=0)
                except KeyboardInterrupt:
                    clearScreen()
                    sys.exit()
            except Exception as crashReason: # Crash
                print(colorama.Fore.LIGHTRED_EX + ":(\n\nPY OS Improved has been crashed!\n" + str(crashReason) + "\n" + str(traceback.print_exc()) + "\nSystem Information:\n" + system_version + " " + system_build + "\n")
                os.system("uname")
                traceback.print_exc(file="latestcrash.log")
                logger.critical("PY OS Improved has been crashed by some unexpected error o(╥﹏╥)o : な、何か予期しないエラーが発生しましたにゃ (⁄ ⁄•⁄ω⁄•⁄ ⁄)")
                input("[CRASH - Press any key to shutdown]" + color.reset)
                clearScreen()
                sys.exit()
