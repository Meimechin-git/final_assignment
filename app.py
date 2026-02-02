import requests
from bs4 import BeautifulSoup
from flask import Flask
import datetime

app = Flask(__name__)

@app.route('/')
def get_weather():
    # 大阪（大阪市）のURL
    url = "https://weather.yahoo.co.jp/weather/jp/27/6200.html"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, "html.parser")
        
        # サイトのタイトル
        title = soup.title.text
        
        forecast_box = soup.find(class_="forecastCity")
        
        weather_text = "取得失敗"
        icon_url = ""

        if forecast_box:
            pict_element = forecast_box.find(class_="pict")
            
            if pict_element and pict_element.find("img"):
                img_tag = pict_element.find("img")
                weather_text = img_tag.get("alt", "不明")
                icon_url = img_tag.get("src", "")
            else:
                first_img = forecast_box.find("img")
                if first_img:
                    weather_text = first_img.get("alt", "不明")
                    icon_url = first_img.get("src", "")
        
        # --------------------

        if weather_text == "取得失敗":
            weather_text = "要素が見つかりませんでした。<br>HTML構造が変わっている可能性があります。"

        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        return f"""
        <!DOCTYPE html>
        <html lang="ja">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Osaka Weather App</title>
            <style>
                body {{ font-family: sans-serif; text-align: center; padding: 50px; background-color: #f4f4f9; }}
                .card {{ background: white; padding: 40px; border-radius: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); display: inline-block; }}
                h1 {{ color: #333; }}
                .weather-val {{ font-size: 30px; font-weight: bold; color: #e67e22; margin: 20px 0; }}
            </style>
        </head>
        <body>
            <div class="card">
                <h1>大阪の天気</h1>
                <p>ページタイトル: {title}</p>
                <div class="weather-val">
                    {f'<img src="{icon_url}" width="120"><br>' if icon_url else ''}
                    {weather_text}
                </div>
                <hr>
                <p><small>{now}</small></p>
            </div>
        </body>
        </html>
        """

    except Exception as e:
        return f"<h1>Error</h1><p>{str(e)}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
