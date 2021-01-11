# Create python3.6
FROM python:3.6-slim-stretch as abase

COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

# Flywheel spec (v0)
WORKDIR /flywheel/v0

# Copy executables into place
COPY run.py /flywheel/v0/
RUN chmod +x ./run.py
COPY manifest.json .

# Add a default ENTRYPOINT
ENTRYPOINT ["/flywheel/v0/run.py"]