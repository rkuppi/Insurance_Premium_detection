# Problem satement
The goal of this project was to predict insurance premium prices based on customer data, including demographic, medical, and lifestyle attributes. The aim was to assist the insurance company in offering competitive yet profitable premium plans by identifying significant risk factors and generating accurate premium estimates.
# Insurance Cost Prediction need
The primary need for this project arises from the challenges insurers face in pricing policies accurately while remaining competitive in the market. Inaccurate predictions can lead to losses for insurers and unfairly high premiums for policyholders. By implementing a machine learning model, insurers can:
- Enhance Precision in Pricing: Use individual data points to determine premiums that reflect actual risk more closely than generic estimates.
- Increase Competitiveness: Offer rates that are attractive to consumers while ensuring that the pricing is sustainable for the insurer.
- Improve Customer Satisfaction: Fair and transparent pricing based on personal health data can increase trust and satisfaction among policyholders.
- Enable Personalized Offerings: Create customized insurance packages based on predicted costs, which can cater more directly to the needs and preferences of individuals.
- Risk Assessment: Insurers can use the model to refine their risk assessment processes, identifying key factors that influence costs most significantly.
- Policy Development: The insights gained from the model can inform the development of new insurance products or adjustments to existing ones.
- Strategic Decision Making: Predictive analytics can aid in broader strategic decisions, such as entering new markets or adjusting policy terms based on risk predictions.
- Customer Engagement: Insights from the model can be used in customer engagement initiatives, such as personalized marketing and tailored advice for policyholders.
# Target Metric
Following performance are used for model evaluation and comparision on both training, test data.
- Root Mean square Error
- Mean Absolute percentage Error
- Mean square error
- R²
- Ajdusted R²

I have mostly concentrated in reducing the MAPE 

# EDA
## Univarient analysis
Histograms/box plot and bar plot are used for univarient analyis

Following are the findings 
- Age is almost evenly destributed across all age groups, so people who has opted for insurance are from all age group ranging from 18 to 66. This is actually good as we coverages for all age individuals
- Height of the individuals are not exactly exactly gaussian but it looks like gaussian destribution, with little left skew. Most of the people height lie in the range 160-180
- Weight destribution is skewed towards right, where there are very less number of people with height > 100, box plot suggests that there are some outliers with the maximum value of weight is 132Kg. But in reality, but in reality individual weight can we 132Kg. Heaviest person ever recorded is 635Kg so 132kg in this context cannot be an outlier. He keep the data as it is.
- The destribution of premium price is broadly divided into 3 categories like low (15k - 21k), medium(20k - 33k) and high (> 33k). Where most of the policies are in mid range premium which is also aligned with weight,  height and age. There are outliers in the premium price as well this could actually be a real value given the fact that individual health condition varies
- All these parameters are for individuals,  adding aditional feature <font color='Red'>Gender</font> will help us to drill down further as height weight stats will depend on gender and age.
![alt text](image.png)