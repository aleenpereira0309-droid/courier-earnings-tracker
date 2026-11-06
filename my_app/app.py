from flask import Flask, jsonify, request
from datetime import datetime, timedelta
import re

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify(message="Hello")

@app.route('/test', methods = ["GET", "POST"])
def test():
    if request.method == "GET": return jsonify(status = "OK", method = "GET")
    if request.method == "POST": return jsonify(status = "OK", method = "POST")

class TimeTracker():
    def __init__(self, date_str: str, start_time: str, end_time: str):
        self.date = self.cleaned_date(date_str)
        self.start = start_time
        self.end = end_time
        self.hours = self.calculate_hours()

    def cleaned_date(self, raw_date:str) -> str:
        #This function will clean raw user input of date
        user_input_date = re.split(r"[-/.\s]+", raw_date.strip())
        normalized = "-".join(user_input_date)
        datetime.strptime(normalized, "%Y-%m-%d")
        return normalized


    def calculate_hours(self) -> float:
        start_time = input("Starting Time (HH:MM): ")
        end_time = input("Ending Time (HH:MM): ")

        self.start = datetime.strptime(start_time, "%H:%M")
        self.end = datetime.strptime(end_time, "%H:%M")

        if self.end < self.start:
            self.end += timedelta(days = 1)
        duration = self.end - self.start
        total_hours = duration.total_seconds() / 3600

        return round(total_hours, 2)