import time
import os
import logo
import getpass
# Start of Main Class

# Variables
divider = '\n═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════\n'
cmds = ['help', 'exit', 'quit', 'menu']

def login():
  time.sleep(0.3)
  username = input("Username: ")
  password = getpass.getpass("Password: ")
  list = open("users.txt", "r")
  for line in list.readlines():
    user, pw = line.strip().split("|")
    if username and password == ' ' :#and username == user and password == pw :
      os.system('clear')
      time.sleep(1)
      print('Successful Login!')
      time.sleep(0.5)
      os.system('clear')
      #time.sleep(1)
      print('Welcome', username, "to (K)ali (I)ndustrialized (N)etworking (G)roup\n", divider)
      main()

    else:
      print('\nWrong Username / Password\n')
      time.sleep(0.5)
      os.system('clear')
      login()

def main():
    logo.start()
    print(divider)
    cmd()


def cmd():
  prefix = 'KING > '
  cmdline = 'None'
  cmdline = input(prefix)
  if cmdline == 'help' or 'h' :
    print("""
    help - display this screen
    exit - log off
    quit - [see exit]
    main - return to main menu
    """)
    del cmdline
    cmd()
  elif cmdline == 'clear' or 'cls' :
    del cmdline
    os.system('clear')
    time.sleep(0.1)
    cmd()
  elif cmdline != cmds :
    del cmdline
    print("[KING] Unknown command, try 'help'")
    cmd()

# Start
os.system('clear')
login()



