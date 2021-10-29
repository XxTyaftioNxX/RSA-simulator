from tkinter import *
import RSA

if __name__=="__main__":

   #creating window
   window = Tk()
   window.title("RSA Encryption and Decryption")
   window.geometry('450x650')

   #selection label 
   first = Label(window, text="Choose the prefered method of input (Default is Random Primes)", font = ('Helvetica 9 bold'))
   first.grid(column=0, row=0, columnspan=3)

   #selection between user input or random generated input
   selected = IntVar()
   rad1 = Radiobutton(window,text='Input Primes', value=1, variable=selected)
   rad2 = Radiobutton(window,text='Random Primes', value=2, variable=selected)

   select = Label(window, text="Enter values of P and Q or press 'Set' button for random values", font = (('Helvetica 9 bold')))
   select.grid(column=0, row=2, columnspan=3)

   rad1.grid(column=0, row=1, padx=5, pady=5)
   rad2.grid(column=1, row=1,padx=5, pady=5)

   #Input values for p
   p_value = StringVar()
   p_label = Label(window, text="Value for p: ")
   p_label.grid(column=0, row=3, sticky=EW, padx=5, pady=5)

   p_entry = Entry(textvariable=p_value, borderwidth=2)
   p_entry.grid(column=1, row=3, sticky=E, padx=5, pady=5)

   #Input values for q
   q_value = StringVar()
   q_label = Label(window, text="Value for q: ")
   q_label.grid(column=0, row=4, sticky=EW, padx=5, pady=5)

   q_entry = Entry(textvariable = q_value,borderwidth=2)
   q_entry.grid(column=1, row=4, sticky=E, padx=5, pady=5)

   #initializing primes as global variables
   prime1, prime2 = 0, 0

   # set_pq button
   def get_pq():   
      global prime1, prime2
      print(selected.get())
      if selected.get() == 1:
         prime1 = int(p_value.get())
         prime2 = int(q_value.get())
      else:
         prime1, prime2 = RSA.get_random_primes()
      
      #letting user confirm the primes they have selected
      pq_values.configure(text="The value for P is {} and Q is {}".format(prime1, prime2))

   #set the values for P and Q
   set_button = Button(window, text="Set p and q", command=get_pq, borderwidth=2)
   set_button.grid(column=2, row=4, sticky=E, padx=5, pady=5)

   #show the values for P and Q
   pq_values = Label(window, text="Set values for P and Q")
   pq_values.grid(column=0, row=5, columnspan=3, padx=5, pady=5)

   #initializing keys
   public, private = 0, 0

   #used to generate keys and store to global variables
   def generate():  
      global public, private
      public, private = RSA.generate_key_pair(prime1, prime2)
      output.delete(1.0, END)
      output.insert('1.0', 'Generating Keys....\nThe Public Key Pair (e, N) --> \n{}\n The Private Key Pair (d, N)--> \n{}'.format(public, private))

   #button to run generate()
   generate_keys = Button(window, text="Click to Generate Public and Private Key pairs", command=generate, borderwidth=2)
   generate_keys.grid(column=0, row=6,columnspan=2,padx=5, pady=5)  

   #output key pairs
   output = Text(window, width = 48, height=5, borderwidth=2)
   output.grid(padx=5, pady=5, columnspan=5)
   output.insert('1.0', 'Generated Keys will be shown here')

   ##Encryption

   encryption = Label(window, text="Enter the text you want to encrypt once you have generated Keys", font = ('Helvetica 9 bold'))
   encryption.grid(column=0, row=10, columnspan=3, padx=5, pady=5)

   #initilizing encrypted code since it is created as list i.e. ['12312', '123123', ....] and pass on to decrypter
   enc = 0

   #used to encrypt the user input data 
   def printInput():
      global enc
      #gathering user input
      inp = encrypt_input.get(1.0, "end-1c")
      #passing through encrypt to get the encrypted data
      enc = RSA.encrypt(public, inp)
      #deleting the existing text on screen
      encrypt_input.delete(1.0, END)
      #inserting encrypted data on to encrypt and decrypt boxes
      encrypt_input.insert("1.0", ''.join(map(lambda x: str(x), enc)))
      decrypt_input.insert("1.0", ''.join(map(lambda x: str(x), enc)))
   
   #the encrypt box for user to input data
   encrypt_input = Text(window, height = 4, width = 48, borderwidth=2)  
   encrypt_input.grid(padx=5, pady=5, columnspan=5)
   
   #button to run printInput
   encrypt_button = Button(window, text = "Encrypt", command = printInput, borderwidth=2)
   encrypt_button.grid(row=16, column=2, columnspan=2, padx=5, pady=5)

   ##Decryption

   #using list format of encrypted data to decrypt
   def printOutput():
      #recieving data to decrypt
      dec = RSA.decrypt(private, enc)
      #deleting pre-existing ciphertext in box
      decrypt_input.delete(1.0, END)
      #inserting new decrypted data
      decrypt_input.insert("1.0", dec)

   decryption = Label(window, text="Ciphertext generated above will be copied below for you to decrypt :D", font = ('Helvetica 9 bold'))
   decryption.grid(column=0, row=18, columnspan=3, padx=5, pady=5)

   #box holding ciphertext / text from printInput
   decrypt_input = Text(window, height = 4, width = 48,  borderwidth=2) 
   decrypt_input.grid(padx=5, pady=5, columnspan=5)

   #button to run printOutput
   encrypt_button = Button(window, text = "Decrypt", command = printOutput, borderwidth=2)
   encrypt_button.grid(row=20, column=2, columnspan=2, padx=5, pady=5)

   window.mainloop()