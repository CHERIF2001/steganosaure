import cv2
import os

def lsb1_stegano(image_path, message):
	image_array=cv2.imread(image_path)

	#rendre l'image paire

	image_array=image_array-image_array%2
	#convertir le message en binaire
	binary_message=''.join(format(ord(carac), '08b') for carac in message)

	if len(binary_message)> image_array.size:
		raise Exception("La taille du message est superieur au nombre de pixel present dans l'image")


	#on écrit le message dans l'image
	nb_rows, nb_cols, nb_canals= image_array.shape
	"""print(nb_cols)
	print("_"*80)"""
	index_binary_message = 0
	for index_row in range(nb_rows):
		for index_col in range(nb_cols): 
			for index_canal in range(nb_canals):
				if index_binary_message< len(binary_message):
					image_array[index_row, index_col, index_canal]+= int(binary_message[index_binary_message])
					index_binary_message+=1
				else:
					break



	#print(image_array[:,:,:])

	cv2.imwrite("C:/HETIC/python/ala.png", image_array)
	cv2.imshow("aladdin", image_array)
	cv2.waitKey(0)
	cv2.destroyAllWindows()


if __name__=="__main__":
	lsb1_stegano("../aladdin.jpg","Hello les amis")