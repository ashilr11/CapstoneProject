#This class will have various methods which will take in data and provide statistical data that can be used anywhere,

class Statistics:

    def noOfMales(self, theIncidents):
        count = 0
        for i in theIncidents:
            if (i.sex == 'Male'):
                count += 1
        return count

    def noOfFemales(self, theIncidents):
        count = 0
        for i in theIncidents:
            if (i.sex == 'Female'):
                count += 1
        return count

    def noFromGugulethu(self, theIncidents):
        count = 0
        for i in theIncidents:
            if (i.site == 'Gugulethu'):
                count += 1
        return count

    def noFromMandalay(self, theIncidents):
        count = 0
        for i in theIncidents:
            if (i.site == 'Mandalay'):
                count += 1
        return count

    def noOfHivExposed(self, theIncidents):
        count = 0
        for i in theIncidents:
            if (i.hivExposed == 'Yes'):
                count += 1
        return count

    def noOfVaccinated(self, theIncidents):
        count = 0
        for i in theIncidents:
            if (i.vaccine == 'PCV'):
                count += 1
        return count
