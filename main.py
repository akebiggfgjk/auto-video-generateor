import hashlib
import base64
import sys
import os

# 自行在环境变量设置千帆的参数
# os.environ["QIANFAN_ACCESS_KEY"] = "ALTAKc5yYaLe5QS***********"
# os.environ["QIANFAN_SECRET_KEY"] = "eb058f32d47a4c5*****************"

from dotenv import load_dotenv
try:
    load_dotenv('.env')
except:
    print('load env file failed!')

if len(sys.argv) == 1:
    from auto_video_generateor.v4_free_checking_webui import demo
elif sys.argv[1] in ["1", "simple"]:
    from auto_video_generateor.v1_simple_webui import demo
elif sys.argv[1] in ["2", "qianfan"]:
    from auto_video_generateor.v2_qianfan_based_webui import demo
elif sys.argv[1] in ["3", "free"]:
    from auto_video_generateor.v3_free_webui import demo
elif sys.argv[1] in ["4", "checking"]:
    from auto_video_generateor.v4_free_checking_webui import demo
else:
    assert sys.argv[1] in '1234'


def auth_checking(username, password):
    password_true = username
    return password in [password_true, password_true.lower(), password_true.upper()]


if __name__ == "__main__":
    demo.queue(max_size=1022).launch(
        server_name="0.0.0.0",
        # inbrowser=True,
        share=True,
        server_port=8000,
        quiet=True,
        # auth=auth_checking,
        auth_message='欢迎来到自动视频生成的世界'
    )
