import zmq

class ZMQServer(object):

	def __init__(self,context=None):
		self.rep="tcp://127.0.0.1:4500"
		self.req="tcp://127.0.0.1:4501"

		self.context=context or zmq.Context.instance()
		self.reqSock=self.context.socket(zmq.REQ)
		self.repSock=self.context.socket(zmq.REP)
		self.dealerSock=self.context.socket(zmq.DEALER)
		self.routerSock=self.context.socket(zmq.ROUTER)

		self.porxy=zmq.proxy(self.router,self.dealer)

		self.runServer()
		time.sleep(1)
		self.runProxy()
		self.runClient()

	def runServer(self):
		while True:
			self.repSock.bind(self.rep)
			data=self.repSock.get()
			print(data)

	def runProxy(self):
		self.dealerSock.connect(self.rep)
		self.routerSock.bind(self.req)

	def runClient(self):
		self.reqSock.connect(self.req)
		for i in range(100):
			self.reqSock.send(i)
