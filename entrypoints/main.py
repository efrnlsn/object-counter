from adapters.object_detector import FakeObjectDetector, TFSObjectDetector
from domain.actions import CountDetectedObjects

if __name__ == '__main__':
    with open('/home/feed9001/work/spikes/object_detection_tfs/coco/val/val2017/000000010363.jpg', 'rb') as img:
        predictions_ = TFSObjectDetector('localhost', 8501, 'rfcn').predict(img)
        CountDetectedObjects(TFSObjectDetector('localhost', 8501, 'rfcn')).execute(img)

        print(predictions_)