Yes, this is Quicksort. The objective of this and sucksort was to write a sorting algorithm from scratch with no reference of any kind allowed. Sucksort was the first attempt/implementation, this is the second.

binnedsort
==========

A sorting function that sucks a lot less. Hopefully.

binsort():

>Sorting random list of size          1 :  1.21593475342e-05 s  
>Sorting random list of size         10 :  0.000102043151855 s  
>Sorting random list of size        100 :  0.00152397155762 s  
>Sorting random list of size      1,000 :  0.0136051177979 s  
>Sorting random list of size     10,000 :  0.0525209903717 s  
>Sorting random list of size    100,000 :  0.305780887604 s  
>Sorting random list of size  1,000,000 :  3.01092505455 s  
>Sorting random list of size 10,000,000 :  31.5117769241 s  

binsort2():

>Sorting random list of size           1 :  1.69277191162e-05 s  
>Sorting random list of size          10 :  4.41074371338e-05 s  
>Sorting random list of size         100 :  0.000423908233643 s  
>Sorting random list of size       1,000 :  0.00493311882019 s  
>Sorting random list of size       2,000 :  0.0104310512543 s  
>Sorting random list of size       3,000 :  0.0170900821686 s  
>Sorting random list of size       5,000 :  0.0333061218262 s  
>Sorting random list of size      10,000 :  0.0858099460602 s  
>Sorting random list of size     100,000 :  0.0860228538513 s  
>Sorting random list of size   1,000,000 :  0.0838658809662 s  
>Sorting random list of size  10,000,000 :  0.083890914917 s  
>Sorting random list of size 100,000,000 :  0.0829861164093 s  

0.8s for n>10k? Oh. Maximum recursion depth. Hm.

Todo:
========
Modify middle-element to contain all items equal to the pivot
Modify the flow so that we're tossing things in to L/R as we go through the list (current implementation was just for the sake of using list comprehensions). Right now we're doing 3 walks of it when we should only need to do one.
