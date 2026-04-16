# Serverless Spark ETL Pipeline on AWS

## 📌 Project Overview

This project demonstrates the implementation of a fully automated, event-driven serverless ETL pipeline using AWS services. The pipeline processes raw product review data stored in Amazon S3 using an AWS Glue Spark job, triggered automatically by AWS Lambda upon file upload.

---

## 🎯 Objective

* Build an automated, event-driven data pipeline
* Process and transform raw CSV data using PySpark
* Generate analytical insights using Spark SQL
* Store processed and aggregated results in Amazon S3

---

## 🏗️ Architecture

S3 (Landing Bucket) → Lambda Trigger → AWS Glue (Spark ETL Job) → S3 (Processed + Analytics Output)

---

## 📂 Dataset

* File: `reviews.csv`
* Columns:

  * review_id
  * product_id
  * customer_id
  * rating
  * review_date
  * review_text

---

## ⚙️ AWS Services Used

### 1. Amazon S3

* Landing Bucket: Stores raw input data (`reviews.csv`)
* Processed Bucket: Stores cleaned data and analytics results

---

### 2. AWS Lambda

* Function Name: `start_glue_job_trigger`
* Trigger: S3 Object Created event
* Purpose: Automatically starts the Glue ETL job when new data is uploaded

---

### 3. AWS Glue (Spark ETL)

* Job Name: `process_reviews_job`
* Script Language: PySpark
* Responsibilities:

  * Read raw CSV data from S3
  * Perform data cleaning and transformations
  * Execute Spark SQL queries
  * Write processed data and results back to S3

---

### 4. AWS IAM

* Role: `AWSGlueServiceRole-Reviews`
* Permissions:

  * S3 access
  * Glue job execution
  * Lambda permission to start Glue job

---

### 5. Amazon CloudWatch

* Used for monitoring:

  * Lambda execution logs
  * Glue job logs
* Helps in debugging and tracking pipeline execution

---

## 🔄 Data Pipeline Workflow

1. Upload `reviews.csv` to the S3 landing bucket
2. S3 event triggers Lambda function
3. Lambda invokes AWS Glue job
4. Glue job:

   * Cleans and transforms data
   * Runs Spark SQL queries
5. Outputs are written to S3 processed bucket

---

## 🧪 Transformations Performed

* Cast `rating` to integer and handle null values
* Convert `review_date` to proper date format
* Fill missing `review_text` with default value
* Normalize `product_id` to uppercase

---

## 📊 Analytical Queries

### 1. Average Rating per Product

* Calculates average rating and total reviews per product

### 2. Date-wise Review Count

* Computes number of reviews submitted per day

### 3. Top 5 Most Active Customers

* Identifies customers with highest number of reviews

### 4. Rating Distribution

* Counts number of reviews per rating value (1–5)

---

## 📁 Output Structure

```id="x3m4q2"
processed-bucket/
  ├── processed-data/
  └── Athena Results/
        ├── daily_review_counts/
        ├── top_5_customers/
        ├── rating_distribution/
```

---

## 🚀 How to Run

1. Upload `reviews.csv` to the S3 landing bucket
2. Lambda triggers automatically
3. Glue job runs and processes data
4. Check processed S3 bucket for outputs

---

## ⚠️ Challenges & Solutions

### 1. Lambda Timeout Issue

* Problem: Lambda timed out while triggering Glue job
* Solution: Increased timeout from 3 seconds to 15 seconds

### 2. Permission Errors

* Problem: Lambda unable to start Glue job
* Solution: Added `glue:StartJobRun` permission

### 3. Concurrent Execution Error

* Problem: Multiple triggers caused concurrent job execution error
* Solution: Ensured single execution or handled retries

---

## 💡 Key Learnings

* Building event-driven serverless pipelines
* Working with AWS Glue for Spark-based ETL
* Using Lambda for orchestration
* Handling real-world debugging scenarios (timeouts, permissions)
* Writing Spark SQL queries for analytics

---

## 📌 Conclusion

This project demonstrates how AWS serverless services can be combined to build a scalable and automated data pipeline. The use of Lambda and Glue eliminates manual intervention, enabling efficient and real-time data processing.

---
