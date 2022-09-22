import pandas as pd
import numpy as np

# load dataset into Pandas DataFrame
dataset = pd.read_excel(r'Tomato_Dataset_all_sorted.xlsx')

# print(tomato)
df = pd.DataFrame(dataset)


def applyfunc(s):
    return ''


df['Type'] = df['File Name'].apply(applyfunc)

df['Type'][df['File Name'].str.contains("Sa")] = "Standard"
df["Type"][df['File Name'].str.contains("Be")] = "Beef"
df["Type"][df['File Name'].str.contains("Ch")] = "Cherry"

Type = df["Type"]
TomatoSection = df['Type of Tomato Section']
MaxHeight = df['Maximum Height (cm)']
MaxWidth = df['Maximum Width (cm)']
Area = df['Area (cm)']
ShapeIndex = df['Shape Index']
ShapeTriangle = df['Shape Triangle']
Eccentric = df['Eccentric']
Obovoid = df['Obovoid']
Ovoid = df['Ovoid']
HorAsym = df['Horizontal Asymmetry']
VerAsym = df['Vertical Asymmetry']
ProxAng = df['Proximal Angle (rad)']
DistAng = df['Distal Angle (rad)']
ProxBlock = df['Proximal Blockiness']
DistBlock = df['Distal Blockiness']
ProxSH = df['Proximal Shoulderheight']
DistSH = df['Distal Shoulderheight']
Circular = df['Circular']
Ellipsoid = df['Ellipsoid']
ProxHeart = df['Proximal Heart']
DistHeart = df['Distal Heart']
Rectangular = df['Rectangular']

Standard = df[Type == 'Standard']
St_CP_Ex_R = Standard[TomatoSection == 'CP-Ex-R']
St_CP_Ex_U = Standard[TomatoSection == 'CP-Ex-U']
St_CD_En_R = Standard[TomatoSection == 'CD-En-R']
St_CD_Ex_R = Standard[TomatoSection == 'CD-Ex-R']
St_CD_Ex_U = Standard[TomatoSection == 'CD-Ex-U']
St_CD_En_U = Standard[TomatoSection == 'CD-En-U']
St_L_Ex_R = Standard[TomatoSection == 'L-Ex-R']
St_L_En_R = Standard[TomatoSection == 'L-En-R']

Beef = df[Type == 'Beef']
Be_CP_Ex_R = Beef[TomatoSection == 'CP-Ex-R']
Be_CP_Ex_U = Beef[TomatoSection == 'CP-Ex-U']
Be_CD_En_R = Beef[TomatoSection == 'CD-En-R']
Be_CD_Ex_R = Beef[TomatoSection == 'CD-Ex-R']
Be_CD_Ex_U = Beef[TomatoSection == 'CD-Ex-U']
Be_CD_En_U = Beef[TomatoSection == 'CD-En-U']
Be_L_Ex_R = Beef[TomatoSection == 'L-Ex-R']
Be_L_En_R = Beef[TomatoSection == 'L-En-R']

Cherry = df[Type == 'Cherry']
Ch_CP_Ex_R = Cherry[TomatoSection == 'CP-Ex-R']
Ch_CP_Ex_U = Cherry[TomatoSection == 'CP-Ex-U']
Ch_CD_En_R = Cherry[TomatoSection == 'CD-En-R']
Ch_CD_Ex_R = Cherry[TomatoSection == 'CD-Ex-R']
Ch_CD_Ex_U = Cherry[TomatoSection == 'CD-Ex-U']
Ch_CD_En_U = Cherry[TomatoSection == 'CD-En-U']
Ch_L_Ex_R = Cherry[TomatoSection == 'L-Ex-R']
Ch_L_En_R = Cherry[TomatoSection == 'L-En-R']

Multi = df[Type == '']
Mu_CP_Ex_R = Multi[TomatoSection == 'CP-Ex-R']
Mu_CP_Ex_U = Multi[TomatoSection == 'CP-Ex-U']
Mu_CD_En_R = Multi[TomatoSection == 'CD-En-R']
Mu_CD_Ex_R = Multi[TomatoSection == 'CD-Ex-R']
Mu_CD_Ex_U = Multi[TomatoSection == 'CD-Ex-U']
Mu_CD_En_U = Multi[TomatoSection == 'CD-En-U']
Mu_L_Ex_R = Multi[TomatoSection == 'L-Ex-R']
Mu_L_En_R = Multi[TomatoSection == 'L-En-R']

# Standard mean values

MeanSt_CP_Ex_R = [np.mean(St_CP_Ex_R['Maximum Height (cm)']), np.mean(St_CP_Ex_R['Maximum Width (cm)']),
                  np.mean(St_CP_Ex_R['Area (cm)']), np.mean(St_CP_Ex_R['Shape Index']),
                  np.mean(St_CP_Ex_R['Shape Triangle']),
                  np.mean(St_CP_Ex_R['Obovoid']), np.mean(St_CP_Ex_R['Ovoid']),
                  np.mean(St_CP_Ex_R['Horizontal Asymmetry']), np.mean(St_CP_Ex_R['Vertical Asymmetry']),
                  0, 0, np.mean(St_CP_Ex_R['Proximal Blockiness']), np.mean(St_CP_Ex_R['Distal Blockiness']), 0, 0,
                  np.mean(St_CP_Ex_R['Circular']), np.mean(St_CP_Ex_R['Ellipsoid']), 0, 0,
                  np.mean(St_CP_Ex_R['Rectangular'])]

MeanSt_CP_Ex_U = [np.mean(St_CP_Ex_U['Maximum Height (cm)']), np.mean(St_CP_Ex_U['Maximum Width (cm)']),
                  np.mean(St_CP_Ex_U['Area (cm)']), np.mean(St_CP_Ex_U['Shape Index']),
                  np.mean(St_CP_Ex_U['Shape Triangle']),
                  np.mean(St_CP_Ex_U['Obovoid']), np.mean(St_CP_Ex_U['Ovoid']),
                  np.mean(St_CP_Ex_U['Horizontal Asymmetry']), np.mean(St_CP_Ex_U['Vertical Asymmetry']),
                  0, 0, np.mean(St_CP_Ex_U['Proximal Blockiness']), np.mean(St_CP_Ex_U['Distal Blockiness']), 0, 0,
                  np.mean(St_CP_Ex_U['Circular']), np.mean(St_CP_Ex_U['Ellipsoid']), 0, 0,
                  np.mean(St_CP_Ex_U['Rectangular'])]

MeanSt_CD_Ex_R = [np.mean(St_CD_Ex_R['Maximum Height (cm)']), np.mean(St_CD_Ex_R['Maximum Width (cm)']),
                  np.mean(St_CD_Ex_R['Area (cm)']), np.mean(St_CD_Ex_R['Shape Index']),
                  np.mean(St_CD_Ex_R['Shape Triangle']),
                  np.mean(St_CD_Ex_R['Obovoid']), np.mean(St_CD_Ex_R['Ovoid']),
                  np.mean(St_CD_Ex_R['Horizontal Asymmetry']), np.mean(St_CD_Ex_R['Vertical Asymmetry']),
                  0, 0, np.mean(St_CD_Ex_R['Proximal Blockiness']), np.mean(St_CD_Ex_R['Distal Blockiness']), 0, 0,
                  np.mean(St_CD_Ex_R['Circular']), np.mean(St_CD_Ex_R['Ellipsoid']), 0, 0,
                  np.mean(St_CD_Ex_R['Rectangular'])]

MeanSt_CD_En_R = [np.mean(St_CD_En_R['Maximum Height (cm)']), np.mean(St_CD_En_R['Maximum Width (cm)']),
                  np.mean(St_CD_En_R['Area (cm)']), np.mean(St_CD_En_R['Shape Index']),
                  np.mean(St_CD_En_R['Shape Triangle']),
                  np.mean(St_CD_En_R['Obovoid']), np.mean(St_CD_En_R['Ovoid']),
                  np.mean(St_CD_En_R['Horizontal Asymmetry']), np.mean(St_CD_En_R['Vertical Asymmetry']),
                  0, 0, np.mean(St_CD_En_R['Proximal Blockiness']), np.mean(St_CD_En_R['Distal Blockiness']), 0, 0,
                  np.mean(St_CD_En_R['Circular']), np.mean(St_CD_En_R['Ellipsoid']), 0, 0,
                  np.mean(St_CD_En_R['Rectangular'])]

MeanSt_CD_En_U = [np.mean(St_CD_En_U['Maximum Height (cm)']), np.mean(St_CP_Ex_R['Maximum Width (cm)']),
                  np.mean(St_CD_En_U['Area (cm)']), np.mean(St_CP_Ex_R['Shape Index']),
                  np.mean(St_CP_Ex_R['Shape Triangle']),
                  np.mean(St_CD_En_U['Obovoid']), np.mean(St_CP_Ex_R['Ovoid']),
                  np.mean(St_CD_En_U['Horizontal Asymmetry']), np.mean(St_CP_Ex_R['Vertical Asymmetry']),
                  0, 0, np.mean(St_CD_En_U['Proximal Blockiness']), np.mean(St_CP_Ex_R['Distal Blockiness']), 0, 0,
                  np.mean(St_CD_En_U['Circular']), np.mean(St_CP_Ex_R['Ellipsoid']), 0, 0,
                  np.mean(St_CP_Ex_R['Rectangular'])]

MeanSt_CD_Ex_U = [np.mean(St_CD_Ex_U['Maximum Height (cm)']), np.mean(St_CD_Ex_U['Maximum Width (cm)']),
                  np.mean(St_CD_Ex_U['Area (cm)']), np.mean(St_CD_Ex_U['Shape Index']),
                  np.mean(St_CD_Ex_U['Shape Triangle']),
                  np.mean(St_CD_Ex_U['Obovoid']), np.mean(St_CD_Ex_U['Ovoid']),
                  np.mean(St_CD_Ex_U['Horizontal Asymmetry']), np.mean(St_CD_Ex_U['Vertical Asymmetry']),
                  0, 0, np.mean(St_CD_Ex_U['Proximal Blockiness']), np.mean(St_CD_Ex_U['Distal Blockiness']), 0, 0,
                  np.mean(St_CD_Ex_U['Circular']), np.mean(St_CD_Ex_U['Ellipsoid']), 0, 0,
                  np.mean(St_CD_Ex_U['Rectangular'])]

MeanSt_L_Ex_R = [np.mean(St_L_Ex_R['Maximum Height (cm)']), np.mean(St_L_Ex_R['Maximum Width (cm)']),
                 np.mean(St_L_Ex_R['Area (cm)']), np.mean(St_L_Ex_R['Shape Index']),
                 np.mean(St_L_Ex_R['Shape Triangle']),
                 np.mean(St_L_Ex_R['Obovoid']), np.mean(St_L_Ex_R['Ovoid']),
                 np.mean(St_L_Ex_R['Horizontal Asymmetry']), np.mean(St_L_Ex_R['Vertical Asymmetry']),
                 0, 0, np.mean(St_L_Ex_R['Proximal Blockiness']), np.mean(St_L_Ex_R['Distal Blockiness']), 0, 0,
                 np.mean(St_L_Ex_R['Circular']), np.mean(St_L_Ex_R['Ellipsoid']), 0, 0,
                 np.mean(St_L_Ex_R['Rectangular'])]

MeanSt_L_En_R = [np.mean(St_L_En_R['Maximum Height (cm)']), np.mean(St_L_En_R['Maximum Width (cm)']),
                 np.mean(St_L_En_R['Area (cm)']), np.mean(St_L_En_R['Shape Index']),
                 np.mean(St_L_En_R['Shape Triangle']),
                 np.mean(St_L_En_R['Obovoid']), np.mean(St_L_En_R['Ovoid']),
                 np.mean(St_L_En_R['Horizontal Asymmetry']), np.mean(St_L_En_R['Vertical Asymmetry']),
                 np.mean(St_L_En_R['Proximal Angle (rad)']), np.mean(St_L_En_R['Distal Angle (rad)']),
                 np.mean(St_L_En_R['Proximal Blockiness']), np.mean(St_L_En_R['Distal Blockiness']),
                 np.mean(St_L_En_R['Proximal Shoulderheight']), np.mean(St_L_En_R['Distal Shoulderheight']),
                 np.mean(St_L_En_R['Circular']), np.mean(St_L_En_R['Ellipsoid']),
                 np.mean(St_L_En_R['Proximal Heart']), np.mean(St_L_En_R['Distal Heart']),
                 np.mean(St_L_En_R['Rectangular'])]

# Beef mean values
MeanBe_CP_Ex_R = [np.mean(Be_CP_Ex_R['Maximum Height (cm)']), np.mean(Be_CP_Ex_R['Maximum Width (cm)']),
                  np.mean(Be_CP_Ex_R['Area (cm)']), np.mean(Be_CP_Ex_R['Shape Index']),
                  np.mean(Be_CP_Ex_R['Shape Triangle']),
                  np.mean(Be_CP_Ex_R['Obovoid']), np.mean(Be_CP_Ex_R['Ovoid']),
                  np.mean(Be_CP_Ex_R['Horizontal Asymmetry']), np.mean(Be_CP_Ex_R['Vertical Asymmetry']),
                  0, 0, np.mean(Be_CP_Ex_R['Proximal Blockiness']), np.mean(Be_CP_Ex_R['Distal Blockiness']), 0, 0,
                  np.mean(Be_CP_Ex_R['Circular']), np.mean(Be_CP_Ex_R['Ellipsoid']), 0, 0,
                  np.mean(Be_CP_Ex_R['Rectangular'])]

MeanBe_CP_Ex_U = [np.mean(Be_CP_Ex_U['Maximum Height (cm)']), np.mean(Be_CP_Ex_U['Maximum Width (cm)']),
                  np.mean(Be_CP_Ex_U['Area (cm)']), np.mean(Be_CP_Ex_U['Shape Index']),
                  np.mean(Be_CP_Ex_U['Shape Triangle']),
                  np.mean(Be_CP_Ex_U['Obovoid']), np.mean(Be_CP_Ex_U['Ovoid']),
                  np.mean(Be_CP_Ex_U['Horizontal Asymmetry']), np.mean(Be_CP_Ex_U['Vertical Asymmetry']),
                  0, 0, np.mean(Be_CP_Ex_U['Proximal Blockiness']), np.mean(Be_CP_Ex_U['Distal Blockiness']), 0, 0,
                  np.mean(Be_CP_Ex_U['Circular']), np.mean(Be_CP_Ex_U['Ellipsoid']), 0, 0,
                  np.mean(Be_CP_Ex_U['Rectangular'])]

MeanBe_CD_Ex_R = [np.mean(Be_CD_Ex_R['Maximum Height (cm)']), np.mean(Be_CD_Ex_R['Maximum Width (cm)']),
                  np.mean(Be_CD_Ex_R['Area (cm)']), np.mean(Be_CD_Ex_R['Shape Index']),
                  np.mean(Be_CD_Ex_R['Shape Triangle']),
                  np.mean(Be_CD_Ex_R['Obovoid']), np.mean(Be_CD_Ex_R['Ovoid']),
                  np.mean(Be_CD_Ex_R['Horizontal Asymmetry']), np.mean(Be_CD_Ex_R['Vertical Asymmetry']),
                  0, 0, np.mean(Be_CD_Ex_R['Proximal Blockiness']), np.mean(Be_CD_Ex_R['Distal Blockiness']), 0, 0,
                  np.mean(Be_CD_Ex_R['Circular']), np.mean(Be_CD_Ex_R['Ellipsoid']), 0, 0,
                  np.mean(Be_CD_Ex_R['Rectangular'])]

MeanBe_CD_En_R = [np.mean(Be_CD_En_R['Maximum Height (cm)']), np.mean(Be_CD_En_R['Maximum Width (cm)']),
                  np.mean(Be_CD_En_R['Area (cm)']), np.mean(Be_CD_En_R['Shape Index']),
                  np.mean(Be_CD_En_R['Shape Triangle']),
                  np.mean(Be_CD_En_R['Obovoid']), np.mean(Be_CD_En_R['Ovoid']),
                  np.mean(Be_CD_En_R['Horizontal Asymmetry']), np.mean(Be_CD_En_R['Vertical Asymmetry']),
                  0, 0, np.mean(Be_CD_En_R['Proximal Blockiness']), np.mean(Be_CD_En_R['Distal Blockiness']), 0, 0,
                  np.mean(Be_CD_En_R['Circular']), np.mean(Be_CD_En_R['Ellipsoid']), 0, 0,
                  np.mean(Be_CD_En_R['Rectangular'])]

MeanBe_CD_En_U = [np.mean(Be_CD_En_U['Maximum Height (cm)']), np.mean(Be_CP_Ex_R['Maximum Width (cm)']),
                  np.mean(Be_CD_En_U['Area (cm)']), np.mean(Be_CP_Ex_R['Shape Index']),
                  np.mean(Be_CP_Ex_R['Shape Triangle']),
                  np.mean(Be_CD_En_U['Obovoid']), np.mean(Be_CP_Ex_R['Ovoid']),
                  np.mean(Be_CD_En_U['Horizontal Asymmetry']), np.mean(Be_CP_Ex_R['Vertical Asymmetry']),
                  0, 0, np.mean(Be_CD_En_U['Proximal Blockiness']), np.mean(Be_CP_Ex_R['Distal Blockiness']), 0, 0,
                  np.mean(Be_CD_En_U['Circular']), np.mean(Be_CP_Ex_R['Ellipsoid']), 0, 0,
                  np.mean(Be_CP_Ex_R['Rectangular'])]

MeanBe_CD_Ex_U = [np.mean(Be_CD_Ex_U['Maximum Height (cm)']), np.mean(Be_CD_Ex_U['Maximum Width (cm)']),
                  np.mean(Be_CD_Ex_U['Area (cm)']), np.mean(Be_CD_Ex_U['Shape Index']),
                  np.mean(Be_CD_Ex_U['Shape Triangle']),
                  np.mean(Be_CD_Ex_U['Obovoid']), np.mean(Be_CD_Ex_U['Ovoid']),
                  np.mean(Be_CD_Ex_U['Horizontal Asymmetry']), np.mean(Be_CD_Ex_U['Vertical Asymmetry']),
                  0, 0, np.mean(Be_CD_Ex_U['Proximal Blockiness']), np.mean(Be_CD_Ex_U['Distal Blockiness']), 0, 0,
                  np.mean(Be_CD_Ex_U['Circular']), np.mean(Be_CP_Ex_U['Ellipsoid']), 0, 0,
                  np.mean(Be_CP_Ex_U['Rectangular'])]

MeanBe_L_Ex_R = [np.mean(Be_L_Ex_R['Maximum Height (cm)']), np.mean(Be_L_Ex_R['Maximum Width (cm)']),
                 np.mean(Be_L_Ex_R['Area (cm)']), np.mean(Be_L_Ex_R['Shape Index']),
                 np.mean(Be_L_Ex_R['Shape Triangle']),
                 np.mean(Be_L_Ex_R['Obovoid']), np.mean(Be_L_Ex_R['Ovoid']),
                 np.mean(Be_L_Ex_R['Horizontal Asymmetry']), np.mean(Be_L_Ex_R['Vertical Asymmetry']),
                 0, 0, np.mean(Be_L_Ex_R['Proximal Blockiness']), np.mean(Be_L_Ex_R['Distal Blockiness']), 0, 0,
                 np.mean(Be_L_Ex_R['Circular']), np.mean(Be_L_Ex_R['Ellipsoid']), 0, 0,
                 np.mean(Be_L_Ex_R['Rectangular'])]

MeanBe_L_En_R = [np.mean(Be_L_En_R['Maximum Height (cm)']), np.mean(Be_L_En_R['Maximum Width (cm)']),
                 np.mean(Be_L_En_R['Area (cm)']), np.mean(Be_L_En_R['Shape Index']),
                 np.mean(Be_L_En_R['Shape Triangle']),
                 np.mean(Be_L_En_R['Obovoid']), np.mean(Be_L_En_R['Ovoid']),
                 np.mean(Be_L_En_R['Horizontal Asymmetry']), np.mean(Be_L_En_R['Vertical Asymmetry']),
                 np.mean(Be_L_En_R['Proximal Angle (rad)']), np.mean(Be_L_En_R['Distal Angle (rad)']),
                 np.mean(Be_L_En_R['Proximal Blockiness']), np.mean(Be_L_En_R['Distal Blockiness']),
                 np.mean(Be_L_En_R['Proximal Shoulderheight']), np.mean(Be_L_En_R['Distal Shoulderheight']),
                 np.mean(Be_L_En_R['Circular']), np.mean(Be_L_En_R['Ellipsoid']),
                 np.mean(Be_L_En_R['Proximal Heart']), np.mean(Be_L_En_R['Distal Heart']),
                 np.mean(Be_L_En_R['Rectangular'])]

# Cherry mean values
MeanCh_CP_Ex_R = [np.mean(Ch_CP_Ex_R['Maximum Height (cm)']), np.mean(Ch_CP_Ex_R['Maximum Width (cm)']),
                  np.mean(Ch_CP_Ex_R['Area (cm)']), np.mean(Ch_CP_Ex_R['Shape Index']),
                  np.mean(Ch_CP_Ex_R['Shape Triangle']),
                  np.mean(Ch_CP_Ex_R['Obovoid']), np.mean(Ch_CP_Ex_R['Ovoid']),
                  np.mean(Ch_CP_Ex_R['Horizontal Asymmetry']), np.mean(Ch_CP_Ex_R['Vertical Asymmetry']),
                  0, 0, np.mean(Ch_CP_Ex_R['Proximal Blockiness']), np.mean(Ch_CP_Ex_R['Distal Blockiness']), 0, 0,
                  np.mean(Ch_CP_Ex_R['Circular']), np.mean(Ch_CP_Ex_R['Ellipsoid']), 0, 0,
                  np.mean(Ch_CP_Ex_R['Rectangular'])]

MeanCh_CP_Ex_U = [np.mean(Ch_CP_Ex_U['Maximum Height (cm)']), np.mean(Ch_CP_Ex_U['Maximum Width (cm)']),
                  np.mean(Ch_CP_Ex_U['Area (cm)']), np.mean(Ch_CP_Ex_U['Shape Index']),
                  np.mean(Ch_CP_Ex_U['Shape Triangle']),
                  np.mean(Ch_CP_Ex_U['Obovoid']), np.mean(Ch_CP_Ex_U['Ovoid']),
                  np.mean(Ch_CP_Ex_U['Horizontal Asymmetry']), np.mean(Ch_CP_Ex_U['Vertical Asymmetry']),
                  0, 0, np.mean(Ch_CP_Ex_U['Proximal Blockiness']), np.mean(Ch_CP_Ex_U['Distal Blockiness']), 0, 0,
                  np.mean(Ch_CP_Ex_U['Circular']), np.mean(Ch_CP_Ex_U['Ellipsoid']), 0, 0,
                  np.mean(Ch_CP_Ex_U['Rectangular'])]

MeanCh_CD_Ex_R = [np.mean(Ch_CD_Ex_R['Maximum Height (cm)']), np.mean(Ch_CD_Ex_R['Maximum Width (cm)']),
                  np.mean(Ch_CD_Ex_R['Area (cm)']), np.mean(Ch_CD_Ex_R['Shape Index']),
                  np.mean(Ch_CD_Ex_R['Shape Triangle']),
                  np.mean(Ch_CD_Ex_R['Obovoid']), np.mean(Ch_CD_Ex_R['Ovoid']),
                  np.mean(Ch_CD_Ex_R['Horizontal Asymmetry']), np.mean(Ch_CD_Ex_R['Vertical Asymmetry']),
                  0, 0, np.mean(Ch_CD_Ex_R['Proximal Blockiness']), np.mean(Ch_CD_Ex_R['Distal Blockiness']), 0, 0,
                  np.mean(Ch_CD_Ex_R['Circular']), np.mean(Ch_CD_Ex_R['Ellipsoid']), 0, 0,
                  np.mean(Ch_CD_Ex_R['Rectangular'])]

MeanCh_CD_En_R = [np.mean(Ch_CD_En_R['Maximum Height (cm)']), np.mean(Ch_CD_En_R['Maximum Width (cm)']),
                  np.mean(Ch_CD_En_R['Area (cm)']), np.mean(Ch_CD_En_R['Shape Index']),
                  np.mean(Ch_CD_En_R['Shape Triangle']),
                  np.mean(Ch_CD_En_R['Obovoid']), np.mean(Ch_CD_En_R['Ovoid']),
                  np.mean(Ch_CD_En_R['Horizontal Asymmetry']), np.mean(Ch_CD_En_R['Vertical Asymmetry']),
                  0, 0, np.mean(Ch_CD_En_R['Proximal Blockiness']), np.mean(Ch_CD_En_R['Distal Blockiness']), 0, 0,
                  np.mean(Ch_CD_En_R['Circular']), np.mean(Ch_CD_En_R['Ellipsoid']), 0, 0,
                  np.mean(Ch_CD_En_R['Rectangular'])]

MeanCh_CD_En_U = [np.mean(Ch_CD_En_U['Maximum Height (cm)']), np.mean(Ch_CP_Ex_R['Maximum Width (cm)']),
                  np.mean(Ch_CD_En_U['Area (cm)']), np.mean(Ch_CP_Ex_R['Shape Index']),
                  np.mean(Ch_CP_Ex_R['Shape Triangle']),
                  np.mean(Ch_CD_En_U['Obovoid']), np.mean(Ch_CP_Ex_R['Ovoid']),
                  np.mean(Ch_CD_En_U['Horizontal Asymmetry']), np.mean(Ch_CP_Ex_R['Vertical Asymmetry']),
                  0, 0, np.mean(Ch_CD_En_U['Proximal Blockiness']), np.mean(Ch_CP_Ex_R['Distal Blockiness']), 0, 0,
                  np.mean(Ch_CD_En_U['Circular']), np.mean(Ch_CP_Ex_R['Ellipsoid']), 0, 0,
                  np.mean(Ch_CP_Ex_R['Rectangular'])]

MeanCh_CD_Ex_U = [np.mean(Ch_CD_Ex_U['Maximum Height (cm)']), np.mean(Ch_CD_Ex_U['Maximum Width (cm)']),
                  np.mean(Ch_CD_Ex_U['Area (cm)']), np.mean(Ch_CD_Ex_U['Shape Index']),
                  np.mean(Ch_CD_Ex_U['Shape Triangle']),
                  np.mean(Ch_CD_Ex_U['Obovoid']), np.mean(Ch_CD_Ex_U['Ovoid']),
                  np.mean(Ch_CD_Ex_U['Horizontal Asymmetry']), np.mean(Ch_CD_Ex_U['Vertical Asymmetry']),
                  0, 0, np.mean(Ch_CD_Ex_U['Proximal Blockiness']), np.mean(Ch_CD_Ex_U['Distal Blockiness']), 0, 0,
                  np.mean(Ch_CD_Ex_U['Circular']), np.mean(Ch_CP_Ex_U['Ellipsoid']), 0, 0,
                  np.mean(Ch_CP_Ex_U['Rectangular'])]

MeanCh_L_Ex_R = [np.mean(Ch_L_Ex_R['Maximum Height (cm)']), np.mean(Ch_L_Ex_R['Maximum Width (cm)']),
                 np.mean(Ch_L_Ex_R['Area (cm)']), np.mean(Ch_L_Ex_R['Shape Index']),
                 np.mean(Ch_L_Ex_R['Shape Triangle']),
                 np.mean(Ch_L_Ex_R['Obovoid']), np.mean(Ch_L_Ex_R['Ovoid']),
                 np.mean(Ch_L_Ex_R['Horizontal Asymmetry']), np.mean(Ch_L_Ex_R['Vertical Asymmetry']),
                 0, 0, np.mean(Ch_L_Ex_R['Proximal Blockiness']), np.mean(Ch_L_Ex_R['Distal Blockiness']), 0, 0,
                 np.mean(Ch_L_Ex_R['Circular']), np.mean(Ch_L_Ex_R['Ellipsoid']), 0, 0,
                 np.mean(Ch_L_Ex_R['Rectangular'])]

MeanCh_L_En_R = [np.mean(Ch_L_En_R['Maximum Height (cm)']), np.mean(Ch_L_En_R['Maximum Width (cm)']),
                 np.mean(Ch_L_En_R['Area (cm)']), np.mean(Ch_L_En_R['Shape Index']),
                 np.mean(Ch_L_En_R['Shape Triangle']),
                 np.mean(Ch_L_En_R['Obovoid']), np.mean(Ch_L_En_R['Ovoid']),
                 np.mean(Ch_L_En_R['Horizontal Asymmetry']), np.mean(Ch_L_En_R['Vertical Asymmetry']),
                 np.mean(Ch_L_En_R['Proximal Angle (rad)']), np.mean(Ch_L_En_R['Distal Angle (rad)']),
                 np.mean(Ch_L_En_R['Proximal Blockiness']), np.mean(Ch_L_En_R['Distal Blockiness']),
                 np.mean(Ch_L_En_R['Proximal Shoulderheight']), np.mean(Ch_L_En_R['Distal Shoulderheight']),
                 np.mean(Ch_L_En_R['Circular']), np.mean(Ch_L_En_R['Ellipsoid']),
                 np.mean(Ch_L_En_R['Proximal Heart']), np.mean(Ch_L_En_R['Distal Heart']),
                 np.mean(Ch_L_En_R['Rectangular'])]

# Multi mean values
MeanMu_CP_Ex_R = [np.mean(Mu_CP_Ex_R['Maximum Height (cm)']), np.mean(Mu_CP_Ex_R['Maximum Width (cm)']),
                  np.mean(Mu_CP_Ex_R['Area (cm)']), np.mean(Mu_CP_Ex_R['Shape Index']),
                  np.mean(Mu_CP_Ex_R['Shape Triangle']),
                  np.mean(Mu_CP_Ex_R['Obovoid']), np.mean(Mu_CP_Ex_R['Ovoid']),
                  np.mean(Mu_CP_Ex_R['Horizontal Asymmetry']), np.mean(Mu_CP_Ex_R['Vertical Asymmetry']),
                  0, 0, np.mean(Mu_CP_Ex_R['Proximal Blockiness']), np.mean(Mu_CP_Ex_R['Distal Blockiness']), 0, 0,
                  np.mean(Mu_CP_Ex_R['Circular']), np.mean(Mu_CP_Ex_R['Ellipsoid']), 0, 0,
                  np.mean(Mu_CP_Ex_R['Rectangular'])]

MeanMu_CP_Ex_U = [np.mean(Mu_CP_Ex_U['Maximum Height (cm)']), np.mean(Mu_CP_Ex_U['Maximum Width (cm)']),
                  np.mean(Mu_CP_Ex_U['Area (cm)']), np.mean(Mu_CP_Ex_U['Shape Index']),
                  np.mean(Mu_CP_Ex_U['Shape Triangle']),
                  np.mean(Mu_CP_Ex_U['Obovoid']), np.mean(Mu_CP_Ex_U['Ovoid']),
                  np.mean(Mu_CP_Ex_U['Horizontal Asymmetry']), np.mean(Mu_CP_Ex_U['Vertical Asymmetry']),
                  0, 0, np.mean(Mu_CP_Ex_U['Proximal Blockiness']), np.mean(Mu_CP_Ex_U['Distal Blockiness']), 0, 0,
                  np.mean(Mu_CP_Ex_U['Circular']), np.mean(Mu_CP_Ex_U['Ellipsoid']), 0, 0,
                  np.mean(Mu_CP_Ex_U['Rectangular'])]

MeanMu_CD_Ex_R = [np.mean(Mu_CD_Ex_R['Maximum Height (cm)']), np.mean(Mu_CD_Ex_R['Maximum Width (cm)']),
                  np.mean(Mu_CD_Ex_R['Area (cm)']), np.mean(Mu_CD_Ex_R['Shape Index']),
                  np.mean(Mu_CD_Ex_R['Shape Triangle']),
                  np.mean(Mu_CD_Ex_R['Obovoid']), np.mean(Mu_CD_Ex_R['Ovoid']),
                  np.mean(Mu_CD_Ex_R['Horizontal Asymmetry']), np.mean(Mu_CD_Ex_R['Vertical Asymmetry']),
                  0, 0, np.mean(Mu_CD_Ex_R['Proximal Blockiness']), np.mean(Mu_CD_Ex_R['Distal Blockiness']), 0, 0,
                  np.mean(Mu_CD_Ex_R['Circular']), np.mean(Mu_CD_Ex_R['Ellipsoid']), 0, 0,
                  np.mean(Mu_CD_Ex_R['Rectangular'])]

MeanMu_CD_En_R = [np.mean(Mu_CD_En_R['Maximum Height (cm)']), np.mean(Mu_CD_En_R['Maximum Width (cm)']),
                  np.mean(Mu_CD_En_R['Area (cm)']), np.mean(Mu_CD_En_R['Shape Index']),
                  np.mean(Mu_CD_En_R['Shape Triangle']),
                  np.mean(Mu_CD_En_R['Obovoid']), np.mean(Mu_CD_En_R['Ovoid']),
                  np.mean(Mu_CD_En_R['Horizontal Asymmetry']), np.mean(Mu_CD_En_R['Vertical Asymmetry']),
                  0, 0, np.mean(Mu_CD_En_R['Proximal Blockiness']), np.mean(Mu_CD_En_R['Distal Blockiness']), 0, 0,
                  np.mean(Mu_CD_En_R['Circular']), np.mean(Mu_CD_En_R['Ellipsoid']), 0, 0,
                  np.mean(Mu_CD_En_R['Rectangular'])]

MeanMu_CD_En_U = [np.mean(Mu_CD_En_U['Maximum Height (cm)']), np.mean(Mu_CP_Ex_R['Maximum Width (cm)']),
                  np.mean(Mu_CD_En_U['Area (cm)']), np.mean(Mu_CP_Ex_R['Shape Index']),
                  np.mean(Mu_CP_Ex_R['Shape Triangle']),
                  np.mean(Mu_CD_En_U['Obovoid']), np.mean(Mu_CP_Ex_R['Ovoid']),
                  np.mean(Mu_CD_En_U['Horizontal Asymmetry']), np.mean(Mu_CP_Ex_R['Vertical Asymmetry']),
                  0, 0, np.mean(Mu_CD_En_U['Proximal Blockiness']), np.mean(Mu_CP_Ex_R['Distal Blockiness']), 0, 0,
                  np.mean(Mu_CD_En_U['Circular']), np.mean(Mu_CP_Ex_R['Ellipsoid']), 0, 0,
                  np.mean(Mu_CP_Ex_R['Rectangular'])]

MeanMu_CD_Ex_U = [np.mean(Mu_CD_Ex_U['Maximum Height (cm)']), np.mean(Mu_CD_Ex_U['Maximum Width (cm)']),
                  np.mean(Mu_CD_Ex_U['Area (cm)']), np.mean(Mu_CD_Ex_U['Shape Index']),
                  np.mean(Mu_CD_Ex_U['Shape Triangle']),
                  np.mean(Mu_CD_Ex_U['Obovoid']), np.mean(Mu_CD_Ex_U['Ovoid']),
                  np.mean(Mu_CD_Ex_U['Horizontal Asymmetry']), np.mean(Mu_CD_Ex_U['Vertical Asymmetry']),
                  0, 0, np.mean(Mu_CD_Ex_U['Proximal Blockiness']), np.mean(Mu_CD_Ex_U['Distal Blockiness']), 0, 0,
                  np.mean(Mu_CD_Ex_U['Circular']), np.mean(Mu_CP_Ex_U['Ellipsoid']), 0, 0,
                  np.mean(Mu_CP_Ex_U['Rectangular'])]

MeanMu_L_Ex_R = [np.mean(Mu_L_Ex_R['Maximum Height (cm)']), np.mean(Mu_L_Ex_R['Maximum Width (cm)']),
                 np.mean(Mu_L_Ex_R['Area (cm)']), np.mean(Mu_L_Ex_R['Shape Index']),
                 np.mean(Mu_L_Ex_R['Shape Triangle']), np.mean(Mu_L_Ex_R['Obovoid']),
                 np.mean(Mu_L_Ex_R['Ovoid']),
                 np.mean(Mu_L_Ex_R['Horizontal Asymmetry']), np.mean(Mu_L_Ex_R['Vertical Asymmetry']),
                 0, 0, np.mean(Mu_L_Ex_R['Proximal Blockiness']), np.mean(Mu_L_Ex_R['Distal Blockiness']), 0, 0,
                 np.mean(Mu_L_Ex_R['Circular']), np.mean(Mu_L_Ex_R['Ellipsoid']), 0, 0,
                 np.mean(Mu_L_Ex_R['Rectangular'])]

MeanMu_L_En_R = [np.mean(Mu_L_En_R['Maximum Height (cm)']), np.mean(Mu_L_En_R['Maximum Width (cm)']),
                 np.mean(Mu_L_En_R['Area (cm)']), np.mean(Mu_L_En_R['Shape Index']),
                 np.mean(Mu_L_En_R['Shape Triangle']), np.mean(Mu_L_En_R['Obovoid']),
                 np.mean(Mu_L_En_R['Ovoid']),
                 np.mean(Mu_L_En_R['Horizontal Asymmetry']), np.mean(Mu_L_En_R['Vertical Asymmetry']),
                 np.mean(Mu_L_En_R['Proximal Angle (rad)']), np.mean(Mu_L_En_R['Distal Angle (rad)']),
                 np.mean(Mu_L_En_R['Proximal Blockiness']), np.mean(Mu_L_En_R['Distal Blockiness']),
                 np.mean(Mu_L_En_R['Proximal Shoulderheight']), np.mean(Mu_L_En_R['Distal Shoulderheight']),
                 np.mean(Mu_L_En_R['Circular']), np.mean(Mu_L_En_R['Ellipsoid']),
                 np.mean(Mu_L_En_R['Proximal Heart']), np.mean(Mu_L_En_R['Distal Heart']),
                 np.mean(Mu_L_En_R['Rectangular'])]

# MeanSt_CP_EX_R.append(np.mean(St_CP_Ex_R['Eccentric']))
Row_Names = ['CP_Ex_R', 'CD_En_R', 'CD_En_U', 'CD_Ex_R', 'CD_Ex_U', 'CP_Ex_U', 'L_En_R', 'L_Ex_R']

MeanSt = np.row_stack((MeanSt_CP_Ex_R, MeanSt_CD_En_R, MeanSt_CD_En_U, MeanSt_CD_Ex_R, MeanSt_CD_Ex_U,
                       MeanSt_CP_Ex_U, MeanSt_L_En_R, MeanSt_L_Ex_R))
MeanSt = np.column_stack((Row_Names, MeanSt))
MeanBe = np.row_stack((MeanBe_CP_Ex_R, MeanBe_CD_En_R, MeanBe_CD_En_U, MeanBe_CD_Ex_R, MeanBe_CD_Ex_U,
                       MeanBe_CP_Ex_U, MeanBe_L_En_R, MeanBe_L_Ex_R))
MeanBe = np.column_stack((Row_Names, MeanBe))
MeanCh = np.row_stack((MeanCh_CP_Ex_R, MeanCh_CD_En_R, MeanCh_CD_En_U, MeanCh_CD_Ex_R, MeanCh_CD_Ex_U,
                       MeanCh_CP_Ex_U, MeanCh_L_En_R, MeanCh_L_Ex_R))
MeanCh = np.column_stack((Row_Names, MeanCh))
MeanMu = np.row_stack((MeanMu_CP_Ex_R, MeanMu_CD_En_R, MeanMu_CD_En_U, MeanMu_CD_Ex_R, MeanMu_CD_Ex_U,
                       MeanMu_CP_Ex_U, MeanMu_L_En_R, MeanMu_L_Ex_R))
MeanMu = np.column_stack((Row_Names, MeanMu))

# for n in range(0,len(df)):
# if df["Type"] == "Standard" and df['Type of Tomato Section'] == "CP-Ex-R":

Column_Names = ["Type of Tomato Section", "Mean Height (cm)", "Mean Width (cm)", "Mean Area (cm)", "Shape Index",
                "Shape Triangle", "Obovoid", "Ovoid", "Horizontal Asymmetry", "Vertical Asymmetry",
                "Proximal Angle (rad)", "Distal Angle (rad)", "Proximal Blockiness", "Distal Blockiness",
                "Proximal Shoulderheight", "Distal Shoulderheight", "Circular", "Ellipsoid", "Proximal Heart",
                "Distal Heart", "Rectangular"]


MeanSt_df = pd.DataFrame(MeanSt)
MeanSt_df.columns = Column_Names
MeanSt_df.rows = Row_Names
MeanSt_df.to_excel('MeanSt.xlsx')

MeanBe_df = pd.DataFrame(MeanBe)
MeanBe_df.columns = Column_Names
MeanBe_df.rows = Row_Names
MeanBe_df.to_excel('MeanBe.xlsx')

MeanCh_df = pd.DataFrame(MeanCh)
MeanCh_df.columns = Column_Names
MeanCh_df.rows = Row_Names
MeanCh_df.to_excel('MeanCh.xlsx')

MeanMu_df = pd.DataFrame(MeanMu)
MeanMu_df.columns = Column_Names
MeanMu_df.rows = Row_Names
MeanMu_df.to_excel('MeanMu.xlsx')
