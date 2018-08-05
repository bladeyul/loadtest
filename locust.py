from locust import HttpLocust,TaskSet,task
import json
from queue import Queue

#test upload and download MaterialPackage
class MaterialPackage(TaskSet):
    min_wait = 3000 * 60 * 10
    max_wait = 5000 * 60 * 30

    @task(1)
    def downloadMaterialPackage(self):
        pass

    @task(1)
    def uploadMaterialPackage(self):
        pass


#test algorithms run
class Algorithms(TaskSet):
    min_wait = 3000 * 60 * 10
    max_wait = 5000 * 60 * 30

    @task(1)
    def startAlgorithms(self):
        params = {}
        res = self.client.get("/dldmp/algorithms/getMark")
        if self.status_code == 200:
            if json.loads(res.json())['result']:
                res.success()

    def startDetectAlgorithms(self):
        params={}

#test mark get and insert
class Mark(TaskSet):

    @task(1)
    def getMark(self):
        params = {}
        res = self.client.get("/dldmp/mark/getMark")
        if self.status_code == 200:
            if json.loads(res.json())['result']:
                res.success()



    @task(5)
    def setMark(self):
        params={}
        res=self.client.post("/dldmp/mark/setMark")
        if self.status_doe==200:
            if json.loads(res.json())['result']:
                res.success()




#test Media play
class Meida(TaskSet):
    min_wait=1000*60*10
    max_wait=1000*60*30

    @task(10)
    def getMedia(self):
        params={}


class DataPrepare(object):

    @classmethod
    def prepareMediaData(cls):
        cls.mediaQueue=Queue()
        for i in range(60):
            for j in range(1,6):
                fileName=str(i)+'/'+str(j)+'.mp4'
                params={"fileName":fileName}
                cls.mediaQueue.put(params)
        return cls.mediaQueue

    @classmethod
    def prepareUploadData(cls):
        cls.uploadQueue=Queue()
        for i in range(10):
            for j in range(10):
                fileName=str(i)+'/'+str('j')+'.zip'
                params={}
                cls.mediaQueue.put(params)
        return cls.mediaQueue

    @classmethod
    def prepareDownloadData(cls):
        cls.uploadQueue=Queue()
        for i in range(10):
            for j in range(10):
                fileName=str(i)+'/'+str('j')+'.zip'
                params={}
                cls.mediaQueue.put(params)
        return cls.mediaQueue

class DldmpTest(HttpLocust):
    mediaQueue=DataPrepare.prepareMediaData()
    uploadQueue=DataPrepare.prepareUploadData()
    downloadQueue=DataPrepare.prepareDownloadData()

    task_set=[MaterialPackage,Algorithms,Mark,Meida]


