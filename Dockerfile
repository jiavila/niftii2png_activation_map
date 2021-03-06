# Create python3.6
FROM python:3.6-slim-stretch as base

COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

# Flywheel spec (v0)
WORKDIR /flywheel/v0

# Copy files into place
COPY run.py \
     niftii2png_activation_map.py \
     nipy-templates-0.2 /flywheel/v0/
RUN ls
RUN python setup.py install
RUN chmod +x ./run.py
COPY manifest.json ./maniffest.json

# Add a default ENTRYPOINT
ENTRYPOINT ["/flywheel/v0/run.py"]