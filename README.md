# Simple echo web-server
Simple web-server on Python with socket default library.

Socket library official docs [here](https://docs.python.org/3/library/socket.html).

## Main Features

- Server listen port 2500 on localhost and send response
- Headers added to the response, all browsers will be able to process the response correctly


## Tech

- Socket library
- Python 

## Installation

- Install the python interpreter from [official site](https://www.python.org/downloads/).
- Clone this repository on you local machine 
  ```
  git clone https://github.com/AlexanderSeryakov/echo-web-server.git
  ```
- Move to directory on main.py file
- Start the server with command on Windows

  ```
  python main.py
  ```
  or on Linux
  ```
  python3 main.py
  ```
- If all success you`ll see message in console:
  
  ```The server is running and waiting for a request```

## Use it

- Move to you browser and send some request to: 
  ```
  http://127.0.0.1:2500/somemessage
  ```
- In you terminal you can see this request and on page in browser you`ll see this message:
![Response1 (2)](https://github.com/AlexanderSeryakov/echo-web-server/assets/110708669/4cc8fa71-d67f-4a4c-bb54-73759d6d50f8)

