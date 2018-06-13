# This program calculates the sum of lower and upper spiral of the given matrix

import numpy as np

def UpperSpiralSum(a,r,c): # a is the matrix, r is no. of rows & c is no. of columns
    
    k=0;l=0;m=r;n=c;count=0
    s=np.zeros(50)  # 1D zero numpy array s of size 50
    print('\n\n The elements of upper spiral of the matrix are:: \n\n')
    while (k<m and l<n):

    	#collecting the elements of 1st row 
    	#& remaining rows in s array
    	for i in range(l,n):
    		s[count]=a[k][i]
    		print(s[count], end = " ")
    		count+=1

    	k+=1

    	#collecting the elements from
    	#remaining columns in s array
    	for i in range(k,m):
    		s[count]=a[i][n-1]
    		print(s[count], end = " ")
    		count+=1

    	n-=1

    	#collecting the elements from
    	#the remaining rows in s array

    	if(k<m):

    		for i in range(n-1,(l-1),-1):
    			s[count]=a[m-1][i]
    			print(s[count], end = " ")
    			count+=1

    		m-=1

    	#collecting the elements from 1st column
    	#& the remaining columns in s array

    	if(l<n):
    		for i in range(m-1,k-1,-1):
    			s[count]=a[i][l]
    			print(s[count], end = " ")
    			count+=1

    		l+=1
    return(s) #returning the numpy array

def LowerSpiralSum(a,r,c): # a is the matrix, r is no. of rows & c is no. of columns
    
    k=r;l=c;m=0;n=0;count=0
    s=np.zeros(50)  # 1D zero numpy array s of size 50
    print('\n\nThe elements of lower spiral of the matrix are:: \n\n')
    while (k>m and l>n):

    	#collecting the elements of 1st row 
    	#& remaining rows in s array
    	for i in range(n,l):
    		s[count]=a[k-1][i]
    		print(s[count], end = " ")
    		count+=1

    	k-=1

    	#collecting the elements from
    	#remaining columns in s array
    	for i in range(k-1,m-1,-1):
    		s[count]=a[i][l-1]
    		print(s[count],end = " ")
    		count+=1

    	l-=1

    	#collecting the elements from
    	#the remaining rows in s array

    	if(k>m):

    		for i in range(l-1,n-1,-1):
    			s[count]=a[m][i]
    			print(s[count], end = " ")
    			count+=1

    		m+=1

    	#collecting the elements from 1st column
    	#& the remaining columns in s array

    	if(l>n):
    		for i in range(m,k):
    			s[count]=a[i][n]
    			print(s[count], end = " ")
    			count+=1

    		n+=1
    return(s) #returning the numpy array


def main():
    
    a=np.array([[1,2,3,13],[4,5,6,14],[7,8,9,15],[10,11,12,16],[17,18,19,20]]) #Assigned matrix 5*4
    r=5;c=4                                                                    #Rows=5, columns=4
    choice= print('Calulating upper spiral & lower spiral sum of given matrix:.. \n\n')
    Us=UpperSpiralSum(a,r,c)
    usum=np.sum(Us)
    print('\n\nThe upper spiral sum of the given matrix is:  ',usum)
    ls=LowerSpiralSum(a,r,c)
    lsum=np.sum(ls)
    print('\n\nThe lower spiral sum of the given matrix is:  ',lsum)


if __name__ == '__main__':
	main()

