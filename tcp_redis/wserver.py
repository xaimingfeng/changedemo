import socket
import time
import redis

pool = redis.ConnectionPool(host='192.168.10.80',port=6379,password='jmuser',db=2)#创建连接池
r = redis.Redis(connection_pool=pool)#获取连接对象

class WSGIServer(object):
    """对tcp做流量限制每分钟三个数据包，  得到的数据全部放到Redis队列"""""
    def __init__(self):
        # 1. 创建套接字
        self.tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # 2. 绑定
        self.tcp_server_socket.bind(("", 7890))

        # 3. 变为监听套接字
        self.tcp_server_socket.listen(128)

    def service_client(self,new_socket):
        rec_count=0
        #获取的数据列表

        resdata=new_socket.recv(1024).decode("utf-8")

        print(resdata)

        rec_count=rec_count+1
        return resdata


    def run_server(self):
        data_list = []
        ago_time = time.time()
        print("ago_time:",ago_time)
        while True:
            new_socket, client_addr=self.tcp_server_socket.accept()
            receice=self.service_client(new_socket)
            data_list.append(receice)
            nowtime=time.time()
            there_time=nowtime-ago_time
            print("there time:",there_time)
            if there_time>60 and data_list.__len__()>3:
                print(data_list)
                for inter in data_list:
                    r.set(inter)
            new_socket.close()

        self.tcp_server_socket.close()




if __name__ == '__main__':
    wserver=WSGIServer()
    wserver.run_server()









