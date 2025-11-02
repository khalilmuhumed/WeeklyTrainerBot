from robocorp.tasks import task
from RPA.Excel.Files import Files
from RPA.FileSystem import FileSystem
from datetime import datetime
import os

DATA_DIR = "data"
OUTPUT_DIR = "output"
RECIPIENTS_FILE = os.path.join(DATA_DIR, "recipients.xlsx")
ATTACHMENT_FILE = os.path.join(DATA_DIR, "training_schedule.pdf")
LOG_FILE = os.path.join(OUTPUT_DIR, "log.txt")

@task
def weekly_trainer_bot():
    """Simulated WeeklyTrainerBot: Reads Excel + PDF, logs actions"""
    ensure_output_folder()
    week_number = get_current_week()
    log(f"🚀 Starting WeeklyTrainerBot for week {week_number}")

    # 1. Read recipients
    recipients = read_recipients(RECIPIENTS_FILE)

    # 2. Validate PDF
    validate_attachment(ATTACHMENT_FILE, week_number)

    # 3. Simulate sending
    simulate_sending(recipients, week_number, ATTACHMENT_FILE)

    log(f"✅ Completed successfully for week {week_number}\n")


def ensure_output_folder():
    """Ensure output folder & log file exist."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w") as f:
            f.write("*** WeeklyTrainerBot Log ***\n")


def get_current_week():
    """Return current ISO week number."""
    return datetime.now().isocalendar().week


def read_recipients(path):
    """Read email list from Excel."""
    if not os.path.exists(path):
        msg = f"⚠️ ERROR: Recipients file missing: {path}"
        log(msg)
        raise FileNotFoundError(msg)

    excel = Files()
    excel.open_workbook(path)
    table = excel.read_worksheet_as_table(header=True)
    excel.close_workbook()

    emails = [row["Email"] for row in table if "Email" in row and row["Email"]]
    if not emails:
        msg = "⚠️ ERROR: No emails found in Excel!"
        log(msg)
        raise ValueError(msg)

    log(f"📄 Recipients loaded: {emails}")
    return emails


def validate_attachment(path, week):
    """Check that the PDF exists."""
    fs = FileSystem()
    if not fs.does_file_exist(path):
        msg = f"❌ PDF missing for week {week}: {path}"
        log(msg)
        raise FileNotFoundError(msg)
    log(f"📎 PDF found for week {week}: {path}")


def simulate_sending(recipients, week, attachment):
    """Simulate sending message instead of real email."""
    subject = f"Weekly Training Schedule – Week {week}"
    body = f"Hello team! Please find attached the training schedule for week {week}."
    log("✉️ Simulating email sending...")
    log(f"To: {recipients}")
    log(f"Subject: {subject}")
    log(f"Attachment: {attachment}")
    log(f"Body: {body}")
    log("📤 (Simulated) Email would be sent successfully.")


def log(message):
    """Write both to console and log.txt"""
    print(message)
    with open(LOG_FILE, "a") as f:
        f.write(f"{message}\n") 