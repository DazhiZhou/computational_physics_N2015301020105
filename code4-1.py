print ('Give the time during which you want to pridict the population,0<T<100')
T=input('T=')
T=float(T)
print ('Give the initial population N0, 0<0N<2000')
N0=input('N0=')
N0=float(N0)
if 0<T<1000:
    if 0<N0<2000:
        Num=['a']*10000001#make a list vacant to store the results
        t=['a']*10000001#make a list to store the t
        deltat=T/10000000
        Num[0]=N0
        t[0]=0
        i=0
        while i<10000000:#At this part use this part, we use 
            i0=i+1
            Num[i0]=Num[i]+Num[i]*10*deltat
            t[i0]=deltat*i0
            i=i+1
        import pylab as pl
        pl.plot(t,Num,'r')
        pl.title('Prediction of the number of population')
        pl.xlabel('Number')
        pl.ylabel('t')
        pl.xlim(0,T)
        pl.ylim(0,Num[10000000])
        pl.show()
    else:
        print ('The initial population is too large or too small')
else:
    print ('T is too large or too small')
