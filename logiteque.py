from flask import Flask,jsonify
import os

app = Flask(__name__)
app.config['JSON_SORT_KEYS']=False

def scan(path):
    files=[]
    try:
        currentdir= os.listdir(path)
        for f in currentdir:
            if f.startswith('.') or f==="desktop.ini":
                continue

            if os.path.isdir(path+'/'+f):
                a={
                    'name':f,
                    'type':'folder',
                    'path':path+'/'+f,
                    'items': scan(path+'/'+f),
                }
                files.append(a)
            else:
                a = {
                        'name': f,
                        'type': 'file',
                        'path': path+'/'+f,
                        'size':os.path.getsize(path+'/'+f)
                }
                files.append(a)
    except:
        print("")

    return files

 

@app.route('/<path>')
def hello_world(path):
    os.chdir('C:/'+path)

    dir=scan('.')
    response={
        'name':path,
        'type':'folder',
        'path':path,
        'items':dir
    }
    return jsonify(response)
if __name__ == '__main__':
    app.run()
