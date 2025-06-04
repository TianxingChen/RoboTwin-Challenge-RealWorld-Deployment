#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 注意: 示例代码无法直接运行，需要安装SDK后才能运行
from typing import Optional
import time, os
import socket
from piper_sdk.piper_sdk import *  # Assuming this is a placeholder for actual SDK imports
import threading
import sys


class ControlArm:
    def __init__(self, can_name="can_left_1"):
        host = "127.0.0.1"
        if can_name == "can_left_1":
            port = 9990
        elif can_name == "can_right_1":
            port = 9991
        elif can_name == "can_left_2":
            port = 9992
        elif can_name == "can_right_2":
            port = 9993
        self.can_name = can_name
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect_to_server()

    def connect_to_server(self):
        try:
            self.client_socket.connect((self.host, self.port))
            print(f"Connected to server at {self.host}:{self.port}")
        except Exception as e:
            print(f"Failed to connect to server: {e}")
            sys.exit(1)

    def control(self, joints):  # joints: 7 dim
        try:
            # Convert the joints list to a comma-separated string
            joints_str = ",".join(map(str, joints))
            print(f"Sending joints: {joints_str}")
            # Send the joints data to the server
            self.client_socket.sendall(joints_str.encode())
        except Exception as e:
            print(f"Error sending data: {e}")

    def close_connection(self):
        self.client_socket.close()
        print("Connection closed.")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(
            "Usage: python3 control_arm_client.py <LEFT_CAN_NAME> <LEFT_HOST> <LEFT_PORT> <RIGHT_CAN_NAME> <RIGHT_HOST> <RIGHT_PORT>"
        )
        sys.exit(1)

    left_can_name = sys.argv[1]

    right_can_name = sys.argv[2]

    left_arm = ControlArmClient(left_can_name)
    right_arm = ControlArmClient(right_can_name)

    position = [0, 0, 0, 0, 0, 0, 0]
    count = 0

    while True:
        print(f"Count: {count}")
        if count == 0:
            print("1-----------")
            position = [0, 0, 0, 0, 0, 0, 0]
        elif count == 100:
            print("2-----------")
            position = [0.2, 0.2, -0.2, 0.3, -0.2, 0.5, 0.08]
        elif count == 200:
            print("1-----------")
            position = [0, 0, 0, 0, 0, 0, 0]
            count = 0

        joints_list = position + position  # Duplicate for left and right arms
        left_arm.control(joints_list[:7])
        right_arm.control(joints_list[7:])
        time.sleep(0.03)
        count += 1
