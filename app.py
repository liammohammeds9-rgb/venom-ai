from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route('/api', methods=['POST'])
def api():
    data = request.get_json()
names = [item['name'] for item in data]
return jsonify(n=names)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)
