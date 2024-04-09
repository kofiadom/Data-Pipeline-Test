# Use the official Python image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the requirements
RUN pip install -r requirements.txt

# Add the data generator script and CSV file to the container
ADD newmont_ahafo_data_generator.py /app/newmont_ahafo_data_generator.py
ADD newmont_ahafo_south_mine_dataset.csv /app/newmont_ahafo_south_mine_dataset.csv

# Copy the ingest_data script into the container
COPY ingest_data.py .

# Run the ingest_data script when the container launches
CMD ["python", "ingest_data.py"]

