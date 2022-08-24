from flask import Flask, render_template,request, send_file
from pytube import YouTube
from io import BytesIO

app = Flask(__name__, template_folder='template', static_folder='static')

@app.route('/', methods=['POST', 'GET'])
def hello():
    if request.method == 'POST':
        text = request.form['LINK_VALUE']
        # YouTube(text).streams.get_highest_resolution().download()
        buffer = BytesIO()
        yt = YouTube(text)
        video = yt.streams.get_by_itag(18)
        video.stream_to_buffer(buffer)
        buffer.seek(0)
        return send_file(
            buffer,
            as_attachment=True,
            download_name="cool-video.mp4",
            mimetype="video/mp4",
        )
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
