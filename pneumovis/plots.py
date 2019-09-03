from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt, mpld3
import numpy as np
from io import BytesIO
import base64

class Plots:

	def createOverview(self, hivExposedList, gugulethuList, mandalayList, maleList, femaleList, serotypeList):
		# create overview plot
		groups = 26
		fig, ax = plt.subplots(figsize=(18,7.5))
		index = np.arange(groups)
		bar_width = 0.35
		opacity = 0.75

		stems1 = plt.stem(index, hivExposedList, label='Hiv Exposed', linefmt='C9-', markerfmt='C9x')
		rects1 = plt.bar(index, gugulethuList, bar_width,
		alpha=opacity,
		color='b',
		label='Guguletho')

		rects2 = plt.bar(index + bar_width, mandalayList, bar_width,
		alpha=opacity,
		color='k',
		label='Mandalay')

		lines1 = plt.plot(index, maleList, marker='o', color='r', label='Males')
		lines2 = plt.plot(index, femaleList, marker='o', color='y', label='Females')

		plt.xlabel('Serotypes')
		plt.ylabel('Number of Incidents')
		plt.xticks(index + bar_width, serotypeList)
		plt.legend()
		plt.tight_layout()
		return mpld3.fig_to_html(fig)

	def createHivVsPresence(self, hivExposedList, presenceList):
		fig, ax = plt.subplots(figsize=(5,5))
		groups = 26
		index = np.arange(groups)

		lines1 = plt.plot(index, hivExposedList, marker='o', color='k', label='Hiv Exposed')
		lines2 = plt.plot(index, presenceList, marker='o', color='y', label='Presence of bacteria')

		plt.ylabel('Number of Incidents')
		plt.xlabel('Serotypes as shown in the order of the overview')
		plt.legend()
		plt.tight_layout()
		return mpld3.fig_to_html(fig)

	def createVaccineVsPresence(self, vaccinatedList, notVaccinatedList, presenceList):
		fig, ax = plt.subplots(figsize=(5,5))
		groups = 26
		index = np.arange(groups)

		lines1 = plt.plot(index, vaccinatedList, marker='o', color='k', label='Vaccinated')
		#lines2 = plt.plot(index, notVaccinatedList, marker='o', color='b', label='Not Vaccinated')
		lines3 = plt.plot(index, presenceList, marker='o', color='y', label='Presence of bacteria')

		plt.ylabel('Number of Incidents')
		plt.xlabel('Serotypes as shown in the order of the overview')
		plt.legend()
		plt.tight_layout()
		return mpld3.fig_to_html(fig)

	def createSitesGraph(self, gugulethuList, mandalayList):
		fig, ax = plt.subplots(figsize=(5,5))
		groups = 26
		index = np.arange(groups)

		lines1 = plt.plot(index, gugulethuList, marker='o', color='k', label='Guguletho')
		lines2 = plt.plot(index, mandalayList, marker='o', color='y', label='Mandalay')

		plt.ylabel('Number of Incidents')
		plt.xlabel('Serotypes as shown in the order of the overview')
		plt.legend()
		plt.tight_layout()
		return mpld3.fig_to_html(fig)
