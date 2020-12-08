# set base image (host OS)
FROM python:3

# set the working directory in the container
WORKDIR /usr/src/app

# copy the dependencies file to the working directory
COPY requirements/prod.txt ./

# install dependencies
RUN pip install --no-cache-dir -r prod.txt

# copy the content of the local src directory to the working directory
COPY . .

# command to run on container start
CMD [ "python", "./app.py" ]
