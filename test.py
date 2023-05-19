#/bin/python3


OUTPUT_PATH="Desktop/output.txt"

import math
import os
import random
import re
import sys

from numpy import insert


#
# Complete the 'valuation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER reqArea
#  2. LONG_INTEGER_ARRAY area
#  3. LONG_INTEGER_ARRAY price
#

def valuation(reqArea, area, price):
    # Write your code here
    
        
        
    


 # Check for Outliars
    
    test_list = []
    for i in range(price_count):
        
         tested_price = price[i]
         tested_area = area[i]
         final_area = area.copy()
         final_price = price.copy()
         test_list.append(area[i]/price[i]) 
         compList = []

         if area.count(area[i]) > 1:
           # Creating compList
            for k in range(area_count):
                if i == k:
                    continue
                if area[i] == area[k]:
                    compList.append(price[k])

         else:
            compList = []
       
         test_list.append(compList) 
  

         try:
           
           price_mean = sum(compList)/len(compList)
           test_list.append(price_mean)

         except ZeroDivisionError:
             test_list.append("NIL")

         
        # Standarad Devation
        
             
          
             
         standarad_deviaiont_elements = []
         for i in range(len(compList)):
            
                standarad_deviaiont_elements.append (pow (compList[i] - price_mean,2))

    
         try:
             standard_deviaiont = math.sqrt(sum(standarad_deviaiont_elements)/len(compList))
             test_list.append(standard_deviaiont)

         except ZeroDivisionError:
           test_list.append("N/A")
     

             
         # Check for Outliar
         for i in range(len(compList)):
            
            outlier_factor = abs(tested_price - price_mean)
            standard_deviaiont_multipliear = standard_deviaiont * 3
            is_it_outlier = False
            if (outlier_factor > standard_deviaiont_multipliear):
                 is_it_outlier = True

            elif (outlier_factor <= standard_deviaiont):
              is_it_outlier = False
         test_list.append(outlier_factor)
         test_list.append(standard_deviaiont_multipliear)
         test_list.append(is_it_outlier)
         if (is_it_outlier == True):
             print(tested_price)
             area.remove(tested_area)
             price.remove(tested_price)
             print(final_price)
             print(final_area)
         if final_price == []:
             final_price.append(reqArea*1000)
             

         elif len(final_area) == 1:
             final_price[0]
         elif final_area.count(reqArea) >= 1:
                 price_mean_sum = []
                 for i in range(final_area):
                     if reqArea == final_area[i]:
                         price_mean_sum += final_price[i]
                 return price_mean_sum/len(final_price)
         elif reqArea >min(final_area) and reqArea < max(final_area):
                min_values_abs = []
                for i in range(len(final_area)):
                  
                    min_values_abs.append(abs(reqArea - final_area[i]))  
                   
                   
                index_min1 = min_values_abs.index(min(min_values_abs)) 
                min_values_abs.pop(index_min1)
                index_min2 =  min_values_abs.index(min(min_values_abs))
                interpolate_means = final_price[index_min1] + (final_price[index_min2]-final_price[index_min1])/(final_area[index_min2] - final_area[index_min1]) * (reqArea - final_area[index_min1])
                print(final_price[index_min1])
                print(final_price[index_min2])
                print(final_area[index_min1])
                print(final_area[index_min2])



                
         elif reqArea < min(final_area) and reqArea > max(final_area):
                  for i in range(len(final_area)):
                    min_values = []
                    min_values.append(abs(reqArea - final_area[i]))

                  index_min1_extrapolate = min_values.index(min(min_values))
                  min_values.remove(min(min_values))
                  index_min2_extrapolate =  min_values.index(min(min_values))
                  extrpolate = final_price[index_min1_extrapolate] + (reqArea - final_area[index_min1_extrapolate])/(final_area[index_min2_extrapolate] - final_area[index_min1_extrapolate]) * (final_price[index_min2_extrapolate - final_price[index_min1_extrapolate]])
                  return round(extrpolate)
                

                 
                   

                 
             
                     
                     
         
    
    print(test_list)
    print(min_values_abs)
    print(final_area)
    print(final_price)

    
    # Price Mean

        # for  j in range(price_count):
         #   if price[i] == price[j]:
        #
         #      compList[i] = price[i]
          #  if len(compList) == 1:







if __name__ == '__main__':
   # fptr = open("output.txt", 'w')

    reqArea = int(input("input req").strip())

    area_count = int(input("input req").strip())

    area = []

    for _ in range(area_count):
        area_item = int(input().strip())
        area.append(area_item)

    price_count = int(input("input req").strip())

    price = []

    for _ in range(price_count):
        price_item = int(input().strip())
        price.append(price_item)

    result = valuation(reqArea, area, price)

    #fptr.write(str(result) + '\n')

    #fptr.close()
