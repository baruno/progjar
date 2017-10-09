import socket              

s = socket.socket()        
host = socket.gethostname() 
port = 12345                 

s.connect((host, port))
s.send("Hello server!")
f = open('tosend.png','rb')
print 'Sending...'
l = f.read(1024)
while (l):
    print 'Sending...'
    s.send(l)
    l = f.read(1024)
f.close()
print "Done Sending"
print s.recv(1024)
s.close                     