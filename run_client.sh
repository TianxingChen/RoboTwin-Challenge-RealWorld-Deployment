#!/bin/bash

# 获取环境变量 PLAYER
player_value=$(printenv PLAYER)

# 检查环境变量是否存在且是数字
if [ -z "$player_value" ]; then
    echo "环境变量 PLAYER 未设置" >&2
    exit 1
fi

if ! [[ "$player_value" =~ ^[0-9]+$ ]]; then
    echo "环境变量 PLAYER 必须是一个整数" >&2
    exit 1
fi

# 根据 PLAYER 的值执行不同的操作
if [ "$player_value" -eq 1 ]; then
    echo "Player 1"
    left_can="can_left_1"
    right_can="can_right_1"
    left_host="127.0.0.1"
    right_host="127.0.0.1"
    left_port="9990"
    right_port="9991"
elif [ "$player_value" -eq 2 ]; then
    echo "Player 2"
    left_can="can_left_2"
    right_can="can_right_2"
    left_host="127.0.0.1"
    right_host="127.0.0.1"
    left_port="9992"
    right_port="9993"
else
    echo "PLAYER 值无效，必须是 1 或 2" >&2
    exit 1
fi

# 输出结果（可以根据需要进行其他操作）
echo "Left CAN: $left_can"
echo "Right CAN: $right_can"
echo "Left Host: $left_host"
echo "Right Host: $right_host"
echo "Left Port: $left_port"
echo "Right Port: $right_port"

python3 control_joints.py "$left_can" "$right_can"