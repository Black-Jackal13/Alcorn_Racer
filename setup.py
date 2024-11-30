import subprocess
import sys


def install_requirements(file_name):
    try:
        with open(file_name, 'r') as file:
            packages = file.readlines()
            packages = [pkg.strip() for pkg in packages if pkg.strip() and not pkg.startswith('#')]

            if packages:
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'])  # Upgrade pip first
                subprocess.check_call([sys.executable, '-m', 'pip', 'install'] + packages)
                print("All packages installed successfully.")
            else:
                print(f"No packages found in {file_name}.")
    except FileNotFoundError:
        print(f"File {file_name} not found.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred during the installation process: {e}")


if __name__ == "__main__":
    install_requirements("requirements.txt")
