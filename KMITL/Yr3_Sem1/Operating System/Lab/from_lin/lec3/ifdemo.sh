echo "Is it morning? yes or no" 
read timeofday  
if [ $timeofday = "yes" ] 
then  
 echo "Good Morning" 
elif [ $timeofday = "no" ] 
then  
 echo "Good Afternoon" 
else  
 echo "Sorry, $timeofday not recognized" 
 exit 1 
fi  
exit 0  
