idxstart=1486
idxend=1509
for((idx=$idxstart;idx<=$idxend;idx++));  
do   
python post_apply.py -url http://dxonline.ruc.edu.cn/index.php\?s\=/Index/vedio_cont/id/$idx.html
done
