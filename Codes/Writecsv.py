
import csv

out_path="D:\\MS\\DWBI\\Project\\Dataset2\\output.csv"
out_pathD="D:\\MS\\DWBI\\Project\\Dataset2\\Details.csv"

def WriteHeaderD(title='App',c='Category',R='Rating',S='Size',I='Installs',Type='Type',Price='Price',Con='Content.Rating',G='Genre'):
    print("File created and Header inserted")
    #print(title,c,R,S,I,Type,Price,Con,G)
    with open(str(out_pathD), 'w', newline='',encoding="utf-8") as he:
      fieldnames = ['title', 'c', 'R', 'S', 'I', 'Type', 'Price', 'Con', 'Genre']
      writer = csv.DictWriter(he,fieldnames=fieldnames)
      writer.writerow({'title':title,'c':c,'R':R,'S':S,'I':I,'Type':Type,'Price':Price,'Con':Con,'Genre':G})


def AppDetails(Title,c='N/A',R='N/A', S='N/A', I='N/A', Type='Free', Price='0', Con='Everyone'):
    print(Title+" Application Details Written")
    #print(Title,c,R,S,I,Type,Price,Con,c)
    with open(str(out_pathD), 'a', newline='',encoding="utf-8") as D:
     fieldnames = ['Title', 'c', 'R','S','I','Type','Price','Con','Genre']
     writer = csv.DictWriter(D,fieldnames=fieldnames)
     writer.writerow({'Title':Title,'c':c,'R':R,'S':S,'I':I,'Type':Type,'Price':Price,'Con':Con,'Genre':c})


def WriteHeader(a,r,u):
    print("File created and Header inserted")
    with open(str(out_path), 'w', newline='', encoding="utf-8") as h:
        fieldname=['Application Name','Review','Application URL']
        writer = csv.DictWriter(h,fieldname=fieldname)
        writer.writerow({'Application Name':a,'Review':r,'Application URL':u})


def WriteCsv(title,review='N/A',Appurl='N/A'):

  re=[]
  re.append({'Application Name':title,'Reviews':review,'Application Url':Appurl})
  for r in re:
      print(title+" review Written in file")
      #print(r['Application Name'] ,r['Reviews'])
      with open(str(out_path),'a',newline='',encoding="utf-8") as w:
          fieldnames = ['Application Name', 'Reviews','Application Url']
          writer = csv.DictWriter(w, fieldnames=fieldnames)
          writer.writerow({'Application Name':r['Application Name'],'Reviews':r['Reviews'],'Application Url':r['Application Url']})







