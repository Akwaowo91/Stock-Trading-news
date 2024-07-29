##  📖 Table Of Contents
- About
- How to Build
- Documentation
- Code explanation
    - Enviromental Variable
    - Api Endpoint 
- Feedback and Contributions
- Contacts

## 🚀 About
**Stock Trading news** This project is a Python script that monitors the stock price of a specified company (Tesla Inc. in this case). When the stock price changes by a specified percentage, the script retrieves the latest news articles related to the company and sends an SMS alert with the news headlines using the Twilio API.

## 📝 How to Build
**Prerequisites**
  - Python 3.x
  - requests library
  - Twilio

  **To build the project follow these steps:**
  - **installation:**

```shell
# Open a terminal (Command Prompt or PowerShell for Windows, Terminal for macOS or Linux)

# Ensure Git is installed
# Visit https://git-scm.com to download and install console Git if not already installed
            
# Clone the repository
git clone https://github.com/Akwaowo91/Stock-Trading-news.git
cd Stock-Trading-news       

# Install the required package
pip install Twilio
pip install requests

```
  - **Running The Script:**
    ```shell
    python stock_news_alert.py
    ```
    - Input your exercise:
        - When prompted, type the exercise you did (e.g., "ran 3 miles").
    - View the result:
        - The script will fetch the exercise details from the Nutritionix API and log them into the specified Google Sheet.
    
  - **Documentation:**
      - Twilio: https://www.twilio.com/docs
      - Request: https://requests.readthedocs.io/en/latest/
   
## 📄 Code Explanation
  - **Environmnet Variable**
      - The following environment variables must be set for the script to function correctly:
          - TWILIO_ACCOUNT_SID: Your Twilio Account SID.
          - TWILIO_AUTH_TOKEN: Your Twilio Auth Token.
          - stock_api_key: Your Alpha Vantage API Key.
          - news_api_key: Your NewsAPI Key.
          - ADD_ROW_ENDPOINT: The Sheety API endpoint for adding rows to your Google Sheet.
          - TOKEN: The Bearer Token for the Sheety API.
    - Example .env File:
       ```shell
       APP_ID=your_nutritionix_app_id
       API_KEY=your_nutritionix_api_key
       ADD_ROW_ENDPOINT=https://api.sheety.co/your_endpoint
       TOKEN=your_sheety_bearer_token
       ```
  - **API Endpoints**
      - Alpha Vantage Stock API Endpoint:
          - URL: https://www.alphavantage.co/query
          - Method: GET
          - Parameters:
              - function: "TIME_SERIES_DAILY"
              - symbol: The stock symbol (e.g., "TSLA" for Tesla).
              - apikey: Your Alpha Vantage API Key.
           
  - **NewsAPI Endpoint**
      - URL: https://newsapi.org/v2/everything
      - Method: GET
      - Parameters:
          - q: The company name (e.g., "Tesla Inc").
          - sortBy: "popularity"
          - apikey: Your NewsAPI Key.
        
## 🤝 Feedback and Contributions
I have made every effort to implement all the main aspects of the Stock Trading Capstone project in the best possible way. However, the development journey doesn't end here, and your input is crucial for our continuous improvement.

> [!IMPORTANT]
> Whether you have feedback on features, have encountered any bugs, or have suggestions for enhancements, we're eager to hear from you. Your insights help us make the Stock Trading Capstone project more robust and user-friendly.

Please feel free to submit an issue or open an issue on this repository, if you have any feedback or suggestions.
Contributions are welcome! Please fork this repository and submit a pull request for any improvements or new features.
I appreciate your support and look forward to making this product even better with your help!

## ©️ Contact
For more questions you can reach me through:  
- email: akwaowoudokop15@gmail.com
- LinkedIn: https://www.linkedin.com/in/akwaowo-udokop-474662229/
