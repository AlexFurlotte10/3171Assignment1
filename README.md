# 3171Assignment1 - Alex Furlotte
## Alex Furlotte, B00803204, Alex.Furlotte@dal.ca

## Repository
https://github.com/AlexFurlotte10/3171Assignment1

## Description
I have chosen to use the web server option of the socket programming assignment.
The solution is written using Python and I was able to perform part A

## Explanation
My program runs a one request at a time server. To start, the program establishes the connection at port 6789. From here the program accepts one http header into the socket and if connected properly and GET for file is received properly, it sends a 200 OK status code. If the file is not found there is an IOError where we send a 404 error to the client. Once done execution we close the socket and exit the system.

## Execution 
Run the program at http://192.168.0.7:6789/HelloWorld.html

##Screenshots
![Assignment1-Screenshots](https://user-images.githubusercontent.com/75178770/121568011-97730480-c9f5-11eb-8a50-298d43c56078.jpg)
![image](https://user-images.githubusercontent.com/75178770/121568093-af4a8880-c9f5-11eb-9545-5837cf385e20.png)


## Resources
I used part of this and adapted it to fit my configuration by adding changes neccessary. 
https://dncsite.wordpress.com/2012/10/01/web-server-socket-assignment/

