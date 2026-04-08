import os

from app.app import app


if __name__ == '__main__':
    host = os.getenv("BOOTCAMP_HOST", "127.0.0.1")
    port = int(os.getenv("BOOTCAMP_PORT", "8000"))
    app.run(host=host, port=port, debug=False)
