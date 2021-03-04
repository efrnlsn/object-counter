from counter import config
from counter.adapters.object_detector import TFSObjectDetector

if __name__ == '__main__':
    with open('/home/feed9001/work/spikes/object_detection_tfs/coco/val/val2017/000000010363.jpg', 'rb') as img:
        predictions = config.get_count_action().execute(img)

        print(predictions)
