from flask import Flask
import os

# static 폴더의 절대 경로 지정
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
static_path = os.path.join(base_dir, 'static')

app = Flask(__name__, static_folder=static_path, static_url_path='/static')

@app.route('/')
def home():
    return '''
    <html>
        <body>
            <h1>샘플 이미지</h1>
            <img src="/static/Images/sample.png" alt="샘플 이미지">
        </body>
    </html>
    '''

if __name__ == '__main__':
    print("static 경로:", static_path)
    print("이미지 존재?", os.path.exists(os.path.join(static_path, 'Images/sample.png')))
    app.run(debug=True)
