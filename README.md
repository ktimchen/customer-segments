# Customer Segmentation
Goal: Identify Customers from a Mailout Campaign.

<p align="center">
 <img src=clusters.png>
</p>

This project is based on the data from Arvato Financial Solutions (https://www.kaggle.com/c/udacity-arvato-identify-customers/data). In the project, a mail-order sales company in Germany is interested in identifying segments of the general population to target with their marketing in order to grow. Demographics information has been provided for both the general population at large as well as for prior customers of the mail-order company in order to build a model of the customer base of the company. The target dataset contains demographics information for targets of a mailout marketing campaign. The objective is to identify which individuals are most likely to respond to the campaign and become customers of the mail-order company.


This project consists of the following notebooks:

- Identify_Customer_Segments_Data_Wrangling.ipynb
- Identify_Customer_Segments-Clustering.ipynb

The first notebook, Identify_Customer_Segments_Data_Wrangling.ipynb, contains the following steps:
 - Preprocessing:
   - Converting missing value codes to NaNs
   - Removing the columns with 30% to 90% of data missing 
   - Assessing missing data in each row
 - Re-encoding features:
   - re-encoding categorical features
   - engineering mixed-value features
 - Cleaning function based on the previous steps:
   - clean_data.py

The second notebook, Identify_Customer_Segments-Clustering.ipynb, implements the following steps:
 - Feature transformation:
   - feature scaling
   - dimensionality reduction
   - interpretaion of the principal components
 - Clustering:
   - clustering of the general population
   - clustering of the customer data
 - Comparison of the general population and customers
 
 
 
 
 
 
 
 
 


