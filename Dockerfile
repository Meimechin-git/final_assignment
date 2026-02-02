# 軽量なPythonイメージを使用
FROM python:3.10-slim

# 作業ディレクトリの設定
WORKDIR /app

# ライブラリのインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションコードのコピー
COPY app.py .

# コンテナ起動時のコマンド
CMD ["python", "app.py"]
