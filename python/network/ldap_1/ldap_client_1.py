#encoding=utf-8
import ldap

SERVER_NAME = '192.168.1.9'
SERVER_PORT = 389

try:
    conn = ldap.open("127.0.0.1")
    conn.protocol_version = ldap.VERSION3 #设置ldap协议版本 

    username = "user=Groups,dc=test,dc=com" #身份信息
    password = "yaowu" #访问密码
    conn.simple_bind_s(username,password) # 开始绑定，验证成功的话不会抛出异常
except ldap.LDAPError, e: #捕获出错信息
    print e
