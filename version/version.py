class Version:
	def __init__(self, version):
		import re
		m = re.match(r"^(?P<major>0|[1-9]\d*)\.(?P<minor>0|[1-9]\d*)\.(?P<patch>0|[1-9]\d*)(?:-(?P<prerelease>(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+(?P<buildmetadata>[0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$", version)
		try:
			self.major = m.group('major')
		except:  # usually AttributeError
			print(f"'{version}' is not a valid version according to https://semver.org/")
			import sys
			sys.exit(1)
		self.version = version
		self.minor = m.group('minor')
		self.patch = m.group('patch')
		# Optional fields
		self.prerelease = "-" + m.group('prerelease') if m.group('prerelease') else ''
		self.buildmetadata = "+" + m.group('buildmetadata') if m.group('buildmetadata') else ''

	def __str__(self):
		return f"{self.major}.{self.minor}.{self.patch}{self.prerelease}{self.buildmetadata}"

	def next_major(self):
		self.major = int(self.major) + 1
		self.minor = 0
		self.patch = 0
		self.prerelease = ''
		self.buildmetadata = ''

	def next_minor(self):
		self.minor = int(self.minor) + 1
		self.patch = 0
		self.prerelease = ''
		self.buildmetadata = ''

	def next_patch(self):
		self.patch =  int(self.patch) + 1
		self.prerelease = ''
		self.buildmetadata = ''

	def next_rc(self):
		import re
		m = re.match(r"^-((?P<lower>rc)|(?P<upper>RC))(?P<digit>\d+)", self.prerelease)
		if m:
			rc = m.group('lower') if m.group('lower') else m.group('upper')
			digit = int(m.group('digit')) + 1
			self.prerelease = f"-{rc}{digit}"
		else:
			self.prerelease = '-RC0'
		# self.buildmetadata = ''  # Needed ?

	def set_prerelease(self, string):
		self.prerelease = string

	def set_buildmetadata(self, string):
		self.buildmetadata = string


# v = Version("3.5.4-fdsjkhh+toto")
v = Version("3.5.4-rc0")
v = Version("3.5.4-RC10")
print(v)
v.next_rc()
print(v)
v.next_patch()
print(v)
v.next_minor()
print(v)
v.next_major()
print(v)
v.next_rc()
print(v)