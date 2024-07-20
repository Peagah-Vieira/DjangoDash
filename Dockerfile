FROM python:3.11-alpine3.19
LABEL mantainer="peagahvieira2003@gmail.com"

# This environment variable is used to control whether Python should 
# write bytecode files (.pyc) to disk. 1 = No, 0 = Yes
ENV PYTHONDONTWRITEBYTECODE 1

# Defines that Python output will be displayed immediately in the console or in 
# other output devices, without being buffered.
# In short, you will see Python outputs in real time.
ENV PYTHONUNBUFFERED 1

# Copy the local directory and "scripts" into the container.
COPY . /djangoapp
COPY scripts /scripts

# Enter the djangoapp folder in the container
WORKDIR /djangoapp

# Port 8000 will be available for connections external to the container
# It is the port we will use for Django.
EXPOSE 8000

# Install NPM package in docker.
# npm install installs the depedendencies in your package. json config.
# npm run build runs the script "build" and created a script which runs your application.
RUN apk add npm && \
  npm install && \
  npm run build

# RUN executes commands in a shell inside the container to build the image. 
# The result of executing the command is stored in the file system 
# image as a new layer.
# Grouping commands into a single RUN can reduce the number of layers in the 
# image and make it more efficient.
RUN python -m venv /venv && \
  /venv/bin/pip install --upgrade pip && \
  /venv/bin/pip install -r /djangoapp/requirements.txt && \
  adduser --disabled-password --no-create-home duser && \
  chown -R duser:duser /venv && \
  chmod -R +x /scripts

# Add the scripts and venv/bin folder 
# in the container's $PATH.
ENV PATH="/scripts:/venv/bin:$PATH"

# Change user to duser
USER duser

# Execute the scripts/commands.sh file
CMD ["commands.sh"]