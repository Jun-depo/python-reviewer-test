import subprocess
import sys
import boto3
import datetime
from shlex import quote

s3 = boto3.client('s3')

def main(argv):
    cmd = argv
    log_file_name = datetime.datetime.now(datetime.timezone.utc).strftime("%m_%d_%Y") + "_logfile"
    kickoff_subprocess(cmd, log_file_name)
    upload_output_to_S3(log_file_name, aws_region)

def kickoff_subprocess(cmd, log_file_name):
    process = subprocess.call(quote(cmd))
    with file = open(log_file_name, "a+"):
    	timestamp = datetime.datetime.now(datetime.timezone.utc).strftime("%m/%d/%Y, %H:%M:%S")
    	output = timestamp + " Command: "+ cmd[0] + " | Return Code: " + str(process) + "\n"
    	file.write(output)

def upload_output_to_S3(log_file_name, aws_region):
    with f = open(log_file_name, "rb"):
    	s3.upload_fileobj(f, aws_region, log_file_name)

if __name__ == "__main__":
   main(sys.argv[1:])
