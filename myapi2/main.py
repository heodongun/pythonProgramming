from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import random

app = FastAPI()

# 1. 가짜 날씨 데이터 생성
def generate_fake_weather_data():
    cities = ["서울", "부산", "대구", "인천", "광주", "대전", "울산", "수원"]
    weather_conditions = ["맑음", "구름 많음", "비", "눈", "흐림", "바람"]

    data = []
    for city in cities:
        temperature = round(random.uniform(-5, 35), 1)  # -5도에서 35도 사이
        humidity = random.randint(30, 90)  # 30%에서 90% 사이
        condition = random.choice(weather_conditions)

        if condition == "맑음":
            icon = "☀️"
        elif condition == "구름 많음":
            icon = "☁️"
        elif condition == "비":
            icon = "🌧️"
        elif condition == "눈":
            icon = "❄️"
        elif condition == "흐림":
            icon = "🌥️"
        elif condition == "바람":
            icon = "💨"
        else:
            icon = "❓"

        data.append({
            "city": city,
            "temperature": temperature,
            "humidity": humidity,
            "condition": f"{condition} {icon}"
        })

    return data

# 2. FastAPI 엔드포인트
@app.get("/", response_class=HTMLResponse)
async def show_weather():
    data = generate_fake_weather_data()

    # HTML 테이블 생성
    table_html = """
    <table>
        <thead>
            <tr>
                <th>도시</th>
                <th>온도 (°C)</th>
                <th>습도 (%)</th>
                <th>날씨</th>
            </tr>
        </thead>
        <tbody>
    """
    for row in data:
        table_html += f"""
        <tr>
            <td>{row['city']}</td>
            <td>{row['temperature']}</td>
            <td>{row['humidity']}</td>
            <td>{row['condition']}</td>
        </tr>
        """
    table_html += "</tbody></table>"

    # HTML 페이지 생성
    html_content = f"""
    <html>
        <head>
            <title>대한민국 주요 도시 날씨</title>
            <style>
                body {{ font-family: Arial, sans-serif; text-align: center; }}
                table {{ margin: 0 auto; border-collapse: collapse; width: 80%; }}
                th, td {{ padding: 10px; border: 1px solid #ddd; text-align: center; }}
                th {{ background-color: #f4f4f4; }}
            </style>
        </head>
        <body>
            <h1>대한민국 주요 도시 날씨 정보</h1>
            {table_html}
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)
