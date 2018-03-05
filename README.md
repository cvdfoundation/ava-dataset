# AVA Dataset
The AVA dataset densely annotates 80 atomic visual actions in 351k movie clips with actions localized in space and time, resulting in 1.65M action labels with multiple labels per human occurring frequently. Clips are drawn from 15-minute contiguous segments of movies, to open the door for temporal reasoning about activities. The dataset is split into 242 videos for training, 66 videos for validation, and 144 videos for test, with the test set to be released in the near future. This page aims to provide the download instructions and mirror sites for Open Images Dataset. Please visit the [project page](https://research.google.com/ava/) for more details on the dataset.
# Download Videos
CVDF hosts 242 videos for training and 66 videos for validation in the AVA dataset. Please download the videos with the url pattern:
```
https://s3.amazonaws.com/ava-dataset/trainval/[file_name]
```
You can download the list of file names from [here](https://s3.amazonaws.com/ava-dataset/annotations/ava_file_names_trainval.txt).
# Download Annotations
The trainval annotations can be downloaded [here](https://s3.amazonaws.com/ava-dataset/annotations/ava_trainval.zip).
