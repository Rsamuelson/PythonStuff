letter_lookup = {
   1: 'n', 2: 'o', 3: 'p', 4: 'q', 5: 'r', 6: 's', 7: 't', 8: 'u',
   9: 'v', 10: 'w', 11: 'x', 12: 'y', 13: 'z', 14: 'a', 15: 'b', 16: 'c',
   17: 'd', 18: 'e', 19: 'f', 20: 'g', 21: 'h', 22: 'i', 23: 'j', 24: 'k',
   25: 'l', 26: 'm', 27: ' ', 28: '.'}

def decode(number_list):
   # Complete this function.

   decoded_string = ''
   for number in number_list:
      #print(number)
      letter = letter_lookup[number]
      #print(letter)
      decoded_string = decoded_string + letter
   return decoded_string

input_str = input("Enter a list of numbers separated by commas (e.g., '21,22,28'): ")
#input_str = '12,15,6,1'
input_list = [int(x.strip()) for x in input_str.split(',')]
print("Decoded message:", decode(input_list))