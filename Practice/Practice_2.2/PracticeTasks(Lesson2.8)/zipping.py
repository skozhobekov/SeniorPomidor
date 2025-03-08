import zipfile

your_name = "Sanjar"


file_paths = [
    "basic_info.py",
    "user_profile.py",
    "testCaseStats.py",
    "bug_reports.py",
    "bug_details.py",
    "bug_filter.py",
    "script_analysis.txt",
    "data_types.txt",
    "discount_calculator.py",
    "list_vs_tuple.py",
    "log_processing.py",
    "testBugTracker.py",
    "testCaseValidation.py",
]

archive_name = f"homework_fullstack_basics_{your_name}.zip"


with zipfile.ZipFile(archive_name, "w") as archive:
    for file_path in file_paths:
        archive.write(file_path, arcname=file_path)

print(f"Архив {archive_name} успешно создан!")
