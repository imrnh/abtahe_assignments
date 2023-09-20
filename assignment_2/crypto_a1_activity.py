#import cryptography
from cryptography.fernet import Fernet # for encryption and decryption
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes
import base64
import sys
# if you get an error on the above line, you might need to run 
# pip install INSERT_LIBRARY_NAME or install the library another way.

#Below are some TODO comments.


def file_read(file_name):
    _file = open(file_name, "r")
    file_contents = _file.read()
    _file.close()
    return file_contents


def file_write(file_name, open_mode , file_contents):
    try:
        _file = open(file_name, open_mode)
        _file.write(file_contents)
        _file.close()
    except:
        raise "File write Error"
    
    return None


def generate_mq_key(key_string="please don't use the default"):
    if(len(key_string)<32):
       key_string = str(key_string + "abcdefghijklmnopqrstuvwxyz012345")
    key_string = key_string[0:32]
    key_string_bytes = str(key_string).encode("ascii")
    key = base64.urlsafe_b64encode(key_string_bytes)
    return key

def encrypt_file(input_filename, output_filename, key = ""):
    try:
        file_contents = file_read(input_filename)  # reading the decrypted data from the input file.
        file_contents = file_contents.encode('utf-8') # converting the string type data int bytes.
        fernet = Fernet(key)
        encrypted_data = fernet.encrypt(file_contents) #encrpyting the data using Fernet.
        writing_status = file_write(output_filename, "wb", encrypted_data) #writing the data into the output file.
        return True
    except: #if any issue raised during file write, the task is not considered complete.
        return False
    

    #TODO: use fernet, open the file input_filename
    #read and encrypt the contents of the file
    #store the encrypted contents in another file who's name
    #is stored in output_filename
    #https://cryptography.io/en/latest/fernet/


def decrypt_file(input_filename, output_filename, key = ""):
    try:
        file_contents = file_read(input_filename)  # reading the encrypted data from the file.   
        fernet = Fernet(key)
        decrypted_data = fernet.decrypt(file_contents) #decrpyting the data using Fernet.
        writing_status = file_write(output_filename, "wb", decrypted_data) #writing the data into the output file.
        return True
    except: #if any issue raised during file write, the task is not considered complete.
        return False


def generate_hash(input_filename, output_filename, key = ""):
    try:
        file_contents = file_read(input_filename)
        sha256_obj = hashes.Hash(hashes.SHA256())
        file_contents = file_contents.encode('utf-8') #converting the string type file content into bytes.
        sha256_obj.update(file_contents)
        gen_hash = sha256_obj.finalize().hex() #if hex value is not required, please remve the .hex() function call.
        file_write(output_filename, "w", gen_hash)
        return True
    except:
        return False
    


###############################################################################

def task_1(student_id,input_file_name , output_file_name):
    key = generate_mq_key(str(student_id)) # generating key for decryption.
    if (decrypt_file(input_file_name, output_file_name, key)):
        print("Completed Task 1")


def task_2(student_id, input_file_name , output_file_name):
    # python   crypto_a1_activity.py   YOUR_STUDENT_NUMBER  task2   datafile.encrypted   datafile_enc_decr
    key = generate_mq_key(str(student_id))
    if (encrypt_file(input_file_name, output_file_name, key)):
        print("Completed Task 2")


def task_3(student_id, input_file_name , output_file_name):
    try:
        encrypt_file(input_file_name,  "temp_task3.txt", student_id) # storing the encrypted data into a temporary file called temp_task3.txt
        decrypt_file("temp_task3.txt", output_file_name, student_id) # read data from temp file and decrypt it.
        print("Success")
        print("Completed Task 3")
    except:
        print("not success")


def task_4(student_id, input_file_name , output_file_name):
    if (generate_hash(input_file_name, output_file_name, student_id)):
        print("Completed Task 4")


def task_5(student_id, input_file_name , output_file_name):
    if (generate_hash(input_file_name, output_file_name, student_id)):
        print("Completed Task 5")

###############################################################################
#You don't need to edit anything below here.
def main():
    if len(sys.argv) < 5:
        print("not enough arguments have been entered. Use the following format from the IDE console:")
        print("\npython crypto_a1_activity.py 41234567 task1 inputFileName outputFileName\n\nor")
        print("\npython3 crypto_a1_activity.py 41234567 task1 inputFileName outputFileName\n\n")
    else:
        student_id = sys.argv[1] # student ID
        encryption_actitiy = sys.argv[2] # encrypt, decrypt, or hash
        input_file_name = sys.argv[3]
        output_file_name = sys.argv[4]
        if(encryption_actitiy == "task1"):
            task_1(student_id,input_file_name , output_file_name)

        elif(encryption_actitiy == "task2"):
            task_2(student_id,input_file_name , output_file_name)

        elif(encryption_actitiy == "task3"):
            task_3(student_id,input_file_name , output_file_name)

        elif(encryption_actitiy == "task4"):
            task_4(student_id,input_file_name , output_file_name)

        elif(encryption_actitiy == "task5"):
            task_5(student_id,input_file_name , output_file_name)
        else:
            print("couldn't work out what to do.")
            print("Please use the following format when running the file:\n")
            print("python   crypto_a1_activity.py   STUDENT_NUMBER  ACTIVITY   INPUT_FILENAME   OUTPUT_FILENAME")
            print("\nACTIVITY can be any of the following words:")
            print("task1")
            print("task2")
            print("task3")
            print("task4")
            print("task5")



if __name__ == "__main__":
    main()