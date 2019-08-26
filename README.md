# Queue-Data-Analytics
PROBLEM STATEMENT
Long lines at some specific time ticketing windows and services counter at Railway station, Bus stand, RTO office, Banks and other places could lead to bad services experiences. On many occasions lines are longer at specific time of day but empty/short at other times. It would be very user if real-time and historical queue length can be made available via website or mobile app to user and facility managers. This would in longterm help deliver better experience and smarter cities. Key technical challenge to solve this problem is to identify persons in specific area. 
 
 The proposed solution is to develop a web application where real-time and historical queue length will be made available to the user and facility managers. Raspberry-pi with cam / webcams with computational power use Tensorflow object detection API to process the video frames for every fixed interval to obtain the number of people detected. The count of people is stored in a file and also recorded in a historical log file along with the timestamp and camera id. The count is then displayed on the front end on a web page along with the historical data upon users or facility manager‟s request.
 
INTRODUCTION
The project targets on providing a user-friendly interface so that the user can refer to the service counter of his/her choice and get the current queue length of the requested service window of his/her city. 
The project is based on machine learning approaches to detect the objects of specified type captured via security cameras and to count the detected objects. 
A web-based approach is used to retrieve the count from the security cameras of service windows and make it available on a web interface visible to the end user. 
The project aims at providing a good user experience of the service windows to the user by letting them avoid long queues at the service windows. 


Description:- 
Front End 
• User requests queue length for a specific counter via the webpage. 
• On the request of live count the web page fetches the live count from the respective web (hosted by flask) address of the cam‟s live count using xhttp request and displays it on the webpage. 
• Similarly it also fetches the historical from the respective web (hosted by flask) address of the cam‟s historical data using xhttp request and displays it on the webpage on the historical data request. 
• The data on the webpage is modified using Ajax. 
Back End 
• Webcam/ Security camera captures the video feed. 
• The captured video feed is processed by Opencv library frame by frame which returns a numpy array respective to each and every frame in the video feed. 
• The numpy array data is processed by Tensorflow object detection API(ssd_mobilenet_v1_coco model) which detects the specified target objects ("person") and returns count of the same. 
• The processed count is rewritten onto a live count file after certain interval of time.  
• The processed count is also appended in a historical log file. 
• Using Flask the python script reads the count from file and hosts the count a webserver (http://localhost/livecount). 
• Simultaneously  Flask also reads the historical data from the historical log file and hosts it on a web route (http://localhost/historicaldata).
