# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json


class BankStatementController(http.Controller):

    @http.route('/mficonsult/bank_statement/update_file',
                type='http', auth='user', methods=['POST'], csrf=False)
    def update_file(self, **kwargs):
        """
        接收前端上传的 zip 文件。需已登录（auth='user'），依赖浏览器 Cookie/Session。
        前端使用 FormData: form.append('file', file)
        """
        # 读取上传的文件（字段名与前端 FormData 保持一致：'file'）
        upload = request.httprequest.files.get('file')
        if not upload:
            return request.make_json_response({'error': 'file is required'}, status=400)

        filename = upload.filename or ''
        # 仅允许 zip
        if not filename.lower().endswith('.zip'):
            return request.make_json_response({'error': 'only .zip allowed'}, status=400)

        # 读取字节内容（如需限制大小可在这里检查）
        content = upload.read()

        # TODO: 你可以将 content 传入后端模型做进一步处理：
        # env = request.env(user=request.session.uid)
        # env['your.model'].process_zip(content, filename)

        # 这里按你的需求返回固定值
        return request.make_json_response({'result': 100}, status=200)
