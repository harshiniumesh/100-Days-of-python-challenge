# Day 033 - API Endpoints & API Parameters: ISS Overhead Notifier

## Concepts Practised
* Application Programming Interfaces (APIs) & Endpoints
* HTTP Status Codes (`200 OK`, `404 Not Found`, `401 Unauthorized`)
* Making HTTP GET Requests using the `requests` Module
* Parsing JSON Data Payloads
* Passing Parameters to APIs (Sunrise-Sunset API)
* Combining API Polling with Email Notifications (`smtplib`)

---

## Output Preview

```text
==================================================
      I S S   O V E R H E A D   N O T I F I E R   
==================================================

Current Coordinates: Lat 12.9716, Lng 77.5946
Fetching ISS Position...
  - ISS Latitude:  13.1024
  - ISS Longitude: 77.4812

Distance Check: ISS is overhead! (Within ±5 degrees)
Sun Position: It is currently dark outside.

Connecting to SMTP Server...
Sending notification email: "Look up! The ISS is passing above."
--------------------------------------------------
Status: Alert email dispatched successfully! 🛰️
==================================================
> █