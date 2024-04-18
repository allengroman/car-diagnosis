import unittest
from Chatbot import getChat, getDiagnosis, askQuestion, getParts, partsList  # Import your module here

class TestChatbotFunctions(unittest.TestCase):

    def test_getChat(self):
        question = "What should I check if my car won't start?"
        expected = "Check the battery, starter motor, and ensure the car is not out of fuel."
        result = getChat(question)
        self.assertIn("battery", result)  # Just an example of check

    def test_getDiagnosis(self):
        carDetails = "2010 Ford Mustang"
        carIssue = "Engine makes strange noise when accelerating."
        result = getDiagnosis(carDetails, carIssue)
        self.assertIn("engine", result.lower())  # Expected to mention engine in the diagnosis

    def test_askQuestion(self):
        carIssue = "Leaking oil"
        carDetails = "2008 Honda Civic"
        carDiagnosis = "Oil pan gasket failure"
        userQuestion = "How do I fix it?"
        result = askQuestion(carIssue, carDetails, carDiagnosis, userQuestion)
        self.assertIn("replace", result.lower())  # Check if the answer includes suggestion to replace something

    def test_getParts(self):
        carIssue = "Brake failure"
        carDetails = "2012 Toyota Corolla"
        carDiagnosis = "Worn out brake pads"
        result = getParts(carIssue, carDetails, carDiagnosis)
        self.assertTrue(isinstance(eval(result), list))  # Ensure it returns a list

    def test_partsList(self):
        partsString = '[["Brake pads", 4, 35.50]]'
        result = partsList(partsString)
        self.assertEqual(result, [["Brake pads", 4, 35.50]])  # Check for accurate conversion

# Run the tests
if __name__ == '__main__':
    unittest.main()
