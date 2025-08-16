import odoorpc
#python 解释器没有解释到

# 1. 创建连接对象
odoo = odoorpc.ODOO('154.12.252.210', port=8069)

# 2. 登录 Odoo
odoo.login('odoo', 'admin', 'MIma12345678')

# 3. 检查服务器版本
print('Odoo version:', odoo.version)

# 4. 设置数据库到期日期
target_key = 'database.expiration_date'
new_value  = '2099-12-31'

#定义icp模型
ICP = odoo.env['ir.config_parameter']

#搜索icp
ids = ICP.search([('key','=',target_key)]) 

#写入icp
if ids:
    ICP.write(ids, {'value': new_value})