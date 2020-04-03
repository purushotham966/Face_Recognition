## The project is about detecting and displaying the name of the person. If unknown person detected that wasn't in your database then it would send message through mail or sms .
Firstly for creating a database run creat_data.py it would capture your photos and will be saved in the database with the folder name already created in dataset folder.
Then after creating the dataset it would be trained with the help of "LBPH algorithm" one of the oldest and most popular algorithm.After trainning save the id's and names of person in pickle file(dictionary format) and save the trainning data in trainning.yml.
    
 Then comming to main part face.py here by using pickle file and trainning set we are able to label the name of the detected image and
 get the accuracy acording to the confidence.If unknown face is reconized many times then it sends the messege to mail or sms.If you
 don't have account in "way2sms" it's better send to mail. And you can see the unknown person image it would be saved in a file. 
 
 
