from prometheus_client import start_http_server, Summary, Counter
import socketserver
import json
import random
import time

# Exercice : ajouter la mesure du nombre distinct d'utilisateurs ayant déclenché au moins une action


REQUEST_SUMMARY = Summary('request_process_handle', 'Time spent processing request')
DISTINCT_USER = Counter('nb_distinct_users', 'Nb distinct users')
CONNECTED_USERS = set()

class ReferenceTCPWolf(socketserver.BaseRequestHandler):

    @REQUEST_SUMMARY.time()
    def handle(self):

        actions = {
            "list": lambda *args, **kwargs: {
                "status": "OK",
                "response": {"id_parties": [1, 2, 3]},
            },
            "subscribe": lambda *args, **kwargs: {
                "status": "OK",
                "response": {"role": "wolf", "id_player": 23},
            },
            "party_status": lambda *args, **kwargs: {
                "status": "OK",
                "response": {
                    "party": {
                        "id_party": 23,
                        "id_player": 12,
                        "started": True,
                        "round_in_progress": 12,
                        "move": {"next_position": {"row": -1, "col": 0}},
                    }
                },
            },
            "gameboard_status": lambda *args, **kwargs: {
                "status": random.choice(['OK', 'KO']),
                "response": {"visible_cells": "010010000"},
            },
            "action": lambda *args, **kwargs: {
                "status": "OK",
                "response": {
                    "round_in_progress": 12,
                    "move": {"next_position": {"row": -1, "col": 0}},
                },
            },
        }

        # self.request is the TCP socket connected to the client
        pieces = [b""]
        total = 0
        while b"\n" not in pieces[-1] and total < 10_000:
            pieces.append(self.request.recv(2000))
            total += len(pieces[-1])
        self.data = b"".join(pieces)
        print(f"Received from {self.client_address[0]}:")
        result_decoded = self.data.decode("utf-8")
        result_json = json.loads(result_decoded)
        time.sleep(random.randint(1,5))
        user_id = result_json['user_id']
        
        if user_id not in CONNECTED_USERS:
            DISTINCT_USER.inc()
            CONNECTED_USERS.add(user_id)
        result = actions[result_json["action"]](None,result_json["parameters"])
        # just send back the same data, but upper-cased
        self.request.sendall(json.dumps(result).encode())
        # after we return, the socket will be closed.


if __name__ == "__main__":
    start_http_server(9998)
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), ReferenceTCPWolf) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()
