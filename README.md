# Anomaly Detection

In this project, I have used YOLO v3 to detect anomalies. You can read the documentation of YOLO v3:
https://pjreddie.com/darknet/yolo/

Also, you can read the documentation to train your model:
https://github.com/mdv3101/darknet-yolov3

# Approach
For this project, we can use YOLO or Tensorflow object detection API.
But as I mentioned I have used YOLO v3 to train the model because it is the last official version that was released. For collecting the dataset I converted sample videos to images and then annotated them using [labelImg](https://pypi.org/project/labelImg/).

# Dependencies

At the first make sure that you installed Git & Python on your machine.

Then install these libraries:
 - `pip install opencv-python`
 - `pip install opencv-contrib-python`

# Run

To run the project, go to the cloned repository's directory and then run `detection.py` file, Also you can run the code with the command prompt using this command: `python detection.py`.
If you want to change the sample video you can change the path of the video in the detection file, [line 4](https://github.com/RealTourani/Anomaly-detection/blob/3e404d1da6d7117e9c2cdd8e6ff53272d5b2d1c7/detection.py#L4).

 
# Other

 - `frame.py` will convert sample videos to images and store them into a
   folder.
   
 - `anomaly.zip` is the dataset with the annotation files.
 - config folder includes trained model and configuration file.
