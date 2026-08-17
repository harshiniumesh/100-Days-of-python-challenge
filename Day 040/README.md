# Day 040 - Capstone Part 2: Flight Club

## Concepts Practised
* Managing Customer Profiles & Storing User Emails via Sheety API
* Handling Stopovers & Multi-Leg Flight Searches (Tequila/Amadeus API)
* Exception Handling for Non-Direct Flights & Edge Cases
* Automated Bulk Email Notifications to Subscribers (`smtplib`)
* Generating & Formatting Direct Flight Booking Deep Links

---

## Output Preview

```text
==================================================
           F L I G H T   C L U B                  
==================================================

Welcome to Flight Club!
We find the best flight deals and email them to you.

What is your first name? Jane
What is your last name? Doe
What is your email? jane@example.com
Type your email again: jane@example.com
You're in the club!

Fetching member list from Google Sheets...
Found 12 subscribers.

Searching flights from London (LON)...
[!] DEAL FOUND with 1 stopover:
    London (LON) -> Tokyo (TYO)
    Price: £390 (Target: £500)
    Dates: 2026-10-05 to 2026-10-20
    Route: London (STN) -> Frankfurt (FRA) -> Tokyo (HND)

Connecting to SMTP Server...
Broadcasting deal to 12 members...
  [✓] Sent to: jane@example.com
  [✓] Sent to: john@example.com
--------------------------------------------------
Status: Club emails dispatched successfully! ✈️✉️
==================================================
> █