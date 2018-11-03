#_*_coding:utf-8_*_
import socket
import os,sys,datetime

#global_variables
a = socket.gethostbyname_ex(socket.gethostname())[2]
k = a[2]
def host_finder(ip,port):
    try:
        print("[*] Trying :" + str(port))
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((ip,port))
        print("[+] "+str(port)+":Open")
        s.close()
    except:
        print("[-] "+str(port)+": Closed")

if __name__ == '__main__':
    time = datetime.datetime.now()
    zaman = time.strftime("%H:%M:%S")
    print(zaman)
    if len(sys.argv) < 2:
        options = input("Tarama Secenekleri \n[1]Local Ip Tara:{} \n[2]Remoto Ip Tara ".format(k))

        if options == '1':
            for i in range(80,81):
                host_finder(k,i)
        elif options == '2':
            r = input("Remote Ip: ")
            for i in range(79,81):
                host_finder(r,i)

    else:
        for i in range(79,81):
            host_finder(sys.argv[1],i)

    time2 = datetime.datetime.now()
    fark = time2 - time
    print ("\n",fark.seconds," saniye sürdü")