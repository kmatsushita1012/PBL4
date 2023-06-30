from input import input

def main():

    info = Input()

    coordinate = Face_recognition(info["num"]) 

    Area_definition(coordinate, info)

    while():
        judge = Cheating_judgement()
        if(judge == False):
            suspect = Coordinate_judgement(judge)
            Notification(suspect)
        if(time == False):
            break
