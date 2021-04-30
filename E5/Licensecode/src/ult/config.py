MSGLEN = 128
# 收发UDP报文最大长度

ServerIP_Port = ('127.0.0.1', 10000)
# 服务器IP地址与端口号

lenTicket = 10
# 票据位数

lenLicense = 10
# 许可证位数

databaseName='info.db'
# SQLite数据库名称

class RefusedError(Exception):
    pass