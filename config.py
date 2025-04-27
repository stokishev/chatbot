import decimal
import json

# Define the credit card fees and rates data
# This dictionary holds all the structured information about fees and rates.
credit_card_fees_and_rates_structured = {
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


# Function to serialize Decimal objects for JSON
def decimal_serializer(obj):
    """JSON serializer for objects not serializable by default."""
    if isinstance(obj, decimal.Decimal):
        return str(obj) # Convert Decimal to string
    # More robust handling for un-serializable types if needed
    try:
        return json.JSONEncoder().default(obj)
    except TypeError:
        return str(obj) # Fallback to string representation
    
# --- Convert structured data to a plain text format (JSON string) for RAG ---
# Using json.dumps for a structured text representation
fees_data_text = "Credit Card Fees and Rates Information:\n" + json.dumps(
    credit_card_fees_and_rates_structured,
    indent=2,
    default=decimal_serializer # Use the custom serializer
)

# --- New Card Comparison Data as Text ---
card_comparison_text = """
Compare Credit Cards – Standard Chartered HK 
 
1. Smart Card 
Up to 5% CashBack 
Welcome Offer: HKD800 CashBack 
Benefits 
Up to 5% CashBack: CashBack at everyday merchants 
Save 1.95% foreign exchange fees and no cash advance fees 
Annual Fee: No annual fee 
Eligibility 
Hong Kong resident aged 18 or above 
Annual income of HKD96,000 or above 
 
2. Simply Cash 
1.5% Cashback on spending in local currency 
Welcome Offer: HKD600 CashBack 
Benefits 
1.5%: Unlimited CashBack on spending in local currency 
2%: Unlimited CashBack on spending foreign currencies 
Annual Fee: HKD2,000(annual fee waiver in first year) 
Eligibility 
Hong Kong resident aged 18 or above 
Annual income of HKD96,000 or above 
 
3. Cathay Mastercard 
HKD4 = 1 mile on overseas spending 
Welcome Offer: Up to 40,000 Miles 
Benefits 
HKD4 = 1 Asia Mile: Dining, Hotels and Overseas Spending 
HKD6 = 1 Asia Mile: Other HKD Spending 
Annual Fee: HKD2,000(annual fee waiver in first year) 
Eligibility 
Hong Kong resident aged 18 or above 
Annual income of HKD96,000 or above 
Existing Asia Miles Member 
 
4. Cathay Mastercard – Priority Banking 
HKD3 = 1 mile on overseas spending 
Welcome Offer: Up to 100,000 Miles 
Benefits 
4 shareable Cathay Pacific Business Class lounge passes per credit card membership year 
Priority check-in at Premium Economy class counters 
Enjoy same priority boarding line for Premium Economy class passengers 
HKD3 = 1 Asia Mile: Overseas Spending 
HKD4 = 1 Asia Mile: Dining and Hotels Spending 
HKD6 = 1 Asia Mile: Other HKD Spending 
Annual Fee: HKD4,000 
Eligibility 
Hong Kong resident aged 18 or above 
Annual income of HKD96,000 or above 
Existing Asia Miles Member 

5. Cathay Mastercard – Priority Private 
HKD2 = 1 mile on overseas spending 
Welcome Offer: Up to 120,000 Miles 
Benefits 
2 shareable Cathay Pacific First Class lounge passes and 8 shareable Business Class lounge passes per credit card membership year 
Priority check-in at Business class counters 
Enjoy same priority boarding line for Business class passengers 
HKD2 = 1 Asia Mile: Overseas Spending 
HKD4 = 1 Asia Mile: Dining and Hotels Spending 
HKD6 = 1 Asia Mile: Other HKD Spending 
Annual Fee: HKD8,000 
Eligibility 
Hong Kong resident aged 18 or above 
Annual income of HKD96,000 or above 
Existing Asia Miles Member 
 
6. A. Point Card 
0% Taobao Handling Fee Offer 
Welcome Offer: Up to HKD2,000 Welcome Rewards 
Benefits 
0% Taobao Handling Fee Offer 
Annual Fee: No annual fee 
Eligibility 
Hong Kong resident aged 18 or above 
Annual income of HKD96,000 or above 
"""

faq_help_centre_text = """
Credit Cards Help Centre – Standard Chartered HK (https://www.sc.com/hk/help/credit-cards/?intcid=web_listing-sc_com_top_nav-na-staticmedia_others-sng-na-cc_credit_card_help_center-sc_com_organic-hk-en)

Credit Card Transactions FAQs
•	What should I do if there are unauthorised transactions on my credit card account?
Please report these transactions to us immediately. To protect your interests, the related credit card would be immediately deactivated, and a replacement credit card (with a new card number) would be issued to you.
Before initiating dispute request for credit card transactions, please take note of important information such as eligibility and timeline. Learn more (https://www.sc.com/hk/credit-cards/dispute-resolution/)

•	How can I view my credit card transactions?
You can log on to Online Banking or SC Mobile to view your credit card balances.
For Online banking:
1.	Click ‘Overview’ and select credit card you need to view.
2.	View your credit card transactions up to 90 days.
For SC Mobile:
3.	After login to SC Mobile, tap the credit card accounts you wish to view.
4.	View your credit card transactions up to 90 days.
Learn more (https://www.sc.com/hk/bank-with-us/digital-banking/)

•	How can I make bill payments with my credit card?
You can pay bills of selected merchants by credit cards through Online Banking or SC Mobile.
If you pay your bill by Standard Chartered credit card within the month of / one month before the card expiry date shown on the credit card, please activate the renewed Credit Card upon receipt before making payment.

•	Can I use my credit card with FPS?
You can now pay your rent, government bills, education expenses, car park fees and even friends using your credit card as a debit source for FPS.
For SC Mobile:
1.	Choose payee from phone book or enter payee’s mobile number/email/FPS ID.
2.	Choose either payee’s default bank account or specific bank account to send money to.
3.	Select payment by credit card.
4.	Select your preferred credit card.
5.	Confirm transfer amount and payment description (optional), then slide to proceed the transfer.
Please note that handling fees may apply. Learn more (https://www.sc.com/hk/bank-with-us/local-third-party-transfer/)

•	Why does the Bank charge 1% handling fee for DCC transactions when I use HKD to settle payments online?
Visa/Mastercard International will impose a reimbursement charge of 1% on the Bank for transactions in Hong Kong Dollars incurred outside of Hong Kong or with any merchants not registered in Hong Kong (e.g. internet transactions), the same will be charged by the Bank on such transactions on behalf of Visa/Mastercard International.
The fee is applicable to transactions initiated by you and/or the merchant depending on the merchant’s setting. Learn more (https://av.sc.com/hk/content/docs/hk-credit-card-key-facts-statement.pdf)

Credit Card Rewards FAQs
•	What credit card transactions are eligible for earning CashBack?
CashBack is earned in accordance with the relevant terms and conditions under the CashBack Programme for each Qualified CashBack Card. Learn more (https://www.sc.com/hk/credit-cards/360rewards/faq/)
For transactions of each Qualified CashBack Card which will be eligible for CashBack, please refer to reward program terms and conditions for each respective card type. Learn more (https://www.sc.com/hk/credit-cards/)

•	What are the rewards scheme details for different credit cards?
You can refer to the Terms and Conditions for Points Redemption (https://av.sc.com/hk/content/docs/hk-rewards-tncs-en.pdf) and our FAQ page (https://www.sc.com/hk/credit-cards/360rewards/faq/).

Credit Card Repayments FAQs
•	How can I settle my Standard Chartered credit card bills?
The most convenient way to settle your credit card bills is via Online Banking or SC Mobile:
1.	Select “SC Credit Cards” under “Payments”.
2.	Follow the instructions and select the appropriate details such as the credit card account for settlement, the account to debit from and the amount.
3.	Review and confirm the details.
4.	Submit the payment.
You can also pay your credit card bill via Direct Debit Authorization Service, Payment by Phone Service (PPS), and Standard Chartered / JETCO ATMs or Cash and Cheque Deposit Machines. Full details are available on the back of your credit card account statement. Learn more (https://www.sc.com/hk/bank-with-us/services-video/online-banking/credit-card-payment/)

•	How can I transfer out my credit balance if I’ve made excess payment to my credit card or received a merchant refund?
You can utilise your credit balance by selecting your credit card as a debit source for FPS. Learn more (https://www.sc.com/hk/bank-with-us/local-third-party-transfer/)
Alternatively, you can also perform a Credit Balance Transfer via Online banking or SC Mobile. Learn more (https://www.sc.com/hk/help/other-credit-card-services/)

•	Can merchant refund received after my statement date and before my payment due date offset my statement balance?
Merchant refunds are not considered as payments to your card account. Please ensure payments are made to your account by the payment due date which is indicated in your statement, to avoid any late payment fees. If the refund is posted after the issuance of your current month’s statement, the refunded amount will be taken into account in the statement balance of your next statement.

Credit Card Additional Authentication for Online Transactions FAQs
•	Do all the online purchase transactions require additional authentication?
No, only participating online merchants will require additional authentication in order to complete transactions. If you failed to receive the Push Notification via SC Mobile app, an OTP will be sent to the principal/ supplementary cardholder’s valid mobile telephone number via SMS.

•	Does my supplementary cardholder enjoy this service?
Supplementary cardholders can use the same service to proceed the online transaction by inputting the name printed on the supplementary card. By then Supplementary cardholder will be asked to authenticate the transaction via SC Mobile App, or input the OTP which sent to the registered mobile telephone number.

•	What are the benefits of additional authentication?
The additional authentication provides added assurance by authenticating you while using your Standard Chartered Visa Card / Mastercard when making payments to participating online merchants.

•	Do I need to register my Standard Chartered Credit Card to enjoy this service?
No registration is required to enjoy this service. However, this service is only applicable to cardholders who have registered SC Mobile Key in the SC Mobile App or have a local mobile telephone number registered with the bank.
Activate SC Mobile Key in your SC Mobile App Learn more (https://www.sc.com/hk/bank-with-us/sc-mobile-key-howto/)

•	How will I know if I need additional authentication to complete the online purchase transaction?
Look for the Verified by Visa or Mastercard® SecureCode™ or American Express SafeKey mark on participating online stores.

•	Can I enjoy the benefit of this service at online stores that are not participating in the service?
No, but the service has become available to more and more online stores now.

•	What should I do if I do not receive the OTP?
OTP is only applicable to the Principal Cardholder with a valid Hong Kong mobile phone number registered with the credit card system of the Bank. If you do not receive your OTP within 20 seconds after submitting your request, you may click “Resend OTP” to request for another one. You should also check if your mobile phone number registered with the credit card system of the Bank is updated.

•	What happens if I key in a wrong OTP for many times?
You will not be allowed to click “Resend OTP” to request for another one if you have input a wrong OTP for many times. Please restart the entire online purchase transaction again.

•	When does the OTP expire? What should I do if I am not able to confirm the transaction before the OTP expires?
The OTP will only valid for a certain period after it is issued. You can click “Resend OTP” to request for another OTP if the OTP has expired.

Other Credit Card services FAQs
•	What service requests can I apply for online for my credit cards?
We offer a series of services online, designed to make account management easy and frictionless for you. Learn more (https://www.sc.com/hk/bank-with-us/standard-chartered-digital-banking/)

•	How can I link my Standard Chartered banking account to my credit card?
You can apply for ATM facilities on your credit card by submitting the Additional Benefits Form.

•	What are the telephone requirements for receiving one-time passwords (OTP) relating to credit card transactions or authorisations?
A valid mobile telephone number refers to a local Hong Kong 8-digit mobile number, with international mobile telephone numbers excluded. Learn more (https://www.sc.com/hk/credit-cards/secure-online-shopping-otp/)

•	How can I adjust my credit limit?
You can increase credit limit by submitting request online (Learn more (https://www.sc.com/hk/help/other-credit-card-services/)) or adjust your credit limit by submitting the Additional Benefits Form (https://av.sc.com/hk/content/docs/hk-scb-cc-abf.pdf).

•	How can I waive my credit card service charges?
If your credit cards have been charged with annual fees, overlimit charges, late charges or finance charges within the last month, you may submit a waiver request online. Learn more (https://www.sc.com/hk/help/other-credit-card-services/)

•	How can I block my account temporarily?
As an additional security measure, you now have the option to place temporary blocks on your cards and resume usage when desired.
All credit card functions, including online/offline transactions, mobile wallets, and ATM cash withdrawal will be suspended until you initiate an unblock. Pre-authorized transactions, including Octopus AAVS or direct-debit authorization (DDA) set up by merchants will not be impacted by the temporary block. Learn more (https://www.sc.com/hk/help/other-credit-card-services/)

•	My physical credit card has been damaged, how can I obtain a new card?
You can apply for a replacement of your physical credit card by submitting request online (Learn more (https://www.sc.com/hk/help/other-credit-card-services/)) or by submitting the Cancellation or Replacement Request Form (https://av.sc.com/hk/content/docs/hk-scb-cc-cancellation.pdf).

•	How can I cancel my credit card?
We’re sorry to see you go. You can apply for a cancellation of your principal credit card by submitting the Cancellation or Replacement Request Form (https://av.sc.com/hk/content/docs/hk-scb-cc-cancellation.pdf). If you would like to cancel your supplementary card only, please approach one of our branches (https://www.sc.com/hk/atm-branch-locator/) with your physical supplementary credit card.

•	What should I take note of if my credit card gets cancelled?
•	Supplementary cards will be cancelled at the same time
•	Remaining balances for active instalment plans (including interest-free hire purchase, statement balance instalment or dial-a-check) will be accelerated with the remaining outstanding balance to be posted in the next statement
•	Automatic-Add-Value Service (AAVS) can only be cancelled by Octopus, please contact the Octopus Customer Service Hotline at 2266-2222
•	Direct Debit Authorization (DDA) and Payment by Phone Service (PPS) services will be terminated, please contact the service provider for rearrangement
•	Unredeemed rewards will be forfeited
•	Priority Pass services for Visa Infinite and Priority Banking Credit Card cardholders will be terminated
•	eStatements/eAdvices issued previously will no longer be available for access, please download previous eStatements/eAdvices as you see fit or contact us for statement retrieval request
Credit Cards Download Centre – Standard Chartered HK (https://www.sc.com/hk/help/download-centre/credit-cards-forms-and-documents/?intcid=web_listing-sc_com_top_nav-na-staticmedia_others-sng-na-cc_credit_card_form_and_document_download-sc_com_organic-hk-en)
Forms and Documents
Additional Benefits Form [PDF] (https://av.sc.com/hk/content/docs/hk-scb-cc-abf.pdf)
Direct Debit Authorization (for HKD Account) [PDF] (https://av.sc.com/hk/content/docs/hk-scb-mccl-dda-wp-0216.pdf)
Direct Debit Authorization (for CNY Account) [PDF] (https://av.sc.com/hk/content/docs/cc_dda.pdf)
Octopus Automatic Add Value Service Application/Change Request Form [Online Form] (https://www.sc.com/hk/credit-cards/octopus-aavs/apply/?)
Octopus Automatic Add Value Service Application/ Change Request Form [PDF] (https://av.sc.com/hk/content/docs/hk-octopus-agreement.pdf)
Supplementary Card Application Form [PDF]
For supplementary card application, please read together with the documents below:
•	Client Terms [PDF] (https://av.sc.com/hk/content/docs/client-terms.pdf)
•	Credit Card Terms [PDF] (https://av.sc.com/hk/zh/content/docs/hk-gn177.pdf)
•	Notice of Change/Important Notes in relation to Standard Chartered/MANHATTAN Credit Cards (“Cards”) (https://av.sc.com/hk/content/docs/HK-NOC-Final-EN.pdf)
•	Notice to customers and other individuals relating to the Personal Data (Privacy) Ordinance (“Ordinance”) and the Code of Practice on Consumer Credit Data [PDF] (https://av.sc.com/hk/content/docs/hk-gn050-v2.pdf)
•	Credit Card Key Facts Statement For Standard Chartered and MANHATTAN Cardholders [PDF] (https://av.sc.com/hk/content/docs/hk-credit-card-key-facts-statement.pdf)
Cardholder’s Declaration of Dispute [PDF] (https://av.sc.com/hk/content/docs/hk-scb-disputeletter-1116.pdf)
Cancellation or Replacement Request Form [PDF] (https://av.sc.com/hk/content/docs/hk-scb-cc-cancellation.pdf)

Credit Card Promotions and Offers – Standard Chartered HK (https://www.sc.com/hk/credit-cards/offers/?intcid=web_listing-sc_com_top_nav-na-staticmedia_others-sng-na-cc_view_all_credit_card_promotions-sc_com_organic-hk-en)
"""

promotions_text = """
Credit Card Promotions and Offers – Standard Chartered HK 

Standard Chartered Credit Cards Offers 

Hot Promotions 

 

Hot offers 

 

SHKP 

Enjoy up to a total of $2600 Point Dollar and Lucky Draw privileges 

From 1 March to 15 May 2025 (unless otherwise specified), Standard Chartered credit cardholders can enjoy the following offers at SHKP Malls 

Offer 1: Up to a total of $2,600 Point Dollar 

Basic Reward: 

Applicable to designated spending requirements, please refer to the table stated in below. 

Same-day cumulative net spending amount is calculated based on a maximum of 3 Eligible Transactions from different merchants in the same Participating Mall which are fully settled by the same Eligible Card on the same day with a spending amount of at least HKD100 for each Eligible Transaction. Each Eligible Transaction can only be counted once for the purpose of calculating the same-day cumulative net spending amount. 

Holiday Tasty Top-up Reward: 

Holiday Tasty Top-up Reward: must be redeemed together with Reward 1/ Reward 2/ Reward 3. Standalone redemption of the Holiday Tasty Top-up Reward will not be accepted. 

At least one single eligible sales slip must be issued by F&B merchants with spending amount of HKD300 or above. 

Please refer to the table stated in below for details. 

 

Offer 2: Register to grab the lucky draw chance to win Samsung Galaxy S25 (Total 10 winners) 

Each eligible transaction of HKD100 or above that is successful registered here will be entitled to 1 lucky draw chance. 

If you hold a valid payroll account* for payment settlement, you will entitle to 8X lucky draw chances automatically for each registered eligible transaction. 

* A valid payroll account refers to clients who have used Standard Chartered’s auto-payroll services starting from the first day of the Promotion Period until the month of Lucky Draw Prize allotment. 

Detail of Offer 1: 

REWARD 

SAME-DAY CUMULATIVE NET SPENDING AMOUNT* 
(MAXIMUM 3 ELIGIBLE TRANSACTIONS FROM DIFFERENT MERCHANTS) 

POINT DOLLAR 

HOLIDAY TASTY TOP-UP REWARD^: 

1 

HKD1,500 – HKD2,999 

$50 

Extra $30 Point Dollar; AND Redemption Pass to redeem 
i. A GODIVA Dark Chocolate Soft Serve 
(Original price: HKD59) 
OR 
ii. A cup of Tea WG tea (Hot/Cold) 
(Original price: HKD48) at $30 Point Dollar 

2 

HKD3,000 – HKD7,999 

$110 

3 

HKD8,000 or above 

$330 

* Same-day cumulative spending is calculated based on a maximum of 3 eligible transactions from different merchants in the same Participating Mall which settled by the same eligible credit card with the spending amount of each receipt should be at least HKD100. 

^ Holiday Tasty Top-up Reward is applicable on 1-2 March, 7-9 March, 14-16 March, 21-23 March, 28-30 March, 4-6, 11-13, 18-21, 25-27 April, 1-5 and 9-11 May of 2025. 

List of Participating Malls for the redemption location and time, please click here. 

Remark: 

All offers are first-come-first-served, while stocks last. Please check the redemption details with the staff of the redemption counter. 

Cardholders must be existing members or have successfully registered as members of The Point to join these offers. Each cardholder can enjoy Reward 1, Reward 2, Reward 3 and Holiday Tasty Top-up Reward ONCE at each Participating Mall each day. Maximum 5 times across all Participating Malls for the whole promotion period. 

All offers are applicable to Mobile Payment Purchase (including Apple Pay, Google Pay™ , Samsung Pay, Huawei Pay and UnionPay QuickPass), but NOT applicable to the transactions made via any e-wallets (including but not limited to Octopus, Alipay, WeChat Pay, Tap & Go and PayMe). 

 

 

Festival Walk 

Festival Walk Lucky Draw Programme Winner Announcement 

 

Standard Chartered Credit Card x Harbour City Lucky Draw Programme 

Winner Announcement 

 

Agoda 

Apply Standard Chartered Cathay Mastercard® to unlock up to HKD300 CashBack and limited offer up to 16% off hotel bookings at Agoda 

Exclusive to Agoda: Up to 120,000 Miles and HKD300 CashBack 

New cardholders1 who successfully apply for Standard Chartered Cathay Mastercard®by 4 April 2025 can get welcome offer up to 120,000 miles! What’s more, you can earn extra HKD300 CashBack on any Agoda transactions of HKD3,250 or above within the first 2 months of card issuance; while existing cardholders2 can also get HKD150 CashBack! 

Terms and conditions apply. 

Up to 16% off on hotel bookings at Agoda 

Standard Chartered Cathay Mastercard: Up to 16% off  [Quota full] 

Standard Chartered Credit Cards: 7% off 

Promotion period: 18 February 2025 to 4 April 2025 
Period of Stay: 18 February 2025 to 31 December 2025 

Agoda designated website: www.agoda.com/scbhk 

Terms and conditions apply. 

 

Hotels.com 

Enjoy up to HKD300 for pre-pay hotel bookings and enter designated promo code at designated website.  

MORE  

￼ 

RentSmart 

Exclusive offers for Standard Charted Cathay Mastercard – first time service fee waiver, up to 5,000 miles and have a chance to win HKD20,000 rental reward 

MORE  

￼ 

Samsung 

Enjoy up to 8% CashBack and interest-free instalment offers 

MORE  

Offer 1: Up to 8% CashBack 

Up to 8% CashBack upon single net spending of HKD8,000 or more. 

Up to 6% CashBack upon single net spending of HKD3,000 – HKD7,999.99. 

Remarks: 

Quota: the first 2,000 eligible new transactions. 

Each cardholder is eligible to the CashBack once, i.e., HKD2,000 CashBack in maximum during the whole promotion period. 

To be eligible for the offer, cardholders are required to register here for patronage at designated Samsung Experience Stores. For patronage at Samsung Online Shop and Samsung Shop App, registration is not required. 

All the offers are NOT applicable to transactions made via any e-wallets (including but not limited to Alipay, WeChat Pay and Tap & Go. 

 

Offer 2: Interest-free merchant instalment 

Please contact Samsung and apply via Samsung Online Shop, Samsung Shop App and designated Samsung Experience Stores. 

Remarks: 

Offer 1 and Offer 2 can be used in conjunction. Application for this Interest-free instalment offer via the Bank after the purchase will not be accepted. Please apply it at Samsung Online Shop, Samsung Shop App and designated Samsung Experience Stores before settling the payment. 

 

Samsung Online Shop: shop.samsung.com/hk_en/sc 

Samsung Shop App: https://samsungshop.onelink.me/6zKq/k46mzsa5 

Designated Samsung Experience Stores: 

Central 
Address: Shop G3 – G4, China Building, 29 Queen’s Road Central, Central 
Phone No.: +852-2559-3560 

Tsim Sha Tsui 
Address: Shop 332, Ocean Centre, Tsim Sha Tsui 
Phone No.: +852-2432-4668 

Kowloon Bay 
Address: Shop G56-57, Telford Plaza I, 33 Wai Yip Street, Kowloon Bay 
Phone No.: +852-3572-0466 

Tseung Kwan O 
Address: Shop G38-39, PopCorn 1, 9 Tong Yin Street, Tseung Kwan O, N.T. 
Phone No.: +852-2694-1899 

Tsuen Wan 
Address: G001B, G/F, KOLOUR, Tsuen Wan I, 68 Chung On Street, Tsuen Wan 
Phone No.: +852-2701-4062 

Sha Tin 
Address: Shop 602, 6/F, New Town Plaza, Shatin 
Phone No.: +852-5337-6180 

Yuen Long 
Address: Shop 2006-2007, Level 2, YOHO Mall I, 9 Long Yat Road, Yuen Long, N.T. 
Phone No.: +852-2358-0338 

Mongkok 
Address: Shop No. M55, MTR Floor, MOKO, 193 Prince Edward Road West, Mongkok 
Phone No.: +852-2690-0155 

Kai Tak 
Address: Shop No. L216 & 217, 2nd Floor, AIRSIDE, 2 Concorde Road, Kai Tak 
Phone No.: +852-2705-5366 

Taikoo Shing 
Address: Shop 219, 2/F, Cityplaza, 18 Taikoo Shing Road, Taikoo Shing 
Phone No.: +852-2386-8078 

Hong Kong International Airport 
Address: Unit No. 7E101A, Level 7, Departures East Hall, Terminal 1 (Restricted Area), Hong Kong International Airport, Lantau Island 
Phone No.: +852-2893-8208 
"""

more_promotions_text = """
 

Booking.com# x Mastercard 

16% Wallet Credit Back on selected hotel bookings till 31Mar25, checkout till 30Jun25 

MORE  

 

 

iPhone for Life Plan 

The affordable way to have the latest iPhone 

MORE  

From 20 September 2024 onwards, Standard Chartered Visa and Mastercard® holders can enjoy the following offers when purchasing the new iPhone 16 Pro and iPhone 16 Series (“iPhone”) at designated mobile service providers. 

Buy the latest iPhone by using iPhone for Life 

Low monthly instalments 

Up to 36 months interest-free merchant instalment 

No handling fee 

Applicable to purchase of iPhone together with the subscription of designated service plan of mobile service providers; or purchase of standalone handset* 

* Terms and conditions apply with respect to the arrangement of standalone handsets provided by respective mobile service providers. 

 

Flexible options: 

1. Upgrade* to the latest iPhone by returning the original iPhone to respective mobile service providers (trade-in) to offset the remaining instalment payment similar to “Guaranteed Buy-Back Value“; or 
2. Keep your iPhone and continue to pay the remaining balance by instalments till the end of the original tenor. 

* Terms and conditions apply with respect to the “Product Return Option” provided by respective mobile service providers. 

 

Participating mobile service providers: 

For more product details, please visit retail outlets of the mobile service providers. 

• China Mobile Hong Kong Learn More & other offers 
• CSL Learn More 
• Hong Kong Broadband Network Learn More 
• SmarTone Learn More 
• SUPREME  Learn More 
• Telecom Digital SUN Mobile Learn More 
• 1O1O Learn more 
• 3 Hong Kong Learn More 

 

Limited time Offer: Earn an extra 3,000 miles rewards / HKD300 CashBack 

Thank you for your support. The registration of Extra Rewards has been completed, and the relevant reward will be credited to the account of eligible cardholders within Apr 2025. 

To be eligible for the limited time offer, cardholders shall register through this webpage and purchase either (a) an iPhone using the iPhone for Life Plan during 20 September 2024 to 31 January 2025 or (b) a standalone iPhone in a single net transaction of HKD8,000 or above during 1 November 2024 to 31 January 2025 at designated mobile service providers with Eligible Cards. 

Earn 3,000 Miles with Standard Chartered Cathay Mastercard. 

Earn HKD300 CashBack with other credit cards. 

– Only the first 3,500 successfully registered Cardholders are eligible. Registration will be closed when the quota is full. 

– Each Cardholder can only register ONE Eligible Card during the Promotion Period, and only that ONE registered Eligible Card will be used to calculate the Eligible Transactions and the relevant miles / CashBack / Cash Rebate. 

– Each Cardholder is only entitled to enjoy the Rewards (either in the form of miles / CashBack / Cash Rebate) once during the Promotion Period, regardless of how many times the offer requirements are met and how many Eligible Cards each Cardholder is holding. 

– If the quota is full, it will be stated in this webpage, please visit here before patronage. 

Earn an extra 500 Miles or HKD50 CashBack upon purchasing an iPhone by using iPhone for Life at China Mobile Hong Kong. 

Learn More 

 

Celebrating Flavours with Standard Chartered 

Exclusive dining offers for Standard Chartered Cathay Mastercard cardholders. Wine, dine and get rewarded now! 

MORE  

 
Feuille 

Buy-3-Get-1-Free on Dinner Tasting Menu (HKD1,599/head) 

MORE  

￼ 

Hansik Goo 

Buy-3-Get-1-Free on Dinner Tasting Menu (HKD1,480/head) 

MORE  

￼ 

Hopewell Inn 

20% Off on “Standard Chartered Cathay Mastercard” Signature Set (HKD888/head) 

MORE  

￼ 

Kaen Teppanyaki 

Buy 1, Get 50% Off on 2nd Designated Menu (HKD1,580/head) 

MORE  

￼ 

KITCHEN 

Buy-2-Get-2-Free on Buffet (HKD498/head and up) 

MORE  

￼ 

Lucciola Restaurant & Bar 

Buy-2-Get-1-Free on 4-Course Weekend Brunch (HKD688/head) 

MORE  

￼ 

Monkey Café 

Buy-1-Get-1-Free on Weekend Brunch Semi-Buffet (HKD438/head (Adult); HKD338/head (Children / Senior Citizen)) 

MORE  

￼ 

Nicholini's 

Buy-2-Get-1-Free on “Ciao Italia!” Saturday Brunch (HKD798/head and up) 

MORE  

￼ 

Oyster & Wine Bar 

Buy-1-Get-1-Free on “Luscious Lobster Land” Dinner Set (HKD1,590/head) 

MORE  

 

Unkai Japanese Cuisine 

Buy-2-Get-1-Free on Designated Teppanyaki Dinner Set (HKD1,400/head) 

MORE  

￼ 

Zoku Restaurant & The Terrace 

Buy-2-Get-1-Free on Full-Course Weekend Brunch (HKD688/head) 

 

 

Visa Privileges* 

Enjoy a series of exclusive offers at Sands Resorts Macao 

MORE  

 

 

Trip.com 

8% off hotel bookings/ HKD200 off air ticket at designated webpage with promo code 

MORE  

 

 

iPhone for Life Plan 

The affordable way to have the latest iPhone 

MORE  

From 22 September 2023 onwards, Standard Chartered Visa and Mastercard® holders can enjoy the following offers when purchasing the new iPhone 15 Pro and iPhone 15 Series (“iPhone”) at designated mobile service providers. 

Buy the latest iPhone by using iPhone for Life 

Low monthly instalments 

•  Up to 36 months interest-free merchant instalment 
•  No handling fee 
•  Applicable to purchase of iPhone together with the subscription of designated service plan of mobile service providers; or purchase of standalone handset* 

* Terms and conditions apply with respect to the arrangement of standalone handsets provided by respective mobile service providers. 

Flexible options: 

1. Upgrade* to the latest iPhone by returning the original iPhone to respective mobile service providers (trade-in) to offset the remaining instalment payment similar to “Guaranteed Buy-Back Value“; or 
2. Keep your iPhone and continue to pay the remaining balance by instalments till the end of the original tenor. 

* Terms and conditions apply with respect to the “Product Return Option” provided by respective mobile service providers. 

Participating mobile service providers: 

For more product details, please visit retail outlets of the mobile service providers. 

• China Mobile Hong Kong Learn More & other offers 
• CSL Learn More 
• Hong Kong Broadband Network Learn More 
• SUPREME  Learn More 
• 1O1O Learn more 
• 3 Hong Kong Learn More 

Limited time Offer: Earn an extra 1,500 miles rewards / up to HKD300 CashBack 

Thank you for your support. The registration of Extra Rewards has been completed, and the relevant reward will be credited to the account of eligible cardholders within May 2024. 

To be eligible for the offer, cardholders shall register through this webpage and buy an iPhone by using iPhone for Life at designated mobile service providers with Eligible Cards. 

Earn 1,500 Miles with Standard Chartered Cathay Mastercard. 

Earn HKD300 CashBack with Smart Card. 

Earn HKD150 CashBack with other credit cards. 

– Only the first 3,000 successfully registered Cardholders are eligible. Registration will be closed when the quota is full. 

– Each Cardholder can only register ONE Eligible Card during the Promotion Period, and only that ONE registered Eligible Card will be used to calculate the Eligible Transactions and the relevant miles / CashBack / Cash Rebate. 

– Each Cardholder is only entitled to enjoy the Rewards (either in the form of miles / CashBack / Cash Rebate) once during the Promotion Period, regardless of how many times the offer requirements are met and how many Eligible Cards each Cardholder is holding. 

– If the quota is full, it will be stated in this webpage, please visit here before patronage. 

Earn an extra 500 Miles or HKD50 CashBack upon purchasing an iPhone by using iPhone for Life at China Mobile Hong Kong. 

Learn More 

 

 

Expedia 

8% off on selected hotel bookings (Coupon code: SCBHK08) 

MORE  

 

 

Mastercard Travel Rewards*^ 

Shop around the world with premium brands. Check out the available travel offers and sign up to enjoy cash rewards now. 

MORE  
"""

more_promotions_text_2 = """
iPhone for Life Plan 

The affordable way to have the latest iPhone 

MORE  

From 16 September 2022 onwards, Standard Chartered Visa and Mastercard® holders can enjoy the following offers when purchasing the new iPhone 14 Pro and iPhone 14 series (“iPhone”) at designated mobile service providers. 

Buy the latest iPhone by using iPhone for Life 

Low monthly instalments 

– Up to 36 months interest-free merchant instalment 

– No handling fee 

– Applicable to purchase of iPhone together with the subscription of designated service plan of mobile service providers; or purchase of standalone handset* 

* Terms and conditions apply with respect to the arrangement of standalone handsets provided by respective mobile service providers. 

Flexible options: 

1. Upgrade* to the latest iPhone by returning the original iPhone to respective mobile service providers (trade-in) to offset the remaining instalment payment similar to “Guaranteed Buy-Back Value“; or 

2. Keep your iPhone and continue to pay the remaining balance by instalments till the end of the original tenor. 

* Terms and conditions apply with respect to the “Product Return Option” provided by respective mobile service providers. 

Participating mobile service providers: 

For more product details, please visit retail outlets of the mobile service providers. 

• China Mobile Hong Kong Learn More 

• CSL Learn More 

• Hong Kong Broadband Network Learn More 

• 1O1O Learn more 

• 3 Hong Kong Learn More 

 

Limited time Offer: Earn an extra 1,500 miles rewards / up to HKD250 CashBack 

Thank you for your support. The registration of Extra Rewards has been completed, and the relevant reward will be credited to the account of eligible cardholders within March 2023. 

To be eligible for the offer, cardholders shall register through this webpage and buy an iPhone by using iPhone for Life at designated mobile service providers with Eligible Cards. 

Earn 1,500 Miles with Standard Chartered Cathay Mastercard. 

Earn HKD250 CashBack with Smart Card. 

Earn HKD150 CashBack with other credit cards. 

– Only the first 2,000 successfully registered Cardholders are eligible. Registration will be closed when the quota is full. 

– Each Cardholder can only register ONE Eligible Card during the Promotion Period, and only that ONE registered Eligible Card will be used to calculate the Eligible Transactions and the relevant miles / CashBack / Cash Rebate. 

– Each Cardholder is only entitled to enjoy the Rewards (either in the form of miles / CashBack / Cash Rebate) once during the Promotion Period, regardless of how many times the offer requirements are met and how many Eligible Cards each Cardholder is holding. 

– If the quota is full, it will be stated in this webpage, please visit here before patronage. 

Learn More 

 

 

Smart card Year-round Offer 

Up to 5% CashBack at Japan Home Centre, PARKnSHOP, Watsons and more 

MORE  

Standard Chartered Smart Credit Card 

Earn and save on your everyday spending. 
All you need is ONE card! 

Year-round Offer 

Up to 5% CashBack 

On designated everyday merchants. No registration and available every day*. 

Fees, Goodbye! 

No foreign exchange fees, no annual fees, no cash advance fees. Ever. 

Welcome offer: HKD800 CashBack 

From now to 2 July 2025, New Cardholders2 can enjoy HKD800 CashBack upon making Accumulated Eligible Transactions3 of HKD3,500 within the first month from the date of issuance. 

Up to 5% CashBack* at Designated Merchants, earn and save on your everyday spending 

Grocery shopping & Home: HKTVmall, 759 Store, Circle K Convenience Store, Japan Home Centre, PARKnSHOP 

Beauty & Health care: Watsons, Sasa 

Food and beverage: McDonald’s Hong Kong 

Sport & Entertainment: Decathlon, Klook, HK Ticketing, selected online video and music streaming platforms 

Digital Lifestyle: China Mobile Hong Kong and s/ash 

Minimum spending requirements apply. 

Learn More 

No foreign currency transaction fees during travel and No other fees 

Waive 1.95% fee and earn up to 1.2% CashBack on foreign currency retail transaction 

No annual fees 

No Cash advance fees 

Learn More 

Credit Card Promotions & Services 

Pay bills and make transfers without fees 

Skip the fees. Now you can pay your rent, education expenses, car park fees and even your family and friends with your credit card without handling fees! 

Learn More 

Credit Card Instant Loan 

Get quick cash in as fast as 30 seconds this travel season, at APR as low as 2.91% with Credit Card Instant Loan and enjoy up to HKD10,000 CashBack. 

Learn More 

360° Rewards Redemption Platform 

360° Rewards Redemption Platform now serve with refresh outlook enable you to redeem rewards with your earned Points and CashBack 

Learn More 

Visa Signature offer 

Enjoy Visa Signature offers with Smart card around the globe 

Learn More 

 

 

Hong Kong Disneyland hotel 

12-month interest-free instalment offer for online hotel bookings 

MORE  

The Good Life Entertainment Rewards 

From now on until 31 December 2025 (unless otherwise specified), Standard Chartered / MANHATTAN Visa or Mastercard credit cardholders can enjoy the following offer when booking selected hotel at Hong Kong Disneyland Resort through the official website. Enjoy a magical Disney resort vacation today and “Play, Shop, Dine, Stay!” 

A Warm Reminder:  
Please click the Standard Chartered credit card payment option when you make your hotel booking at the official website of Hong Kong Disneyland Resort in order to enjoy the applicable interest-free instalment offer. 

Remarks: 

Any change after the hotel reservation completes shall be treated as a cancellation of the hotel reservation. A new reservation is required for the hotel stay. 

The cardholder authorises Hongkong International Theme Parks Limited (“HKITP”) to (i) withhold or deduct from the payment made and/or (ii) charge on the cardholder’s credit card account the applicable cancellation charges and all costs, interests, fees, expenses, losses or other liabilities incurred by HKITP arising from the cardholder’s instalment payment arrangement. 

Unless otherwise specified, the offers cannot be used in conjunction with other promotional offers or discounts. 

Images are for marketing purposes only. All Guests must wear face masks and maintain appropriate social distancing. Please visit official website for details. 

 

 

Hong Kong Disneyland 

12-month interest free instalment offer for purchase of Magic Access (Annual Pass) 

MORE  

From now on until 31 December 2025, Standard Chartered / MANHATTAN Credit cardholders1 can enjoy 12-month interest free instalment offer2 and other privileges upon the purchase or renewal of Magic Access Membership Card / Certificate. 
"""

magic_access_and_good_life_text = """
Magic Access 
MAGIC ACCESS 
PLATINUM 
GOLD 
SILVER 
Valid dates 
No blockout days 
Most weekdays and weekends of the park’s operation days and designated public holidays during the membership term 
Most weekdays (excluding public holidays) of the park’s operation days during membership term 
Park admission is subject to the park’s operation days which may change from time to time and will require advance reservation. Reservations are subject to a limited quota. 
Parking at Auto Plaza (This benefit is not applicable to Child membership cards. Subject to availability and Benefit Limit.) ±± 
Free 
24 times of free parking during current membership term, and additional parking with HKD40 off for private cars and HKD15 off for motorcycles 
HKD40 off for private car parking, 
HKD15 off for motorcycle parking 
Additional member exclusive benefit 
(e.g. priority seating, etc.)^ 
✔ 
– 
– 
Free park admission on weekend or public holiday# 
– 
– 
1 free park admission with the first 5 park visits 
Price 
General (formerly known as “Adult”): aged 12-59 
HKD4,678 
HKD2,558 
HKD1,468 
Student (Aged 12-25 full time student) 
HKD3,558 
HKD1,918 
HKD1,148 
Child (Aged 3-11) 
HKD3,368 
HKD1,818 
HKD1,088 
Senior (Aged 60 or above) 
HKD890 
HKD525 
HKD316 
 
 
The Good Life year-round offers 
Enjoy fabulous dining, shopping and travel offers all year-round 
MORE  
​Standard Chartered card offers – dining, shopping, staycation and more 
Enjoy fabulous offers at FORTRESS, Agoda and more with your Standard Chartered credit card or Multi-Currency Mastercard debit card, if applicable. 
Not yet a cardholder? Apply now to enjoy Standard Chartered credit card offers and rewards. 
 
Häagen-Dazs™ 
8% off ice-cream cake 
For Visa, Mastecard. Valid till 31 Dec 2025 
 
Trip.com 
Up to HKD200 instant discount upon purchase of designated international flight ticket of designated amount and 8% off on selected hotel bookings 
For Visa, Mastecard. Valid till 31 Dec 2025 
 
Wing On Travel 
Up to a total of HKD270 off on designated travel products booking 
For Visa, Mastecard. Valid till 31 Dec 2025 
 
Agoda 
7% off on hotel booking at designated webpage 
For Visa, Mastecard. Valid till 31 Dec 2025 
 
AIRSIM 
HKD88 for AIRSIM HKD120 pre-paid card (with HKD100 stored value) 
For Visa, Mastecard. Valid till 31 Dec 2025 
 
Expedia 
8% off on selected hotel bookings at designated webpage (Coupon code: SCBHK08) 
For Visa, Mastecard, and UnionPay. Valid till 31 Dec 2025 
 
FORTRESS 
HKD100 off upon single purchase of HKD2,000 on designated regular-priced items. 
For Visa, Mastecard, and UnionPay. Valid till 31 Dec 2025 
 
Hong Kong Suning 
HKD100 off upon single net spending of HKD2,000 or above on regular-priced item 
For Visa, Mastecard, and UnionPay. Valid till 31 Dec 2025 
 
Hotels.com 
8% off on selected hotel bookings at designated webpage (Coupon code: SCB8) 
For Visa, Mastecard, and UnionPay. Valid till 31 Dec 2025 
 
Ruby Tuesday 
35% off à la carte steakhouse items for dine-in only and enjoy a 720-day Ruby Tuesday Premier Membership at special price of HKD1,200 (regular price HKD1,500) 
For Visa, Mastecard, and UnionPay. Valid till 31 Dec 2025 
 
YOHO 
HKD80 instant discount upon making a single net transaction of HKD2,000 or above on designated products of selected brands at YOHO eShop (Promotion code: SC2025) 
For Visa, Mastecard. Valid till 31 Dec 2025 
 
ZALORA 
15% off 
For Visa, Mastecard, and UnionPay Valid till 31 Dec 2025 
 
More year-round offers 
Hotel & Dining 

MORE  
￼ 
Shopping & Lifestyle 
MORE  
 
Health & Wellness 

MORE  
￼ 
Online & Travel 
MORE  
￼ 
Up to 36-month Interest-Free Instalment 

 
Financial Flexibility 
Credit Limit Increase 
Credit limit increase now available on Standard Chartered Online Banking and SC Mobile App 
MORE  
￼ 
Cash out your credit limit and get up to HKD10,000 CashBack 
Enjoy up to HKD10,000 CashBack for this travel season! Apply online to get quick cash from credit limit in as fast as 30 seconds at APR as low as 2.91% and enjoy rewards to go with your cash flow! 
MORE  
￼ 
CashBack with our limited Spring Giveaway 
Embrace the new year with exciting rewards! Enjoy up to HKD1,000 CashBack by splitting your card bills via online successfully. 
MORE 
"""

rewards_360_text = """
360 Rewards | CashBack & Asia Miles – Standard Chartered HK 

Note to 360° Rewards 

Effective from 28 February 2020, air miles redemption has been amended as follows: 

Points required for every 1,000 Asia Miles conversion are 25,000 points 

KrisFlyer Miles are removed from the 360° Rewards Catalogue 

Please click here to login to 360° Rewards Redemption Platform via Standard Chartered Online Banking or SC mobile Apps to browse and redeem available rewards. If you are non-Online Banking user, please click here for registration guidelines. 

The 360o Rewards Redemption Platform currently supports most desktop, laptop and mobile. As for tablets, due to the differing resolutions, the user experience is compromised. Hence, we recommend that you access our Rewards Redemption Platform on your desktop, laptop, or mobile device. 

In view of the credit card account type, your 360° Rewards Points may subject to expiry. You can login to 360° Rewards Redemption Platform or refer to your credit card monthly statement for the expiry date of Rewards Points. 

Access to 360° Rewards 

REGISTERED STANDARD CHARTERED ONLINE BANKING USERS 

Simply log in the 360° Rewards Redemption Platform to redeem your favourite items 

Login Now using your current Standard Chartered Online Banking username and password 

NON-REGISTERED STANDARD CHARTERED ONLINE BANKING USERS 

You just need your ATM Card/ credit card and personal information for registration. Please follow the steps below to register Standard Chartered Online Banking 

Customer with any Standard Chartered Bank Accounts Register Now | Guide for registration 

Customer with Standard Chartered / MANHATTAN Credit Card only Register Now | Guide for registration 

 

Rewards Categories 

360° REWARDS POINTS 

You can convert your Points to cash or air miles. Point to Cash is only applicable to designated credit card account， Points cannot be combined during the redemption. (The minimum threshold for Cash redemption is HKD50 per account with designated multiplier.) Learn More 
How do I earn 360° Rewards Points? Our 360° Rewards programme not only rewards your credit card spending, but also your mortgage, investments, deposits and online transactions. Find out more 

CASHBACK 

With the CashBack of your credit card， CashBack cannot be combined during the redemption. (The minimum threshold for Cash redemption is HKD50 per account with designated multiplier.), you can choose to redeem cash via our 360° Rewards Redemption Platform. Learn More 
How do I earn CashBack? Use any Standard Chartered Credit Card with the CashBack feature, or participate in our promotions to build your CashBack balance. Find out more 

 

360° Rewards Redemption Platform 

360° Rewards Redemption Platform maximises the benefits of Points or CashBack. Enjoy the following benefits for redemptions: 

One-stop redemption platform to Standard Chartered & MANHATTAN credit cardholders for Points and CashBack redemption 

Flexible conversion of your Points or CashBack to cash or air miles 

Manage your Points and CashBack with more flexibility: 

Monitor your Points and CashBack with a breakdown of balance 

Check the expiry date of your Points (if applicable) 

Make instant points redemption by converting your points to cash or air miles 

Receive SMS and e-mail confirmation upon redemption 

 

Points to Cash and CashBack 

Points to Cash 

Select the amount you would like to redeem (minimum redemption amount is HKD50 with a multiple of HKD50, HKD100, HKD500 or HKD1,000), click “Redeem” then click "Confirm" to convert Points to Cash 

CashBack to Cash 

Select the amount you would like to redeem (minimum redemption amount is HKD50 with a multiple of HKD50, HKD100, HKD500 or HKD1,000), click “Redeem” then click "Confirm" to convert CashBack to Cash 

 

Points to Air Miles and Asia Miles Membership Information Registration / Update 

Points to Air Miles 

Scroll to select points for air miles, click "Redeem" and then click "Confirm" to redeem air miles 

Register Asia Miles Membership Information 

After click “Register”, input Asia Miles Membership Number, Member First Name and Member Last Name then click “Submit”  

Follow the steps with mobile device to authenticate your Asia Miles membership information registration instruction, once finish you can click “Confirm” to redeem air miles 

Update Asia Miles Membership Information 

After click “Redeem”, click “Update Membership Information” to edit Asia Miles Membership Number, Member First Name and Member Last Name then click “Submit” 

Follow the steps with mobile device to authenticate your Asia Miles membership information update instruction, once finish you can click “Confirm” to redeem air miles 

 

A more secure online rewards redemption experience 

To provide you a more secure online rewards redemption experience, effective from early May 2017, an One-time Password (“OTP”) will be required when you perform designated rewards redemptions via 360° Rewards Redemption Platform. No registration is required for this enhanced service. Simply maintain an updated and valid mobile phone number with the Bank, and you can enjoy a peace of mind rewards redemption experience. 

Protect your Online Banking account from unauthorised access. Always take good care of your username and password, and keep your password and devices updated regularly. Check out Online and Mobile Security Tips. 

Update your mobile phone number with ease 

If you need to update your mobile phone number with the Bank, please submit your request via the following channels: 

Download the Change of Contact Information Form for Individual Client and mail it back to the Bank 

Visit any of our branch to submit the Change of Contact Information Form for Individual Client 

Remarks: 

The service is only applicable to the Principal Cardholder with a valid Hong Kong mobile phone number registered with the credit card system of the Bank. 

OTP is only applicable to local mobile phone numbers starting with 4, 5, 6, 7, 8 or 9. Cardholders with mobile phone numbers starting with other digit are not able to complete the relevant online rewards redemptions. 

Notice of Change: Mileage Redemption via Online Banking from 18 November 2018 

To provide you with a more convenient and secure rewards redemption experience, effective from 18 November 2018: 

For customer who performed mileage redemption during April to November 2018, your Air Miles membership information (including Air Miles membership number and name) has been verified and registered as Bank’s records. You can now redeem mileage via Online Banking or SC Mobile Apps*. 

For Standard Chartered Asia Miles Mastercard cardholder, your Asia Miles membership information has been automatically registered after verification by the Bank. You can also redeem mileage via Online Banking or SC Mobile Apps 

For other customers who want to redeem mileage, or if you want to change your Air Miles membership information registered with us, you can now register or update your Air Miles membership information via Online Banking or SC Mobile Apps. 

*If you cannot find your Air Miles membership information to perform mileage redemption, Please register your Air Miles membership information via Online Banking or SC Mobile Apps. 
"""

other_services_text = """
Other Credit Card Services – Standard Chartered HK 

 

Manage your credit card through Digital Banking 

Trying to keep tabs on multiple credit cards? Our Online Banking and SC Mobile App features are designed to make card management easy and frictionless for you, anytime and anywhere. 

 

Register SC Mobile App 

Step 1: Tap ‘Login’ on welcome screen. 

Step 2: Tap "New to SC Mobile App? Register here" 

Step 3: Register with you ATM Card or Credit Card. 

Step 4: Personal Banking Customer: Register with ATM Card 
Enter you ATM Card Number, Card Expiry Date and Personal Identification Number (PIN). 

Credit Card Customer: Register with Credit Card 
Enter your Credit Card Number, Card Expiry Date, Date of Birth and HK Identity Card Number. 

Step 5: Confirm your registered mobile number in our bank record and you will receive One-Time-Password (OTP) via SMS. 

Step 6:Enter your OTP. 

Step 7: Create your username and password. 

 

Initiate Dispute Request 

You may initiate a dispute request online via the Bank for reversing or refunding transactions under specific circumstances of the dispute resolution scheme, such as unauthorized transactions or failed delivery of goods/ services by the merchant after a one-off pre-payment. 
For any transactions in doubt, you should raise the dispute within 60 days upon the statement issuance date. 
Learn More 

Step 1:Click “Help & Services” for Online Banking; “Services” > “Credit Cards” for SC Mobile App 

Step 2:Click “Credit Card Transaction Dispute” 

Step 3: Select the card you wish to submit the application for 

Step 4: Select the dispute reason 

Step 5: Select the transaction(s) with an issue 

Step 6: Fill in additional details and upload documents 

Step 7: Read the important notes carefully and confirm to proceed further 

Application submitted! Updates will be delivered via SMS and email. 

 

Report Lost/Stolen Credit Card 

If your card is lost or stolen, or your PIN number has been disclosed to a third party, please contact the Bank immediately to make a report. 

Step 1: Click “Help & Services” for Online Banking; “Services” > “Credit Cards” for SC Mobile App 

Step 2: Click “Report Lost / Stolen Credit Card” 

Step 3: Select the cards you wish to report as lost 

Step 4: Read the important notes carefully 

Step 5: Confirm to proceed further 

Success! The replacement card will be issued and sent to your registered address 

 

Activate New Credit Card 

You may activate your physical credit card online within 3 months upon receipt. 

Step 1: Click “Help & Services” for Online Banking; “Services” > “Credit Cards” for SC Mobile App 

Step 2: Click “Credit Card Activation” 

Step 3: Select the card(s) you wish to activate  

Step 4: Enter your HKID number and Date of Birth 

Step 5: Confirm the activation 

Activation completed! The new PIN will be sent to you within 2 working days 

View Credit Card Details – CVV and Expiry Date 

Don’t have your physical credit card with you or want to start spending before your newly approved credit card arrives? If you have applied for your credit card online and registered for full digital banking services, you can check your CVV and expiry date online. 

Step 1: Select one of your credit cards listed on the account summary page 

Step 2: Click “Details” 

Step 3: Scroll down and click “Card Details” > eye icon 

Step 4: Authorise this action by using the SC Mobile App Key on your SC Mobile App 

Step 5: Once successfully authorised, you can use the CVV and expiry date for adding your credit card to mobile wallets or making online transactions 

 

Manage Credit Limit 

Adjust Credit Limit 

To prevent fraudulent activities with unused credit limit, adjust your credit limit with just a few clicks. 

Step 1: Click “Manage Credit Limit” for Online Banking; “Services” > “Credit Cards” for SC Mobile App 

Step 2: Click “Manage Credit Limit” 

Step 3: Select the card you wish to submit the application for 

Step 4: Adjust or input your preferred credit limit 

Step 5: Read the Terms & Conditions and confirm your application  

Application submitted! You will receive a result notification from us accordingly. 

Increase Credit Limit 

Want to spend more? You can easily apply to increase your credit limit online. 

Step 1: Click “Help & Services” for Online Banking; “Services” > “Credit Cards” for SC Mobile App 

Step 2: Click “Increase Credit Limit” 

Step 3: Select the card(s) you wish to submit the application for 

Step 4: Input the new credit limit 

Step 5: Select the reason for limit increase application 

Step 6: Read the Terms & Conditions and confirm your application 

Application submitted! Your application will be processed within 7 working days 

 
Request for Credit Card Service Charge Waiver 

Request for Credit Card Service Charge Waiver 

If your credit cards have been charged with annual fees, overlimit charges, late charges or finance charges within the last month, you may submit a waiver request online. 

Step 1: Click “Help & Services” for Online Banking; “Services” > “Credit Cards” for SC Mobile App 

Step 2: Click “Credit Card Service Charge Waiver” 

Step 3: Select the fee type 

Step 4: Select the card(s) you wish to submit the application for 

Step 5: Select the fee(s) to be waived 

Step 6: Confirm the details of your fee waiver application 

Application submitted! The waiver result will be delivered via SMS and email notifications in 3 business days. 

 

Temporarily Block/Unblock Credit Card 

Temporarily block/unblock card 

As an additional security measure, you now have the option to place temporary blocks on your cards and resume usage when desired. 
All credit card functions, including online/offline transactions, mobile wallets, and ATM cash withdrawal will be suspended until you initiate an unblock. Pre-authorized transactions, including Octopus AAVS or direct-debit authorization (DDA) set up by merchants will not be impacted by the temporary block. 

Step 1: Click “Help & Services” for Online Banking; “Services” > “Credit Cards” for SC Mobile App 

Step 2: Click “Temporary Block / Unblock Credit Card” 

Step 3: Select the card(s) you wish to block/unblock  
– Cards with a red toggle are currently in blocked status, you may toggle the icon to unblock the card 

Step 4: – Cards with a dimmed toggle are currently in active status, you may toggle the icon to block the card 

 
Transfer Out Credit Balance 

Transfer Out Credit Balance 

Have a credit balance on your credit card? You can now transfer it to your other Standard Chartered credit cards or banking accounts online. 

Step 1: Click “Help & Services” for Online Banking; “Services” > “Credit Cards” for SC Mobile App 

Step 2: Click “Credit Card Balance Refund” 

Step 3: Select the card(s) you wish to submit the application for 

Step 4: Select a refund method to your Standard Chartered savings/current account or other credit card 

Step 5: Select the receiving Standard Chartered credit card 

Step 6: Input the transfer amount and proceed 

Step 7: Confirm the request details 

Application submitted! Your credit balance transfer will be processed in 3 working days. 

 

Reset Credit Card PIN 

Reset Credit Card PIN 

Forgot your credit card PIN but need to access an ATM? You can instantly reset your credit card PIN via SC Mobile App, without having to call our customer service hotline or wait for mail delivery of your new PIN. 

Step 1: Click “Help & Services” for Online Banking; “Services” > “Credit Cards” for SC Mobile App 

Step 2: Click “Credit Card PIN Reset” 

Step 3: Set your new credit card PIN 

Step 4: Authorise this action by using the SC Mobile App Key on your SC Mobile App 

Success! Your credit card PIN has been reset 

 

Replace Credit Card 

Replace Credit Card 

Having issues with your physical credit card? You can apply for a replacement of your physical credit card online. 
Your physical credit card will be deactivated and cannot be used until you have received the new credit card and performed card activation. Supplementary cards (if any) will be deactivated along with the principal card. 

Step 1: Click “Help & Services” for Online Banking; “Services” > “Credit Cards” for SC Mobile App 

Step 2: Click “Credit Card Replacement” 

Step 3: Select credit card to replace 

Step 4: Confirm details to proceed 

Success! The replacement card will be issued and sent to your registered address 

 

Manage Credit Card Online Transactions Limits 

Manage Credit Card Online Transactions Limits 

Now you can personalize your credit card online transaction setting and limits effortlessly, right from your device. 

Step 1: “Services” > “Credit Cards” for SC Mobile App 

Step 2: Select “Manage Credit Card Online Transactions Limits” 

Step 3: Choose your desired credit card 

Step 4: Customise your experience by enabling or disabling online transactions 

Step 5: You may adjust your online transaction limits after enabled online transactions 

Step 6: Read the important notes carefully and confirm to proceed further 

Success! Your credit card online transaction setting and limits have been updated 

 

Additional Authentication for Credit Card Online Transactions 

Additional Authentication for Credit Card Online Transactions 

Receive real-time notifications on your mobile for approval of credit card online transactions* by proceeding with additional authentication on your SC Mobile App. 
Activate SC Mobile Key in your SC Mobile App, learn more here, and authorise the online transaction following the instructions in the app: 
*Only participating online merchants will require additional authentication. 

Step 1: When you are performing an online transaction which requires additional authentication. Click the push notification of relevant transaction from the SC Mobile App or open the App 

Step 2: Carefully review the transaction details such as merchant name and transaction amount to ensure they are correct and click “Approve”^, otherwise click “Reject”. 
^ Once the authorization for the transaction is approved, the Bank cannot cancel the transaction unilaterally for you.  

Step 3: Return to the merchant’s transaction page to proceed 
"""

# --- Combine all knowledge into a single text variable ---
# Add a clear separator between the two data sources
full_knowledge_text = (
    fees_data_text +
    "\n\n---\n\n" +  # Separator
    card_comparison_text +
    "\n\n---\n\n" +  # Separator
    faq_help_centre_text +
    "\n\n---\n\n" +  # Separator
    promotions_text +
    "\n\n---\n\n" +  # Separator
    more_promotions_text +
    "\n\n---\n\n" +  # Separator
    more_promotions_text_2 +
    "\n\n---\n\n" +  # Separator
    magic_access_and_good_life_text +
    "\n\n---\n\n" +  # Separator
    rewards_360_text +
    "\n\n---\n\n" +  # Separator
    other_services_text
)