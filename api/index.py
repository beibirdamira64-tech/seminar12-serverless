
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        params = parse_qs(urlparse(self.path).query)

        name = params.get("name", ["Студент"])[0]
        date = params.get("date", ["25.11.2026"])[0]
        subject = params.get("subject", ["Информатика"])[0]
        time = params.get("time", ["09:00"])[0]

        message = (
            f"Сәлем, {name}! "
            f"{date} күні сағат {time}-де "
            f"{subject} сабағы болады. "
            f"Сабаққа кешікпей келіңіз!"
        )

       
result = {
    "student": "Дамира",
    "date": "21.11.2026",
    "time": "12:00",
    "subject": "Бұлттық технология",
    "room": "310",
    "message": (
        "Сәлем, Дамира! "
        "21.11.2026 күні сағат 12:00-де "
        "310-кабинетте Бұлттық технология "
        "сабағы болады. "
        "Сабақ кестесін көру үшін батырманы басыңыз."
    )
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
