#This class will have various methods which will take in data and provide statistical data that can be used anywhere,

class Statistics:

    def noOfMales(self, theIncidents):
        count = 0
        for i in theIncidents:
            if (i.sex == 'Male'):
                count++
        return count

    def noOfFemales(self, theIncidents):
        count = 0
        for i in theIncidents:
            if (i.sex == 'Females'):
                count++
        return count

    def noFromGuguletho(self, theIncidents):
        count = 0
        for i in theIncidents:
            if (i.site == 'Guguletho'):
                count++
        return count

    def noFromMandalay(self, theIncidents):
        count = 0
        for i in theIncidents:
            if (i.site == 'Mandalay'):
                count++
        return count

    def noOfHivExposed(self, theIncidents):
        count = 0
        for i in theIncidents:
            if (i.hivExposed == 'Yes'):
                count++
        return count

    def noOfVaccinated(self, theIncidents):
        count = 0
        for i in theIncidents:
            if (i.vaccine == 'PCV'):
                count++
        return count
