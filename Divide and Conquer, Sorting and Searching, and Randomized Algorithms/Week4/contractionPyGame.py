from graphNode import graphNode
import pygame as py

# initialize pygame and also set up screen object
py.init()

width, height = 1500,800
scrn = py.display.set_mode([width,height])
py.display.set_caption("Random Contraction Algorithm")

# Gather input and turn into and adjacency list
f = open("kargerMinCut.txt","r")
adjList = {}
for each in f.readlines():
    tmp = each.split("\t")
    tmp.remove("\n")
    tmp = list(map(int,tmp))
    adjList[tmp[0]] = tmp[1:]


# Function that contains all relevant game related things
def main():
    open = True
    
    # Turn adjacency list into a list of node objects for the graph
    graph = []
    for each in adjList:
        node = graphNode(each,adjList[each])
        graph.append(node)

    #Drawing the original graph on the screen first before the algorithm starts
    scrn.fill((255,255,255))
    font = py.font.SysFont("monospace",10)
    for circle in graph:
        label = font.render(str(circle.number),True,(0,0,0))
        py.draw.circle(scrn,circle.color,circle.position,10)
        scrn.blit(label,[circle.position[0]-4,circle.position[1]-4])
    py.display.flip()

    while open:

        for event in py.event.get():

            if event.type == py.QUIT:
                open = False
            


    py.display.quit()
    
main()

