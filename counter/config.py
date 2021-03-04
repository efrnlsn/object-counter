import os

from counter.adapters.object_detector import TFSObjectDetector, FakeObjectDetector
from counter.domain.actions import CountDetectedObjects


def dev_count_action() -> CountDetectedObjects:
    return CountDetectedObjects(FakeObjectDetector())


def prod_count_action():
    host = os.environ.get('TFS_HOST', 'localhost')
    port = os.environ.get('TFS_PORT', 8501)
    return CountDetectedObjects(TFSObjectDetector(host, port, 'rfcn'))


def get_count_action():
    env = os.environ.get('ENV', 'dev')
    count_action_fn = f"{env}_count_action"
    return globals()[count_action_fn]()
