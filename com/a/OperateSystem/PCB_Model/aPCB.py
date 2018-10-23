class pcb:
    'This class is Progress which uses to save data about progress'

    __status = 'reserve'

    def __init__(self, id, runTime):
        self.__id = id
        self.__runTime = runTime

    def getID(self):
        return self.__id

    def getRunTime(self):
        return self.__runTime

    def getStatus(self):
        return self.__status

    def block(self):
        self.__status = 'blocked'

    def ready(self):
        self.__status = 'ready'

    def run(self):
        self.__status = 'running'
