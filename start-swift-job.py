#!/usr/bin/env python3

import subprocess
import datetime

def get_current_date_time():
    now = datetime.datetime.now()
    date_time = now.strftime("%Y%m%d-%H%M%S")
    return date_time

# THIS CREATES A POD, NOT A JOB
def submit_job(image, command, job_name):
    cmd = f"kubectl run {job_name} --image={image} --restart=Never --command -- {command}"
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    (output, error) = process.communicate()
    return output.decode("utf-8").strip()

if __name__ == "__main__":
    image = "fedora:rawhide"
    command = "/bin/bash -c 'dnf update -y;dnf install -y git;cd /;git clone https://github.com/tachoknight/swift-lang-packaging-fedora.git;cd /swift-lang-packaging-fedora/;./setup-container.sh;./justbuild.sh'"
    job_name = f"swift-builder-job-{get_current_date_time()}"
    print(submit_job(image, command, job_name))
