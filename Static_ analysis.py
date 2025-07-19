import subprocess

def run_static_analysis(apk_path):
    print("[*] Running static analysis using APKTool...")
    subprocess.run(["apktool", "d", apk_path, "-o", "output_apk"], check=True)
    
    # Add custom logic to detect hardcoded credentials, insecure permissions, etc.
    findings = {"insecure_permissions": ["INTERNET", "READ_SMS"]}
    print("[+] Static analysis complete.")
    return findings
