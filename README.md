# Calculator
## Assignment02 - DOT503

## File Structure
```bash
project/
├── calc.py # Main calculator module
├── test_calc.py # Unit tests for the calculator module
├── build.py # Script for compiling, testing, and packaging
├── requirements.txt # List of project dependencies
└── README.md # Project documentation (you are here!!! :p)
```

## Installation and Usage

### 1. Prerequisites

- Python 3.x installed on your system
- `pip` package manager installed

### 2. Clone the Repository

```bash
git clone https://github.com/VimanthaPerera09/calculator.git
cd calculator
```
## Install Dependencies
```bash
pip install -r requirements.txt
```

## Run Unit Tests
```bash
python test_calc.py
```
## Build and Install Package the Application
```bash
python build.py
#answer the menu
```

## Execute the Calculator
```bash
cd dist #Navigate to dist directory through if youre using GUI
calculator.exe
```

## Run docker image from jenkins
After giving the image name for the docker image in pipeline and after the run is completed,
use the following commands to run the container and program

### Run in interactive mode
```bash
#This will directly run the calculator program
docker run -it <image_name>
```

### Login to the container and run
```bash
#Run container in background
docker run -d -t <image_name>

#Get the output of the above command which is the container id
docker exec -it <container_id> bash

#Or use the below command to get the id for the corresponding image
docker ps -a

#Then run the docker exec command which is mentioned above
```

