from control_joints import *
import time, os

if __name__ == "__main__":
    # 获取环境变量 PLAYER
    player_value = os.getenv("PLAYER")

    # 检查环境变量是否存在且是数字
    if player_value is None:
        raise ValueError("环境变量 PLAYER 未设置")
    try:
        player_value = int(player_value)
    except ValueError:
        raise ValueError("环境变量 PLAYER 必须是一个整数")

    # 根据 PLAYER 的值执行不同的操作
    if player_value == 1:
        print("Player 1")
        left_can, right_can = "can_left_1", "can_right_1"
    elif player_value == 2:
        print("Player 2")
        left_can, right_can = "can_left_2", "can_right_2"
    else:
        raise ValueError("PLAYER 值无效，必须是 1 或 2")
    # ==== Deploy Action ====
    controller = ControlJoints(left_can=left_can, right_can=right_can)
    for i in range(3):
        positions = [0] * 14
        controller.control(positions)
        time.sleep(0.1)
