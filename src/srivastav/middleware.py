import platform
import psutil
import socket
import os
import requests


class Middleware:

    def __init__(self, get_response):
        self.get_response= get_response

    def __call__(self, request):
        response= self.get_response(request)  

        def bytes_to_MB(bytes):
            mb = bytes/(1024*1024)
            mb = round(mb, 2)
            return mb
        
        physical_memory = psutil.virtual_memory()
        disk_partitions1 = psutil.disk_partitions()
        load1, load5, load30 = os.getloadavg()
        load_1= round(load1, 2)
        load_5= round(load5, 2)
        load_30= round(load30, 2)

        for partition in disk_partitions1:
            disk_info1 = psutil.disk_usage(partition.mountpoint)
            bytes_to_MB(disk_info1.total)
            bytes_to_MB(disk_info1.used)

        api_request = {
            "Request": {
                "Scheme": request.scheme,
                "Path": request.path,
                "Path_Information" : request.path_info,
                "Method": request.method,
                "Encoding": request.encoding,
                "Content_Type": request.content_type,
                "Content_Params": request.content_params,
                "Host": request.get_host(),
                "Meta" : request.META,
                "Headers": request.headers,
                "Body": request.body,
            },
            "Response":{
                "Headers": response.headers,
                "Content": response.content
            },
            # "System_info":{
            #     'technology': 'python2',
            #     'technology_version': platform.python_version(),
            #     'da_version': 0.1,
            #     'da_app_name': 'python_app',
            #     'os_name': platform.system(),
            #     'os_version': platform.version(),
            #     'os_arch': platform.architecture(),
            #     'avg_load_1_min': load_1, 
            #     'avg_load_5_min': load_5,
            #     'avg_load_30_min': load_30,
            #     'client_ip': socket.gethostbyname(socket.gethostname()),
            #     'total_memory_mb': bytes_to_MB(physical_memory.total),
            #     'used_memory_mb': bytes_to_MB(physical_memory.used),
            #     'user_name': (os.environ.get('USERNAME')), 
            #     'total_disk_mb': bytes_to_MB(disk_info1.total),
            #     'used_disk_mb': bytes_to_MB(disk_info1.used),

            # }
           
        } 
        
        url_enpoint="http://stage.linqer.in/"

        # url_resp= requests.get(url_enpoint, params= api_request)
        # print(url_resp.url)
        print(api_request)
        return response
