#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask,request
from flask_cors import CORS
from pycocotools.coco import COCO
import numpy as np
import skimage.io as io
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import pylab
matplotlib.use("Agg")
app = Flask(__name__)
CORS(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
def draw_box(plt, bbox, color, cat_id, alpha):
    rect = patches.Rectangle((bbox[0], bbox[1]), bbox[2], bbox[3], linewidth=1,
                           edgecolor=color, facecolor='none', alpha=alpha)
    plt.gca().add_patch(rect)
    plt.annotate(str(ans[cat_id]), (bbox[0] + 0.5 * bbox[2], bbox[1] + 0.5 * bbox[3]), color='w', weight='bold',
              fontsize=10, ha='center', va='center', alpha=1.0)
@app.route('/api/images/')
def images():
    bar = request.args.to_dict()
    first = bar['a']
    second = bar['b']
    catIds = coco.getCatIds(catNms=[first,second]);
    imgIds = coco.getImgIds(catIds=catIds );
    img = coco.loadImgs(imgIds[0:8])
    if(len(img)<8):
        return 'Please try a different combination', 400
    else:
        for i in range(0,8):
            I = io.imread(img[i]['coco_url'])        
            plt.imshow(I); plt.axis('off')
            annIds = coco.getAnnIds(imgIds=img[i]['id'], catIds=catIds, iscrowd=None)    
            anns = coco.loadAnns(annIds)
            colors = ['b','g','r','c','m','y','b','g','r','c','m','y','b','g','r','c','m','y']
            count = 0
            for gt in anns:    
                draw_box(plt, gt['bbox'], colors[count], gt['category_id'], 1.0)
                count=count+1  
            plt.savefig('./Output/image{0}.jpg'.format(i)) 
            plt.close()        
    return 'Success', 200
    

if __name__ == '__main__':   
    pylab.rcParams['figure.figsize'] = (8.0, 10.0)    
    annFile = './instances_val2017.json'
    coco=COCO(annFile)
    cats = coco.loadCats(coco.getCatIds())
    ans = {} 
    for cat in cats:
        nms=cat['name']
        ids=cat['id']
        ans[ids]=nms
    app.run(debug=True)

