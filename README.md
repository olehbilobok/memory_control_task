# memory_control_task
The project contains following files: cpu_parser.py which is tracking the cpu of current machine and sending requests to the api.
These requests are handling by api which has been implemented in the api.py file and saving data into mongodb database.
Both services(mongodb and api) work into separate docker containers.

Run the project:

1. python3 -m venv venv (activate virtual environment)
2. Docker-compose up (the images will be built and all required dependencies will be installed)
3. python3 cpu_parser (run the script)
