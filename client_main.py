# -*- encoding: utf-8 -*-
"""
@Project    :   Gomoku
@File       :   client_main.py
@Time       :   2021/4/8 14:11
@Author     :   Thooooor
@Version    :   1.0
@Contact    :   thooooor999@gmail.com
@Describe   :   Run this in Client
"""

from GUI.board import *

host_url = "39.107.251.174"
port = 8888


def connect_server():
    """ Build connect to Server

    :return: client
    """
    client = Client()
    client.connect(host_url, port)
    return client


def get_username():
    username = ""

    return username


class MainClient:
    """Build Client and Board

    First, get basic information (color, id)  from Server.
    Second, build Chess Board.

    Attributes: None
    """
    def __init__(self):
        self.player = get_username()
        self.client = connect_server()

        self.color, self.id = self.get_info()
        self.draw_board()

    def get_info(self):
        """Get info from Server, including color and id

        Sending request to Server then get info from Server

        :argument:
            None

        :return:
            if Succeed: color and id
            else: False
        """
        s_msg = {
            "request": "color",
            "info": self.player
        }
        self.client.send(json.dumps(s_msg))
        r_msg = json.loads(self.client.receive())
        self.client.sock.close()

        if r_msg["response"] == "color":
            return r_msg["color"], r_msg["id"]
        else:
            return False

    def draw_board(self):
        """Draw Chess Board using info from Server

        :return:
        """
        window = tk.Tk()
        info = {
            "player": "You",
            "color": self.color,
            "id": self.id,
            "opponent": "Others"
        }
        chess_board_gui = ChessBoardFrame(window, info=info, client=self.client)
        chess_board_gui.pack()
        window.mainloop()


if __name__ == '__main__':
    MainClient()
