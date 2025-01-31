# Use a base image with Python
FROM python:3.12.3

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the requirements.txt into the container
COPY requirements.txt /app/

# Step 4: Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the rest of the application code into the container
COPY . /app/

# Step 6: Expose port 5000 (default Flask port)
EXPOSE 5000

# Step 7: Run the Flask app when the container starts
CMD ["python", "challenge_4_2.py"]
