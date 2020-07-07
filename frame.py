from csv import DictReader
from pytube import YouTube
import librosa
import librosa.display
import matplotlib.pyplot as plt
import sklearn
import os


class Frame:

	def create_image(self, title, start, end):
		wav, s = librosa.core.load(title + '.mp4', sr = 44100)

		wav = wav[start:end]
		#MFCC  feature extraction automatically performs framing . Th default value for the noOfMFCC = 20
		 
		mfcc = librosa.feature.mfcc(wav, sr = 44100)

		print(mfcc.shape)

		# Feature scaling , so that the feature with higher magnitude does not become main deciding feature
		mfcc = sklearn.preprocessing.scale(mfcc, axis=1)

		#Creation of the image
		fig = plt.figure()

		ax = fig.add_subplot(111)

		ax.axes.get_xaxis().set_visible(False)

		ax.axes.get_yaxis().set_visible(False)

		ax.set_frame_on(False)

		librosa.display.specshow(mfcc, sr=44100, x_axis='time' , cmap = 'gray_r')
		
		#Saving the image
		fig.savefig(title + '.png')
		print('Image Created')

	#Function to parse the csv files and create list of those youtube items with the required Label.
	def list_of_cry(self, csv_file):

		l1 = []
	
		with open(csv_file) as file:
			csv_res = DictReader(file)
			for elem in csv_res:
				s = elem['positive_labels']
				x = s.split(',')
				for st in x:
					if st == '/t/dd00001':
						l1.append(elem)
		
		for var in l1:
			print(var)
		print(len(l1))
		return l1

	def download_yt(self, list_of_csv, dire, count_of_images):

		i = 1 
		dick = {}
		flag = False
		for row in list_of_csv:
			vid = row['YTID']
			start = int(float(row['start_seconds']))*44100
			end = int(float(row['end_seconds']))*44100
			url = 'https://www.youtube.com/watch?v='+vid
			j = 0
			while True:
				#Many times downloading fails, this is to specify attempt 20 times before giving up for a video
				j = j + 1
				if j > 20:
					break
				try:
					yt = YouTube(url)
					stream = yt.streams.filter(only_audio=True).all()
					stream = stream[0]
					print(yt.title)
					print(stream.download(dire, filename=str(i)))
					flag = True
				except Exception as e:
					print(e)
					print('Attempt ' + str(j))
					continue
				break
			if flag == True:
				self.create_image(str(i), start, end)
				i = i + 1
				if i > count_of_images:	
					break
			flag = False

def main():
	f = Frame()
	#test.csv file is the csv file downloaded from Audioset which contains the annotated list of youtube videos for over 500 classes.
	cry = f.list_of_cry('test.csv')
	#Directory of the download
	dire = '/home/blackbrd/Desktop/Pratyush/Projects/youtube-dl-master'
	count_of_images = 6
	f.download_yt(cry, dire, count_of_images)
	

if __name__ == '__main__':
	main()

















