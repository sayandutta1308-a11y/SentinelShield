import webview
import threading
from app import app


def run_flask():
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False
    )


if __name__ == "__main__":

    flask_thread = threading.Thread(
        target=run_flask
    )

    flask_thread.daemon = True
    flask_thread.start()


    webview.create_window(
        "SentinelShield Security Platform",
        "http://127.0.0.1:5000",
        width=1200,
        height=800
    )

    webview.start()