FROM python:3.11.3
LABEL mantainer="peagahvieira2003@gmail.com"

# This environment variable is used to control whether Python should
# write bytecode (.pyc) files to disk. 1 = No, 0 = Yes
ENV PYTHONDONTWRITEBYTECODE 1

# Defines that Python output will be displayed immediately in the console or in
# other output devices, not buffered.
# In short, you'll see Python outputs in real time.
ENV PYTHONUNBUFFERED 1

# Copy the "current folder" and "scripts" folder into the container.
COPY . /djangoapp
COPY scripts /scripts

# Enter the djangoapp folder in the container
WORKDIR /djangoapp

# Port 8000 will be available for external connections to the container
# It's the port we're going to use for Django.
EXPOSE 8000

# RUN runs commands in a shell inside the container to build the image.
# The result of executing the command is stored in the file system of the
# image as a new layer.
# Grouping the commands into a single RUN can reduce the amount of layers in the
# image and make it more efficient.
RUN python -m venv /venv && \
  /venv/bin/pip install --upgrade pip && \
  /venv/bin/pip install -r /djangoapp/requirements.txt && \
  adduser --disabled-password --no-create-home duser && \
  mkdir -p /data/web/static && \
  mkdir -p /data/web/media && \
  chown -R duser:duser /venv && \
  chown -R duser:duser /data/web/static && \
  chown -R duser:duser /data/web/media && \
  chmod -R 755 /data/web/static && \
  chmod -R 755 /data/web/media && \
  chmod -R +x /scripts

# Add scripts folder and venv/bin
# in the $PATH of the container.
ENV PATH="/scripts:/.venv/bin:$PATH"

# Change user to duser
USER duser

# Run the scripts/commands.sh file
CMD ["commands.sh"]