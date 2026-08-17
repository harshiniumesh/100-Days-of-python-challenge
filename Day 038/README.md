# Day 038 - Workout Tracking Using Google Sheets

## Concepts Practised
* Natural Language Processing with Nutritionix API
* Parsing Natural Language Exercise Queries (e.g., "Ran 3 miles and walked 2 km")
* Authenticating & Writing Data to Google Sheets using Sheety API
* Securing API Credentials with Environment Variables & Basic/Bearer Authentication
* Generating Structured Timestamps & Activity Logs via `datetime`

---

## Output Preview

```text
==================================================
     W O R K O U T   T R A C K E R   A P P        
==================================================

Tell me which exercises you did: ran 5k and walked 20 mins

Parsing exercise data with Nutritionix API...
Detected Exercises:
  - Running: 31.0 mins | 350.5 kcal
  - Walking: 20.0 mins | 75.2 kcal

Connecting to Sheety API...
Posting to Google Sheet (My Workouts):
  [✓] 17/08/2026 | 13:54:37 | Running | 31.0 mins | 350.5 kcal
  [✓] 17/08/2026 | 13:54:37 | Walking | 20.0 mins | 75.2 kcal

--------------------------------------------------
Status: Rows added to Google Sheets successfully! 🏃‍♀️
==================================================
> █