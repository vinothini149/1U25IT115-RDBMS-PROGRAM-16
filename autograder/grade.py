import os
import re
import sys

def run_autograder():
    file_path = "student_code.sql"
    
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found.")
        sys.exit(1)

    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    # Clean content (strip single-line and multi-line comments)
    content_clean = re.sub(r'--.*', '', content)
    content_clean = re.sub(r'/\*.*?\*/', '', content_clean, flags=re.DOTALL)
    content_upper = content_clean.upper()

    tests = [
        (
            "TC01 - FOR LOOP is used",
            r"FOR\s+\w+\s+IN\s+.*LOOP"
        ),
        (
            "TC02 - Loop starts from 1",
            r"FOR\s+\w+\s+IN\s+1\s*\.\."
        ),
        (
            "TC03 - Loop ends at 10",
            r"\.\.\s*10\s+LOOP"
        ),
        (
            "TC04 - DBMS_OUTPUT.PUT_LINE is used",
            r"DBMS_OUTPUT\.PUT_LINE\s*\("
        ),
        (
            "TC05 - PL/SQL BEGIN/END block exists",
            r"BEGIN[\s\S]+END\s*;"
        ),
        (
            "TC06 - Numbers are not hard-coded ten times",
            r"DBMS_OUTPUT\.PUT_LINE\s*\(\s*[a-zA-Z_]\w*\s*\)"
        )
    ]

    score = 0
    total = len(tests)

    print("\n--- RUNNING AUTOGRADER ---")
    for name, pattern in tests:
        if re.search(pattern, content_upper, re.IGNORECASE):
            print(f"PASS: {name}")
            score += 1
        else:
            print(f"FAIL: {name}")

    print("-" * 30)
    print(f"TOTAL SCORE: {score}/{total}")
    print("-" * 30)

    if score < total:
        print("AUTOGRADER RESULT: FAIL")
        sys.exit(1)
    else:
        print("AUTOGRADER RESULT: PASS")
        sys.exit(0)

if __name__ == "__main__":
    run_autograder()
