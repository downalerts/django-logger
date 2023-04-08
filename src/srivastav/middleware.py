


class Middleware:

    def __init__(self, get_response):
        self.get_response= get_response
        # self.server = Server()

    def __call__(self, request):
        response= self.get_response(request)  

        api_request = {
            # "server_info": self.server.get_info(),
            
                "url_scheme": request.scheme,
                "path": request.path,
                "path_information" : request.path_info,
                "method": request.method,
                "encoding": request.encoding,
                "content_type": request.content_type,
                "content_params": request.content_params,
                "host": request.get_host(),
                # "meta" : request.META,
                "headers": request.headers,
                "body": request.body,
            
            
                "headers": response.headers if "headers" in response else response,
                "content": response.content
                       
        } 
        
        
        
        # print(api_request)
        return response
