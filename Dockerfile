# Use the official Python image as base
FROM python:3.8-slim

# Install binutils package
RUN apt-get update && apt-get install -y binutils

# Set the working directory inside the container
WORKDIR /app

RUN mkdir /app/calculator

# Copy the entire current directory into the container
COPY . /app/calculator/.

# Install dependencies
RUN pip install --upgrade pip && \
    pip install -r /app/calculator/requirements.txt

# Define environment variable to prevent Python from writing bytecode
ENV PYTHONDONTWRITEBYTECODE 1

# Define environment variable to prevent Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

# Define the command to run your application when the container starts
RUN cd /app/calculator && python build.py --jenkins --clean --build_executable
#CMD ["python", "build.py", "--jenkins", "--clean", "--build_executable"]
CMD ["/app/calculator/dist/calculator"]