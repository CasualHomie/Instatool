# Set the working directory
WORKDIR / InstaTool

# Copy the batch files
COPY install_modules.bat .
COPY run.bat .

# Run the install_modules.bat file
RUN install_modules.bat

# Set the command to run the application
CMD ["cmd", "/C", "run.bat"]
