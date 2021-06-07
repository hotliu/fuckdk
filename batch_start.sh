idxstart=1486
idxend=1509
for((idx=$idxstart;idx<=$idxend;idx++));  
do   
python start.py -url http://dxonline.ruc.edu.cn/index.php\?s\=/Index/vedio_cont/id/$idx.html
done
