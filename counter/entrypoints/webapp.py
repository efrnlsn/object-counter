from io import BytesIO

from flask import Flask, request, jsonify

from counter import config

app = Flask(__name__)

count_action = config.get_count_action()


@app.route('/object-count', methods=['POST'])
def object_detection():
    uploaded_file = request.files['file']
    threshold = float(request.form.get('threshold', 0.5))
    image = BytesIO()
    uploaded_file.save(image)
    count_response = count_action.execute(image, threshold)
    return jsonify(count_response)


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
