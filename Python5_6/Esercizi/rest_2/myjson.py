import json



def JsonSerialize(data, sFile):
    #if type(dData) is not dict:
    #    return False
    #try:
        with open(sFile, "w") as write_file:
            json.dump(data, write_file,indent=4)
    #    return True
    #except:
    #    return False

def JsonDeserialize(sFile):
    with open(sFile, "r") as read_file:
        return json.load(read_file)
