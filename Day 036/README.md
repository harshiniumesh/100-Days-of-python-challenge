# Day 036 - Stock Trading News Alert Project

## Concepts Practised
* Fetching Stock Market Data via Alpha Vantage API
* Calculating Day-over-Day Percentage Change in Stock Closing Prices
* Querying & Filtering Headline News via NewsAPI
* Slicing Top Articles & Dynamic Message Formatting
* Automated SMS Dispatch via Twilio API on Price Volatility

---

## Output Preview

```text
==================================================
   S T O C K   N E W S   A L E R T   A P P        
==================================================

Target Stock: TSLA (Tesla Inc)
Fetching closing prices:
  - Yesterday: $210.50
  - Day Before Yesterday: $200.00
Price Difference: +$10.50 (+5.25% 🔺)

Trigger condition met (Difference > 5%)!
Fetching top 3 news articles...

Connecting to Twilio Client...
Sending SMS 1/3:
  TSLA: 🔺5%
  Headline: Were Hedge Funds Right About Piling Into Tesla?
  Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds...

Sending SMS 2/3:
  TSLA: 🔺5%
  Headline: Tesla's latest quarterly delivery numbers beat estimates.
  Brief: Tesla shares jumped over 5% following the publication of...

--------------------------------------------------
Status: 3 Alert messages dispatched successfully! 📈
==================================================
> █