from input import input
from pbl_mail import mail
from reco_init import reco_init
from mktable import mktable
from coor_check import coor_check
from cheating import cheating

def main():
    time = True
    
    info = input()
    
    coordinate = reco_init(info["num"]) 

    mktable(coordinate, info)

    while():
        judge = cheating()
        if(judge == False):
            suspect = coor_check(judge)
            mail(info["address"],suspect,info["class"])
        if(time == False):
            break
