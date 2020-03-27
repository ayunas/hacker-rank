#torsion angle == dihedral angle
#a torsion angle is defined as a particular example of a dihedral angle.
#https://en.wikipedia.org/wiki/Dihedral_angle

ø = Tor(p1,p2,p3,p4)
e21 = p2 - p1
e32 = p3 - p2
e43 = p4 - p3
ɸ = Tor(e21,e32,e43)  #edges needs the vertices, but torsion depends on the edges, not the vertices
plane = 'perpendicular to b'

#calculate edges
#find plane by projecting perpendicular to b.
#project a and b onto the plane
#measure angle from a counterclockwise to c -Pa -> Pc
θ = arg(x,y)
cos ɸ = (X.Y) / |X||Y|

X = (AB X BC)
e21 X e32 
Y = (BC X CD)
e32 X e43








