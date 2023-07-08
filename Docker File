# Base image with Windows and desired programming language
FROM mcr.microsoft.com/windows:ltsc2019

# Set the working directory
WORKDIR /app

# Copy the batch files
COPY install_modules.bat .
COPY run.bat .

# Run the install_modules.bat file
RUN install_modules.bat

# Copy the application code
COPY . .

# Expose the desired port(s)
EXPOSE 8000

# Set the command to run the application
CMD ["cmd", "/C", "run.bat"]
