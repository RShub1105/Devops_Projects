import subprocess
import platform
import shutil

SERVICE = "nginx"

def service_restater_mac(service):
    """Checks and restarts a Homebrew service on macOS."""
    try:
        # Dynamically find brew in PATH
        brew_path = shutil.which("brew")
        if not brew_path:
            print("❌ Error: 'brew' command not found. Is Homebrew installed and in your PATH?")
            return

        # Get the list of all brew services and their statuses
        result = subprocess.run(
            [brew_path, "services", "list"],
            capture_output=True,
            text=True,
            check=True
        )
        
        # Find the line corresponding to our service
        service_line = ""
        for line in result.stdout.splitlines():
            if line.startswith(service):
                service_line = line
                break
        
        # Check if the service is running ('started')
        if "started" in service_line:
            print(f"✅ {service} is running fine.")
        else:
            print(f"⚠️ {service} is stopped or not found! Restarting...")
            # Restart the service using brew
            subprocess.run([brew_path, "services", "restart", service])
            print(f"🚀 {service} restarted.")

    except subprocess.CalledProcessError as e:
        print(f"❌ Brew command failed: {e}")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")

# Check that we are on macOS before running
if platform.system() == "Darwin":
    service_restater_mac(SERVICE)
else:
    print("This script is designed to run on macOS.")
