print("Assignment #3")

#Pseudocode

#Add pyfiglet to use for fonts
from pyfiglet import Figlet
font = Figlet(font="bulbhead")
font_name = Figlet(font="digital")
font_job = Figlet(font="digital")
font_hobby= Figlet(font="digital")
font_age= Figlet(font="digital")
font_sex= Figlet(font="digital")

#Add input for name
name = input("\033[1;31m" + font_name.renderText("Please enter your Name: "))
#Line for Printing name
#Add a font & color for name
print("\033[0m")
print("\033[1;7m Your name is: \033[0m")
print("\033[1;93m" + font.renderText(name))
print("\033[0m")

#Add input for age
age = input("\033[1;30m" + font_age.renderText("Please enter your age: "))
#Line for Printing age
#Add a font & color for age
print("\033[0m")
print("\033[1;40m Your age is: \033[0m")
print("\033[1;33m" + font.renderText(age))
print("\033[0m")


#Add input for sex
sex = input("\033[1;32m" + font_job.renderText("Please enter your sex: "))
#Line for Printing sex
#Add a font & color for sex
print("\033[0m")
print("\033[1;43m Your sex is: \033[0m")
print("\033[1;32m" + font.renderText(sex))
print("\033[0m")

#Add input for dream job
Dream_Job = input("\033[1;34m" + font_job.renderText("Please enter your dream Job: "))
#Line for Printing dream job
#Add a font & color for dream job
print("\033[0m")
print("\033[1;42m Your Job is: \033[0m")
print("\033[1;33m" + font.renderText(Dream_Job))
print("\033[0m")

#Add input for hobby
hobby = input("\033[1;35m" + font_hobby.renderText("Please enter your Hobby: "))
#Line for Printing hobby
#Add a font & color for hobby
print("\033[0m")
print("\033[1;36m Your Hobby is: \033[0m")
print("\033[1;32m" + font.renderText(hobby))
print("\033[0m")
