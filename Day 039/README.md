# Day 039 - Capstone Part 1: Flight Deal Finder

## Concepts Practised
* Structuring Modular Python Programs using OOP (Model-View-Controller)
* Fetching & Updating Google Sheets Data via Sheety API
* Querying Flight Search Endpoints & IATA Codes via Flight Search APIs (Tequila/Amadeus)
* Implementing Price Comparison & Threshold Alert Logic
* Dispatching Low-Fare Deal Alerts via SMS (Twilio API)

---

## Output Preview

```text
==================================================
     F L I G H T   D E A L   F I N D E R          
==================================================

Loading destinations from Google Sheet...
Destination list: [Paris, Frankfurt, Tokyo, Sydney, Istanbul, New York]

Checking IATA codes:
  - Paris -> PAR
  - Frankfurt -> FRA
  - Tokyo -> TYO
  - Sydney -> SYD
  - Istanbul -> IST
  - New York -> NYC

Searching flights from London (LON) within next 6 months...

[!] DEAL FOUND:
    London (LON) -> Paris (PAR)
    Price: £38 (Target: £55)
    Dates: 2026-09-12 to 2026-09-19

Connecting to Twilio Client...
Sending SMS alert: "Low price alert! Only £38 to fly from London-LON to Paris-PAR..."
--------------------------------------------------
Status: Flight deals evaluated & alerts sent! ✈️
==================================================
> █