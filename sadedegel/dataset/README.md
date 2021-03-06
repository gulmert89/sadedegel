<a href="http://sadedegel.ai"><img src="https://sadedegel.ai/assets/img/logo-2.png?s=280&v=4" width="125" height="125" align="right" /></a>

# SadedeGel Datasets

SadedeGel provides various datasets to consolidate various NLP data sources for Turkish Language,
train prebuilt models, and benchmark models.

## `raw` Sadedegel News Corpus

[raw](raw/) sadedegel news corpus is a relatively small news corpus (roughly 100 documents) gathered using  [scraper]
and **installed** with with sadedegel installation. No extra download required.


### Using Corpus

```python
from sadedegel.dataset import load_raw_corpus

raw = load_raw_corpus()
```

## `sents` Sadedegel News Corpus

[sents](sents/) sadedegel news corpus is the sentences boundary detected (human annotation) version of [raw](raw/) corpus
and also **installed** with with sadedegel installation. No extra download required.

### Using Corpus

```python
from sadedegel.dataset import load_sentence_corpus

sents = load_sentence_corpus()
```

## `annotated` Sadedegel News Corpus

[annotated](annotated/) sadedegel news corpus is the sentences importance (aka `relevance`) annotated (human annotation) version of [sentences](sentences/) corpus
and also **installed** with with sadedegel installation. No extra download required.

### Using Corpus

```python
from sadedegel.dataset import load_annotated_corpus

sents = load_annotated_corpus()
```

## `extended` Sadedegel News Corpus

[extended](extended/) is a collection of corpus (corpura) that can be defined as the extended version of [raw](raw/) and [sents](sents/):

* [extended](extended/) **raw** is simply a larger collection of news documents collected by [scraper]
* [extended](extended/) **sents** is generated using [extended](extended/) **raw** and ML based sentence boundary detector trained over [sents](sents/) corpus
 


### Download Dataset 

You can download extended dataset using 

```bash
python -m sadedegel.dataset.extended download
```

Sub command requires two flags to access GCS buckets 
* `access-key`
* `secret-key`

Those can be passed in 3 ways:
1. Set `sadedegel_access_key` and/or `sadedegel_secret_key` in you environment.
2. Pass `--access-key` and `--secret-key` options in commandline
3. You will be prompted to provide them if they are not provided at 1 or 2.


### Check Metadata

You can assert your extended dataset using 

```bash
python -m sadedegel.dataset.extended metadata 
```

If everything is OK you will get

```bash
{'bytes': {'raw': 170014810, 'sents': 210067269},
 'count': {'raw': 36131, 'sents': 36131}}
```

If there is a problem with base directory you will get a similar warning

```
~/.sadedegel_data not found.

Ensure that you have properly downloaded extended corpus using
         
            python -m sadedegel.dataset.extended download --access-key xxx --secret-key xxxx
            
        Unfortunately due to data licensing issues we could not share data publicly. 
        Get in touch with sadedegel team to obtain a download key.
```




* Refer to [Sentences Corpus Tokenize](#sentence-corpus-tokenize)



### Sentence Corpus Tokenize

Preprocessing stage of sentence tokenization before human annotator.

```bash
python -m sadedegel.dataset tokenize
```

### Sentence Corpus Validate

Validation process ensures that hand annotated sentence tokenization does not violate any of the following span rule

1. All sentences should cover a span in corresponding raw document.
2. All sentences spans should be stored in order at `sentences` (of list type) field of `json` document.

```bash
python -m sadedegel.dataset validate
```

## `tscorpus`

[tscorpus] is an invaluable contribution by [Taner Sezer].

Corpora consist of two corpus
* [tscorpus] raw
* [tscorpus] tokenized, word tokenized version of [tscorpus] raw corpus

 Each corpus is splited into subsections per news category:
* art_culture
* education
* horoscope
* life_food
* politics
* technology
* economics
* health
* life
* magazine
* sports
* travel

[tscorpus] allows us to 
1. Verify/Calibrate word tokenizers (bert, simple, etc.) available in sadedegel
2. Ship a prebuilt news classifier.

### Using Corpora

To load [tscorpus] for word tokenization tasks

```python
from sadedegel.dataset.tscorpus import load_tokenization_tokenized, load_tokenization_raw

raw = load_tokenization_raw()
tok = load_tokenization_tokenized()
```

Refer [tokenizer](../bblock/TOKENIZER.md) for details.

To load [tscorpus] for classification tasks

```python
from sadedegel.dataset.tscorpus import load_classification_raw

data = load_classification_raw()
```

Refer  [news classification](../prebuilt/README.md) for details


## `profanity`
Corpus used in [SemEval-2020 Task 12](https://arxiv.org/pdf/2006.07235.pdf) to implement profanity classifier over Turkish tweeter dataset.

Training dataset contains 31277 documents, whereas test dataset consists of 3515 documents.

### Using Corpus

```python
from sadedegel.dataset.profanity import load_offenseval_train ,load_offenseval_test_label,load_offenseval_test

tr = load_offenseval_train()
tst = load_offenseval_test()
tst_label = load_offenseval_test_label()

next(tr)

#{'id': 20948,
# 'tweet': "@USER en güzel uyuyan insan ödülü jeon jungkook'a gidiyor...",
# 'profanity_class': 0}

next(tst)
#{'id': 41993, 'tweet': '@USER Sayın başkanım bu şekilde devam inşallah👏'}

next(tst_label)
#{'id': 41993, 'profanity_class': 0}
```

For more details please refer [tweet profanity](../prebuilt/README.md)

## `tweet_sentiment`
[Twitter Dataset](https://www.kaggle.com/mrtbeyz/trke-sosyal-medya-paylam-veri-seti) is another corpus used to build prebuilt 
tweeter sentiment classifier.

For more details please refer [tweet sentiment](../prebuilt/README.md)

[scraper]: https://github.com/GlobalMaksimum/sadedegel-scraper
[Taner Sezer]: https://github.com/tanerim
[tscorpus]: tscorpus/