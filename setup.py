import subprocess
import sys

def install_requirements():
    try:
        # Check if pip is installed
        subprocess.check_call([sys.executable, '-m', 'pip', '--version'])

        # Install requirements
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])

        print("Requirements installed successfully")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install requirements: {e}")