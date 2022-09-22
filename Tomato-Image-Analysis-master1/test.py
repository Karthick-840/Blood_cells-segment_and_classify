# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 10:20:26 2020

@author: GKSME
"""

import requests

url = "https://{domain_prefix}.vendhq.com/api/2.0/products/{product_id}/actions/image_upload"
files = {'image': open('{file_path}', 'rb')}
headers = {
    'authorization': "Bearer {token}"
}
response = requests.request("POST", url, files=files, headers=headers)

print(response.text)


from PIL import Image                                                                                
img = Image.open('C:\Users\GKSME\OneDrive - Monsanto\Migrated from My PC\Documents\Fiji.App\macros\Projects\Tomato Analyzer\Prelim segmentation\testPicture 2with numbers.jpg')
>>> img.show() 

from PIL import Image
with Image.open('C:\Users\GKSME\OneDrive - Monsanto\Migrated from My PC\Documents\Fiji.App\macros\Projects\Tomato Analyzer\Prelim segmentation\testPicture 2with numbers.jpg') as img:
    img.show()

            if merged_left[(merged_left['x']==Temp[0]) & (merged_left['y'] == Temp[1])].empty==False:
    
    
        if Slice2[(Slice2['x']==Tech.iloc[i-1,0]) & (Slice2['y'] == Tech.iloc[i-1,1])].empty==True:
            if Slice2[(Slice2['x']==Tech.iloc[i-1,0])].empty==True:
                Tech.iloc[i-1,0] = Tech.iloc[i-1,0]+1
            else:
                Tech.iloc[i-1,1] = Tech.iloc[i-1,1]+1
        else:
            continue
        
        
        
for i in range(1,len(xs[1][['A']])):
    print(sum(s[:i])/i)
    
fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
ax.scatter(variable['x'],variable['y'],variable['z'],c='r',marker='o')
ax.set_xlabel('x axis')
ax.set_ylabel('y axis')
ax.set_zlabel('z axis')

Slice3['R1','G1','B1'] = Slice3['x','y','z'].map(Slice2.set_index('x','y','z')['R1','G1','B1'])
        
        joined = Slice.reset_index() \
                    [['x', 'y','z','Ux', 'Uy','Uz','R1','G1','B1']] \
                        .merge(Slice2, on=[['x', 'y','z','Ux', 'Uy','Uz','R1','G1','B1']])
df1.loc[joined['index'], df1.columns[:30]] = joined.drop(columns=['index', 'ID'])
if Slice[(Slice['x']==Temp[0]) & (Slice['y'] == Temp[1])].empty==False:
                Slice.loc[np.logical_and(Slice.x == Temp[0], Slice.y == Temp[1]),['R1','G1','B1']] = [0,0,0]
