###Data Processing


**Table of Contents**
- Data
- Genre Classification 
- Data Cleaning 
	- Filtering
	- Merging Tracks
	- Saving Pianorolls
- Generate Bars & Phrases
	- Segmentation
	- Collecting Data



###Data
The processed data are already attached in the project. If you would like to create your own dataset for training, please first download the following data sources: 

LMD Matched : http://hog.ee.columbia.edu/craffel/lmd/lmd_matched.tar.gz

LMD Matched Metadata : http://hog.ee.columbia.edu/craffel/lmd/lmd_matched_h5.tar.gz

LPD5 Cleansed :
https://drive.google.com/uc?id=1XJ648WDMjRilbhs4hE3m099ZQIrJLvUB&export=download

You will need to decompress the data using tar xvzf commands. Example is simply: 

`$ tar xvzf lmd_matched.tar.gz`


### Genre Classification 
To train the model with different genres, we are using LMD-metadata to help us identify the different genres using author information, which is artist_terms_freq to determine the most likely genre. 

To run the processing pipeline, please refer to the genre_selection.py for how to perform genre classification. The output is a npy file containing the file directories pointing to a list of midi files in the lmd_matched dataset. 

### Data Cleaning 

Data cleaning is performed for removing the invalid midi files such that all files will be starting at time 0 and 4/4 time.  To do so, follow the Data_Cleaning jupyter notebook by changing the file directories as well as the number of files to generate in order to complete the data pipeline.  Steps in the pipeline such as data filtering, merging tracks and saving pianorolls should be the same for each genre to be generated.

### Generate Bars and Phrases

In this step, the saved data will be further segmented into musically meaningful bars and phrases.  The number of bars are determined by the sampling rate, and the number of phrases is determined by the Structual Features algorithm. 

To do so, simply following the second part in the data cleaning notebook to generate the result.

##### Segmentation 

Afterwards, simply run the two commands in matlab with the correct file directory to generate phrases: 

main_label.m
main_seg.m 

##### Collecting Data

The last step is to collect the result, simply run the gen_data_bar.py to save the generated bars and phrases. The train, validation and test data will be saved in data_phr folder. 


