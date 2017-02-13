
all:udp_broadcast_client udp_broadcast_server

udp_broadcast_client: udp_broadcast_client.c
	gcc $< -o $@

udp_broadcast_server: udp_broadcast_server.c
	gcc $< -o $@

clean:
	rm udp_broadcast_client udp_broadcast_server
