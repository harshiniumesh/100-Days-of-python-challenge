# Day 037 - Habit Tracking Project: API Post Requests & Headers

## Concepts Practised
* Advanced HTTP Methods: `POST`, `PUT`, and `DELETE`
* Securing API Credentials with HTTP Header Authentication (`headers={"X-USER-TOKEN": TOKEN}`)
* Formatting Dates using `strftime()` (e.g., `YYYYMMDD`)
* Visualizing Data on the Pixela API Platform
* Updating and Deleting Existing Data Points via API Endpoints

---

## Output Preview

```text
==================================================
       H A B I T   T R A C K I N G   A P P        
==================================================

Target Graph: graph1 (Coding Tracker)
Date: 20260817
Quantity: 4.5 hours

Sending HTTP POST request with headers...
Response Code: 200
Response Body: {"message":"Success.","isSuccess":true}

--------------------------------------------------
View your updated habit graph at:
[https://pixe.la/v1/users/harshini/graphs/graph1.html](https://pixe.la/v1/users/harshini/graphs/graph1.html)
==================================================
> █