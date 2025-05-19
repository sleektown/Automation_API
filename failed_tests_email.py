# import os
# import smtplib
# from email.message import EmailMessage
# from bs4 import BeautifulSoup

# # --- CONFIGURE THIS ---
# REPORT_PATH = "C:\\Users\\ANUBHAV GUPTA\\.jenkins\\workspace\\Automtion_API\\report.html"
# EMAIL_SUBJECT = "❌ Pytest Failures Detected in Jenkins Build"
# EMAIL_FROM = "anubhavg713@gmail.com"
# EMAIL_TO = "agwss382512@gmail.com"
# SMTP_SERVER = "smtp.gmail.com"
# SMTP_PORT = 465
# SMTP_USER = "anubhavg713@gmail.com"
# SMTP_PASSWORD = "vkwx xran zbpw aghw"  # App password if using Gmail
# # -----------------------

# def has_failed_tests(report_path):
#     with open(report_path, "r", encoding="utf-8") as file:
#         soup = BeautifulSoup(file, "html.parser")
#         summary = soup.find("div", class_="summary")
#         if summary and "Failed" in summary.text:
#             for part in summary.text.split(","):
#                 if "Failed" in part:
#                     failed_count = int(part.strip().split()[0])
#                     return failed_count > 0
#     return False

# def send_email():
#     msg = EmailMessage()
#     msg["Subject"] = EMAIL_SUBJECT
#     msg["From"] = EMAIL_FROM
#     msg["To"] = EMAIL_TO
#     msg.set_content("One or more tests failed. Please find the attached pytest HTML report.")

#     with open(REPORT_PATH, "rb") as f:
#         file_data = f.read()
#         msg.add_attachment(file_data, maintype="text", subtype="html", filename="report.html")

#     with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
#         smtp.starttls()
#         smtp.login(SMTP_USER, SMTP_PASSWORD)
#         smtp.send_message(msg)

# if __name__ == "__main__":
#     if has_failed_tests(REPORT_PATH):
#         print("❌ Tests failed. Emailing report...")
#         send_email()
#     else:
#         print("✅ All tests passed. No email sent.")



# import os
# import smtplib
# from email.message import EmailMessage
# from bs4 import BeautifulSoup

# # Path to the HTML report
# report_path = "report.html"

# # Read and parse the report
# with open(report_path, "r", encoding="utf-8") as f:
#     soup = BeautifulSoup(f, "html.parser")

# # Find summary text
# summary_text = soup.find("div", class_="summary").text

# # Check if there are failed tests
# if "Failed" in summary_text and not summary_text.startswith("0 Failed"):
#     print("[INFO] Test failure detected. Sending email...")

#     # Email details
#     sender_email = "anubhavg713@gmail.com"
#     sender_password = "vkwx xran zbpw aghw"
#     recipient_email = "agwss382512@gmail.com"
#     subject = "❌ Pytest Report - Test Failures Detected"
#     body = f"The following test failures were found:\n\n{summary_text.strip()}"

#     # Compose the email
#     msg = EmailMessage()
#     msg["From"] = sender_email
#     msg["To"] = recipient_email
#     msg["Subject"] = subject
#     msg.set_content(body)

#     # Attach report
#     with open(report_path, "rb") as f:
#         report_data = f.read()
#         msg.add_attachment(report_data, maintype="text", subtype="html", filename="report.html")

#     # Send via Gmail SMTP (or change as needed)
#     try:
#         with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
#             smtp.login(sender_email, sender_password)
#             smtp.send_message(msg)
#             print("[INFO] Email sent successfully.")
#     except Exception as e:
#         print(f"[ERROR] Failed to send email: {e}")
# else:
#     print("[INFO] No test failures found. Email not sent.")


import smtplib
import os
import re
from bs4 import BeautifulSoup
from email.message import EmailMessage
from email.utils import make_msgid

# Path to the pytest HTML report
report_file = "report.html"

# Ensure the file exists
if not os.path.exists(report_file):
    print("[ERROR] HTML report not found.")
    exit(1)

# Read and parse the HTML report
with open(report_file, "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

# Extract summary section
summary_div = soup.find("div", class_="summary")
if not summary_div:
    print("[ERROR] Could not find summary section in report.")
    exit(1)

summary_text = summary_div.get_text()

# Extract number of failed tests using regex
match = re.search(r"(\d+)\s+Failed", summary_text)
failed_count = int(match.group(1)) if match else 0

# Proceed only if there's a failed test
if failed_count > 0:
    print(f"[INFO] Detected {failed_count} failed test(s). Sending email...")

    # Set up email
    msg = EmailMessage()
    msg["Subject"] = "⚠️ Pytest Report - Test Failures Detected"
    msg["From"] = "anubhavg713@gmail.com"
    msg["To"] = "agwss382512@gmail.com"

    # Embed HTML summary inline
    cid = make_msgid()
    msg.set_content("Some tests have failed. Please see the attached report.")
    msg.add_alternative(f"""
        <html>
            <body>
                <p>Dear Anubhav,</p>
                <p>The following test failures were detected:</p>
                <pre>{summary_text}</pre>
                <p>See attached HTML report for full details.</p>
            </body>
        </html>
    """, subtype='html')

    # Attach the HTML report
    with open(report_file, "rb") as f:
        report_data = f.read()
        msg.add_attachment(report_data, maintype="text", subtype="html", filename="report.html")

    # SMTP configuration (Gmail example)
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.starttls()
            smtp.login("anubhavg713@gmail.com", "vkwx xran zbpw aghw")  # Use an app-specific password
            smtp.send_message(msg)
            print("[INFO] Email sent successfully.")
    except Exception as e:
        print(f"[ERROR] Failed to send email: {e}")

else:
    print("[INFO] No test failures found. Email not sent.")
