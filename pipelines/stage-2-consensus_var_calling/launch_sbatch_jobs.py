import os
import subprocess
import sys

def submit_jobs(input_folder):
    """
    Submit SBATCH jobs for each script file in the specified folder.

    Args:
        input_folder (str): Path to the folder containing the script files.
    """
    
    if not os.path.isdir(input_folder):
        print(f"Error: {input_folder} is not a valid directory.")
        sys.exit(1)
    
    
    os.chdir(input_folder)

    # find all script files ending with '_runViralRecon.sh' to launch
    script_files = [f for f in os.listdir() if f.endswith('_runViralRecon.sh')]

    if not script_files:
        print(f"No script files ending with '_runViralRecon.sh' found in {input_folder}.")
        sys.exit(1)

    for script in script_files:
        try:
            # submit jobs w/ sbatch
            result = subprocess.run(['sbatch', script], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print(f"Submitted {script}: {result.stdout.decode().strip()}")
        except subprocess.CalledProcessError as e:
            print(f"Error submitting {script}: {e.stderr.decode().strip()}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python submit_jobs.py <input_folder>")
        sys.exit(1)
    
    input_folder = sys.argv[1]
    submit_jobs(input_folder)
