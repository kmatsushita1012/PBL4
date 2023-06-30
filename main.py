from input import input
from pbl_mail import mail
from reco_init import reco_init
from mktable import mktable

def main():
    time = True
    
    info = input()
    
    coordinate = reco_init(info["num"]) 

    mktable(coordinate, info)

    while():
        judge = Cheating_judgement()
        if(judge == False):
            suspect = Coordinate_judgement(judge)
            mail(suspect)
        if(time == False):
            break
