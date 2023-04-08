from srivastav.server_info import Server
from srivastav.middleware import Middleware
import asyncio
from aiohttp import request

server1= Server()
middleware1= Middleware()
# class Api:
    
    # def __init__(self):
    #     self.server= Server()
    #     # self.middleware= Middleware()
    #     pass

    # def test(self):
    #     api_response=  {
    #         "server_info": self.server.get_info(),
    #         # "Response_info": Middleware.__call__()
    #     }
    #     print("hiiiii")
    #     return api_response
api_response=  {
            "server_info": server1.get_info(),
         "Response_info": middleware1.__call__()
}
print(api_response)

async def get_task(url):
    async with request('GET', url, params= api_response) as response:
        list= await response.text()
        print(list)
        print(response.url)
        

async def main(url):
    data= await asyncio.gather(get_task(url))
    return data
print("main")

if __name__ == "__main__":
    print("hi") 
    asyncio.run(main("http://stage.linqer.in/"))
    print("how are you")
print("hello")
