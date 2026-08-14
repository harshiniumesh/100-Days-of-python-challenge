# Day 032 - Send Email (smtplib) & Manage Dates (datetime)

## Concepts Practised
* Email Automation with Python's Built-in `smtplib`
* Working with Dates, Times & Timestamps (`datetime` module)
* Parsing CSV Data to Match Current Dates (`pandas`)
* Dynamic Template String Replacement (`[NAME]`)
* Cloud Scheduling & Automation (PythonAnywhere / Cron jobs)

---

## Output Preview

```text
==================================================
   A U T O M A T E D   B I R T H D A Y   W I S H E R
==================================================

Today's Date: 2026-08-14
Checking birthdays.csv...

Match Found:
  - Name: Alex Doe
  - Email: alex@example.com
  - Birthday: 08/14

Generating letter from: letter_templates/letter_2.txt
Connecting to SMTP server (smtp.gmail.com:587)...
TLS Connection secured.
Login successful.

Sending email to alex@example.com...
--------------------------------------------------
Status: Birthday email dispatched successfully! 🎉
==================================================
> █