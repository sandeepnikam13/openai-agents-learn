
from agents import Agent, function_tool
import os
from dotenv import load_dotenv

load_dotenv()




@function_tool(name_override="FD rates repo")
def bankFDRates() :
    return {
        "currency": "INR",
        "data_as_of": "June 2026",
        "interest_rate_range": {
            "regular_min": "2.50%",
            "regular_max": "8.10%",
            "senior_citizen_bonus": "0.50% - 0.75%"
        },
        "major_banks": [
            {
            "bank_name": "State Bank of India (SBI)",
            "type": "Public Sector",
            "rates": {
                "1_year": "6.25%",
                "3_year": "6.30%",
                "5_year": "6.05%",
                "max_senior_citizen": "7.05%"
            }
            },
            {
            "bank_name": "Bank of Baroda",
            "type": "Public Sector",
            "rates": {
                "1_year": "6.25%",
                "3_year": "6.25%",
                "5_year": "6.30%",
                "max_senior_citizen": "7.00%"
            }
            },
            {
            "bank_name": "HDFC Bank",
            "type": "Private Sector",
            "rates": {
                "1_year": "6.25%",
                "3_year": "6.45%",
                "5_year": "6.40%",
                "max_senior_citizen": "6.95%"
            }
            },
            {
            "bank_name": "ICICI Bank",
            "type": "Private Sector",
            "rates": {
                "1_year": "6.25%",
                "3_year": "6.45%",
                "5_year": "6.50%",
                "max_senior_citizen": "7.10%"
            }
            },
            {
            "bank_name": "IDFC FIRST Bank",
            "type": "Private Sector",
            "rates": {
                "1_year": "6.50%",
                "3_year": "7.25%",
                "5_year": "7.15%",
                "max_senior_citizen": "7.50%"
            }
            }
        ],
        "small_finance_banks": [
            {
            "bank_name": "Utkarsh Small Finance Bank",
            "max_rate_regular": "8.10%",
            "max_rate_senior_citizen": "8.60%"
            },
            {
            "bank_name": "Suryoday Small Finance Bank",
            "max_rate_regular": "8.10%",
            "max_rate_senior_citizen": "8.30%"
            },
            {
            "bank_name": "Unity Small Finance Bank",
            "max_rate_regular": "7.50%",
            "max_rate_senior_citizen": "9.50%"
            }
        ]
    }
 

@function_tool(name_override="Home loan interest rates repo")
def bankHomeLoanInterestRates() :
    return {
        "currency": "INR",
        "data_as_of": "June 2026",
        "rate_type": "Floating",
        "major_banks": [
            {
            "bank_name": "State Bank of India (SBI)",
            "type": "Public Sector",
            "starting_rate_best_cibil": "7.25% p.a.",
            "standard_rate_range": "7.50% - 8.70% p.a."
            },
            {
            "bank_name": "Bank of Baroda",
            "type": "Public Sector",
            "starting_rate_best_cibil": "7.20% p.a.",
            "standard_rate_range": "7.20% - 8.95% p.a."
            },
            {
            "bank_name": "HDFC Bank",
            "type": "Private Sector",
            "starting_rate_best_cibil": "7.75% p.a.",
            "standard_rate_range": "7.75% - 13.20% p.a."
            },
            {
            "bank_name": "ICICI Bank",
            "type": "Private Sector",
            "starting_rate_best_cibil": "7.45% p.a.",
            "standard_rate_range": "8.50% - 9.80% p.a."
            },
            {
            "bank_name": "IDFC FIRST Bank",
            "type": "Private Sector",
            "starting_rate_best_cibil": "7.75% p.a.",
            "standard_rate_range": "8.85% p.a. onwards"
            }
        ],
        "small_finance_banks_range": {
            "typical_starting_rate": "9.50% p.a.",
            "typical_max_rate": "14.00% p.a.",
            "note": "Includes Utkarsh, Suryoday, and Unity Small Finance Bank depending on asset risk assessment."
        }
    }


bank_agent = Agent(
    name = "tool_calling_agent",
    instructions = "a simple bank data provider agent, do not provide any analysis, " \
        "just call the tools and share data, if data not avaiable say so politely, respone should not be more than data asked",
    model = os.getenv("MODEL_NAME"),
    tools = [bankFDRates, bankHomeLoanInterestRates]
)
