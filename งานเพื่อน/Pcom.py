import numpy as np
def RowEchelonFrom(Q:list):
    A = np.array(Q[0])
    B = np.array(Q[1])
    C = np.array(Q[2])
    ABC = np.vstack((A,B,C))
    D = np.hstack((A,B,C))
    print("Normal Form")
    print(ABC)
    #step1
    if A[0] != 1:
        A1 = A/A[0]
        if B[0] != 0:
            A = A1(-B[0])
            B0 = np.array([D[4]+A[0],D[5]+A[1],D[6]+A[2],D[7]+A[3]])
        if C[0] != 0:
            A = A(-C[0])/(-B[0])
            C0 = np.array([D[8]+A[0],D[9]+A[1],D[10]+A[2],D[11]+A[3]])
    #A1B0C0 = np.vstack((A1,B0,C0))
    D1 = np.hstack((A1,B0,C0))
    
    #step2
    if B0[1] != 1:
        B1 = B0/B0[1]
        if A1[1] != 0:
            B = B1(-A1[1])
            A01 = np.array([D1[0]+B[0],D1[1]+B[1],D1[2]+B[2],D1[3]+B[3]])
        if C0[1] != 0:
            B = B(-C0[1])/(-A1[1])
            C01 = np.array([D1[8]+B[0],D1[9]+B[1],D1[10]+B[2],D1[11]+B[3]])
    #A0B1C0 = np.vstack((A01,B1,C01))
    D2 = np.hstack((A01,B1,C01))

    #step3
    if C01[2] != 1:
        C1 = C01/C01[2]
        if A01[2] != 0:
            C = C1(-A01[2])
            A02 = np.array([D2[0]+C[0],D2[1]+C[1],D2[2]+C[2],D2[3]+C[3]])
        if B1[2] != 0:
            C = C(-B1[2])/(-A01[2])
            B02 = np.array([D2[4]+C[0],D2[5]+C[1],D2[6]+C[2],D2[7]+C[3]])
    #A0B0C1 = np.vstack((A02,B02,C1))
    D3 = np.hstack((A02,B02,C1))
    D3 = np.array(list(map(lambda x: float(format(float(str(x).replace('-0', '0')),'.2f')), D3))).reshape(3, 4)
    print("Row Echelon From")
    print(D3)
    
Q = [[float(j) for j in input().split(',')] for i in range(0,3) ]
RowEchelonFrom(Q)