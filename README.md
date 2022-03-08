# QIAML
The goal of this project is to produce a model that accurately detects quantifies fluorescent nucleation sites of DNA amplification. Previous work in the Posner Research group has shown that these fluorescent nucleation sites correlate with the concentration of initial DNA concentration [1].

## Motivation
### Abstract
Nucleic Acid Tests (NATs) detect nucleic acid from disease and infection. Detection is based on amplifying low levels of DNA/RNA allowing for detection of a single strand of DNA/RNA. The gold standard for quantitative nucleic acid testing is quantitative polymerase chain reaction (qPCR). However, qPCR is:
* slow
* expensive 
* fragile 

Isothermal DNA amplification technologies, like recombinase polymerase amplification (RPA) have been put forth that are faster, cheaper, and more robust than qPCR. Yet isothermal amplification technologies are limited in their diagnostic capabilities as they are qualitative. However, **Recent studies in the Posner Lab Group have shown that RPA, an isothermal NAT, can also be quantitative through a spot nucleation to initial copy correlation** [1]. Similar nucleation site analysis has been applied to other assays and targets and used ML to produce a quantification model which rivals our linear range [2]. Thus, we are interested in applying ML models to improve the linear range of our assay.
1.  Quantitative Isothermal Amplification on Paper Membranes using Amplification Nucleation Site Analysis
Benjamin P. Sullivan, Yu-Shan Chou, Andrew T. Bender, Coleman D. Martin, Zoe G. Kaputa, Hugh March, Minyung Song, Jonathan D. Posner
bioRxiv 2022.01.11.475898; doi: https://doi.org/10.1101/2022.01.11.475898 
2. Membrane-Based In-Gel Loop-Mediated Isothermal Amplification (mgLAMP) System for SARS-CoV-2 Quantification in Environmental Waters
Yanzhe Zhu, Xunyi Wu, Alan Gu, Leopold Dobelle, Clément A. Cid, Jing Li, and Michael R. Hoffmann
Environmental Science & Technology 2022 56 (2), 862-873
DOI: 10.1021/acs.est.1c04623


### Further details
In the diagnostic world, quantitative nucleic acid amplification tests (qNAATS) are the gold standard for viral load monitoring which indicates viral suppression and infectivity. The workhorse qNAAT is quantitative polymerase chain reaction (qPCR). A recent advancement in qNAATs is digital droplet qPCR (ddPCR). In ddPCR single copies of DNA are isolated in microbubbles then amplified and fluorescently tagged. Then the number of fluorescent microbubbles is counted to gain an absolute initial concentration. Both tools require major investment in laboratory infrastructure, personnel, and equipment-making the best qNAATs unattainable for low-middle income countries. Thus, there has been a desired to replace traditional qPCR workflows with cheaper and more robust isothermal nucleic acid amplification (INAT) methods. INATs are considered non-quantitative due to the lack of traditional markers seen in qPCR. Other groups have tried to correlate absolute fluorescence with initial copy number with little success and INATs are considered qualitative. Recent work in the Posner Lab Group has shown that RPA, an INAT, has the potential to be used as a qNAAT. In this work, RPA reactions are conducted on a fibrous paper pad resulting in DNA nucleation sites (spots/dots). Furthermore, there is a strong correlation between the number of dots and initial DNA concentration with a linear range of 25-1,000 initial copies of DNA. Thus, counting spots and creating a method to quantitate DNA will elevate RPA, an INAT to the level of qPCR that can be conducted, faster, cheaper, and at the point of care.

## Methods
### Import Images
Due to their size, all data set images are cropped and pre-processed using the ``auto_crop.py``. This function isolates the green fluorescent channel (the detection channel of our FAM fluorophore) applied an adaptive blurring and contrasting to the images to improve visual representation. The images are then cropped based on contours of the image, and saved as a 2D NumPy array in an .npy file. To access the images, the ``get_data.py`` file reads in the .npy and saves the data arrays as either a NumPy array or a pandas dataframe. The data available is triplicate images of the end point of the RPA reaction. To ensure the train and test splits contain all data in the range of interest (3-10,000 cp) the triplicate data is split into train and test groups. Here the data in AB,BC, or AC represent the train groups while A, B, or C are the test groups for the training sets BC, AC,AB respectively.
### Other pre ML processing 
Describe here 
### Model training  
Describe here 
### Inital Input Correlation 
Describe results here

## Usage
Code runs with...

# QIAML

Quantitative Isothermal Amplification Machine Learning
goals:
  - cnn-classification 
  - skikit leran 
  - tensor flow
  - patters-unsuperviiers
  -   intensity prediction 
  - supervised-features-target goal 
  - need x and target value for ML
  - classification- 
 what’s the problem 
 who are the users and skill level
 is the user a developer of diagnostics what to expect
 what makes this a success-linearizing the range of response
 how much data do we have
