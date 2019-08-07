# This creates a record for a participant
# There is one record for each particpant
# The records shows a merge of all incidents regarding the participant

class records:
    def __init__(participantNo, npa_a4_growth, dateCollected, presence, dateOfBirth, sex, hivExposed, site, serotype, sequenceType, vaccineStatus):
        self.participantNo = particpantNo
        self.npa_a4_growth = npa_a4_growth
        self.dateCollected = dateCollected
        self.presence = presence
        self.dateOfBirth = dateOfBirth
        self.sex = sex
        self.hivExposed = hivExposed
        self.site = site
        self.serotype = serotype
        self.sequenceType = sequenceType
        self.vaccineStatus = vaccineStatus
