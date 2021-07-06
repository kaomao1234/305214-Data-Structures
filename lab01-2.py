for i  in range(2,13):
      print('{} {}'.format(' '+str(i) if i<10 else i,' '.join([' '+str(i*j) if i*j<10 else str(i*j) for j in range(2,8)])))
   
