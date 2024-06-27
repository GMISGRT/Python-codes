with open("D:\\.vscode\\Welcome.txt","w") as file:
    file.write("Welcome to Python.")

with open("D:\\.vscode\\Welcome.txt","a+")as file:
    file.write("Python is dynamic.")

with open("D:\\.vscode\\Welcome.txt","a+")as file:
    file.write("Lorem Ipsum is simply dummy text of the printing and typesetting industry.\
   Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,\
   when an unknown printer took a galley of type and scrambled it to make a type \
   specimen book. It has survived not only five centuries, but also the leap into \
   electronic typesetting, remaining essentially unchanged. It was popularised in \
   the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, \
   and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")

with open("D:\\.vscode\\Welcome.txt","r")as file:
    data=file.readline()
    x=file.tell()
    print(x)
    file.seek(78)
    print(file.tell())

print(data)

with open("D:\\.vscode\\Welcome.txt","r") as file:
    for f in file:
        print(f,end=" ")