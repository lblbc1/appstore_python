# 厦门大学计算机专业 | 前华为工程师
# 专注《零基础学编程系列》  http://lblbc.cn/blog
# 包含：Java | 安卓 | 前端 | Flutter | iOS | 小程序 | 鸿蒙
# 公众号：蓝不蓝编程
from sqlalchemy import Column, Integer, String

from database import Base


class AppInfo(Base):
    __tablename__ = "appstore_app"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200))
    logo_url = Column(String(200))
    screenShot_urls = Column(String(1000))
    description = Column(String(1000))
    apk_url = Column(String(500))
    file_size = Column(String(50))
    download_count = Column(String(50))


class Category(Base):
    __tablename__ = "appstore_category"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))


class AppCategory(Base):
    __tablename__ = "appstore_app_category"
    id = Column(Integer, primary_key=True, index=True)
    category_id = Column(String(50))
    app_id = Column(String(50))
