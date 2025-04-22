import decimal
import json

# Define the credit card fees and rates data
# This dictionary holds all the structured information about fees and rates.
credit_card_fees_and_rates = {
    "effective_date": "2024-12-01",
    "interest_and_charges": [
        {
            "item": 1,
            "type": "Annualised Percentage Rate (APR) for Retail Purchase / Finance charge for purchase",
            "card_type": "All Credit Cards",
            "description": {
                "apr": decimal.Decimal("35.70"),
                "daily_rate": decimal.Decimal("0.0914"),
                "notes": "When you open your account and it will be reviewed from time to time. Interest free if balance paid in full by due date. Otherwise, interest charged daily on unpaid balance from previous statement date and on new transactions from transaction date."
            }
        },
        {
            "item": 2,
            "type": "APR for Cash Advance / Finance charge for Cash Advance",
            "card_type": "All Credit Cards (not applicable to Smart Credit Card)",
            "description": {
                "apr": decimal.Decimal("35.93"),
                "daily_rate": decimal.Decimal("0.0847"),
                "notes": "When you open your account and it will be reviewed from time to time. Interest charged daily from transaction date until payment in full."
            }
        },
        {
            "item": 2,
            "type": "APR for Cash Advance / Finance charge for Cash Advance",
            "card_type": "Smart Credit Card",
            "description": {
                "apr": decimal.Decimal("34.11"),
                "daily_rate": decimal.Decimal("0.0847"),
                "notes": "When you open your account and it will be reviewed from time to time. Interest charged daily from transaction date until payment in full."
            }
        },
        {
            "item": 3,
            "type": "Delinquent APR / Default rate",
            "card_type": "All Credit Cards",
            "description": "Waived"
        },
        {
            "item": 4,
            "type": "Interest Free Period",
            "card_type": "Standard Chartered Credit Card",
            "description": "Up to 56 days"
        },
        {
            "item": 4,
            "type": "Interest Free Period",
            "card_type": "MANHATTAN Credit Card",
            "description": "Up to 59 days"
        },
        {
            "item": 5,
            "type": "Minimum Payment / Minimum Payment Due",
            "card_type": "All Credit Cards",
            "description": "All interest, fees, charges (including Annual Fee(s)), the total of the overlimit amount and/or the overdue amount (where applicable) that may be charged, plus 1% of outstanding principal or HK$/CNY220, whichever is higher."
        }
    ],
    "fees": [
        {
            "item": 6,
            "type": "Annual Membership Fee / Annual Fee / Annual Fee Anniversary (charge per card on annual basis)",
            "card_type": "Classic Credit Card / executive Credit Card / Shop’n Gain Credit Card",
            "description": {
                "principal_card": "HK$250",
                "supplementary_card": "HK$125"
            }
        },
        {
            "item": 6,
            "type": "Annual Membership Fee / Annual Fee / Annual Fee Anniversary (charge per card on annual basis)",
            "card_type": "Gold Credit Card",
            "description": {
                "principal_card": "HK$550",
                "supplementary_card": "HK$275"
            }
        },
        {
            "item": 6,
            "type": "Annual Membership Fee / Annual Fee / Annual Fee Anniversary (charge per card on annual basis)",
            "card_type": "Titanium Credit Card",
            "description": {
                "principal_card": "HK$600",
                "supplementary_card": "HK$300"
            }
        },
        {
            "item": 6,
            "type": "Annual Membership Fee / Annual Fee / Annual Fee Anniversary (charge per card on annual basis)",
            "card_type": "Platinum Credit Card / executive platinum Credit Card / Preferred Banking Credit Card / UnionPay Dual Currency Platinum Credit Card / Shop’n Gain Platinum Credit Card",
            "description": {
                "principal_card": "HK$1,800",
                "supplementary_card": "Waived"
            }
        },
        {
            "item": 6,
            "type": "Annual Membership Fee / Annual Fee / Annual Fee Anniversary (charge per card on annual basis)",
            "card_type": "Corporate Credit Card / Visa Signature Business Card",
            "description": {
                "principal_card": "HK$1,800",
                "supplementary_card": "N/A"
            }
        },
         {
            "item": 6,
            "type": "Annual Membership Fee / Annual Fee / Annual Fee Anniversary (charge per card on annual basis)",
            "card_type": "Priority Banking Credit Card",
            "description": {
                "principal_card": "HK$2,400",
                "supplementary_card": "Waived" # Note 6: Free for up to 3, subsequent HK$1,200
            }
        },
        {
            "item": 6,
            "type": "Annual Membership Fee / Annual Fee / Annual Fee Anniversary (charge per card on annual basis)",
            "card_type": "Visa Infinite Card",
            "description": {
                "principal_card": "HK$6,000",
                "supplementary_card": "Waived"
            }
        },
        {
            "item": 6,
            "type": "Annual Membership Fee / Annual Fee / Annual Fee Anniversary (charge per card on annual basis)",
            "card_type": "Smart Credit Card",
            "description": {
                "principal_card": "Waived",
                "supplementary_card": "Waived"
            }
        },
         {
            "item": 6,
            "type": "Annual Membership Fee / Annual Fee / Annual Fee Anniversary (charge per card on annual basis)",
            "card_type": "Cathay Mastercard",
            "description": {
                "principal_card": "HK$2,000",
                "supplementary_card": "Waived"
            }
        },
         {
            "item": 6,
            "type": "Annual Membership Fee / Annual Fee / Annual Fee Anniversary (charge per card on annual basis)",
            "card_type": "Cathay Mastercard – Priority Banking",
            "description": {
                "principal_card": "HK$4,000",
                "supplementary_card": "Waived"
            }
        },
         {
            "item": 6,
            "type": "Annual Membership Fee / Annual Fee / Annual Fee Anniversary (charge per card on annual basis)",
            "card_type": "Cathay Mastercard – Priority Private",
            "description": {
                "principal_card": "HK$8,000",
                "supplementary_card": "Waived"
            }
        },
         {
            "item": 6,
            "type": "Annual Membership Fee / Annual Fee / Annual Fee Anniversary (charge per card on annual basis)",
            "card_type": "Simply Cash Visa Card",
            "description": {
                "principal_card": "HK$2,000",
                "supplementary_card": "Waived"
            }
        },
         {
            "item": 6,
            "type": "Annual Membership Fee / Annual Fee / Annual Fee Anniversary (charge per card on annual basis)",
            "card_type": "MANHATTAN Platinum Credit Card",
            "description": {
                "principal_card": "HK$1,800",
                "supplementary_card": "HK$900"
            }
        },
         {
            "item": 6,
            "type": "Annual Membership Fee / Annual Fee / Annual Fee Anniversary (charge per card on annual basis)",
            "card_type": "MANHATTAN Titanium / Gold Credit Card",
            "description": {
                "principal_card": "HK$600",
                "supplementary_card": "HK$300"
            }
        },
         {
            "item": 6,
            "type": "Annual Membership Fee / Annual Fee / Annual Fee Anniversary (charge per card on annual basis)",
            "card_type": "MANHATTAN 21 / Infinity Credit Card",
            "description": {
                "principal_card": "HK$330",
                "supplement_card": "HK$160"
            }
        },
        {
            "item": 6,
            "type": "Annual Membership Fee / Annual Fee / Annual Fee Anniversary (charge per card on annual basis)",
            "card_type": "MANHATTAN Visa",
            "description": {
                "principal_card": "HK$216",
                "supplementary_card": "HK$108"
            }
        },
        {
            "item": 7,
            "type": "Reduced Annual Fee on any subsequent Standard Chartered Credit Card sharing a combined credit limit (Principal Card only)",
            "card_type": "Classic Credit Card",
            "description": "HK$125"
        },
        {
            "item": 7,
            "type": "Reduced Annual Fee on any subsequent Standard Chartered Credit Card sharing a combined credit limit (Principal Card only)",
            "card_type": "Gold Credit Card (not applicable to Platinum / Co-branded)",
            "description": "HK$275"
        },
        {
            "item": 8,
            "type": "Cash Advance / Cash Advance Fee",
            "card_type": "Corporate Credit Card",
            "description": "3% of the cash advance amount per transaction (minimum HK$55), over the counter or via Jetco ATM, Visa ATM Network."
        },
        {
            "item": 8,
            "type": "Cash Advance / Cash Advance Fee",
            "card_type": "UnionPay Dual Currency Platinum Credit Card",
            "description": "3.5% of the cash advance amount per transaction (minimum HK$100), over the counter or via Jetco ATM, UnionPay International ATM Network."
        },
        {
            "item": 8,
            "type": "Cash Advance / Cash Advance Fee",
            "card_type": "Smart Credit Card",
            "description": "Waived, over the counter or via Jetco ATM/ Visa International ATM Network."
        },
         {
            "item": 8,
            "type": "Cash Advance / Cash Advance Fee",
            "card_type": "Other Credit Cards (not applicable to Smart Credit Card)",
            "description": "3.5% of the cash advance amount per transaction (minimum HK$100), over the counter or via Jetco ATM, Visa / Mastercard International ATM Network (as available to the relevant Credit Card type(s))."
        },
        {
            "item": 9,
            "type": "Fees relating to Foreign Currency Transactions / Foreign Currency (Currencies other than Hong Kong Dollars) Transactions incurred in or outside of Hong Kong",
            "card_type": "UnionPay Dual Currency Platinum Credit Card",
            "description": "All settlements in HKD/CNY. Transactions in foreign currency (incl. CNY in China) converted at wholesale market rate + 0.6% UnionPay International reimbursement charge + 0.4% Bank charge (1% total). Exchange rate may differ from transaction date. Except for transactions in Foreign Currency (Currencies other than Hong Kong Dollars) incurred in Hong Kong."
        },
        {
            "item": 9,
            "type": "Fees relating to Foreign Currency Transactions / Foreign Currency (Currencies other than Hong Kong Dollars) Transactions incurred in or outside of Hong Kong",
            "card_type": "Smart Credit Card",
            "description": "Waived. All settlements in HKD. Transactions in foreign currency converted at Visa International wholesale market rate. Exchange rate may differ from transaction date."
        },
        {
            "item": 9,
            "type": "Fees relating to Foreign Currency Transactions / Foreign Currency (Currencies other than Hong Kong Dollars) Transactions incurred in or outside of Hong Kong",
            "card_type": "Visa (not applicable to Smart Credit Card) / Mastercard",
            "description": "All settlements in HKD. Transactions in foreign currency converted at Visa/Mastercard International wholesale market rate + 1% Visa/Mastercard International reimbursement charge + 0.95% Bank charge (1.95% total). Exchange rate may differ from transaction date. Except for transactions in Foreign Currency (Currencies other than Hong Kong Dollars) incurred in Hong Kong."
        },
        {
            "item": 10,
            "type": "Fees relating to Settling Foreign Currency (Currencies other than Hong Kong Dollars) Transaction in Hong Kong Dollars / Transactions in Hong Kong Dollars Incurred Outside of Hong Kong",
            "card_type": "UnionPay Dual Currency Platinum Credit Card",
            "description": "Not Applicable"
        },
        {
            "item": 10,
            "type": "Fees relating to Settling Foreign Currency (Currencies other than Hong Kong Dollars) Transaction in Hong Kong Dollars / Transactions in Hong Kong Dollars Incurred Outside of Hong Kong",
            "card_type": "Smart Credit Card",
            "description": "Waived. Option to settle in HKD overseas may be offered by merchants, ask merchants for rates and handling fees as cost may be higher than foreign currency transaction handling fee. Refer to item 9 if settling in foreign currency."
        },
        {
            "item": 10,
            "type": "Fees relating to Settling Foreign Currency (Currencies other than Hong Kong Dollars) Transaction in Hong Kong Dollars / Transactions in Hong Kong Dollars Incurred Outside of Hong Kong",
            "card_type": "Visa (not applicable to Smart Credit Card) / Mastercard",
            "description": "Visa/Mastercard International imposes 1% reimbursement charge on the Bank for transactions in HKD incurred outside HK or with non-HK registered merchants (e.g. internet), charged by the Bank to customer. Fee applicable to transactions initiated by customer and/or merchant depending on merchant’s setting. Option to settle foreign currency transactions in HKD overseas may be offered by merchants, ask merchants for rates and handling fees as cost may be higher than foreign currency transaction handling fee. Refer to item 9 if choosing to settle foreign currency transactions incurred in or outside of Hong Kong."
        },
        {
            "item": 11,
            "type": "Transactions in CNY Currency",
            "card_type": "UnionPay Dual Currency Platinum Credit Card",
            "description": "All transactions in CNY incurred outside of Hong Kong will not be converted into Hong Kong Dollars. China transactions will be directly posted in terms of CNY currency on CNY credit card account."
        },
        {
            "item": 12,
            "type": "Late Payment Fee / Late Charge (Fail to pay Minimum Payment Due by Payment Due date)",
            "card_type": "Corporate Credit Card",
            "description": "EITHER 5% of the Minimum Payment Due (subject to a minimum cap of HK$220 and a maximum cap of HK$350) OR the Minimum Payment Due, whichever is lower."
        },
        {
            "item": 12,
            "type": "Late Payment Fee / Late Charge (Fail to pay Minimum Payment Due by Payment Due date)",
            "card_type": "Other Credit Cards",
            "description": "EITHER 5% of the Outstanding Balance (subject to a minimum cap of HK$/CNY220 and a maximum cap of HK$/CNY350) OR the Minimum Payment Due, whichever is lower."
        },
        {
            "item": 13,
            "type": "Late Fee (Fail to pay Minimum Payment Due for 3 Consecutive months or more)",
            "card_type": "All Credit Cards",
            "description": "Waived"
        },
        {
            "item": 14,
            "type": "Over-the-limit Fee / Overlimit Charge",
            "card_type": "All Credit Cards (not applicable to Visa Infinite Card and Corporate Credit card)",
            "description": "HK$180 per statement cycle"
        },
         {
            "item": 15,
            "type": "Returned Payment Fee/ Returned Item Fee",
            "card_type": "All Credit Cards",
            "description": "HK$/CNY120 per item"
        },
        {
            "item": 16,
            "type": "360° Rewards Points mileage redemption handling fee",
            "card_type": "All Credit Cards",
            "description": "HK$300 per each redemption"
        },
         {
            "item": 17,
            "type": "Card Replacement Fee",
            "card_type": "All Credit Cards",
            "description": "HK$100 per credit card account"
        },
         {
            "item": 18,
            "type": "Charge for Foreign Currency Cheque Repayment",
            "card_type": "Standard Chartered Credit Card",
            "description": "HK$/CNY100 per cheque"
        },
        {
            "item": 18,
            "type": "Charge for Foreign Currency Cheque Repayment",
            "card_type": "MANHATTAN Credit Card",
            "description": "Minimum HK$15, maximum HK$100 per cheque"
        },
        {
            "item": 19,
            "type": "Sales Draft Retrieval Fee (Photocopy)",
            "card_type": "Standard Chartered Credit Card",
            "description": "HK$40 per copy"
        },
        {
            "item": 19,
            "type": "Sales Draft Retrieval Fee (Photocopy)",
            "card_type": "MANHATTAN Credit Card",
            "description": "HK$50 per copy"
        },
         {
            "item": 20,
            "type": "Sales Draft Retrieval Fee (Original copy)",
            "card_type": "All Credit Cards",
            "description": "HK$70 per copy"
        },
         {
            "item": 21,
            "type": "Statement Retrieval Fee",
            "card_type": "Corporate Credit Card",
            "description": "HK$30 per statement issued within the latest 2 months (photocopy), HK$50 per statement issued beyond the latest 2 months (photocopy)"
        },
        {
            "item": 21,
            "type": "Statement Retrieval Fee",
            "card_type": "Other Credit Cards",
            "description": "HK$50 per copy*. *Waiver for eStatement registered customers (up to 6 copies per request for past 7 years) except for Standard Chartered SHOP’n GAIN/SHOP’n GAIN Platinum Credit Card, and designated Mastercard (card number starting with 5488)."
        },
        {
            "item": 22,
            "type": "Cash Withdrawal Fee (By cheque/cashier order)",
            "card_type": "Standard Chartered Credit Card",
            "description": "HK$/CNY75 per cheque"
        },
        {
            "item": 22,
            "type": "Cash Withdrawal Fee (By cheque/cashier order)",
            "card_type": "MANHATTAN Credit Card",
            "description": "Free if transfer to Standard Chartered account, HK$75 per cheque"
        },
        {
            "item": 23,
            "type": "Over-the-Counter Payment Handling Fee",
            "card_type": "All Credit Cards (not applicable to Priority Banking Credit Card and Visa Infinite Card)",
            "description": "HK$30 per transaction"
        },
         {
            "item": 24,
            "type": "Limit on Cash Advance",
            "card_type": "All Credit Cards",
            "description": "Your Limit on Cash Advance will be reviewed from time to time by the Bank. Your latest Limit on Cash Advance at any relevant time can be ascertained by calling 24-hour Customer Service Hotline."
        },
        {
            "item": 25,
            "type": "Over-limit electronic fund transfer handling fee",
            "card_type": "All Credit Cards",
            "description": "A 3.5% handling fee will apply to the transferred amount beyond HK$25,000 if total accumulated money transfers using electronic banking services, P2P payment services or mobile device/app/electronic funds transfer platform from Standard Chartered/MANHATTAN Credit Card(s) exceed HK$25,000 per Cardholder in a calendar month (based on transaction date). Charges debited to card with highest transferred amount. Specific rules apply for month-end transactions. Customer acknowledges fee in Online Banking/mobile app."
        },
        {
            "item": 26,
            "type": "Paper Statement Fees",
            "card_type": "All Credit Cards except Standard Chartered SHOP’n GAIN Platinum Credit Card, Standard Chartered SHOP’n GAIN Credit Card, Standard Chartered Corporate VISA Card, Standard Chartered Visa Signature Business Card and designated Mastercard (card number starting with 5488)",
            "description": "HK$10 per month, applicable to customers who receive any paper statement(s) (Consolidated Statement, Credit Card Statement, Current/Savings account Statement(s), Standard Chartered Revolving Cash Card Statement(s) AND MANHATTAN Revolving Personal Loan Statement(s)). Fee waived for customers aged below 18 or 65 and above, customers who hold Click-a-Count, and recipients of government disability allowances/allowance for elderlies or Comprehensive Social Security Assistance."
        }
    ]
}


def decimal_serializer(obj):
    """JSON serializer for objects not serializable by default."""
    if isinstance(obj, decimal.Decimal):
        return str(obj)
    # Let the default encoder handle other types
    return json.JSONEncoder().default(obj)

