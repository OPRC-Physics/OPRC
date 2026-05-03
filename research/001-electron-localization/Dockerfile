# Use a lightweight python image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy artifacts
COPY requirements.txt .
COPY band_gap_simulation.py .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the simulation
CMD ["python", "band_gap_simulation.py"]
