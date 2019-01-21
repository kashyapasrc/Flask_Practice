from flask import Flask, render_template, request
from werkzeug import secure_filename
from flask import send_file

import uuid
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('upload.html')
	
@app.route('/uploader', methods = [ 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(str(uuid.uuid4())+".png")
      #f.save(secure_filename(f.filename))
      return 'file uploaded successfully'



@app.route('/get_image')
def get_image():
    if request.args.get('type') == '1':
       filename = 'icon.png'
    else:
       filename = 'ic_launcher.png'
    return send_file(filename, mimetype='image/png')
		
if __name__ == '__main__':
   app.run()
