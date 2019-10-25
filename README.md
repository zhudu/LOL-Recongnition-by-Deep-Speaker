# LOL-Recongnition-by-Deep-Speaker

 We adopted the voice package of league of legends, based on the audio information of 142 heroes in league of legends, classified them, and identified which hero the audio object was by obtaining audio features. 

### Audio Samples

 We package the audio data and store it on baidu cloud. Please scan the qr code by Wechat to download.  The extraction code is  “ tt8w”.

![](https://p.qlogo.cn/qqmail_head/tFvCianWnUl4FlklZ5cbcsR599vrZLo2IEShPmfibms3zGbBMSVldLg8gbqs0tM7e1mA1WhG5KGf0/0)

## Quick Start

### Installing dependencies

1. Install Python 3.

2. Install the latest version of [TensorFlow](https://www.tensorflow.org/install/) for your platform. For better performance, install with GPU support if it's available. This code works with TensorFlow 1.3 and later.

3. Install requirements:

   ```
   pip install -r requirements.txt
   ```

## Visual 

```python
python SpeakerRecog.pyw
```

## Model

We package the model data and store it on baidu cloud. Please scan the qr code by Wechat to download. The extraction code is  “ 6umw”.

![](https://p.qlogo.cn/qqmail_head/tFvCianWnUl4FlklZ5cbcsR599vrZLo2IEShPmfibms3z4R2IJtWjdY9dqVVk9OCKKfqpnjDEqPJA/0)

 After unpacking, your tree should look like this for model.

```
model
	|- pre-model
	|- train-model
			|- best_checkpoint
			|- GRU
			|- ResidualCNN
```

## Training

1. Download the speech dataset. 

Unzip the absolute path to constants.py, or unzip the path to the same path as the DATASET_DIR in constants.py. see “Audio Samples” for the download link.

2. Preprocess the data

```python
python pre_process.py
```

3. Train a model

```python
python train.py
```

note : Pre-training and then training is recommended to reduce training time.

Pre-train:

```python
python pretraining.py
```

## Notes

