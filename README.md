# final_assignment

Dockerコンテナ上で動作し、Webスクレイピングを用いて「現在の東京の天気」を表示するPython (Flask) アプリケーションです。
Windows (WSL2) 環境での構築手順を記載します。

## プロジェクト概要

* **機能**: Yahoo!天気から情報を取得し、アイコンと天気予報を表示します。
* **技術スタック**:
    * Infrastructure: Docker
    * OS: Windows 11 (WSL2 - Ubuntu)
    * Language: Python 3.10
    * Framework: Flask
    * Library: BeautifulSoup4 (Scraping)

## ディレクトリ構成

```text
.
├── app.py              # アプリケーション本体
├── Dockerfile          # コンテナ構築設定
├── requirements.txt    # 依存ライブラリ一覧
└── README.md           # 手順書（本書）
