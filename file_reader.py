class FileReader:
	def load(self, lang):
		fname = 'commands/'+lang+'.txt'
		phrase2CmdMap = {}
		with open(fname) as f:
			lines = f.readlines()
			for line in lines:
				(phrase, cmd) = line.decode('utf-8').split(":",2)
				phrase2CmdMap[phrase.strip()] = cmd.strip()
		print phrase2CmdMap
		return phrase2CmdMap
