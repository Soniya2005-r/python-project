import os
import importlib.util
from datetime import datetime

def run_all_tests():
    results = []

    for filename in os.listdir("test_cases"):
        if filename.endswith(".py"):
            filepath = os.path.join("test_cases", filename)
            spec = importlib.util.spec_from_file_location(filename[:-3], filepath)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            for name in dir(module):
                if name.startswith("test_"):
                    test_func = getattr(module, name)
                    results.append(test_func())

    return results

def save_report(results):
    report_file = f"reports/test_report_{datetime.today().date()}.txt"
    with open(report_file, "w") as f:
        for case_id, title, result in results:
            f.write(f"{case_id} - {title}: {result}\n")
    print(f"Report saved to {report_file}")

if __name__ == "__main__":
    results = run_all_tests()
    save_report(results)
