import pandas as pd

df = pd.read_csv('video_data.csv')
id = df.iloc[:,0].to_list()
print(id)

url = []
for i in id:
    base = "https://www.youtube.com/watch?v="
    link = base+i
    url.append(link)

print(url)

output = pd.DataFrame({"hyperlink": url})
output.to_csv("Hyperlink.csv")


"""OR"""


df = pd.read_csv('video_data.csv').iloc[:,0].to_list()
url =['https://www.youtube.com/watch?v='+x for x in df]

pd.DataFrame({"hyperlinks": url}).to_csv()


