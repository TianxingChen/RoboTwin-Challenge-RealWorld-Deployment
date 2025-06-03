import time
from piper_sdk.piper_sdk import *
import pdb, os


class JointReader:
    def __init__(self, left_can, right_can):
        self.piper_left = C_PiperInterface_V2(
            can_name=left_can,
            judge_flag=False,
            can_auto_init=True,
            dh_is_offset=1,
            start_sdk_joint_limit=False,
            start_sdk_gripper_limit=False,
        )

        self.piper_right = C_PiperInterface_V2(
            can_name=right_can,
            judge_flag=False,
            can_auto_init=True,
            dh_is_offset=1,
            start_sdk_joint_limit=False,
            start_sdk_gripper_limit=False,
        )
        self.piper_left.ConnectPort()
        self.piper_right.ConnectPort()

    def get_joint_value(self):

        factor = 57295.7795  # 1000*180/3.1415926

        left_joints = self.piper_left.GetArmJointMsgs()
        left_gripper = self.piper_left.GetArmGripperMsgs()
        right_joints = self.piper_right.GetArmJointMsgs()
        right_gripper = self.piper_right.GetArmGripperMsgs()

        def update(joint_message):
            joint_1 = joint_message.joint_state.joint_1
            joint_2 = joint_message.joint_state.joint_2
            joint_3 = joint_message.joint_state.joint_3
            joint_4 = joint_message.joint_state.joint_4
            joint_5 = joint_message.joint_state.joint_5
            joint_6 = joint_message.joint_state.joint_6
            return [joint_1, joint_2, joint_3, joint_4, joint_5, joint_6]

        left_joints_list = update(left_joints)
        right_joints_list = update(right_joints)
        left_gripper_list = [left_gripper.gripper_state.grippers_angle]
        right_gripper_list = [right_gripper.gripper_state.grippers_angle]
        full_state = (
            left_joints_list
            + left_gripper_list
            + right_joints_list
            + right_gripper_list
        )

        return [x / factor for x in full_state]


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
    reader = JointReader(left_can=left_can, right_can=right_can)
    print(reader.get_joint_value())
