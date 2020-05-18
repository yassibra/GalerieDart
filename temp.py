import numpy as np  
import matplotlib.pyplot as plt
import numpy.random as alea

def visu_point(matPoint,style):
    # matPoint contient les coordonnées des points
    x = matPoint[0, :]
    y = matPoint[1, :]
    plt.plot(x, y, style)
    
def visu_segment(P1,P2,style):
    # attention P1 et P2 sont des tableaux (2,1)
    matP = np.concatenate((P1,P2),1)
    visu_point(matP,style)
    
def quadrilatere(a,b,c,d,e,f,g,h):
    visu_point(np.array([[a,c],[b,d]]),'k-')
    visu_point(np.array([[a,e],[b,f]]),'k-')
    visu_point(np.array([[g,e],[h,f]]),'k-')
    visu_point(np.array([[c,g],[d,h]]),'k-')
  
def mat_rotation(theta):
    # si pas besoin des coordonnées homogènes
    mat = np.array([[np.cos(theta), -np.sin(theta)],
                    [np.sin(theta), np.cos(theta)]])
    return mat



plt.axis([-50,50,-50,50])

visu_point(np.array([[0,0],[20,0]]),'k-')
visu_point(np.array([[0,20],[20,20]]),'k-')
visu_point(np.array([[20,20],[20,0]]),'k-')
visu_point(np.array([[0,5],[0,0]]),'k-')
visu_point(np.array([[20,15],[0,0]]),'k-')
visu_point(np.array([[5,5],[0,-5]]),'k-')
visu_point(np.array([[15,15],[0,-10]]),'k-')
visu_point(np.array([[15,40],[-10,-10]]),'k-')
visu_point(np.array([[40,40],[-10,-20]]),'k-')
visu_point(np.array([[40,35],[-20,-20]]),'k-')
visu_point(np.array([[35,35],[-20,-35]]),'k-')
visu_point(np.array([[35,40],[-35,-35]]),'k-')
visu_point(np.array([[40,40],[-35,-45]]),'k-')
visu_point(np.array([[40,-40],[-45,-45]]),'k-')
visu_point(np.array([[40,-40],[-45,-45]]),'k-')
visu_point(np.array([[-40,-40],[-45,-30]]),'k-')
visu_point(np.array([[-40,-35],[-30,-30]]),'k-')
visu_point(np.array([[-35,-35],[-30,-25]]),'k-')
visu_point(np.array([[-35,-30],[-25,-25]]),'k-')
visu_point(np.array([[-30,-30],[-25,-35]]),'k-')
visu_point(np.array([[-30,-25],[-35,-35]]),'k-')
visu_point(np.array([[-25,-25],[-35,-40]]),'k-')
visu_point(np.array([[-25,-20],[-40,-40]]),'k-')
visu_point(np.array([[-20,-20],[-40,-20]]),'k-')
visu_point(np.array([[-20,0],[-20,-20]]),'k-')
visu_point(np.array([[0,0],[-20,-10]]),'k-')




plt.axis('scaled') # la position est importante
taille = 50
delta = 0
plt.xlim(-taille-delta, taille+delta)  
plt.ylim(-taille-delta, taille+delta)

# le segment (A,B) et son vecteur normal :



A = np.array([[0],[20]]) #print(matP[:,0])  #print(A)
B = np.array([[20],[20]])

vecAB = B-A
vecN = np.dot(mat_rotation(np.pi/2),vecAB)
S = np.array([[15],
              [10]])


# le point source S et le vecteur du lancé de rayon :

maliste = [S]

# le point d'impact :
vecS = np.array([[1],[-1]])

for x in np.linspace(1,2*np.pi,16): 

    vecS = np.dot(mat_rotation(x),vecS)
    #norme = np.sqrt(np.dot(vecS.T,vecS))
    #vecS = vecS*(1/norme)
    t = np.dot((A-S).T,vecN)/np.dot(vecS.T,vecN)

    visu_segment(S,S+vecS*15 ,'b:')
    if (t>0):
        
        Pimpact = S + t*vecS
        
        #visu_point(Pimpact,'ro')
        #A = matP[:,0].reshape(2,1) #print(matP[:,0])  #print(A)
        #B = matP[:,1].reshape(2,1)

        vecAB = B-A
        xAB = [A[0,0], B[0,0]]
        if Pimpact[0,0] > np.min(xAB) and Pimpact[0,0] < np.max(xAB):  
            maliste.append(Pimpact)
            visu_point(Pimpact,'ro')  # sur le segment
        #else:
        #   visu_point(Pimpact,'ro')  # en dehors du segment
    
maliste.remove(maliste[0])
for i in maliste:
    visu_segment(maliste[i],maliste[i+1],'ro')
    

visu_point(S,'bo')
#visu_segment(S,S+vecS*2,'b-')
#visu_segment(S,S+vecS*7,'b:')
visu_point(A,'ko')
visu_point(B,'ko')
print(maliste)
