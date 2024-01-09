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

	cv2.imwrite("../watermarked_image.png", image_array)
	cv2.imshow("aladdin", image_array)
	cv2.waitKey(0)
	cv2.destroyAllWindows()


def lsb1_extract_message(watermarked_image_path):
	watermarked_image_array = cv2.imread(watermarked_image_path)
	binary_array_message = watermarked_image_array % 2


# On flatten la matrice binaire qui contient le message caché
	nb_rows, nb_cols, nb_canals= watermarked_image_array.shape
	binary_message_list = []

	for index_row in range(nb_rows):
		for index_col in range(nb_cols):
			for index_canal in range(nb_canals):				
				binary_message_list.append(str(binary_array_message[index_row, index_col, index_canal]))


	"""print(binary_message_list)
	print("_"*80)"""
# On élimine les caractères vides 
	for index_binary_char in range(0, nb_rows*nb_cols*nb_canals,8):
		if binary_message_list[index_binary_char: index_binary_char+8] ==["0"]*8:
			binary_message_list = binary_message_list[: index_binary_char]  #le slicing
			break
	#print(binary_message_list)

# On convertit le message binaire pour recupérer le message caché 
	binary_message = "".join(binary_message_list)
	message = "".join([chr(int(binary_message[i:i+ 8], 2)) for i in range(0, len(binary_message),8)])

	print(message)




if __name__=="__main__":
	lsb1_stegano("../aladdin.jpg","Hello les amis")
	lsb1_extract_message("../watermarked_image.png")