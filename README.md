# Final_Project_Cars
Introduction: This is an end-to-end analysis of used cars in Spain. It includes: 1; ETA 2; EDA 3; Tableau visualization (https://public.tableau.com/app/profile/sergio6080/viz/SecondhandcarsFinalProyect/FP?publish=yes) 4; Price predictor app.
Presentation:https://docs.google.com/presentation/d/1_ITZjGJTpLLUplaK6BSL-e-NtU7w1DjRAMUAJOTcvd4/edit?usp=sharing
The data was extracted by web scraping from https://www.autocasion.com/ and used an XGBoost Machine Learning model to predict prices given the features.

Business case Sometimes is hard to find a way how to start analyzing cars when you want to buy one. Even if you have access to a marketplace and you can filter by the specs you are looking for you get this kind of issue: What is the average mileage for the car I'm looking for from all of the cars? How much is too much millage? How can I compare them between all the options, and how to know if the relationship between price/mileage is the best? What if I'm looking for a specific car not available at the moment? What would be the price market?

Well, with this analysis you can solve all these questions and make an intelligent decision based on actual data available at the moment.

Files included: 1.Autocasion_Scrip_for_Scraping_main_page (autocasion_unique.csv) 2.Script_scraping_specs_List1,2,3,4,5,6,7,8 for multiple webscraping (autocasion_unique_ind_with_links1,2,3,4,5,6,7,8.csv) 3.ETA autocasion DB (main_car_database.csv) 4.EDA autocasion (main_car_database_for_ML.csv) 5.Machine Learning ML Script ML XGBoost

Datasets: 1.autocasion_unique.csv 2.autocasion_unique_ind.csv 3.autocasion_unique_ind_with_links1,2,3,4,5,6,7,8.csv 4.main_cardatabse.csv

Pickles:

model.p
xtest.p
ytest.p
maker_vals.p
App file: 1.flas_ml 1.1 static (css) 1.2 templates (html) 2. app.py 3. xtest.p 5. ytest.p 5. maker_vals.p
