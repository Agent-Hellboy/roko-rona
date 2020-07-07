# roko-rona
This is a project to create a baby cry detection application which can be extended to a baby monitoring application with video and audio feed. 

## Milestones completed
* Dataset has been created of two classes crying and not crying images.
* Images are created by converting the 10s annotated clips of audio from the YouTube videos from AudioSet.
* Crying images are images of the videos that were annotated as crying and the  Not Crying images consist images from sounds from the household with the babies eg:       blabbering, convesations, child speaking, baby laughter etc.
* For prediction, CNNs have been used. 

## How to create dataset from AudioSet?
* Download these csv files from [AudioSet](https://research.google.com/audioset/download.html) accordingly.
  * For evaluation - eval_segments.csv.
  * For balance train - balanced_train_segments.csv
  * For unbalance train - unbalanced_train_segments.csv
* Now you have to download the csv file which has mapped id of the annotated class to the actual label and organised from this [GitHub-repository](https://github.com/ganesh-srinivas/audioset-tutorial)
* To download for a particular class of videos and then intur images create a directory and put the csv file and open terminal and run the frame.py file.
  
  Install the dependencies.
  
  ``` pip3 install -r requirements.txt```

  ```python3 frame.py <class-id> <limit-for-the-images>```
* This will first download the files from YouTube and then convert into images and then the videos will be deleted.

## TODO
- [ ] Improve the predictive deep learning model (possibly using MobileNet)
- [ ] Creating Android application and integerating it with DL model.
- [ ] Adding notification system on the event of baby crying.
- [ ] Adding audio and video feed.