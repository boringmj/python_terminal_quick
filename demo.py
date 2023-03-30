import threading
from terminal_quick.terminal import Terminal

class MyTerminal(Terminal):

    def _handle(self,data:str)->None:
        print("监听到输出",data)

terminal=MyTerminal('/home/qian/steamcmd/steamcmd.sh')

def user_input():
    global terminal
    while True:
        input_=input()
        if input_=='exit':
            terminal.stop()
            break
        input_+='\r'
        terminal.write(input_)

# 开启一个线程用于监听用户输入
threading.Thread(target=user_input).start()