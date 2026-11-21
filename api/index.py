
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        params = parse_qs(urlparse(self.path).query)

        name = params.get("name", ["Студент"])[0]
        date = params.get("date", ["25.11.2026"])[0]

        message = (
            f"Сәлем, {name}! "
            f"{date} күні сағат 09:00-де "
            f"информатика сабағы болады."
        )

        result = {
            "student": name,
            "date": date,
            "message": message
        }

        body = json.dumps(
            result, ensure_ascii=False
        ).encode("utf-8")

        self.send_response(200)
        self.send_header(
            "Content-Type",
            "application/json; charset=utf-8"
        )
        self.end_headers()
        self.wfile.write(body)
