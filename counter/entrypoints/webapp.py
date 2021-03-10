from io import BytesIO

from flask import Flask, request, jsonify

from counter import config

app = Flask(__name__)

count_action = config.get_count_action()


@app.route('/object-detection', methods=['POST'])
def object_detection():
    uploaded_file = request.files['file']
    image = BytesIO()
    uploaded_file.save(image)
    predictions = count_action.execute(image, 0.5)
    return jsonify(predictions)


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)

"""
curl \
  -F "file=@/home/feed9001/work/spikes/object_detection_tfs/coco/val/val2017/000000010363.jpg" \
  http://0.0.0.0:5000/object-detection
  
"""
