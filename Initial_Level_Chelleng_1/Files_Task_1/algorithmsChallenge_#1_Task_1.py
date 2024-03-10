try:
  dateText = open(input("Enter File path: "), "r")
except:
  print("File not faund")
else:
  try:
    text = dateText.readline()
    print(text, "<- TextForRevers: ", "Location file: ", dateText.name )
  except:
    print("File not read")
  else:
    try:
      reversdate = open("files_Task_1/reversText.txt", "w")
      reversdate.write(text[::-1])
    except:
      print("File not reversed")
    else:
      try:
        reversdate = open("files_Task_1/reversText.txt", "r")
        print(reversdate.readline(), "<- ReversText: ", "Location file: ", reversdate.name)
      except:
        print("File not read")
finally:
  dateText.close()
  reversdate.close()