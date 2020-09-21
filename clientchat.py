# Program chatting satu jaringan ini sebagai SERVER

import socket

print("")
print("     _______   ___      ___        ____     ___________") 
print("    /  ____/   | |      | |       / __ \    \___   ___/")
print("   /  /        | |______| |      / /  \ \       | |")
print("  /  /         | _______  |     / /____\ \      | |")
print("  \  \         | |      | |    / ________ \     | |")
print("   \  \______  | |      | |   / /        \ \    | |")
print("    \_______/  |_|      |_|  /_/          \_\   |_|")
print("")

server_address=('localhost',5050) #menentukan alamat server
SIZE=1024 #menentukan ukuran buffer
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #membuat objek socket
s.connect(server_address) #menghubungkan socket ke alamat server
while True:
    print("")
    pesan=s.recv(1024) #menerima pesan
    print "Server :",pesan  #pesan yang diterima dari server
    pesan=raw_input("Bulan : ") #menginput pesan
    s.send(pesan) #mengirim pesan