import padding as padding

print("Hi all, I am")
print("I very good QA tester")
print('STUDENT NAME : Anshu8qa\nE-MAIL : ansh@l.com \nMAJOR:Computer science')
print('COMPUTER PROGRAMMING EXPERIENCE : None')
print('The computer can compute: 12345679 * 9')
print('and the product is:', 12345679 * 9)
print('delete branch')


def indent(string: str, number_of_space: int):


  """
this function is taking indent number and printing the string after indent
string - is str datatype given
number_of_space - is int datatype given
"""
print(" " * number_of_space + string)


def center(string1: str, screen_width: int):
  padding = (screen_width - len(string1)) // 2
  indent(string1, padding)


print("Indented by", padding, "white spaces.")


def read_n_center_text():
  screen_width1 = int(input("Enter your screen width: "))
  text_string = str(input("Enter your text: "))
  center(text_string, screen_width1)
  read_n_center_text()