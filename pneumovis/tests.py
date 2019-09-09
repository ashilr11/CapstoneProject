from django.test import TestCase
from .models import Incident
from .dataHandler import DataHandler
from .statistics import Statistics

class StatsTestCase(TestCase):
    def setUp(self):
        # data same as testData csv file with 10 entries
        Incident.objects.create(participantID = "PT1", npa_a4_growth = "Growth", dateCollected = "03/04/12", presence = "Yes",
                dob = "03/04/12", sex = "Male", hivExposed = "Yes", site = "Gugulethu", serotype = "13", vaccine = "NVT", sequence = "5674")
        Incident.objects.create(participantID = "PT2", npa_a4_growth = "Growth", dateCollected = "03/04/12", presence = "Yes",
                dob = "03/04/12", sex = "Male", hivExposed = "Yes", site = "Gugulethu", serotype = "13", vaccine = "NVT", sequence = "5674")
        Incident.objects.create(participantID = "PT3", npa_a4_growth = "Growth", dateCollected = "03/04/12", presence = "Yes",
                dob = "03/04/12", sex = "Male", hivExposed = "Yes", site = "Gugulethu", serotype = "13", vaccine = "NVT", sequence = "5674")
        Incident.objects.create(participantID = "PT4", npa_a4_growth = "Growth", dateCollected = "03/04/12", presence = "Yes",
                dob = "03/04/12", sex = "Male", hivExposed = "Yes", site = "Gugulethu", serotype = "13", vaccine = "NVT", sequence = "5674")
        Incident.objects.create(participantID = "PT5", npa_a4_growth = "Growth", dateCollected = "03/04/12", presence = "Yes",
                dob = "03/04/12", sex = "Male", hivExposed = "Yes", site = "Gugulethu", serotype = "13", vaccine = "NVT", sequence = "5674")
        Incident.objects.create(participantID = "PT6", npa_a4_growth = "Growth", dateCollected = "03/04/12", presence = "Yes",
                dob = "03/04/12", sex = "Female", hivExposed = "No", site = "Mandalay", serotype = "34", vaccine = "PCV", sequence = "1884")
        Incident.objects.create(participantID = "PT7", npa_a4_growth = "Growth", dateCollected = "03/04/12", presence = "Yes",
                dob = "03/04/12", sex = "Female", hivExposed = "No", site = "Mandalay", serotype = "34", vaccine = "PCV", sequence = "1884")
        Incident.objects.create(participantID = "PT8", npa_a4_growth = "Growth", dateCollected = "03/04/12", presence = "Yes",
                dob = "03/04/12", sex = "Female", hivExposed = "No", site = "Mandalay", serotype = "34", vaccine = "PCV", sequence = "1884")
        Incident.objects.create(participantID = "PT9", npa_a4_growth = "Growth", dateCollected = "03/04/12", presence = "Yes",
                dob = "03/04/12", sex = "Female", hivExposed = "No", site = "Mandalay", serotype = "34", vaccine = "PCV", sequence = "1884")
        Incident.objects.create(participantID = "PT10", npa_a4_growth = "Growth", dateCollected = "03/04/12", presence = "Yes",
                dob = "03/04/12", sex = "Female", hivExposed = "No", site = "Mandalay", serotype = "34", vaccine = "PCV", sequence = "1884")

    def testStats(self):
        theIncidents = Incident.objects.all()
        statsObj = Statistics()
        self.assertEqual(statsObj.noOfMales(theIncidents), 5)
        self.assertEqual(statsObj.noOfFemales(theIncidents), 5)
        self.assertEqual(statsObj.noFromMandalay(theIncidents), 5)
        self.assertEqual(statsObj.noFromGugulethu(theIncidents), 5)
        self.assertEqual(statsObj.noOfHivExposed(theIncidents), 5)
        self.assertEqual(statsObj.noOfVaccinated(theIncidents), 5)

class DataHandlerTestCase(TestCase):
    def setUp(self):
        # data same as testData csv file with 10 entries
        Incident.objects.create(participantID = "PT1", npa_a4_growth = "Growth", dateCollected = "03/04/12", presence = "Yes",
                dob = "03/04/12", sex = "Male", hivExposed = "Yes", site = "Gugulethu", serotype = "13", vaccine = "NVT", sequence = "5647")
        Incident.objects.create(participantID = "PT2", npa_a4_growth = "Growth", dateCollected = "03/04/12", presence = "Yes",
                dob = "03/04/12", sex = "Male", hivExposed = "Yes", site = "Gugulethu", serotype = "13", vaccine = "NVT", sequence = "5647")
        Incident.objects.create(participantID = "PT3", npa_a4_growth = "Growth", dateCollected = "03/04/12", presence = "Yes",
                dob = "03/04/12", sex = "Male", hivExposed = "Yes", site = "Gugulethu", serotype = "13", vaccine = "NVT", sequence = "5647")
        Incident.objects.create(participantID = "PT4", npa_a4_growth = "Growth", dateCollected = "03/04/12", presence = "Yes",
                dob = "03/04/12", sex = "Male", hivExposed = "Yes", site = "Gugulethu", serotype = "13", vaccine = "NVT", sequence = "5647")
        Incident.objects.create(participantID = "PT5", npa_a4_growth = "Growth", dateCollected = "03/04/12", presence = "Yes",
                dob = "03/04/12", sex = "Male", hivExposed = "Yes", site = "Gugulethu", serotype = "13", vaccine = "NVT", sequence = "5647")
        Incident.objects.create(participantID = "PT6", npa_a4_growth = "Growth", dateCollected = "03/04/12", presence = "Yes",
                dob = "03/04/12", sex = "Female", hivExposed = "No", site = "Mandalay", serotype = "34", vaccine = "PCV", sequence = "199")
        Incident.objects.create(participantID = "PT7", npa_a4_growth = "Growth", dateCollected = "03/04/12", presence = "Yes",
                dob = "03/04/12", sex = "Female", hivExposed = "No", site = "Mandalay", serotype = "34", vaccine = "PCV", sequence = "199")
        Incident.objects.create(participantID = "PT8", npa_a4_growth = "Growth", dateCollected = "03/04/12", presence = "Yes",
                dob = "03/04/12", sex = "Female", hivExposed = "No", site = "Mandalay", serotype = "34", vaccine = "PCV", sequence = "199")
        Incident.objects.create(participantID = "PT9", npa_a4_growth = "Growth", dateCollected = "03/04/12", presence = "Yes",
                dob = "03/04/12", sex = "Female", hivExposed = "No", site = "Mandalay", serotype = "34", vaccine = "PCV", sequence = "199")
        Incident.objects.create(participantID = "PT10", npa_a4_growth = "Growth", dateCollected = "03/04/12", presence = "Yes",
                dob = "03/04/12", sex = "Female", hivExposed = "No", site = "Mandalay", serotype = "34", vaccine = "PCV", sequence = "199")

    def testStats(self):
        theIncidents = Incident.objects.all()
        dataHandler = DataHandler()
        neededArray = [[0,0,0,5,5,5,5,5],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[5,5,5,0,0,5,5,0],[0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
        self.assertEqual(dataHandler.handleData(theIncidents), neededArray)
