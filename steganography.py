import cv2
import os

def lsb1_stegano(image_path, message):
	image_array=cv2.imread(image_path, CV2.IMREAD_GRAYSCALE)

	#rendre l'image paire

	image_array=image_array-image_array%2
	#convertir le message en binaire
	binary_message=''.join(format(ord(carac), '08b') for carc in message)

	if len(binary_message)> image_array.size:
		raise Exception("La taille du message est superieur au nombre de pixel present dans l'image")


		#on écrit le message dans l'image
		nb_rows, nb_cols=image_array.shape
		print(nb_cols)
		print("_"*80)
		for index_row in range(nb_rows):
			for index_col in range(nb_cols): 
				if index_row*nb_cols+index_col< len(binary_message):
					image_array[index_row, index_col]+= int(binary_message[index_row*nb_cols+index_col])
				else:
					break



	print(image_array[:,:,:])


	cv2.imshow("aladdin", image_array)
	cv2.waitKey(0)
	cv2.destroyAllWindows()



if__name__=="__main__":
lsb1_stegano(.\steganosaure\aladdin.jpg,"")