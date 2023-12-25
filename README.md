# BDD-Testing

Installation Instructions

Create a 'Virtual Environment' :

    python -m venv env


Activate your 'Virtual Environment' :

    Linux   : Source ./env/bin/activate

    Windows : env\Scripts\activate
    
Clone this Repository :

    git clone https://github.com/Urbano-InfoTech/BDD-Testing.git
    
Install the dependencies :

    pip install -r requirements.txt
    
Navigate to the Folder containing the code :

    cd BDD-Testing/features
    
Run the code:

    behave example.feature

Output:
   
    
    Feature: Test a login form # example.feature:1
    
     Scenario: Test Login                                                  # example.feature:3

       Given go to UH Form                                                 # steps/testOne.py:15 2.838s
       Then the title should be "Urban Health with Perfect Smiles Clinic"  # steps/testOne.py:19 0.009s
       When fill the form                                                  # steps/testOne.py:27 0.229s
       Then I click next                                                   # steps/testOne.py:54 0.054s
       Then fill the form2 & click next                                    # steps/testOne.py:63 0.207s
       Then fill the form3 & click next                                    # steps/testOne.py:72 0.704s
       Then fill the form4 & click next                                    # steps/testOne.py:114 0.321s
       Then validate if form is submitted                                  # steps/testOne.py:136 5.444s
       Then verify title "Million Dollar Smi:)e"                           # steps/testOne.py:149 0.008s

    1 feature passed, 0 failed, 0 skipped
    1 scenario passed, 0 failed, 0 skipped
    9 steps passed, 0 failed, 0 skipped, 0 undefined
    Took 0m9.814s
    
About:

    This code contains 'Behave features' and 'Selenium' code that is designed to 'Test' the functionalities of 'Urban Health with Perfect Smiles Clinic' form. (https://form.care4all.in/students/80312666)
