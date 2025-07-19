def generate_report(static, dynamic, network):
    with open("output_reports/sample_report.html", "w") as f:
        f.write("<h1>Mobile App Security Report</h1>")
        f.write("<h2>Static Analysis</h2>")
        f.write(str(static))
        f.write("<h2>Dynamic Analysis</h2>")
        f.write(str(dynamic))
        f.write("<h2>Network Analysis</h2>")
        f.write(str(network))
    print("[+] Report saved as 'sample_report.html'")
