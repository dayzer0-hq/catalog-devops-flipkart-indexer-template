"""Flipkart search indexer

Deliberately small. What this board is about is everything AROUND this file.
"""
import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = int(os.environ.get("PORT", "8080"))


def payload():
    return {"indexed": 1240, "shard": "search-01"}


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        print(f"{self.command} {self.path}", flush=True)
        if self.path.split("?")[0] in ("/index", "/"):
            body = json.dumps(payload()).encode()
            code = 200
        else:
            body = json.dumps({"error": "not found"}).encode()
            code = 404
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args):
        pass  # the print above is the log line; this silences the default one


if __name__ == "__main__":
    print(f"Flipkart search indexer listening on {PORT}", flush=True)
    HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
