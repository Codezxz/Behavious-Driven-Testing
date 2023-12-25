Feature: Test a login form

Scenario: Test Login
  Given go to UH Form
  Then the title should be "Urban Health with Perfect Smiles Clinic"
  When fill the form
  Then I click next
  Then fill the form2 & click next
  Then fill the form3 & click next
  Then fill the form4 & click next
  Then validate if form is submitted
  Then verify title "Million Dollar Smi:)e"