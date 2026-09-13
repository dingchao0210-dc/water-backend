"""
数字孪生赵口引黄灌区 - 水量调度后端服务
FastAPI 后端，提供调度数据的 RESTful API
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pathlib import Path
import json

app = FastAPI(title="河南省智慧水网监测与调度API", version="1.0.0")

# 跨域支持（开发阶段）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==============================
# 模拟数据（实际项目中应连接数据库）
# ==============================

# 方案设置数据
plan_settings = {
    "supply_plan": "赵口供水方案1",
    "dispatch_plan": "赵口调度方案1",
    "start_date": "2025/04/07",
    "end_date": "2025/04/17",
    "status": "轮灌"
}

# 调度总览数据
dispatch_overview = {
    "total_days": 10,
    "total_days_unit": "天",
    "total_areas": 12,
    "total_areas_unit": "个",
    "total_water": 2144,
    "total_water_unit": "万m³"
}

# 当天径流数据（3个水库）
water_supply_sequence = [
    {"id": 1, "name": "三门峡水库", "volume": 1250, "time": "08:00", "status": "completed"},
    {"id": 2, "name": "小浪底水库", "volume": 2680, "time": "09:30", "status": "active"},
    {"id": 3, "name": "西霞院水库", "volume": 890, "time": "10:15", "status": "pending"},
]

# 地图标签数据
map_tags = [
    {"label": "年供水量", "value": "23.58", "unit": "亿m³", "active": True},
    {"label": "年排沙量", "value": "1.26", "unit": "亿吨", "active": False},
]

# 地图气泡数据（3个水库）
map_bubbles = [
    {"name": "三门峡水库", "volume": 1250, "top": "58%", "left": "7%"},
    {"name": "小浪底水库", "volume": 2680, "top": "46%", "left": "60%"},
    {"name": "西霞院水库", "volume": 890, "top": "53%", "left": "80%"},
]

# 水库标签
canal_labels = [
    {"name": "三门峡", "top": "50%", "left": "5%"},
    {"name": "小浪底", "top": "38%", "left": "58%"},
    {"name": "西霞院", "top": "47%", "left": "78%"},
]

# 排沙数据（3个水库）
sediment_data = [
    {"reservoir": "三门峡水库", "sediment_concentration": "35.2 kg/m³", "sediment_volume": "0.42 亿t", "transport_rate": "286 t/s"},
    {"reservoir": "小浪底水库", "sediment_concentration": "12.8 kg/m³", "sediment_volume": "0.68 亿t", "transport_rate": "152 t/s"},
    {"reservoir": "西霞院水库", "sediment_concentration": "8.5 kg/m³", "sediment_volume": "0.16 亿t", "transport_rate": "78 t/s"},
]

# 水库列表
channels = [
    {"id": "sanmenxia", "name": "三门峡水库", "active": True},
    {"id": "xiaolangdi", "name": "小浪底水库", "active": False},
    {"id": "xixiayuan", "name": "西霞院水库", "active": False},
]


# ==============================
# API 路由
# ==============================

@app.get("/api/plan-settings")
async def get_plan_settings():
    """获取方案设置"""
    return plan_settings


@app.get("/api/dispatch-overview")
async def get_dispatch_overview():
    """获取调度总览"""
    return dispatch_overview


@app.get("/api/water-supply-sequence")
async def get_water_supply_sequence():
    """获取供水水序"""
    return water_supply_sequence


@app.get("/api/map-tags")
async def get_map_tags():
    """获取地图标签数据"""
    return map_tags


@app.get("/api/map-bubbles")
async def get_map_bubbles():
    """获取地图气泡数据"""
    return map_bubbles


@app.get("/api/canal-labels")
async def get_canal_labels():
    """获取渠道标签"""
    return canal_labels


@app.get("/api/sediment-data")
async def get_sediment_data():
    """获取排沙数据"""
    return sediment_data


@app.get("/api/channels")
async def get_channels():
    """获取渠道列表"""
    return channels


@app.get("/api/dashboard")
async def get_dashboard():
    """一次性获取所有仪表盘数据（推荐使用）"""
    return {
        "plan_settings": plan_settings,
        "dispatch_overview": dispatch_overview,
        "water_supply_sequence": water_supply_sequence,
        "map_tags": map_tags,
        "map_bubbles": map_bubbles,
        "canal_labels": canal_labels,
        "sediment_data": sediment_data,
        "channels": channels,
    }


# ==============================
# 静态文件服务（同时托管前端页面）
# ==============================

# 前端根目录（index.html 所在目录），使用 resolve() 确保绝对路径
static_dir = (Path(__file__).parent / "..").resolve()

# 直接挂载到对应路径，使 css/、js/、images/ 等相对路径可正常访问
# 注意：mount 必须放在所有显式路由之后，否则会拦截 /api 等路径
app.mount("/css", StaticFiles(directory=str(static_dir / "css")), name="css")
app.mount("/js", StaticFiles(directory=str(static_dir / "js")), name="js")
app.mount("/images", StaticFiles(directory=str(static_dir / "images")), name="images")


@app.get("/")
async def serve_index():
    """返回首页"""
    return FileResponse(str(static_dir / "index.html"))
