from flask import Flask
import os
from datetime import datetime, timedelta
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    username = os.environ.get('USER') or os.environ.get('USERNAME') or 'Unknown User'

    ist_time = datetime.utcnow() + timedelta(hours=5, minutes=30)

    try:
        top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode('utf-8')
    except Exception as e:
        top_output = f"Error retrieving top output: {str(e)}"

    return f"""
    <html>
        <body>
            <h1>System Info</h1>
            <p>Name: Surya Sai Sundeep</p>
            <p>Username: {username}</p>
            <p>Server Time (IST): {ist_time.strftime('%Y-%m-%d %H:%M:%S')}</p>
            <pre>{top_output}</pre>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
