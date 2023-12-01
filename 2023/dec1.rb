puts "Hello, World!"
#first open a file for reading
file = File.open("realInput", "r")
#file = File.open("testInput", "r")
#read the file into an array of lines
lines = file.readlines.map(&:chomp)
#close the file
file.close

sum=0
#for each line
for line in lines
  #for each character, check if it spells a number starting with that character
  digits = ""
  line_length = line.length
  puts "line " + line

  for i in 0..line_length-1
    #check if a substring starting at i is a "test"
    if i+2<line_length && line[i..i+2] == "one"
      #add the number 1 to the digits string
      digits += "1"
    end
    if i+2<line_length && line[i..i+2] == "two"
      #replace the substring with the number 2
      digits += "2"
    end
    if i+4<line_length && line[i..i+4] == "three"
      #replace the substring with the number 3
      digits += "3"
    end
    if i+3<line_length && line[i..i+3] == "four"
      #replace the substring with the number 4
      digits += "4"
    end
    if i+3<line_length && line[i..i+3] == "five"
      #replace the substring with the number 5
      digits += "5"
    end
    if i+2<line_length && line[i..i+2] == "six"
      #replace the substring with the number 6
      digits += "6"
    end
    if i+4<line_length && line[i..i+4] == "seven"
      #replace the substring with the number 7
      digits += "7"
    end
    if i+4<line_length && line[i..i+4] == "eight"
      #replace the substring with the number 8
      digits += "8"
    end
    if i+3<line_length && line[i..i+3] == "nine"
      #replace the substring with the number 9
      digits += "9"
    end
    #check if the character i is a digit
    if line[i] =~ /\d/
      #add the digit to the digits string
      digits += line[i]
    end
  end

  #if the length is less than 2 characters, skip it
  if line.length < 1
    next
  end
  #multiply the first digit by 10 and add the second digit
  num = digits[0].to_i * 10 + digits[-1].to_i
  puts "sum " + num.to_s
  sum+= num
end
puts sum
