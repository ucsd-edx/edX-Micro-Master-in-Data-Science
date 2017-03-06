import string

# Where users upload programs
UPLOAD_FOLDER = "/path/to/the/uploads"
# For storing running/completed programs
ARCHIVE_FOLDER = "/path/to/the/archive"
# For directing standard output and standard error
OUTPUT_FOLDER = "/path/to/the/output"
# Where we store all information about programs
RESULT_FOLDER = "/path/to/the/results"
# Where we put the programs while it is running
RUNTIME_FOLDER = "/path/to/the/runtime"
SPARK_PATH = "/path/to/spark"

ALLOWED_EXTENSIONS = set(["py"])
MASTER_IP = "<master_ip>"
MASTER_URL = "spark://%s:7077" % MASTER_IP
COMPILE_COMMAND = "python -m py_compile %s"
SUBMIT_COMMAND = (SPARK_PATH + "/bin/spark-submit --master " + MASTER_URL +
                  " --name %s %s")

COMPILE_INTERVAL = 3
REFRESH_INTERVAL = 10
STREAM_LEN = 10240
RANDOM_FILENAME_LENGTH = 8
RANDOM_SET = string.letters + string.digits

SPARK_SERVER = "http://%s:8080/api/v1" % MASTER_IP
APP_STATUS_API = SPARK_SERVER + "/applications"

QUEUE_SIZE = 3
TIMEOUT = 90

COMPILE_MESSAGE = "compiling"
CE_MESSAGE = "compile error"
RUNNING_MESSAGE = "running"
TLE_MESSAGE = "time limit exceeded"
COMPLETED_MESSAGE = "completed"
RTE_MESSAGE = "runtime error"
FAILED_TO_LAUNCH_MESSAGE = "failed to launch on Spark"
