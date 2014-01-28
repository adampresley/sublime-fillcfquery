import sublime, sublime_plugin
import re

class FillCfQueryCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		#
		# Valid SQL parameter types that require quoting
		#
		quotedType = "cf_sql_char", "cf_sql_varchar", "cf_sql_timestamp"

		if len(self.view.sel()) == 1:
			if self.view.sel()[0].empty():
				print("Empty selection")

		for region in self.view.sel():
			if not region.empty():
				selectedText = self.view.substr(region)

				params = self.__populateParameters(selectedText)

				#
				# Find the position of the FROM clause
				#
				fromStart = selectedText.find("FROM")
				firstPart = selectedText[0:fromStart]
				temp = selectedText[fromStart:-1]

				if fromStart > -1:
					for param in params:
						if param["type"].lower() in quotedType:
							replacement = "'%s'" % (param["value"])
						else:
							replacement = param["value"]

						temp = temp.replace("?", replacement, 1)

					whole = firstPart + temp
					queryParamsStart = whole.find("Query Parameter Value")
					whole = whole[0:queryParamsStart]

					self.view.replace(edit, region, whole)


	def __populateParameters(self, text):
		text += "\n"
		start = text.find("Query Parameter Value")
		searchArea = ""
		params = []

		if start > -1:
			searchArea = text[start:-1].split("\n")
			del searchArea[0]

			for param in searchArea:
				m = re.match(r'Parameter\s{1}#[0-9]+\((.*?)\)\s+=\s+(.*)', param, re.M|re.I)
				groups = m.groups()
				params.append({ "type": groups[0], "value": groups[1] })

		return params


