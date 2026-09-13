"""
数字孪生赵口引黄灌区 - 水量调度系统启动脚本
一键启动 FastAPI 后端服务
"""
import sys
import os

def check_dependencies():
    """检查依赖是否已安装"""
    missing = []
    try:
        import fastapi
    except ImportError:
        missing.append("fastapi")
    try:
        import uvicorn
    except ImportError:
        missing.append("uvicorn[standard]")
    try:
        import pydantic
    except ImportError:
        missing.append("pydantic")

    if missing:
        print("=" * 50)
        print("检测到缺少依赖，正在自动安装...")
        print("=" * 50)
        import subprocess
        req_file = os.path.join(os.path.dirname(__file__), "requirements.txt")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", req_file])
        print("依赖安装完成！")
        print("=" * 50)


if __name__ == "__main__":
    check_dependencies()

    import uvicorn
    print("=" * 50)
    print("  数字孪生赵口引黄灌区 - 水量调度系统")
    print("  服务正在启动中...")
    print("  访问地址: http://localhost:8000")
    print("  API文档:  http://localhost:8000/docs")
    print("=" * 50)

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
