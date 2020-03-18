couleur = {2:'yellow2',4:'yellow3',8:'yellow4',16:'dark goldenrod',32:'goldenrod',64:'goldenrod3',128:'goldenrod2',256:'goldenrod1',512:'light goldenrod',1024:'gold2',2048:'gold'}


def creeGrille (n,val):
    res=[0]*n
    for i in range(n):
        res[i]= [val]*n
            
    return res



def dessineGrille(g):
    can.delete(ALL);
    for i in range(n+1):
        can.create_line(x0+c*i,y0,x0+c*i,y0+n*c,fill='')
        can.create_line(x0,y0+c*i,x0+n*c,y0+c*i,fill='')
    for i in range(n):
        for j in range(n):
            x=g[i][j]
            if x==2048:
                decalage_de_pixels = (0.54)*c;
                can.create_rectangle((j*c)+2,(i*c)+2,(j*c)+c+2,(i*c)+c+2,fill=couleur(x),outline='')
                can.create_text((j*c)+decalage_de_pixels,(i*c)+decalage_de_pixels,text=str(x),font=("Ubuntu",13,"bold"),fill="gray20");
            elif x==0:
                decalage_de_pixels = (0.54)*c;
                can.create_rectangle((j*c)+2,(i*c)+2,(j*c)+c+2,(i*c)+c+2,fill=couleur(x),outline='')
                
            else:
                decalage_de_pixels = (0.54)*c;
                can.create_rectangle((j*c)+2,(i*c)+2,(j*c)+c+2,(i*c)+c+2,fill=couleur(x),outline='')
                can.create_text((j*c)+decalage_de_pixels,(i*c)+decalage_de_pixels,text=str(x),font=("Ubuntu",12,"bold"),fill="gray26");
