#Author: Alan Izar
#learning more plotting

import matplotlib.pyplot as plt
import pandas as pd
import plotly
import plotly.plotly as ply


#sign in into plotly
ply.sign_in('alan713ch','ezxjxr1joi')

import plotly.tools as tls

#load the data within a dataframe
gender_degree_data = pd.read_csv("http://www.randalolson.com/wp-content/uploads/percent-bachelors-degrees-women-usa.csv")

#tableau20 colors
tableau20 = [(31, 119, 180), (174, 199, 232), (255, 127, 14), (255, 187, 120),
             (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150),
             (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),
             (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),
             (188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229)]

#scaling down to [0,1] which is what matplotlib can accept
for i in range (len(tableau20)):
    r, g, b = tableau20[i]
    tableau20[i] = (r/255, g/255, b/255)

#gotta specify the size of the plot
#common is (12,9)
plt.figure(figsize=(12, 14))

#create your plot within a variable so you can specify what to do with it
ax = plt.subplot(111)

#such as despine
ax.spines["top"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["right"].set_visible(False)

#specify the ticks
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()

#limit to where the data is (gotta check the data first before you can do this!)
plt.ylim(0, 90)
plt.xlim(1968, 2014)

#size of the ticks!
plt.yticks(range(0,91,10), [str(x) + "%" for x in range (0,91,10)], fontsize=14)
plt.xticks(fontsize = 14)

#baselines
for y in range(10,91,10):
    plt.plot(range(1968, 2012), [y] * len(range(1968,2012)), "--", lw=0.5, color="black", alpha=0.3)

#remove the default tick marks
plt.tick_params(axis="both", which="both", bottom="off", top="off", labelbottom="on",
                left="off", right="off", labelleft="on")

#data!
majors = ['Health Professions', 'Public Administration', 'Education', 'Psychology',
          'Foreign Languages', 'English', 'Communications\nand Journalism',
          'Art and Performance', 'Biology', 'Agriculture',
          'Social Sciences and History', 'Business', 'Math and Statistics',
          'Architecture', 'Physical Sciences', 'Computer Science',
          'Engineering']

for rank, column in enumerate(majors):
    #plot each line with its color
    #color set in order

    plt.plot(gender_degree_data.Year.values,
             gender_degree_data[column.replace("\n", " ")].values,
             lw=2.5, color=tableau20[rank])

    #text labels at the right end
    y_pos = gender_degree_data[column.replace("\n"," ")].values[-1] - 0.5
    if column == "Foreign Languages":
        y_pos += 0.5
    elif column == "English":
        y_pos -= 0.5
    elif column == "Communications\nand Journalism":
        y_pos += 0.75
    elif column == "Art and Performance":
        y_pos -= 0.25
    elif column == "Agriculture":
        y_pos += 1.25
    elif column == "Social Sciences and History":
        y_pos += 0.25
    elif column == "Business":
        y_pos -= 0.75
    elif column == "Math and Statistics":
        y_pos += 0.75
    elif column == "Architecture":
        y_pos -= 0.75
    elif column == "Computer Science":
        y_pos += 0.75
    elif column == "Engineering":
        y_pos -= 0.25

    #again, making sure size of labels is readable
    plt.text(2011.5, y_pos, column, fontsize=14, color=tableau20[rank])

#titles
plt.text(1995, 93, "Percentage of Bachelor's degree conferred to women in the U.S.A"
         ", by major (1970-2012)", fontsize=17, ha="center")

#and of course, citations!
plt.text(1966, -8, "Data source: nces.ed.gov/programs/digest/2013menu_tables.asp"
       "\nAuthor: Randy Olson (randalolson.com / @randal_olson)"
       "\nNote: Some majors are missing because the historical data "
       "is not available for them", fontsize=10)

#plt.savefig("percent-bachelors-degrees-women.png", bbox_inches="tight")

#see if we can put it on plotly
dataviz1 = plt.gcf()
ply.iplot_mpl(dataviz1,resize=False,filename='dataviz1',width=960,height=1120)