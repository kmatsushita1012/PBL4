from input import input
from pbl_mail import mail
from reco_init import reco_init
from mktable import mktable
from coor_check import coor_check
from cheating import cheating

def main():
    time = True
    
    info = input()
    print("a")
    coordinate = reco_init(info["num"]) 

    mktable(coordinate, info)
    print("16")
    while(1):
        judge = cheating()
        if(judge == False):

            suspect = coor_check(judge)
            mail(info["address"],suspect,info["class"])
        if(time == False):
            break
if __name__ == "__main__":
	main()