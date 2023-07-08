# Base image with Windows
FROM windows

# Set the working directory
WORKDIR /app

# Copy the batch file
COPY run.bat .

# Set the command to run the application
CMD ["cmd", "/C", "run.bat"]
