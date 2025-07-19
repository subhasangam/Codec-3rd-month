from analyzer.static_analysis import run_static_analysis
from analyzer.dynamic_analysis import run_dynamic_analysis
from analyzer.network_monitor import monitor_traffic
from utils.report_generator import generate_report

APK_PATH = "test_apks/sample.apk"

def main():
    print("[*] Starting Mobile Security Analysis Framework...")

    static_results = run_static_analysis(APK_PATH)
    dynamic_results = run_dynamic_analysis(APK_PATH)
    network_results = monitor_traffic(APK_PATH)

    generate_report(static_results, dynamic_results, network_results)
    print("[+] Security Analysis Complete. Report generated.")

if __name__ == "__main__":
    main()
