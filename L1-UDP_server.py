import socket

# Buat socket UDP
# UDP_IP_ADDRESS = "127.0.0.1"
# UDP_PORT_NUMBER = 


# Sambungkan socket ke port yang sudah ditentukan
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 10101)
print('startidocumentationng up on {} port {}'.format(*server_address))
sock.bind(server_address) #buat binding ke server

while True:
    print("\menunggu menerima pesan")
    data, address = sock.recvfrom(10101)

    print('Menerima data sebesar {} bytes dari {}'.format(
        len(data), address))
    print(data)

    if data:
        sent = sock.sendto(data, address) #kirimkan data
        print('kirim {} bytes kembali ke {}'.format(
            sent, address))