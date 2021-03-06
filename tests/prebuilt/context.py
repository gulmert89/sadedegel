import sys
from pathlib import Path

sys.path.insert(0, (Path(__file__) / '..' / '..').absolute())

from sadedegel.dataset import load_raw_corpus  # noqa # pylint: disable=unused-import, wrong-import-position
from sadedegel.prebuilt import news_classification, tweet_profanity  # noqa # pylint: disable=unused-import, wrong-import-position
from sadedegel.dataset.tscorpus import CATEGORIES # noqa # pylint: disable=unused-import, wrong-import-position
from sadedegel.dataset.profanity import CLASS_VALUES # noqa # pylint: disable=unused-import, wrong-import-position
from sadedegel.prebuilt import tweet_sentiment # for testing tweet_sentiment.py

