#encoding=utf-8

def do_telnet(Host, username, password, finish, commands):
    import telnetlib
 
    tn = telnetlib.Telnet(Host, port=23, timeout=20)
    tn.set_debuglevel(2)
     
    tn.read_until('User Name : ')
    tn.write(username + '\r')
    
    tn.read_until('Password  : ')
    tn.write(password + '\r')
      
    tn.read_until(finish)
    for command in commands:
        tn.write('%s\r' % command)
    
    tn.read_until(finish)
    tn.close() # tn.write('exit\n')

if __name__=='__main__':
	 # 配置选项
	Host = '192.168.2.108'
	username = 'apc'
	password = 'apc'
	finish = '>'
	commands = ["whoami"]
	do_telnet(Host, username, password, finish, commands)
