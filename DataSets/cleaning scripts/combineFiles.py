

folders = ['ard_click','grid_samp','tool_force','tracker','watch1vector']
myDir = "/media/shabelson/backup_vol1/st3/rosbag_t3/"

import os
import glob
import pandas as pd


for locdir in folders:
    dirName = os.path.join(myDir,locdir)
    extension = 'csv'
    os.chdir(dirName)
    all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
    print (all_filenames)
    combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
    combined_csv.to_csv( "%s_combined_csv.csv"%(locdir), index=False, encoding='utf-8-sig')
    
