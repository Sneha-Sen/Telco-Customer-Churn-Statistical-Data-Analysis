# **Telco Customer Churn – Statistical Data Analysis**

### **Introduction**

Customer churn is when a customer stops using a company’s service.
In the telecom industry, churn directly impacts revenue, making **customer retention** a priority.
This project uses the **Telco Customer Churn dataset** to uncover factors that influence churn, using **statistical hypothesis testing** and **exploratory data analysis (EDA)**.

### **Problem Statement**

The goal is to analyze historical customer data to:

* Identify **key factors** associated with churn
* Test whether these relationships are statistically significant
* Provide **actionable business recommendations** for reducing churn

### **Dataset Description**

* **Source:** Telco Customer Churn dataset ([Kaggle link](https://www.kaggle.com/datasets/blastchar/telco-customer-churn))

### **Tools & Libraries**

* **Python** (pandas, numpy) – data manipulation
* **Matplotlib, Seaborn** – visualization
* **SciPy** – statistical tests (Chi-square, t-test)
* **Visual Studio Code** – development & analysis

### **Methodology**

1. **Data Cleaning**

   * Converted `TotalCharges` to numeric (handled blank spaces)
   * Removed missing values in `TotalCharges`

2. **Exploratory Data Analysis (EDA)**

   * Distribution of churn vs non-churn
   * Visualization of numeric variables (`tenure`, `MonthlyCharges`, `TotalCharges`)
   * Categorical vs churn relationships

3. **Statistical Analysis**

   * **Chi-square test:** tested categorical variables (e.g., Gender, Contract type) against churn
   * **T-test:** compared `MonthlyCharges` mean for churned vs non-churned customers

### **Key Findings & Insights**

* **Contract Type:** Month-to-month customers churn significantly more than yearly contract customers (p < 0.05).
* **Monthly Charges:** Customers who churn have **higher average monthly charges** (p < 0.05).
* **Internet Service:** Fiber optic users churn more than DSL users.
* **Tenure:** Customers with less than 1 year tenure have much higher churn rates.
* **Payment & Billing:** Paperless billing is associated with higher churn.
* **Gender:** No significant relationship with churn (p > 0.05).

### **Business Recommendations**

1. **Encourage longer contracts** for month-to-month customers via discounts or rewards.
2. **Target new customers (<1 year tenure)** with engagement and onboarding offers.
3. **Review fiber optic service quality** and improve customer experience.
4. **Offer lower-priced plans or bundling options** to high-charging customers.
5. **Incentivize traditional billing** for customers at high churn risk.

### **Conclusion**

This statistical analysis shows that **contract type, monthly charges, tenure, and internet service** are strong drivers of churn.
Implementing targeted retention strategies can significantly reduce churn.
Future scope: predictive modeling to estimate churn probability for each customer.

