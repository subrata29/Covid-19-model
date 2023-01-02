import pygame
import numpy as np
import time
import random
 
import math

col_about_to_die = (200, 200, 225)
vaccinated = (0,200,0)
col_alive = (10, 10, 40) #(255, 255, 215)
col_background = (255, 255, 215)#(10, 10, 40)
col_grid = (30, 30, 60)
ne={'l':0,'lu':0,'u':0,'ru':0,'r':0,'rd':0,'d':0,'ld':0,'s':0,'out':0}
obs=np.array([[ne['lu'], ne['u'],ne['ru']],[ne['l'], ne['s'],ne['r']],[ne['ld'], ne['d'],ne['rd']]])
cum0=0
cum1=0
cum2=0

def flinear(surface, cur, sz,rm):
    nxt = np.zeros((cur.shape[0], cur.shape[1])) 
    nxt=cur
    x=cur
    cum1=0
    for r, c in np.ndindex(x.shape):
        ne['l']=x[r,c-1]
        ne['lu']=x[r-1,c-1]
        ne['u']=x[r-1,c]
        ne['ru']=x[r-1,(c+1)%x.shape[1]]
        ne['r']=x[r,(c+1)%x.shape[1]]
        ne['rd']=x[(r+1)%x.shape[0],(c+1)%x.shape[1]]
        ne['d']=x[(r+1)%x.shape[0],c]
        ne['ld']=x[(r+1)%x.shape[0],c-1]
        ne['s']=x[r,c]
        ne['out']=rm[r,c]
        obs=np.array([[ne['lu'], ne['u'],ne['ru']],[ne['l'], ne['s'],ne['r']],[ne['ld'], ne['d'],ne['rd']]]) 
        num_alive = np.sum(obs[0:3, 0:3]) - ne['s']+ne['out']

        if random.uniform(0,1)<num_alive*0.05:
            col = col_alive
            nxt[r, c] = 1
            cum1+=1
        else:
            col = col_alive
            nxt[r, c] = cur[r, c]
        col = col if cur[r, c] == 1 else col_background
        pygame.draw.rect(surface, col, (c*sz, r*sz, sz-1, sz-1))

    return nxt,cum1



def g1(surface, cur, sz,rm):
    nxt = np.zeros((cur.shape[0], cur.shape[1]))
    nxt=cur
    x=cur
    cum0=0
    for r, c in np.ndindex(x.shape):
        ne['l']=x[r,c-1]
        ne['lu']=x[r-1,c-1]
        ne['u']=x[r-1,c]
        ne['ru']=x[r-1,(c+1)%x.shape[1]]
        ne['r']=x[r,(c+1)%x.shape[1]]
        ne['rd']=x[(r+1)%x.shape[0],(c+1)%x.shape[1]]
        ne['d']=x[(r+1)%x.shape[0],c]
        ne['ld']=x[(r+1)%x.shape[0],c-1]
        ne['s']=x[r,c]
        ne['out']=rm[r,c]
        obs=np.array([[ne['lu'], ne['u'],ne['ru']],[ne['l'], ne['s'],ne['r']],[ne['ld'], ne['d'],ne['rd']]])        
        
        num0=0
        num1=0
        num2=0
        for i in range(3):
            for j in range(3):
                if obs[i][j]==2:
                    num2+=1
                elif obs[i][j]==1:
                    num1+=1
                else:
                    num0+=1
        if ne['out']==2:
            num2+=1
        elif ne['out']==1:
            num1+=1
        else:
            num0+=1

        if cur[r, c] == 1 and random.uniform(0,1)<num0*0.1:
            col = col_background
            nxt[r, c]=0
            cum0+=1
        else:
            nxt[r,c] = cur[r,c]


        if nxt[r, c] == 1:
            col=col_alive
        elif nxt[r, c] == 2:
            col=vaccinated
        else:
            col=col_background

        pygame.draw.rect(surface, col, (c*sz, r*sz, sz-1, sz-1))
    return nxt,cum0


def g2(surface, cur, sz,rm):
    nxt = np.zeros((cur.shape[0], cur.shape[1])) 
    nxt=cur
    x=cur
    cum0=0
    for r, c in np.ndindex(x.shape):
        ne['l']=x[r,c-1]
        ne['lu']=x[r-1,c-1]
        ne['u']=x[r-1,c]
        ne['ru']=x[r-1,(c+1)%x.shape[1]]
        ne['r']=x[r,(c+1)%x.shape[1]]
        ne['rd']=x[(r+1)%x.shape[0],(c+1)%x.shape[1]]
        ne['d']=x[(r+1)%x.shape[0],c]
        ne['ld']=x[(r+1)%x.shape[0],c-1]
        ne['s']=x[r,c]
        ne['out']=rm[r,c]
        obs=np.array([[ne['lu'], ne['u'],ne['ru']],[ne['l'], ne['s'],ne['r']],[ne['ld'], ne['d'],ne['rd']]])        
        
        num0=0
        num1=0
        num2=0
        for i in range(3):
            for j in range(3):
                if obs[i][j]==2:
                    num2+=1
                elif obs[i][j]==1:
                    num1+=1
                else:
                    num0+=1
        if ne['out']==2:
            num2+=1
        elif ne['out']==1:
            num1+=1
        else:
            num0+=1

        if cur[r, c] == 1 and random.uniform(0,1)<num0*0.01:
            col = col_background
            nxt[r, c]=0
            cum0+=1

        else:
            nxt[r,c] = cur[r,c]

        if nxt[r, c] == 1:
            col=col_alive
        elif nxt[r, c] == 2:
            col=vaccinated
        else:
            col=col_background
        pygame.draw.rect(surface, col, (c*sz, r*sz, sz-1, sz-1))
    return nxt,cum0


def g3(surface, cur, sz,rm):
    nxt = np.zeros((cur.shape[0], cur.shape[1])) 
    nxt=cur
    x=cur
    cum0=0
    for r, c in np.ndindex(x.shape):
        ne['l']=x[r,c-1]
        ne['lu']=x[r-1,c-1]
        ne['u']=x[r-1,c]
        ne['ru']=x[r-1,(c+1)%x.shape[1]]
        ne['r']=x[r,(c+1)%x.shape[1]]
        ne['rd']=x[(r+1)%x.shape[0],(c+1)%x.shape[1]]
        ne['d']=x[(r+1)%x.shape[0],c]
        ne['ld']=x[(r+1)%x.shape[0],c-1]
        ne['s']=x[r,c]
        ne['out']=rm[r,c]
        obs=np.array([[ne['lu'], ne['u'],ne['ru']],[ne['l'], ne['s'],ne['r']],[ne['ld'], ne['d'],ne['rd']]])       

        num0=0
        num1=0
        num2=0
        for i in range(3):
            for j in range(3):
                if obs[i][j]==2:
                    num2+=1
                elif obs[i][j]==1:
                    num1+=1
                else:
                    num0+=1
        if ne['out']==2:
            num2+=1
        elif ne['out']==1:
            num1+=1
        else:
            num0+=1
            
        
        if cur[r, c] == 1 and random.uniform(0,1)<num0*0.1:
            col = col_background
            nxt[r, c]=0
            cum0+=1
        else:
            nxt[r,c] = cur[r,c]

        if nxt[r, c] == 1:
            col=col_alive
        elif nxt[r, c] == 2:
            col=vaccinated
        else:
            col=col_background


        pygame.draw.rect(surface, col, (c*sz, r*sz, sz-1, sz-1))
    return nxt,cum0
def g4(surface, cur, sz,rm):
    nxt = np.zeros((cur.shape[0], cur.shape[1])) 
    nxt=cur
    x=cur
    cum0=0
    for r, c in np.ndindex(x.shape):
        ne['l']=x[r,c-1]
        ne['lu']=x[r-1,c-1]
        ne['u']=x[r-1,c]
        ne['ru']=x[r-1,(c+1)%x.shape[1]]
        ne['r']=x[r,(c+1)%x.shape[1]]
        ne['rd']=x[(r+1)%x.shape[0],(c+1)%x.shape[1]]
        ne['d']=x[(r+1)%x.shape[0],c]
        ne['ld']=x[(r+1)%x.shape[0],c-1]
        ne['s']=x[r,c]
        ne['out']=rm[r,c]
        obs=np.array([[ne['lu'], ne['u'],ne['ru']],[ne['l'], ne['s'],ne['r']],[ne['ld'], ne['d'],ne['rd']]])        
        
        num0=0
        num1=0
        num2=0
        for i in range(3):
            for j in range(3):
                if obs[i][j]==2:
                    num2+=1
                elif obs[i][j]==1:
                    num1+=1
                else:
                    num0+=1
        if ne['out']==2:
            num2+=1
        elif ne['out']==1:
            num1+=1
        else:
            num0+=1
            
        
        if cur[r, c] == 1 and random.uniform(0,1)<num0*0.2:
            col = col_background
            nxt[r, c]=0
            cum0+=1
        else:
            nxt[r,c] = cur[r,c]



        if nxt[r, c] == 1:
            col=col_alive
        elif nxt[r, c] == 2:
            col=vaccinated
        else:
            col=col_background

        pygame.draw.rect(surface, col, (c*sz, r*sz, sz-1, sz-1))
    return nxt,cum0




def flin2(surface, cur, sz,rm):
    nxt = np.zeros((cur.shape[0], cur.shape[1])) 
    nxt=cur
    x=cur
    cum1=0
    for r, c in np.ndindex(x.shape):
        ne['l']=x[r,c-1]
        ne['lu']=x[r-1,c-1]
        ne['u']=x[r-1,c]
        ne['ru']=x[r-1,(c+1)%x.shape[1]]
        ne['r']=x[r,(c+1)%x.shape[1]]
        ne['rd']=x[(r+1)%x.shape[0],(c+1)%x.shape[1]]
        ne['d']=x[(r+1)%x.shape[0],c]
        ne['ld']=x[(r+1)%x.shape[0],c-1]
        ne['s']=x[r,c]
        ne['out']=rm[r,c]
        obs=np.array([[ne['lu'], ne['u'],ne['ru']],[ne['l'], ne['s'],ne['r']],[ne['ld'], ne['d'],ne['rd']]])
        num_alive = np.sum(obs[0:3, 0:3]) - ne['s']+ne['out']

        if random.uniform(0,1)<num_alive*0.1:
            col = col_alive
            nxt[r, c] = 1
            cum1+=1
        else:
            col = col_alive
            nxt[r, c] = cur[r, c]



        if nxt[r, c] == 1:
            col=col_alive
        elif nxt[r, c] == 2:
            col=vaccinated
        else:
            col=col_background

        pygame.draw.rect(surface, col, (c*sz, r*sz, sz-1, sz-1))
    return nxt,cum1



def fstable(surface, cur, sz,rm):
    nxt = np.zeros((cur.shape[0], cur.shape[1])) 
    nxt=cur
    x=cur
    cum1=0
    for r, c in np.ndindex(x.shape):
        ne['l']=x[r,c-1]
        ne['lu']=x[r-1,c-1]
        ne['u']=x[r-1,c]
        ne['ru']=x[r-1,(c+1)%x.shape[1]]
        ne['r']=x[r,(c+1)%x.shape[1]]
        ne['rd']=x[(r+1)%x.shape[0],(c+1)%x.shape[1]]
        ne['d']=x[(r+1)%x.shape[0],c]
        ne['ld']=x[(r+1)%x.shape[0],c-1]
        ne['s']=x[r,c]
        ne['out']=rm[r,c]
        obs=np.array([[ne['lu'], ne['u'],ne['ru']],[ne['l'], ne['s'],ne['r']],[ne['ld'], ne['d'],ne['rd']]]) 
        
        num0=0
        num1=0
        num2=0
        for i in range(3):
            for j in range(3):
                if obs[i][j]==2:
                    num2+=1
                elif obs[i][j]==1:
                    num1+=1
                else:
                    num0+=1
        if ne['out']==2:
            num2+=1
        elif ne['out']==1:
            num1+=1
        else:
            num0+=1
                    

        
        if cur[r,c]==0:
            if num1>4:
                nxt[r, c] = 1
                cum1+=1
            else:
                nxt[r, c] = 0
        elif cur[r,c]==1:
                nxt[r, c] = 1

        
        else:
            nxt[r, c] = cur[r,c]
        

        if nxt[r, c] == 1:
            col=col_alive
        elif nxt[r, c] == 2:
            col=vaccinated
        else:
            col=col_background

        pygame.draw.rect(surface, col, (c*sz, r*sz, sz-1, sz-1))
    return nxt,cum1

def flog(surface, cur, sz,rm):
    nxt = np.zeros((cur.shape[0], cur.shape[1])) 
    nxt=cur
    x=cur
    for r, c in np.ndindex(x.shape):
        ne['l']=x[r,c-1]
        ne['lu']=x[r-1,c-1]
        ne['u']=x[r-1,c]
        ne['ru']=x[r-1,(c+1)%x.shape[1]]
        ne['r']=x[r,(c+1)%x.shape[1]]
        ne['rd']=x[(r+1)%x.shape[0],(c+1)%x.shape[1]]
        ne['d']=x[(r+1)%x.shape[0],c]
        ne['ld']=x[(r+1)%x.shape[0],c-1]
        ne['s']=x[r,c]
        ne['out']=rm[r,c]
        obs=np.array([[ne['lu'], ne['u'],ne['ru']],[ne['l'], ne['s'],ne['r']],[ne['ld'], ne['d'],ne['rd']]])
        
        
        
        num0=0
        num1=0
        num2=0
        for i in range(3):
            for j in range(3):
                if obs[i][j]==2:
                    num2+=1
                elif obs[i][j]==1:
                    num1+=1
                else:
                    num0+=1
        if ne['out']==2:
            num2+=1
        elif ne['out']==1:
            num1+=1
        else:
            num0+=1
            
        
        if cur[r, c] == 1 and random.uniform(0,1)<0.2:
            nxt[r, c]=0
        elif num0>0:
            if random.uniform(0,1)<(math.log(num0,10)/2):
                nxt[r, c] = 0
            else:
                nxt[r,c] = cur[r,c]
        else:
            nxt[r,c] = cur[r,c]



        if nxt[r, c] == 1:
            col=col_alive
        elif nxt[r, c] == 2:
            col=vaccinated
        else:
            col=col_background


        pygame.draw.rect(surface, col, (c*sz, r*sz, sz-1, sz-1))
    return nxt

def init(dimx, dimy):
    cells = np.zeros((dimy, dimx))
    pos = (3,3)
    pattern = np.zeros((dimy, dimx))


    pattern = np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]);    


   
    
    cells[pos[0]:pos[0]+pattern.shape[0], pos[1]:pos[1]+pattern.shape[1]] = pattern
    return cells


def countCell(cur):
    x=cur
    count0=0
    count1=0
    count2=0
    for r, c in np.ndindex(x.shape):
        if(x[r,c]==1):
            count1+=1
        elif x[r,c]==2:
            count2+=1
        elif x[r,c]==0:
            count0+=1
    return count0,count1,count2

    
def main(dimx, dimy, cellsize):
    path1="infection.txt"
    path2="vaccinated.txt"

    surface = pygame.display.set_mode((dimx * cellsize, dimy * cellsize))
    pygame.display.set_caption("COVID-19 Model")


    cells = init(dimx, dimy)
            
    rm = np.zeros((dimy, dimx))
    for i in range(rm.shape[0]):
        for j in range(i+1):
            if(random.uniform(0,1)<0.010):
                rm[i,j]=1
                rm[j,i]=1
    counter=0
    k=0
    c1=0
    c0=0
    cum0=0
    cum1=0
    with open(path1,'w') as att:
        counter=0
        while counter<30:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            surface.fill(col_grid)
            
            if random.uniform(0,1)<1:
                cells,cum1 = flinear(surface, cells, cellsize, rm)
            else:
                cells,cum0 = g1(surface, cells, cellsize, rm)
            
            gen,inf,vac=countCell(cells)
            c0=c0+cum0

            data=str(c0)+" "+str(inf)+" "+str(vac)
            att.write(data)
            att.write("\n")
            pygame.display.update()
            counter+=1
        counter=0
        c1=inf
        while counter<50:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            surface.fill(col_grid)
            if random.uniform(0,1)<0.7:
                cells,cum1 = flinear(surface, cells, cellsize,rm)
            else:
                cells,cum0 = g1(surface, cells, cellsize,rm)
            gen,inf,vac=countCell(cells)
            c0=c0+cum0
            c1=c1+cum1
            data=str(c0)+" "+str(c1)+" "+str(vac)
            att.write(data)
            att.write("\n")
            pygame.display.update()
            counter+=1
        counter=0
        while counter<30:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
            surface.fill(col_grid)

            if random.uniform(0,1)<0.7:
                cells,cum1 = fstable(surface, cells, cellsize,rm)
            else:
                cells,cum0 = g2(surface, cells, cellsize,rm)
                
            gen,inf,vac=countCell(cells)
            c0=c0+cum0
            c1=c1+cum1
            data=str(c0)+" "+str(c1)+" "+str(vac)
            att.write(data)
            att.write("\n")
            pygame.display.update()
            counter+=1
        counter=0
        while counter<50:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            surface.fill(col_grid)
           
            if random.uniform(0,1)<0.7:
                cells,cum1 = flin2(surface, cells, cellsize,rm)
            else:
                cells,cum0 = g3(surface, cells, cellsize,rm)
            gen,inf,vac=countCell(cells)
            c0=c0+cum0
            c1=c1+cum1
            data=str(c0)+" "+str(c1)+" "+str(vac)
            att.write(data)
            att.write("\n")
            pygame.display.update()
            counter+=1
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            surface.fill(col_grid)
           
            if random.uniform(0,1)<0.7:
                cells,cum1 = flin2(surface, cells, cellsize,rm)
            else:
                cells,cum0 = g4(surface, cells, cellsize,rm)
            gen,inf,vac=countCell(cells)
            c0=c0+cum0
            c1=c1+cum1
            data=str(c0)+" "+str(c1)+" "+str(vac)
            att.write(data)
            att.write("\n")
            pygame.display.update()
            counter+=1
        
if __name__ == "__main__":
    main(120, 90, 8)