from subprocess import Popen, PIPE
from sys import argv
from tkinter import filedialog

def get_hammer_distance(A: str, B: str):
    distance = 0
    error_str = ""
    if len(A) != len(B):
        distance += abs(len(A) - len(B))

    str_length = len(A) if len(A) < len(B) else len(B)
    for i in range(str_length):
        if A[i] != B[i]:
            distance += 1
            error_str += '^'
        else:
            error_str += ' '
    for i in range(str_length, len(error_str)):
        error_str += '^'
    return distance, error_str

def get_subject_name():
    file_name = filedialog.askopenfilename()
    valid_name = False
    while not valid_name:
        try:
            open(file_name, 'r')
        except:
            print("Not a valid file")
            file_name = input("Enter file path:")
        else:
            valid_name = True
    return file_name

def test_subject(subject_name):
    try:
        input_file = open("test_input.txt", 'r')
        output_file = open("test_output.txt", 'r')
    except:
        print("Could not open input or output test files")
        return

    output_data = output_file.readlines()
    input_data = input_file.readlines()

    print("Opening program...")
    process = Popen(['python', subject_name], stdout=PIPE, stderr=PIPE, stdin= PIPE)
    print("Writing to program...")
    for line in input_data:
        print("Input: ", line)
        process.stdin.write( bytes(line, encoding = "utf-8"))
    print("Retreiving output...")

    test_output, errors = process.communicate()
    test_output = str(test_output)
    test_output = test_output[2:]
    test_output = test_output[:-1]
    test_output = test_output.replace("\\n", "\n")
    test_output = test_output.replace("\\r", "")
    test_output = test_output.replace("\\xe4", "ä")
    test_output = test_output.replace("\\xf6", "ö")
    test_output = test_output.split("\n")
    if errors != "":
        print("File had error:\n", errors)

    line_counter = 0
    error_counter = 0
    error_list = []

    for line in test_output:
        if line_counter >= len(output_data):
            break
        output_data[line_counter] = output_data[line_counter].replace("Ã¤", "ä")
        output_data[line_counter] = output_data[line_counter].replace("Ã¶", "ö")
        if line != output_data[line_counter]:
            hammer_distance, error_str = get_hammer_distance(line, output_data[line_counter])
            if hammer_distance > 1:
                print("**********************************")
                print("Wrong answer at line ", line_counter)
                print("Given input: ", input_data[line_counter].strip())
                print("Received output: ", line.strip())
                print("Expected output: ", output_data[line_counter].strip())
                print("                 ", error_str)
                print("Length difference: ", abs(len(line) - len(output_data[line_counter])))
                print("Hammer distance between answers: ", hammer_distance)
                print("**********************************\n")
                error_counter+=1
            
        line_counter+=1
        if not line_counter%100:
            print("At line ", line_counter, " (Currently ", error_counter, " Errors)")
    
    print("*************************")
    print("Total inputs:", line_counter)
    print("Total number of errors", error_counter)
    input()



def main():
    print(""""Welcome to lab 9 tester!\nSelect your solution to test it. Do note that some errors in the output strings, such as a single \
        character being wrong, might not be detected. Also, if a group ends with '(', there may be different answers, but Kattis does not \
        check for this specifik case.""")
    if len(argv) > 1:
        subject_name = argv[1]
    else:
        subject_name = get_subject_name()
    test_subject(subject_name)
    

    

if __name__ == "__main__":
    main()