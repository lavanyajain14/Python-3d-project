import qutip as qt 
psi_0 = qt.basis(2,1)
psi_1 = qt.basis(2,0)
psi_super=(psi_0+psi_1).unit()
sigma_x=qt.sigmax()
sigma_y=qt.sigmay()
sigma_z=qt.sigmaz()
H=0.5*sigma_x
for t in range(0,100):
    U=(-1j*H*t).expm()
    psi_evolved=U*psi_0
    b=qt.Bloch()
    b.make_sphere()
    b.add_states(psi_evolved)
    b.render()
    bb=b.fig
    bb.savefig('Bloch.png')
    
