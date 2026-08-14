# Day 035 - Keys, Authentication & Environment Variables: Rain Alert App

## Concepts Practised
* API Authentication & Securing Sensitive Data using API Keys
* Hourly Weather Forecast Fetching with OpenWeatherMap API
* Condition Code Slicing (Checking next 12-hour forecast)
* Managing Environment Variables (`os.environ`) for Security
* Sending SMS Notifications via the Twilio API

---

## Output Preview

```text
==================================================
          R A I N   A L E R T   A P P             
==================================================

Fetching 12-hour forecast...
Checking weather condition codes: [800, 800, 500, 502, ...]

Condition Check:
  - Rain detected in the next 12 hours (Code < 700 found: 500).

Connecting to Twilio Client...
Sending SMS notification to registered number...

SMS Sent: "It's going to rain today. Remember to bring an ☔"
--------------------------------------------------
Status: Message sent successfully! (SID: SMxxxxxxxx)
==================================================
> █