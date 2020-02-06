import socket

# Membuat socket TCP/IP


#Menghubungkan socket ke port server
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10002)
print('Terhubung dengan jaringan {} dan port {}'.format(*server_address))
sock.bind(server_address) #koneksi socket ke alamat server

sock.listen(1)

while True:
    conn, client_address = sock.accept()
    try:
        data = conn.recv(1000)
        print('menerima {!r}'.format(data))
        if data:
            print('Mengirimkan kembali ke client')
            conn.sendall(data)
        else:
            print('Tidak ada data')
            break
    finally:
	#tutup socket
        print("Tutup konesksi")
        # sock.close()