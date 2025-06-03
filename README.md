# Install 

```
pip install pyrealsense2
cd piper_sdk
pip install -e .
```

# SET PLAYER
因为真机比赛的时候使用一台主机控制多台机器，所以需要利用系统PLAYER变量来指定控制的机械臂以及相机，每次开启终端的时候都需要重新设置，请不要修改`~/.bashrc`文件
```
source set_player 1
or
source set_player 2
```

# Run
`demo_deploy.py`作为部署参考，请保证你的策略可以读取`instruction.txt`，以支持评测时赛方进行修改
```
# reset arm position
python reset.py
# deploy，请完善脚本，使得直接运行以下指令可以开启部署，其中第一行默认调用reset.py使机械臂回0位
bash deploy.sh
```


