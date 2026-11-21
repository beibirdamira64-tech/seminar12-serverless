
from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        student = "Дамира"
        date = "21.11.2026"
        time = "12:00"
        subject = "Бұлттық технология"
        room = "310"

        message = (
            f"Сәлем, {student}! 👋 "
            f"Сізге жаңа сабақ кестесі келді. "
            f"Толық ақпаратты көру үшін "
            f'«Сабақ кестесін көру» батырмасын басыңыз.'
        )

        result = {
            "statusCode": 200,
            "student": student,
            "date": date,
            "time": time,
            "subject": subject,
            "room": room,
            "message": message
        }

        body = json.dumps(
            result,
            ensure_ascii=False
        ).encode("utf-8")

        self.send_response(200)
        self.send_header(
            "Content-Type",
            "application/json; charset=utf-8"
        )
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)
