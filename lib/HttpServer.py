import json
import logging
import math
import os
import re

from bottle import Bottle, run, static_file, request, response


class HttpServer:
    WALLHAVEN_API = "https://wallhaven.cc/"
    app = Bottle()
    WALLHAVEN_CORE = None
    logger = None

    def __init__(self, core):
        HttpServer.WALLHAVEN_CORE = core
        logger = logging.getLogger("WallHaven")

    @staticmethod
    @app.hook('after_request')
    def enable_cors():
        """解决跨域"""
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
        response.headers[
            'Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

    @staticmethod
    @app.route('/<path>')
    def static(path):
        return static_file(path, root=f"{HttpServer.WALLHAVEN_CORE.ABSPATH}/vue")

    @staticmethod
    @app.route('/assets/<path>')
    def assets(path):
        mimetype = "auto"
        if path.endswith(".js"):
            mimetype = "application/javascript"
        elif path.endswith(".css"):
            mimetype = "text/css"
        return static_file(path, root=f"{HttpServer.WALLHAVEN_CORE.ABSPATH}/vue/assets", mimetype=mimetype)

    @staticmethod
    @app.route('/wallhaven/:path#.+#')
    def wallhaven_api(path):
        url = f"{HttpServer.WALLHAVEN_API}{path}?{request.query_string}"
        return HttpServer.WALLHAVEN_CORE.wallhaven_request(url)
        # return {"data": [], "meta": {
        #     "current_page": 1,
        #     "last_page": 0,
        #     "per_page": 0,
        #     "total": 0
        # }}

    @staticmethod
    @app.route('/api/system/bgset', method='POST')
    def download_img():
        """设置壁纸"""
        try:
            imgInfo = json.loads(request.body.read())
            res = HttpServer.WALLHAVEN_CORE.set_bg(imgInfo)
            return res
        except Exception as e:
            return str(e)

    @staticmethod
    @app.route('/api/online/save-param')
    def save_param():
        api_params = re.sub(r'&page=\d+', '', request.query_string)
        print(api_params)
        HttpServer.WALLHAVEN_CORE.localStorage['api_params'] = api_params
        HttpServer.WALLHAVEN_CORE.localStorage['page_index'] = 0
        HttpServer.WALLHAVEN_CORE.localStorage['current_page'] = 1
        HttpServer.WALLHAVEN_CORE.update_page_data()
        return "success"

    @staticmethod
    @app.route('/api/online/download', method='POST')
    def download_img():
        imgInfo = json.loads(request.body.read())
        res = HttpServer.WALLHAVEN_CORE.download(imgInfo['url'], imgInfo['small'], imgInfo['resolution'])
        if res == "file exist":
            return "file exist"
        else:
            return "success"

    @staticmethod
    @app.route('/api/switch/list')
    def switch_list():
        per_page = 24
        root_path = HttpServer.WALLHAVEN_CORE.localStorage['download_dir']
        page = int(request.query.page)
        if request.GET.get("pageSize") is not None:
            per_page = int(request.query.pageSize)
        try:
            images = []
            for root, dirs, files in os.walk(root_path):
                images.extend([i for i in files if i.endswith(HttpServer.WALLHAVEN_CORE.IMG_FILE_TYPE)])
            images = sorted(images, key=lambda x: os.path.getmtime(os.path.join(root_path, x)), reverse=True)
            meta = {
                "current_page": page,
                "last_page": math.ceil(len(images) / per_page),
                "per_page": per_page,
                "total": len(images)
            }
            data = []
            if (page - 1) * per_page <= len(images):
                if page * per_page <= len(images):
                    res_list = images[(page - 1) * per_page: page * per_page]
                else:
                    res_list = images[(page - 1) * per_page: len(images)]
                for img_name in res_list:
                    ima_path = os.path.join(root_path, img_name)
                    data.append({
                        "id": img_name,
                        "file_size": os.path.getsize(ima_path),
                        "resolution": "",
                        "file_type": f"image/{ima_path.split('.')[1]}",
                        "path": ima_path,
                    })

            return {
                'data': data,
                "meta": meta
            }
        except Exception as e:
            return str(e)

    @staticmethod
    @app.route('/api/download/list')
    def download_list():
        return {
            "data": HttpServer.WALLHAVEN_CORE.get_download_list()
        }

    @staticmethod
    @app.route('/api/download/cancel')
    def download_cancel():
        try:
            d_url = request.query.durl
            if HttpServer.WALLHAVEN_CORE.cancel_download(d_url):
                return "success"
            else:
                return "download task not exist"
        except Exception as e:
            return str(e)

    @staticmethod
    @app.route('/api/download/pause')
    def download_pause():
        try:
            d_url = request.query.durl
            if HttpServer.WALLHAVEN_CORE.pause_download(d_url):
                return "success"
            else:
                return "download task not exist"
        except Exception as e:
            return str(e)

    @staticmethod
    @app.route('/api/download/resume')
    def download_resume():
        try:
            d_url = request.query.durl
            if HttpServer.WALLHAVEN_CORE.resume_download(d_url):
                return "success"
            else:
                return "download task not exist"
        except Exception as e:
            return str(e)

    @staticmethod
    @app.route('/api/local/img')
    def local_img():
        try:
            file_path = request.query.path
            content = open(file_path, 'rb')
            response.set_header('Content-type', 'image/jpeg')
            return content
        except Exception as e:
            HttpServer.logger.error(e)
            return str(e)

    @staticmethod
    @app.route('/api/setting/save', method='POST')
    def update_config():
        data = json.loads(request.body.read())
        res = HttpServer.WALLHAVEN_CORE.save_config(data)
        return res

    @staticmethod
    @app.route('/api/update_config', method='POST')
    def start_exe():
        data = json.loads(request.body.read())
        res = HttpServer.WALLHAVEN_CORE.start_exe(data)
        return res

    @staticmethod
    def start(host='localhost', port='1746'):
        # run(HttpServer.app, host=host, port=port)
        run(HttpServer.app, host=host, port=port, server='cherrypy')


if __name__ == '__main__':
    HttpServer(None).start()
