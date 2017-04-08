import os
import math
import sys
import json
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--file")
parser.add_argument("--gpu")
parser.add_argument("--iter")
args = parser.parse_args()
idx = 0
dir_name    = args.file
gpu         = args.gpu
iter        = int(args.iter)
print(dir_name)
conf        = json.loads(open('%s/conf.json'%dir_name, 'r').read())
source      = '%s/%s'%(dir_name, conf['source'])
source_mask = '%s/%s'%(dir_name, conf['source_mask'])
target      = '%s/%s'%(dir_name, conf['target'])
target_mask = '%s/%s'%(dir_name, conf['target_mask'])
matrix      = '%s/mat.mat'%dir_name
print('working on image pair ')
part1_cmd = ' th neuralstyle_seg.lua ' + \
            ' -content_image ./%s'%source + \
            ' -content_seg ./%s'%source_mask + \
            ' -style_image ./%s'%target + \
            ' -style_seg ./%s'%target_mask + \
            ' -index %d'%idx + \
            ' -num_iterations %d '%iter + \
            ' -save_iter 100 ' + \
            ' -print_iter 1' + \
            ' -gpu %s'%gpu + \
            ' -serial %s/tmp_results'%dir_name
part2_cmd = ' th deepmatting_seg.lua ' + \
            ' -content_image ./%s'%source + \
            ' -content_seg ./%s'%source_mask + \
            ' -style_image ./%s'%target + \
            ' -style_seg ./%s'%target_mask + \
            ' -init_image ./%s/tmp_results/out0_t_%d.png'%(dir_name, iter) + \
            ' -index %d'%idx + \
            ' -mat %s'%matrix + \
            ' -num_iterations %d '%iter + \
            ' -save_iter 50' + \
            ' -print_iter 1 '  + \
            ' -gpu %s'%gpu + \
            ' -serial %s/results'%dir_name + \
            ' -f_radius 15 ' + \
            ' -f_edge 0.01 '
os.system(part1_cmd)
os.system(part2_cmd)
