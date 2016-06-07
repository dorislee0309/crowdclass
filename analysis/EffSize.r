library(effsize)
dataA <- c(0.872727272727,0.785714285714,0.52380952381,0.117647058824,0.9375,0.857142857143,0.862068965517,0.843137254902,0.444444444444,0.714285714286,0.735294117647,0.849056603774,0.660714285714,0.72602739726,0.675675675676,0.75,0.923076923077,0.857142857143,0.821428571429,0.738095238095,1.0,0.611111111111,0.827586206897,0.617647058824,0.842105263158,0.846153846154,0.827586206897,0.947368421053,0.857142857143,0.630434782609,0.777777777778,0.75,0.357142857143,0.941176470588,0.84375,0.671641791045,0.717948717949,0.517647058824,0.80487804878,0.888888888889,0.660714285714,0.75,0.84375,0.829787234043,0.777777777778,0.842105263158) 
dataB <- c(0.555555555556,0.923076923077,1.0,0.0,0.5,0.384615384615,0.833333333333,1.0,0.666666666667,0.733333333333,0.8,1.0,0.666666666667,0.0,0.8,0.666666666667,0.454545454545,0.461538461538,0.375,0.533333333333,0.428571428571,1.0,0.75,0.5,1.0,0.666666666667,0.166666666667,0.5,0.315789473684,0.333333333333,0.5,0.5,0.5,1.0,0.533333333333,0.5,0.666666666667,0.333333333333,1.0,0.933333333333,1.0) 
cohen.d(dataA,dataB)
cohen.d(dataA,dataB,hedges.correction=TRUE)