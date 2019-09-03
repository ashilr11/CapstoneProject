# This class has various methods which will take in data and provide statistical data that can be used anywhere,
# These methods are mostly used on the home page to show overview of statistics.

class Statistics:

    # processes the number of incidents and increases the count if the swab was from a male
    def noOfMales(self, theIncidents):
        count = 0
        for i in theIncidents:
            if (i.sex == 'Male'):
                count += 1
        return count

    # processes the number of incidents and increases the count if the swab was from a female
    def noOfFemales(self, theIncidents):
        count = 0
        for i in theIncidents:
            if (i.sex == 'Female'):
                count += 1
        return count

    # processes the number of incidents and increases the count if the swab was from Gugulethu
    def noFromGugulethu(self, theIncidents):
        count = 0
        for i in theIncidents:
            if (i.site == 'Gugulethu'):
                count += 1
        return count

    # processes the number of incidents and increases the count if the swab was from Mandalay
    def noFromMandalay(self, theIncidents):
        count = 0
        for i in theIncidents:
            if (i.site == 'Mandalay'):
                count += 1
        return count

    # processes the number of incidents and increases the count if the swab contained the HIV virus
    def noOfHivExposed(self, theIncidents):
        count = 0
        for i in theIncidents:
            if (i.hivExposed == 'Yes'):
                count += 1
        return count

    # processes the number of incidents and increases the count if the swab contains traces of the vaccine
    def noOfVaccinated(self, theIncidents):
        count = 0
        for i in theIncidents:
            if (i.vaccine == 'PCV'):
                count += 1
        return count
