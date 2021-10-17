import bfs
import hc
import csp



if __name__ == "__main__":
    input_file=open("./AI/input.txt",'r')
    lines=input_file.readlines()

    for line in lines:
        n=int(line[0])
        modle=line[2]
        if modle=='b':
            bfs.bfs(n)
        elif modle=='c':
            csp.csp(n)
        elif modle=='h':
            hc.hc(n)
        else:
            print("wrong input!!")
    print("done!")
    input_file.close()