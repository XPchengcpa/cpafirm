
{
    'name': 'Database Url Manager',
    "version": "18.0.1",
    "author": "Mo Li",
    "category": "Tools",
    "description":"""
① /web/database/ url管理工具，只有白名单的用户能访问，适用于一个数据库。
② 控制只有管理员能使用debug模式
""",
    "license": "LGPL-3",
    "depends": ["web"],
    "data": [
        "security/security.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
}
