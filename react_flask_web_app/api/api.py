from flask import Flask , request,jsonify
import sys
from flask_cors import CORS , cross_origin
import subprocess
import tempfile


sys.path.append('Extract')

app = Flask(__name__)
CORS(app,supports_credentials=True)

@cross_origin(headers=['Content-Type','Authorization'])
@app.route('/pe',methods=['POST','GET','OPTIONS'])
def api():
    if request.method == 'POST':

        store_file =request.files.get('file').read()
        store_filename = request.form.get('fileName')

        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = temp_dir + store_filename 

            with open(file_path, 'wb') as file:
                file.write(store_file)
    
            output = subprocess.check_output(['python3', 'Extract/PE_main.py',file_path])
            res_2 = output.decode().strip()
            return jsonify({'result': res_2})
    else :
        return jsonify({'result': -1})
@cross_origin(headers=['Content-Type','Authorization'])
@app.route('/url',methods=['POST','GET','OPTIONS'])
def url():
    if  request.method == 'POST':
        store = request.get_json()
        output = subprocess.check_output(['python3', 'Extract/url_main.py', store['url']])
        res_2 = output.decode().strip()
        return jsonify({'result': res_2})

    else:
        return 0
if __name__ == "__main__":
    app.run(host='0.0.0.0')