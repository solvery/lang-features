import time
import socket
import select
import struct
import argparse
import threading
from decimal import Decimal


NTP_HEADER_FORMAT = ">BBBBII4sQQQQ"

DEFAULT_BUFFER_SIZE = 64 * 1024
NTP_UTC_OFFSET = 2208988800

HOST = 'localhost'
PORT = 123


def cur_time_with_offset(offset=0):
    current_time = time.time() + NTP_UTC_OFFSET
    with_offset = current_time + offset
    return int(Decimal(with_offset) * (2 ** 32))


class SNTPCheater(threading.Thread):
    def __init__(self, sock, offset):
        super().__init__()
        self.sock = sock
        self.offset = offset
        self.query = None
        self.addr = None
        self.recv_time = None

    def run(self, *args, **kwargs):
        self.query, self.addr = self.receive()
        self.recv_time = cur_time_with_offset()
        self.response()

    def receive(self):
        return self.sock.recvfrom(DEFAULT_BUFFER_SIZE)

    def response(self):
        packet = SNTPAnswer(self.query, self.offset, self.recv_time)
        binary = packet.to_binary()
        self.sock.sendto(binary, self.addr)


class SNTPAnswer:
    LI = 0
    VN = 4
    MODE = 4
    OPTIONS = LI << 6 | VN << 3 | MODE
    STRATUM = 1

    def __init__(self, raw_query, offset, recv_time):
        self.origin_time = self.get_transmit_time(raw_query)
        self.offset = offset
        self.recv_time = recv_time

    def get_transmit_time(self, raw_query):
        return struct.unpack(NTP_HEADER_FORMAT, raw_query)[10]

    def to_binary(self):
        return struct.pack(
            NTP_HEADER_FORMAT,
            self.OPTIONS, self.STRATUM, 0, 0,
            0,
            0,
            b'',
            0,
            self.origin_time,
            self.recv_time,
            cur_time_with_offset(self.offset)
        )


def main(args):
    host = args.host
    port = args.port
    offset = args.offset

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.bind((host, port))
        while True:
            if not select.select([sock], [], [], 1)[0]:
                continue
            SNTPCheater(sock, offset).start()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('offset', type=int,
                        help='Count of seconds we will cheat')
    parser.add_argument('--host', type=str, default=HOST,
                        help='Listening host')
    parser.add_argument('--port', type=int, default=PORT,
                        help='Listening port')
    args = parser.parse_args()
    main(args)
