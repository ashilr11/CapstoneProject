# This class has methods that create different plots/graphs after supplying the methods with data in forms of lists
# Each method returns a string of html code that can inserted into a html page to show the graph

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt, mpld3
import numpy as np
from io import BytesIO
import base64

class Plots:

	# creates the overview graph and returns a string of html of it.
	# Compares number of incidents, number of hiv exposed, numbers from different sites, number of different sexes.
	def createOverview(self, hivExposedList, gugulethuList, mandalayList, maleList, femaleList, serotypeList):

		groups = 26 # number of serotypes
		fig, ax = plt.subplots(figsize=(18,7.5))
		index = np.arange(groups)
		bar_width = 0.35
		opacity = 0.75
		# 5 different types of graph are plotted on the subplots namely, 2 bars, 2 lines, and 1 stem graph
		stems1 = plt.stem(index, hivExposedList, label='HIV Exposed', linefmt='C9-', markerfmt='C9x')
		rects1 = plt.bar(index, gugulethuList, bar_width, alpha=opacity, color='b', label='Gugulethu')
		rects2 = plt.bar(index + bar_width, mandalayList, bar_width, alpha=opacity, color='k', label='Mandalay')
		lines1 = plt.plot(index, maleList, marker='v', color='r', label='Males')
		lines2 = plt.plot(index, femaleList, marker='o', color='y', label='Females')

		plt.xlabel('Serotypes')
		plt.ylabel('Number Of Incidents')
		plt.xticks(index + bar_width, serotypeList)
		plt.legend()
		plt.tight_layout()
		return mpld3.fig_to_html(fig)

	# creates a graph to compare the number of hiv exposed incidents against against the number of incidents with the bacteria present
	# returns a string of html that be put into a page
	def createHivVsPresence(self, hivExposedList, presenceList):
		fig, ax = plt.subplots(figsize=(5,5))
		groups = 26
		index = np.arange(groups)

		lines1 = plt.plot(index, hivExposedList, marker='x', color='k', label='HIV Exposed')
		lines2 = plt.plot(index, presenceList, marker='o', color='y', label='Presence Of Bacteria')

		plt.ylabel('Number Of Incidents')
		plt.xlabel('Serotypes As Shown In The Order Of The Overview')
		plt.legend()
		plt.tight_layout()
		return mpld3.fig_to_html(fig)

	# creates a graph to compare the number of Vaccinated incidents against against the number of incidents with the bacteria present
	# returns a string of html that be put into a page
	def createVaccineVsPresence(self, vaccinatedList, notVaccinatedList, presenceList):
		fig, ax = plt.subplots(figsize=(5,5))
		groups = 26
		index = np.arange(groups)

		lines1 = plt.plot(index, vaccinatedList, marker='x', color='k', label='Vaccinated')
		lines2 = plt.plot(index, presenceList, marker='o', color='y', label='Presence Of Bacteria')
		#lines3 = plt.plot(index, notVaccinatedList, marker='o', color='b', label='Not Vaccinated') left out this line as it is not as useful

		plt.ylabel('Number Of Incidents')
		plt.xlabel('Serotypes As Shown In The Order Of The Overview')
		plt.legend()
		plt.tight_layout()
		return mpld3.fig_to_html(fig)

	# creates a graph to compare the 2 different sites against the number of incidents with the bacteria present
	# returns a string of html that be put into a page
	def createSitesGraph(self, gugulethuList, mandalayList):
		fig, ax = plt.subplots(figsize=(5,5))
		groups = 26
		index = np.arange(groups)

		lines1 = plt.plot(index, gugulethuList, marker='x', color='k', label='Gugulethu')
		lines2 = plt.plot(index, mandalayList, marker='o', color='y', label='Mandalay')

		plt.ylabel('Number Of Incidents')
		plt.xlabel('Serotypes As Shown In The Order Of The Overview')
		plt.legend()
		plt.tight_layout()
		return mpld3.fig_to_html(fig)
