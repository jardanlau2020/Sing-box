import os
import subprocess
import threading
from flask import Flask

# 环境变量配置；填入 ARGO_DOMAIN 和 ARGO_AUTH 使用固定隧道
os.environ.setdefault('FILE_PATH', '.cache')
os.environ.setdefault('UUID', 'ff864e4a-8d94-4716-b1dd-4c5e482d6d9b')
os.environ.setdefault('ARGO_DOMAIN', 'deplexo.2088x.com')
os.environ.setdefault('ARGO_AUTH', 'eyJhIjoiZTRiYzc1YTdjMTVjNDNmNDM1NWJjODg1NTc3M2VjZTgiLCJ0IjoiN2NkZDNlMDQtMzZlYy00MTFlLWJhMTMtZjMxZTczYTcxMzM4IiwicyI6IlptSm1aV1ZqWWpRdFpUQTVOeTAwTldWa0xXRmxZelF0Tm1Zek5qazBZMkl6WlRFMiJ9')
os.environ.setdefault('ARGO_PORT', '8001')
os.environ.setdefault('CFIP', 'saas.sin.fan')
os.environ.setdefault('CFPORT', '443')
os.environ.setdefault('NAME', 'sub')

app = Flask(__name__)

@app.route('/')
def home():
    return "Service is running perfectly!"

def start_go_binary():
    go_bin = os.path.join(os.getcwd(), 'main')
    if os.path.exists(go_bin):
        try:
            os.chmod(go_bin, 0o775)
            # 继承环境变量并启动 Go 二进制
            subprocess.Popen([go_bin], env=os.environ.copy())
            print("Successfully launched ./main Go binary in background!")
        except Exception as e:
            print(f"Error launching ./main: {e}")

# 在后台守护线程中启动 Go 二进制
threading.Thread(target=start_go_binary, daemon=True).start()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', '3000'))
    app.run(host='0.0.0.0', port=port)
